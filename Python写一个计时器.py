import time
class TimeKit:
    def __init__(self):
        self.start_time = -1
        self.stop_time = -1
        print("未开始计时")
    def start(self):
        if self.start_time > -1:
            return "请先调用stop方法"
        self.start_time = time.time()
        return "开始计时"
    def stop(self):
        if self.start_time > 0:
            self.stop_time = time.time()
            ret = self.stop_time - self.start_time
            self.start_time = -1
            self.stop_time = -1
            return "计时结果：%f" % ret
        return "请先调用start"

timekit = TimeKit()
