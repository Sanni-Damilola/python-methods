# autoreload.py
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".py"):
            print(f"Changes detected in {event.src_path}. Restarting...")
            restart_script()

def restart_script():
    subprocess.run(["python", "main.py"])

def watch():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    watch()
