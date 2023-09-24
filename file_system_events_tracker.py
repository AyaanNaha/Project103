import sys, time, random, os, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ayaan/OneDrive/Desktop/WhiteHat/Project103/ProjectFiles" # Change directory to where the project is on your computer

# Initialize Event Handler Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"{event.src_path} was created")
    
    def on_deleted(self, event):
        print(f"{event.src_path} was deleted")
    
    def on_modified(self, event):
        print(f"{event.src_path} was modified")
    
    def on_moved(self, event):
        print(f"{event.src_path} was moved")

# Initialize Observer & event handler
observer = Observer()
event_handler = FileEventHandler()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()