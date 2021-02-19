import signal
import sys
import time
import os

# When your app is running inside a Docker container, 
# Docker expects you to do all the configuration using environment variables
from dotenv import load_dotenv

class App:
    def __init__(self):
        load_dotenv(verbose=True)
        self.loops = int(os.getenv("LOOPS", 5))
        self.shutdown = False
        # CMD instruction allows it to receive signals from operating system - SIGNT and SIGTERM (used to shut down application)
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print('Received:', signum)
        self.shutdown = True

    def start(self):
        print("Start app")

    def run(self):
        print("Running app")
        time.sleep(1)

    def stop(self):
        print("Stop app")


if __name__ == '__main__':
    app = App()
    app.start()
    counter = 0
    while not app.shutdown and counter < app.loops:
        app.run()
        counter += 1
    app.stop()
    sys.exit(0)
