import os
import shutil
import csv
import json
from openpyxl import load_workbook
import logging
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    filename="classification.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s"
)

logger=logging.getLogger("Classification")

class FileProcessor(ABC):
    def __init__(self,file_path,output_dir):
        self.file_path=file_path
        self.filename=os.path.basename(file_path)
        self.output_dir=output_dir

    @abstractmethod
    def process(self):
        pass
  
    def move_file(self, destination):
        os.makedirs(destination, exist_ok=True)
        shutil.move(self.file_path, os.path.join(destination, self.filename))
        logger.info(f"Moved {self.filename} to {destination}")

class CSVProcessor(FileProcessor):
    def process(self):
        with open(self.file_path, newline="") as file:
            reader=csv.DictReader(file)
        self.move_file(os.path.join(self.output_dir, "Structured"))
        logger.info(f"Classified CSV {self.filename} | as Structued ")

class JSONProcessor(FileProcessor):
    def process(self):
        with open(self.file_path) as file:
            json.load(file)
        self.move_file(os.path.join(self.output_dir, "Semi-Structured"))
        logger.info(f"Classified JSON {self.filename} | as Semi-Structured")

class TextProcessor(FileProcessor):
    def process(self):
        self.move_file(os.path.join(self.output_dir, "Unstructured"))
        logger.info(f"Classified TEXT {self.filename} | as Unstructured")

class ExcelProcessor(FileProcessor):
    def process(self):
        wb=load_workbook(self.file_path,read_only=True)
        ws=wb.active
        wb.close()
        self.move_file(os.path.join(self.output_dir, "Structured"))
        logger.info(f"Classified Excel {self.filename} | as Structured")

class ImageProcessor(FileProcessor, ABC):
    def process(self):

        destination = os.path.join(self.output_dir, "Unstructured")
        os.makedirs(destination, exist_ok=True)
        
        shutil.move(self.file_path, os.path.join(destination, self.filename))
       
        logger.info(f"Classified IMAGE {self.filename} | as Unstructured")

def get_processor(file_path, output_dir):
    ext = file_path.lower()
    if ext.endswith(".csv") or ext.endswith(".log"):
        return CSVProcessor(file_path, output_dir)
    elif ext.endswith(".json"):
        return JSONProcessor(file_path, output_dir)
    elif ext.endswith(".txt"):
        return TextProcessor(file_path, output_dir)
    elif ext.endswith(".xlsx"):
        return ExcelProcessor(file_path, output_dir)
    elif ext.endswith(".png") or ext.endswith(".jpg") or ext.endswith(".jpeg"):
        return ImageProcessor(file_path, output_dir)  # You can create a new class

    
class FileClassification:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def scan_files(self):
        return [
            os.path.join(self.input_dir, f)
            for f in os.listdir(self.input_dir)
            if os.path.isfile(os.path.join(self.input_dir, f))
        ]
    
    def handle_file(self, file_path):
        processor=get_processor(file_path, self.output_dir)
        if processor:
            processor.process()

    def run(self):
        files=self.scan_files()
        logger.info(f"Files found: {len(files)}")

        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(self.handle_file, files)

        logger.info("Classification completed")


if __name__ == "__main__":
    service = FileClassification(
        input_dir="files",
        output_dir="classified_data"
    )
    service.run()