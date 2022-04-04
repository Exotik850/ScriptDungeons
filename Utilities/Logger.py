from datetime import datetime

class Logger:
    def __init__(self):
        self.filepath = 'Logs/log{}.txt'.format(datetime.now().strftime("%Y-%m-%d_%H"))
        self.file = open(self.filepath, 'a')

    def log(self, message):
        self.file.write(f'{message} at {datetime.now().strftime("%H:%M%p")}\n')
        print(message)
        self.file.flush()

    def close(self):
        self.file.close()

    def __del__(self):
        self.close()

