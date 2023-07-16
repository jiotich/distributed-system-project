class RESTLogRetrieveParameters:
    def __init__(
        self,
        http_method,
        http_status,
        url,
        server_ip,
        date_day,
        date_month,
        date_year
    ):
        
        self.http_method   = None if http_method == "None" else http_method
        self.http_status   = None if http_status == "None" else http_status
        self.url           = None if url         == "None" else url
        self.server_ip     = None if server_ip   == "None" else server_ip
        self.date_day      = None if date_day    == "None" else date_day
        self.date_month    = None if date_month  == "None" else date_month
        self.date_year     = None if date_year   == "None" else date_year
        