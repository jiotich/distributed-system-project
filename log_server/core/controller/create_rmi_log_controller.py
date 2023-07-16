from core.services import CreateRMILogService
from core.entities import RMILog

class CreateRMILogController:
    def handle(self, log:RMILog):
        create_rmi_log_service = CreateRMILogService()
        response = create_rmi_log_service.execute(log)
        
        return response