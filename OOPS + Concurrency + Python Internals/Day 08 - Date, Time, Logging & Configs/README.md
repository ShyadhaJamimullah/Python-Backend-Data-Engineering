## Task Reminder Scheduler

A Python console app to create, manage, and get reminders for tasks.
Tasks can be one-time or recurring daily, with snooze functionality and logging of events.

### Concepts Used

- **Classes & Functions –** Organizing tasks and reminders.
- **File Handling –** Task data persisted in ```tasks.json```.
- **Scheduling –** Using ```schedule``` module to trigger reminders at set times.
- **Datetime Handling –** Managing one-time and recurring reminders.
- **Logging –** Tracking task creation, reminders, snoozes, and completions.
- **Exception Handling –** Safe operations for invalid inputs or scheduling issues.

### Features

- Add tasks with a name, time, and scope (once/daily).
- Delete existing tasks.
- Run a scheduler that checks tasks in real-time.
- Reminders pop up in the console at the scheduled time.
- Snooze a reminder for 10 minutes.
- Automatic cleanup of completed one-time tasks.

### What I Learned

- Managing tasks with Python and datetime
- Implementing recurring and one-time reminders
- Using the schedule module for time-based actions
- Storing and retrieving persistent data with JSON
- Logging and tracking user actions for better monitoring
