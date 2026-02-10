import os
import csv
import json
import random
import string
from openpyxl import Workbook
from PIL import Image

BASE_DIR = "files"
NUM_FILES = 1
ROWS_PER_CSV = 2000    # ~5–8 MB CSV
LINES_PER_TXT = 150_000    # ~5–7 MB TXT
ENTRIES_PER_JSON = 80_000  # ~5–8 MB JSON

os.makedirs(BASE_DIR, exist_ok=True)

# ---------- CSV FILES ----------
for i in range(NUM_FILES):
    file_path = os.path.join(BASE_DIR, f"sales_{i}.csv")
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["OrderID", "Amount"])
        for j in range(ROWS_PER_CSV):
            writer.writerow([j, round(random.uniform(10, 1000), 2)])

# ---------- JSON FILES ----------
for i in range(NUM_FILES):
    file_path = os.path.join(BASE_DIR, f"user_logs_{i}.json")
    data = []
    for j in range(ENTRIES_PER_JSON):
        data.append({
            "user_id": j,
            "action": random.choice(["login", "logout", "click", "purchase"]),
            "timestamp": j
        })

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

# ---------- TXT FILES ----------
for i in range(NUM_FILES):
    file_path = os.path.join(BASE_DIR, f"error_dump_{i}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(LINES_PER_TXT):
            f.write(
                "".join(random.choices(string.ascii_letters + string.digits, k=80))
                + "\n"
            )

#-----------Excel------------

for i in range(NUM_FILES):
    wb=Workbook()
    ws=wb.active
    ws.title="Products"
    ws.append(["product_id","cost"])
    file_path=os.path.join(BASE_DIR,f"product_{i}.xlsx")
    wb.save(file_path)

# ---------- IMAGE FILES ----------

img = Image.new('RGB', (100, 100), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
img.save(os.path.join(BASE_DIR, f"image_{i}.png"))

# ---------- LOG FILES ----------
with open(os.path.join(BASE_DIR, "system.log"), "w") as f:
    for i in range(100):
        f.write(f"{i} - INFO - Event {random.randint(1000,9999)}\n")

print("Test files generated successfully!")