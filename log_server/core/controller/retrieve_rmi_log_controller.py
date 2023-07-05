from core.services import RetrieveRMILogService
from core.entities import RMILogRetrieveParameters

class RetrieveRMILogController:
    def handle(self, parameters:RMILogRetrieveParameters):
        retrieve_rmi_log_service = RetrieveRMILogService()
        response = retrieve_rmi_log_service.execute(parameters)
        
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
            "nameserver",
            "object_name",
            "object_method",
            "response_status"
        )
        
        for log in response:
            formated_response.append(dict(zip(response_ids, log)))        
        return formated_response