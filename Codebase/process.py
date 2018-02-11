import threading

class ProcessThread(threading.Thread):
    def __init__(self, name, queue, func, *args):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.func = func
        self.args = args
        print("ProcessThread: '%s' created" % self.name)

    def run(self):
        print("Running %s" % self.name)
        self.func(self.queue)