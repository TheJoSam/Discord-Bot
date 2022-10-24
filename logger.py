from datetime import datetime
import colorama
from colorama import Fore
from json import load
from os import path

config_file_path = 'config/logger.json'

class logging:
    def __init__(self, module: str = ''):
        colorama.init(autoreset=True, convert=True)
        if path.exists(config_file_path):
            config_file = open(config_file_path, 'r')
            self.config = load(config_file)
        
        self.module = module
        now = datetime.utcnow()
        self.time = now.strftime(self.config['time_format'])
        self.overwrite = self.config['overwrite']
        
        if not path.exists(self.config['std_log_file']):
            with open(self.config['std_log_file'], 'w') as lf:
                lf.write('')
                
        if self.overwrite:
            with open(self.config['std_log_file'], 'w') as lf:
                lf.write('')
            self.log = open(self.config['std_log_file'], 'a+')
        else:
            with open(self.config['std_log_file'], 'r+') as lf:
                open(f'log_{self.time}.log', 'w').writelines(lf.readlines())
            self.log = open(self.config['std_log_file'], 'a+')
    
    def current_time(self):
        time = datetime.utcnow().strftime(self.config['log_time_format'])
        return time
    
    def on_error(self, message: str, error_code: int, module: str = 'logging class'):
        if self.config['output']:
            print(Fore.RED + '{} raised an exception with error code {}: {}'.format(module, str(error_code), message))
            print(Fore.RED + '[{}][LOGGER][ERROR] {} raised an exception with error code {}: {}'.format(self.current_time(), module, str(error_code), message))
        self.log.write('[{}][LOGGER][ERROR] {} raised an exception with error code {}: {}'.format(self.current_time(), module, str(error_code), message))
    
    def debug(self, message: str, extra: str):
        if self.config['output']:
            print(Fore.LIGHTBLACK_EX + '[{}][{}][DEBUG]{}: {}'.format(self.current_time(), self.module, extra, message))
        self.log.write('[{}][{}][DEBUG]{}: {}'.format(self.current_time(), self.module, extra, message))
    
    def info(self, message: str, extra: str):
        if self.config['output']:
            print(Fore.WHITE + '[{}][{}][INFO]{}: {}'.format(self.current_time(), self.module, extra, message))
        self.log.write('[{}][{}][INFO]{}: {}'.format(self.current_time(), self.module, extra, message))
    
    def warning(self, message: str, extra: str):
        if self.config['output']:
            print(Fore.YELLOW + '[{}][{}][WARN]{}: {}'.format(self.current_time(), self.module, extra, message))
        self.log.write('[{}][{}][WARN]{}: {}'.format(self.current_time(), self.module, extra, message))
    
    def error(self, message: str, extra: str):
        if self.config['output']:
            print(Fore.RED + '[{}][{}][ERROR]{}: {}'.format(self.current_time(), self.module, extra, message))
        self.log.write('[{}][{}][ERROR]{}: {}'.format(self.current_time(), self.module, extra, message))