from ezblock import Taskmgr

class PiStatus():
    def __init__(self):
        self.taskmgr = Taskmgr()
        print(" [.] Created status verifier", self.taskmgr)
    def status(self):
        return str(self.taskmgr.read())

# Usage example
#stats = PiStatus()
#print(stats.status())
