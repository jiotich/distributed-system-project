class User:
    def __init__(self):
        self._id        = None
        self._username  = None
        self._password  = None
        self._posts     = None
        self._followers = None
        self._following = None
        
    def create_user(self, id, username, password):
        self._id        = id
        self._username  = username
        self._password  = password
        self._posts     = []
        self._followers = []
        self._following = []
        
    def get_user_info(self):
        return self._id, self._username, self._password