from core.services import CreateRESTLogService
from core.entities import RESTLog

class CreateRESTLogController:
    def handle(self, log:RESTLog):
        create_rest_log_service = CreateRESTLogService()
        response = create_rest_log_service.execute(log)
        
        return response