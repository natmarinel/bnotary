#script to check if a new file is created inside directory ./file_to_be_notarized/
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler 
from bnotary_api import call_api
from multiprocessing import Process

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = "./file_to_be_notarized/"
    #ignore directry creation
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):

    file_created = event.src_path
    print(file_created)
    print(type(file_created))
    #call_api(file_created)
    #inizialized a varialble
    #call function call_api which uses a process
    #each time the variable is started it creates a new process
    p = Process(target=call_api, args=(file_created,))
    p.start()

path = "./file_to_be_notarized/"
my_event_handler.on_created = on_created
#boolean that allow me to catch all the event that occurs even in the sub directories of my current directory
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
my_observer.start()

try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

