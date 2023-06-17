class PostComentary:
    def __init__(self, id, user_id, post_id, created_date, created_time, content):
        self.id           = id
        self.user_id      = user_id
        self.post_id      = post_id
        self.created_date = created_date
        self.created_time = created_time
        self.content      = content