import requests
from misc.load_config import Configs
from log.rest_log     import RESTLog

class LogServerConnection:
    def __init__(self):
        self.config = Configs().config
        
        self.IP_ADDRESS            = self.config["log-server-connection"]["ip_address"] 
        self.PORT                  = self.config["log-server-connection"]["port"]
        
        self.CREATE_REST_LOG_ROUTE = self.config["log-server-connection"]["routes"]["create_rest_log"]
        self.CREATE_RMI_LOG_ROUTE  = self.config["log-server-connection"]["routes"]["create_rmi_log"]

    def create_rest_log(self, log:RESTLog):
        
        url = f"http://{self.IP_ADDRESS}:{self.PORT}{self.CREATE_REST_LOG_ROUTE}"

        headers = {
            "Content-Type": "application/json"
        }

        body = {
            "timestamp":         log.timestamp,
            "user_ip_address":   log.user_ip_address,
            "username":          log.username,
            "bytes_sent":        log.bytes_sent,
            "bytes_received":    log.bytes_received,
            "time_spent":        log.time_spent,
            "server_ip_address": log.server_ip_address,
            "server_port":       log.server_port,
            "http_method":       log.http_method,
            "url":               log.url,
            "http_status":       log.http_status
        }

        print("ok")
        
        try:
            response = requests.post(
                url=url,
                json=body,
                headers=headers
            )
        except requests.exceptions.ConnectionError:
            print("deu erro")
            return None
        else:
            print(response.status_code)
            return None
