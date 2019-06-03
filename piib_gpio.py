import threading


class PinMonitor(threading.Thread):
    def __init__(self, pin, pin_name):
        threading.Thread.__init__(self)
        self.pin = pin
        self.pin_name = pin_name
        self.status = False
        self.continue_monitoring = True

    def run(self):
        while self.continue_monitoring:
            self.status = self.pin()
