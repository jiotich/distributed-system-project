from core.database     import DatabaseConnection
from core.entities     import RMILogRetrieveParameters
from core.repositories import RetrieveLogRepository

class RetrieveRMILogService:
    def execute(self, parameters:RMILogRetrieveParameters):
        db_connection           = DatabaseConnection()
        retrieve_log_repository = RetrieveLogRepository()    
        
        response = retrieve_log_repository.retrieve_rmi_log(
            parameters,
            db_connection
        )
        
        return response