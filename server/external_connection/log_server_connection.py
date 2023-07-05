import requests

from misc.load_config import Configs
from log.rest_log     import RESTLog
from log.rmi_log      import RMILog


class LogServerConnection:
    def __init__(self):
        self.config = Configs().config
        
        self.IP_ADDRESS            = self.config["log-server-connection"]["ip_address"] 
        self.PORT                  = self.config["log-server-connection"]["port"]
        
        self.CREATE_REST_LOG_ROUTE = self.config["log-server-connection"]["routes"]["create_rest_log"]
        self.CREATE_RMI_LOG_ROUTE  = self.config["log-server-connection"]["routes"]["create_rmi_log"]

    def create_rest_log(self, log:RESTLog):
        
        url = "http://" + self.IP_ADDRESS + ":" + str(self.PORT) + self.CREATE_REST_LOG_ROUTE

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
        
        try:
            response = requests.post(
                url=url,
                json=body,
                headers=headers
            )
        except requests.exceptions.ConnectionError:
            print(f"> REST log failure: {response.status_code}")
            return True
        else:
            print(f"> REST log created: {response.status_code}")
            return False
        
    def create_rmi_log(self, log:RMILog):
        
        url = "http://" + self.IP_ADDRESS + ":" + str(self.PORT) + self.CREATE_RMI_LOG_ROUTE

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
            "nameserver":        log.nameserver,
            "object_name":       log.object_name,
            "object_method":     log.object_method,
            "response_status":   log.response_status
        }

        try:
            response = requests.post(
                url=url,
                json=body,
                headers=headers
            )
        except requests.exceptions.ConnectionError:
            print(f"> RMI log failure: {response.status_code}")
            return True
        else:
            print(f"> RMI log created: {response.status_code}")
            return False
