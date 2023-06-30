import requests
from log.rest_log     import RESTLog
from misc.load_config import Configs


class LogServerConnection:
    def __init__(self):
        self.config = Configs().config
        
    def send_rest_log(self, log: RESTLog):
        
        header = {
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
        
        print(body)
        
        
        log_server_ip   = self.config["log-server-connection"]["ip_address"]
        log_server_port = self.config["log-server-connection"]["port"]
        route           = self.config["log-server-connection"]["routes"]["create_rest_log"]
        
        formated_url = f"http://{log_server_ip}:{log_server_port}{route}"
        
        print(formated_url)
        
        print("===============================")
        response = requests.post(
            url=formated_url,
            json=body,
            headers=header
        )
        
        print("===============================")
        print(response)