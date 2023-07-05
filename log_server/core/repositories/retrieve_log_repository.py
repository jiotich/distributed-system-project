import sqlite3 as SQL

from core.database import DatabaseConnection
from core.database import queries

from core.entities import RESTLogRetrieveParameters
from core.entities import RMILogRetrieveParameters

class RetrieveLogRepository:
    def retrieve_rest_log(
        self,
        parameters: RESTLogRetrieveParameters ,
        db_connection: DatabaseConnection
    ):
        try:
            
            print(type(parameters.date_month))
            
            query_parameters = []
            QUERY = queries.RETRIEVE_REST_LOG_BASE
            
            if (parameters.http_method != None):
                QUERY += queries.RETRIEVE_REST_LOG_HTTP_METHOD_PARAM
                query_parameters.append(parameters.http_method)
            
            if (parameters.http_status != None):
                QUERY += queries.RETRIEVE_REST_LOG_HTTP_STATUS_PARAM
                query_parameters.append(parameters.http_status)
           
            if (parameters.url != None):
                QUERY += queries.RETRIEVE_REST_LOG_URL_PARAM
                query_parameters.append(parameters.url)
                
            if (parameters.server_ip != None):
                QUERY += queries.RETRIEVE_LOG_SERVER_IP_PARAM
                query_parameters.append(parameters.server_ip)
                
            if (parameters.date_day != None):
                QUERY += queries.RETRIEVE_LOG_DAY_PARAM
                query_parameters.append(parameters.date_day)
            
            if (parameters.date_month != None):
                QUERY += queries.RETRIEVE_LOG_MONTH_PARAM
                query_parameters.append(parameters.date_month)
            
            if (parameters.date_year != None):
                QUERY += queries.RETRIEVE_LOG_YEAR_PARAM
                query_parameters.append(parameters.date_year)
                
            cursor = db_connection.start_connection()
            
            cursor.execute(
                QUERY,
                query_parameters
            )
            
            data = db_connection.fetch_data()
            db_connection.finish_connection()
            
        except SQL.IntegrityError:
            return False
        else: 
            return data
        


    def retrieve_rmi_log(
        self,
        parameters: RMILogRetrieveParameters ,
        db_connection: DatabaseConnection
    ):
        try:
            
            query_parameters = []
            QUERY = queries.RETRIEVE_RMI_LOG_BASE
            
            if (parameters.object_name != None):
                QUERY += queries.RETRIEVE_RMI_LOG_OBJECT_NAME_PARAM
                query_parameters.append(parameters.object_name)
            
            if (parameters.object_method != None):
                QUERY += queries.RETRIEVE_RMI_LOG_OJECT_METHOD_PARAM
                query_parameters.append(parameters.object_method)
           
            if (parameters.response_status != None):
                QUERY += queries.RETRIEVE_RMI_LOG_RESPONSE_STATUS_PARAM
                query_parameters.append(parameters.response_status)
                
            if (parameters.server_ip != None):
                QUERY += queries.RETRIEVE_LOG_SERVER_IP_PARAM
                query_parameters.append(parameters.server_ip)
                
            if (parameters.date_day != None):
                QUERY += queries.RETRIEVE_LOG_DAY_PARAM
                query_parameters.append(parameters.date_day)
            
            if (parameters.date_month != None):
                QUERY += queries.RETRIEVE_LOG_MONTH_PARAM
                query_parameters.append(parameters.date_month)
            
            if (parameters.date_year != None):
                QUERY += queries.RETRIEVE_LOG_YEAR_PARAM
                query_parameters.append(parameters.date_year)
                
            cursor = db_connection.start_connection()
            
            cursor.execute(
                QUERY,
                query_parameters
            )
            
            data = db_connection.fetch_data()
            db_connection.finish_connection()
            
        except SQL.IntegrityError:
            return False
        else: 
            return data
        