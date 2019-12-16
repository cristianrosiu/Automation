import sys
import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    """Deals with the transition of
       incoming files when an event occurs"""

    def on_modified(self, event):
        for filename in os.listdir(src_folder):
            if ".png" in filename or ".jpg" in filename or ".jpeg" in filename:
                src = src_folder + "/" + filename
                new_destination = "/home/cristian/Pictures/" + filename
                os.rename(src, new_destination)


class Watcher:
    def __init__(self, src_path):
        self.src_path = src_path
        self.observer = Observer()          # Observes the desiered folder
        self.event_handler = FileHandler()  # Handles the new incoming files

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(10)              #Check for changes every 10 seconds
        except KeyboardInterrupt:
            self.observer.stop()

    def start(self):
        self.observer.schedule(self.event_handler, self.src_path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    src_folder = "/home/cristian/Downloads"
    watcher = Watcher(src_folder)
    watcher.run()
