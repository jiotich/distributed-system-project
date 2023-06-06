class Image():
    def __init__(self, id, data, created_date, created_time):
        self.id           = id
        self.data         = data
        self.created_date = created_date
        self.created_time = created_time
class Post():
    def __init__(self, id, owner_id, description, upvotes, created_date, created_time, image: Image):
        self.id           = id
        self.owner_id     = owner_id
        self.description  = description
        self.upvotes      = upvotes
        self.created_date = created_date
        self.created_time = created_time
        self._image        = image

    def get_image(self):
        return self._image