class RESTLog:
    def __init__(
            self,
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
        ):

        self.timestamp         = timestamp
        self.user_ip_address   = user_ip_address
        self.username          = username
        self.bytes_sent        = bytes_sent
        self.bytes_received    = bytes_received
        self.time_spent        = time_spent
        self.server_ip_address = server_ip_address
        self.server_port       = server_port
        
        self.http_method       = http_method
        self.url               = url                #uri-stem
        self.http_status       = http_status