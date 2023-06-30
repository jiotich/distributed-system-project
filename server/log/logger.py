import datetime
import pytz

from misc.load_config          import Configs
from log.log_server_connection import LogServerConnection
from log.rest_log              import RESTLog

class Logger:
    def __init__(self):
        self.config = Configs().config
        self.log_server_connection = LogServerConnection()
        
    def _get_timestamp(self):
        utd_date = datetime.datetime.now(pytz.UTC)

        timezone_date = utd_date.astimezone(
            pytz.timezone(self.config["log-config"]["timezone"])
        )

        timezone_shift = timezone_date.strftime('%z')
        timezone_shift = timezone_shift[0:3]
        timestamp = timezone_date.strftime('%d/%m/%Y %H:%M:%S ') + 'UTC' + timezone_shift
        
        return timestamp
        
    def new_rest_log(
        self,
        user_ip_address,
        username,
        bytes_sent,
        bytes_received,
        time_spent,
        http_method,
        url,
        http_status
    ):
        
        log = RESTLog(
            self._get_timestamp(),
            user_ip_address,
            username,
            bytes_sent,
            bytes_received,
            time_spent,
            self.config["server"]["ip_address"],
            self.config["server"]["port"],
            http_method,
            url,
            http_status,
        )
        
        self.log_server_connection.send_rest_log(
            log
        )
    
        