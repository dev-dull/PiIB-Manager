import threading


class PinMonitor(threading.Thread):
    def __init__(self, read_pin, pin_name):
        threading.Thread.__init__(self)
        self.read_pin = read_pin
        self.pin_name = pin_name
        self.status = False
        self.continue_monitoring = True

    def run(self):
        # TODO: sampling as fast as we can might be a bad plan.
        # TODO: Test if the main thread can get a garbage due to a partially saved value. Add locking if so.
        while self.continue_monitoring:
            self.status = self.read_pin()
            print(self.pin_name, self.status)
