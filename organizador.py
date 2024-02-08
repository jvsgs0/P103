import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/User/Desktop/YouTube"

class FileSystemEventHandler(FileSystemEventHandler):

    def on_created(self, event):

        print(f"Você criou {event.src_path}!")
    
    def on_deleted(self, event):

        print(f"Você excluiu {event.src_path}!")
    
    def on_modified(self, event):

        print(f"Você modificou {event.src_path}!")

    def on_moved(self, event):

        print(f"Você moveu {event.src_path}!")

event_handler = FileSystemEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()