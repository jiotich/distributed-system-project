import requests
from misc.load_config import Configs
from log.rest_log     import RESTLog

class LogServerConnection:
    def __init__(self):
        self.config = Configs().config

    def create_rest_log(self, log:RESTLog):
        # url = self.config["log_server_connection"]["routes"]["create_rest_log"]
        
        
        url = "http://127.0.0.1:8080/log/rest/new"

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

        response = requests.post(
            url=url,
            json=body,
            headers=headers
        )

        print(response.status_code)