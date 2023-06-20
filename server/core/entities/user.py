class User:
    def __init__(self, id, username, password, description):
        self.id          = id
        self.username    = username
        self.password    = password
        self.description = description
        self.posts       = []
        self.followers   = []
        self.following   = []
    