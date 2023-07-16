
# REST EXCLUSIVE QUERIES

CREATE_REST_LOG = """
    INSERT INTO 
        log_rest (
            id, 
            timestamp, 
            user_ip_address,
            username, 
            bytes_sent,
            bytes_received, 
            time_spent,
            server_ip_address, 
            server_port,
            http_method, 
            url, 
            http_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

RETRIEVE_REST_LOG_BASE = """
    SELECT *
    FROM 
        log_rest
    WHERE 
        1 = 1
"""

RETRIEVE_REST_LOG_HTTP_METHOD_PARAM = """
    AND http_method = (?)
"""

RETRIEVE_REST_LOG_HTTP_STATUS_PARAM = """
    AND http_status = (?)
"""

RETRIEVE_REST_LOG_URL_PARAM = """
    AND url = (?)
"""

# RMI EXCLUSIVE QUERIES

CREATE_RMI_LOG = """
    INSERT INTO 
        log_rmi (
            id, 
            timestamp, 
            user_ip_address,
            username, 
            bytes_sent,
            bytes_received, 
            time_spent,
            server_ip_address, 
            server_port,
            nameserver,
            object_name,
            object_method,
            response_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

RETRIEVE_RMI_LOG_BASE = """
    SELECT *
    FROM 
        log_rmi
    WHERE 
        1 = 1
"""

RETRIEVE_RMI_LOG_OBJECT_NAME_PARAM = """
    AND object_name = (?)
"""

RETRIEVE_RMI_LOG_OJECT_METHOD_PARAM = """
    AND object_method = (?)
"""

RETRIEVE_RMI_LOG_RESPONSE_STATUS_PARAM = """
    AND url = (?)
"""

# COMMON QUERIES

RETRIEVE_LOG_SERVER_IP_PARAM = """
    AND server_ip_address = (?)
"""

RETRIEVE_LOG_DAY_PARAM = """
    AND substr(timestamp, 1, 2) = (?)
"""

RETRIEVE_LOG_MONTH_PARAM = """
    AND substr(timestamp, 4, 2) = (?)
"""

RETRIEVE_LOG_YEAR_PARAM = """
    AND substr(timestamp, 7, 4) = (?)
"""