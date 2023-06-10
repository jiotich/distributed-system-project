import json
from core.services import RemoveFollowerService

class RemoveFollowerController:
    def handle(self, followed_username, follower_username):
        remove_follower_service = RemoveFollowerService()
        response = remove_follower_service.execute(followed_username, follower_username)
        
        if (response):
            return json.dumps({
                "message": "success", "status_code": 200
            })
        else:
            return json.dumps({
                "message": "failed", "status_code": 400
            })
            