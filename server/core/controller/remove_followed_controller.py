import json
from core.services import RemoveFollowedService

class RemoveFollowedController:
    def handle(self, follower_username, followed_username):
        remove_followed_service = RemoveFollowedService()
        response = remove_followed_service.execute(follower_username, followed_username)
        
        if (response):
            return json.dumps({"status_code": "200"})
            
        else:
            return json.dumps({"status_code": "400"})
            