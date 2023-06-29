import datetime
import pytz
import json
import os

class Log: 
    def __init__(self):
        
        self.config = None
        
        with open(os.getcwd() + "/../config.json") as config_file:
            self.config = json.load(config_file)
    
    def _datetime(self):
        utd_date = datetime.datetime.now(pytz.UTC)

        timezone_date = utd_date.astimezone(
            pytz.timezone(self.config["log-config"]["timezone"])
        )

        timezone_shift = timezone_date.strftime('%z')
        timezone_shift = timezone_shift[0:3]
        timestamp = timezone_date.strftime('%d/%m/%Y %H:%M:%S ') + 'UTC' + timezone_shift

        return timestamp

class LogREST(Log):
    def __init__(self):
        super().__init__()
        
        self.timestamp         = self._datetime()
        self.user_ip_address   = None,
        self.username          = None,
        self.http_method       = None,
        self.url               = None,
        self.http_status       = None,
        self.byted_sent        = None,
        self.bytes_received    = None,
        self.time_spent        = None,
        self.server_ip_address = self.config["server"]["ip_address"]
        self.server_port       = self.config["server"]["port"]
    
    def create(
        self,
        user_ip_address,
        username,
        http_method,
        url,
        http_status,
        byted_sent,
        bytes_received,
        time_spent,
    ):
        self.user_ip_address = user_ip_address,
        self.username        = username,
        self.http_method     = http_method,
        self.url             = url,
        self.http_status     = http_status,
        self.byted_sent      = byted_sent,
        self.bytes_received  = bytes_received,
        self.time_spent      = time_spent,
        
        print(
            self.user_ip_address,
            self.username,
            self.http_method,
            self.url,
            self.http_status,
            self.byted_sent,
            self.bytes_received,
            self.time_spent
        )
        
        
        