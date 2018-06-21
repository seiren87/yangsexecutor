from yangsutil import Printer


class APP:
    def __init__(self, args, logger, setting):
        self.args = args
        self.logger = logger
        self.setting = setting

    def start(self):
        Printer.json({
            'args': self.args,
            'logger': self.logger.name,
            'setting': self.setting
        })
