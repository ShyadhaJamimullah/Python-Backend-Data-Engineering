import json
import os
from datetime import datetime,timedelta
import schedule
import logging
import time


dir=os.path.dirname(os.path.abspath(__file__))
task_file=os.path.join(dir,"tasks.json")

logging.basicConfig(filename="task.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def load_tasks():
    if not os.path.exists(task_file):
        return []
    with open(task_file,"r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(task_file,"w") as f:
        json.dump(tasks,f,indent=4)

def add_task():
    task_name=input("Enter task: ")
    time_str=input("Enter time (YYYY-MM-DD HH:MM): ")
    scope=input("Enter scope (once/everday): ").lower()

    format="%Y-%m-%d %H:%M"

    rem_time=datetime.strptime(time_str,format)

    task_dict={
        "TASK":task_name,
        "TIME":rem_time.strftime("%Y-%m-%d %H:%M"),
        "SCOPE":scope
    }

    tasks=load_tasks()
    tasks.append(task_dict)
    save_tasks(tasks)

    logging.info(f"Task added: {task_name}")

    if scope=="everyday":
        schedule.every().day.at(rem_time.strftime("%H:%M")).do(reminder,task_dict)

    elif scope == "once":
        delay = (rem_time - datetime.now()).total_seconds()
        if delay > 0:
            schedule.every(delay).seconds.do(reminder, task_dict)


def delete_task():
    task_name=input("Enter task: ")

    tasks=load_tasks()
    for task in tasks:
        if task["TASK"] ==task_name:
            tasks.remove(task)
            break
    save_tasks(tasks)

def reminder(task):
        task_time=datetime.strptime(task["TIME"],"%Y-%m-%d %H:%M")
        if datetime.now()>=task_time:
            
            logging.info(f"Reminder activated: {task['TASK']}")
            print(f"Reminder {task['TASK']}")

            choice=input("stop or snooze").lower()
            tasks=load_tasks()

            if choice=="snooze":
                new_time = datetime.now() + timedelta(minutes=10)
                task["TIME"] = new_time.strftime("%Y-%m-%d %H:%M")
                for t in tasks:
                    if t["TASK"] == task["TASK"]:
                        t["TIME"] = task["TIME"]
                save_tasks(tasks)
                logging.info("Snoozed")
                return
            
            if task["SCOPE"] == "once":
                print("One-time task completed")
                new_tasks = []
                for t in tasks:
                    if t["TASK"] != task["TASK"]:
                        new_tasks.append(t)
                save_tasks(new_tasks)          
                logging.info("Once task removed")
                return schedule.CancelJob   

            

def main():
    while True:
        print("1.Set Task reminder: ")
        print("2. Delete task")
        print("3. Run scheduler")
        print("4. Exit")

        choice=input("Enter choice: (e.g. 1): ")
        if choice=="1":
            add_task()
        elif choice=="2":
            delete_task()
        elif choice=="3":
            print("Scheduler running..")

            while True:
                schedule.run_pending()
                time.sleep(1)
        elif choice=="4":
            break
    
main()


                    








