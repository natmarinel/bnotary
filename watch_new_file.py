import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler 
from bnotary_api import call_api

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = "./file_to_be_notarized/"
    #ignora creazione di directory
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):

    path_file_created = event.src_path
    print(path_file_created)
    print(type(path_file_created))
    #file_created = open(path_file_created, 'rb')
    file_created = path_file_created
    print(file_created)
    print(type(file_created))
    call_api(file_created)

path = "./file_to_be_notarized/"
my_event_handler.on_created = on_created
#boolean that allow me to catch all the event that occurs even in the sub directories of my current directory
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
my_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
