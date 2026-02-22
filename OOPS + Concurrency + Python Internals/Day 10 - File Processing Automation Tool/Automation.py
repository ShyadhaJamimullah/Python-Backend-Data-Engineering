import os
import shutil
import csv
import json
import logging
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s"
)

logger=logging.getLogger("AutomationService")

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
        total=0
        with open(self.file_path, newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                total+=float(row.get("Amount", 0))
        print(f"Total sales in {self.filename}: {total}")
        self.move_file(os.path.join(self.output_dir, "sales"))
        logger.info(f"Processed CSV {self.filename} | Total: {total}")


class JSONProcessor(FileProcessor):
    def process(self):
        with open(self.file_path) as file:
            json.load(file)
        self.move_file(os.path.join(self.output_dir, "logs"))
        logger.info(f"Processed JSON {self.filename}")


class TextProcessor(FileProcessor):
    def process(self):
        self.move_file(os.path.join(self.output_dir, "text"))
        logger.info(f"Processed TEXT {self.filename}")

def get_processor(file_path, output_dir):
    if file_path.endswith(".csv"):
        return CSVProcessor(file_path, output_dir)
    elif file_path.endswith(".json"):
        return JSONProcessor(file_path, output_dir)
    elif file_path.endswith(".txt"):
        return TextProcessor(file_path, output_dir)
        
class FileAutomationService:
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

    logger.info("Automation completed")


if __name__ == "__main__":
    service = FileAutomationService(
        input_dir="incoming_files",
        output_dir="processed_data"
    )
    service.run()





            










