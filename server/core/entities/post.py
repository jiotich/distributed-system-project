class Post():
    def __init__(self):
        self._owner       = None
        self._description = None
        self._image       = None
        self._upvotes     = None
        
    def create_post(self, owner_id, description, image, upvotes):
        self._owner       = owner_id
        self._description = description
        self._image       = image
        self._upvotes     = 0