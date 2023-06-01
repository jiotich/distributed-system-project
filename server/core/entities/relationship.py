class Relationship:
    def __init__(self):
        self._source_user      = None
        self._destination_user = None
    
    def create_relationship(self, src_owner_id, dest_owner_id):
        self._source_user      = src_owner_id
        self._destination_user = dest_owner_id