import uuid

from core.database     import DatabaseConnection
from core.entities     import RMILog
from core.repositories import CreateLogRepository


class CreateRMILogService:
    def execute(self, log: RMILog):
        db_connection         = DatabaseConnection()
        create_log_repository = CreateLogRepository()    
        
        id = uuid.uuid4()
        
        response = create_log_repository.create_rmi_log(
            id,
            log,
            db_connection
        )
        
        return response
        
        