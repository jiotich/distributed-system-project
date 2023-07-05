from core.services import RetrieveRESTLogService
from core.entities import RESTLogRetrieveParameters

class RetrieveRESTLogController:
    def handle(self, parameters:RESTLogRetrieveParameters):
        retrieve_rest_log_service = RetrieveRESTLogService()
        response = retrieve_rest_log_service.execute(parameters)
        
        formated_response = []
        
        response_ids = (
            "id", 
            "timestamp", 
            "user_ip_address",
            "username", 
            "bytes_sent",
            "bytes_received", 
            "time_spent",
            "server_ip_address", 
            "server_port",
            "http_method",
            "url",
            "http_status"
        )
        
        for log in response:
            formated_response.append(dict(zip(response_ids, log)))        
        return formated_response