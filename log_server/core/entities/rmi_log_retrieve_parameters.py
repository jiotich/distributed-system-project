class RMILogRetrieveParameters:
    def __init__(
        self,
        object_name,
        object_method,
        response_status,
        server_ip,
        date_day,
        date_month,
        date_year
    ):
        
        self.object_name     = None if object_name     == "None" else object_name
        self.object_method   = None if object_method   == "None" else object_method
        self.response_status = None if response_status == "None" else response_status
        self.server_ip       = None if server_ip       == "None" else server_ip
        self.date_day        = None if date_day        == "None" else date_day
        self.date_month      = None if date_month      == "None" else date_month
        self.date_year       = None if date_year       == "None" else date_year
        