from datetime import datetime

class Logger:
    def __init__(self):
        self.filepath = 'Logs/log{}.txt'.format(datetime.now().strftime("%Y-%m-%d_%H"))
        self.file = open(self.filepath, 'a')

    def log(self, message):
        """
        Logs a message to the log file.
        :param message: The message to log.
        :return: None
        """
        self.file.write(f'{message} at {datetime.now().strftime("%H:%M%p")}\n')
        print(message)
        self.file.flush()

    def close(self):
        """
        Closes the log file.
        :return: None
        """
        self.file.close()

    def __del__(self):
        self.close()

