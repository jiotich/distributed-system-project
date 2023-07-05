from core.database     import DatabaseConnection
from core.entities     import RESTLogRetrieveParameters
from core.repositories import RetrieveLogRepository

class RetrieveRESTLogService:
    def execute(self, parameters:RESTLogRetrieveParameters):
        db_connection           = DatabaseConnection()
        retrieve_log_repository = RetrieveLogRepository()    
        
        response = retrieve_log_repository.retrieve_rest_log(
            parameters,
            db_connection
        )
        
        return response