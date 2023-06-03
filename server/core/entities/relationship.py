class Relationship:
    def __init__(self, id, src_owner_id, dest_owner_id, type):
        self.id               = id
        self.source_user      = src_owner_id
        self.destination_user = dest_owner_id
        self.type             = type