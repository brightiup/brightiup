import datetime
from zio import *

class Logger(object):
    def __init__(self, log_type):
        self.type = log_type

    def _get_current_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def debug(self, msg):
        print '[+] [%s] %s'%(self._get_current_time(), msg)

    def info(self, msg):
        print '[*] [%s] %s'%(self._get_current_time(), msg)

    def warn(self, msg):
        print '[!] [%s] %s'%(self._get_current_time(), msg)

    def error(self, msg):
        print '[-] [%s] %s'%(self._get_current_time(), msg)


class GeneralLogger(Logger):
    def __init__(self):
        super(GeneralLogger, self).__init__('general')



class ConsoleLogger(Logger):
    def __init__(self):
        super(ConsoleLogger, self).__init__('console')

    def debug(self, msg):
        log(s='[+] [%s] %s'%(self._get_current_time(), msg), color='green')

    def info(self, msg):
        log(s='[*] [%s] %s'%(self._get_current_time(), msg), color='cyan')

    def warn(self, msg):
        log(s='[!] [%s] %s'%(self._get_current_time(), msg), color='yellow')

    def error(self, msg):
        log(s='[-] [%s] %s'%(self._get_current_time(), msg), color='red')
    
    def message(self, msg):
        log(msg)
