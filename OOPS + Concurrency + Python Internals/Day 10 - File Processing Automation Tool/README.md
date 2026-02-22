## File Automation Tool
The File Automation Tool is a Python-based utility that automatically scans, processes, and organizes files from a given input folder.

### What This Tool Does
- Scans an input directory for files
- Identifies file types automatically
- Processes each file based on its format
- Moves files into appropriate folders after processing
- Handles multiple files simultaneously using multithreading
- Maintains logs for transparency and debugging

### File Processing Logic
**CSV Files**
- Reads data using column headers
- Calculates total sales from the Amount column
- Moves files to the sales folder

**JSON Files**
- Validates JSON structure
- Moves files to the logs folder

**Text Files**
- No modification
- Simply organized into the text folder

### Multithreading
The application uses a thread pool to process multiple files in parallel, improving performance when handling large numbers of files.

### Logging
All file movements and processing details are recorded in automation.log, making it easy to track activity and debug issues.
