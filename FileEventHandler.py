
import os
import shutil
import time
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):

    def no_created(self, event):
        print("Hey, {event.scr_path} has been created!")

    def on_deleted(self, event):
        print("Oops! Someone deleted {event.scr_path}!")

    def on_modifed(self, event):
        print("Hey there! {event.scr_path} has been modified")

    def on_moved(self, event):
        print("Someone moved {event.src_path} to {event.dest_path}")

    
    try:
        while True:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        Observer.stop()
