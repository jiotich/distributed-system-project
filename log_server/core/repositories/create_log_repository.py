import sqlite3 as SQL

from core.database import DatabaseConnection
from core.database import queries

from core.entities import RESTLog
from core.entities import RMILog

class CreateLogRepository:
    def create_rest_log(self, id, log: RESTLog, db_connection: DatabaseConnection):
        try:
            cursor = db_connection.start_connection()
            cursor.execute(
                queries.CREATE_REST_LOG,
                [
                    str(id), 
                    log.timestamp, 
                    log.user_ip_address,
                    log.username, 
                    log.bytes_sent,
                    log.bytes_received, 
                    log.time_spent,
                    log.server_ip_address, 
                    log.server_port,
                    log.http_method, 
                    log.url, 
                    log.http_status, 
                ]
            )
            
            db_connection.commit_operation()
            db_connection.finish_connection()
            
        except SQL.IntegrityError:
            return False
        else: 
            return True
        
    def create_rmi_log(self, id, log: RMILog, db_connection: DatabaseConnection):
        try:
            cursor = db_connection.start_connection()
            cursor.execute(
                queries.CREATE_RMI_LOG,
                [
                    str(id),  
                    log.timestamp, 
                    log.user_ip_address,
                    log.username, 
                    log.bytes_sent,
                    log.bytes_received, 
                    log.time_spent,
                    log.server_ip_address, 
                    log.server_port,
                    log.nameserver,
                    log.object_name,
                    log.object_method,
                    log.response_status
                ]
            )
            
            db_connection.commit_operation()
            db_connection.finish_connection()
            
        except SQL.IntegrityError:
            return False
        else: 
            return True
        