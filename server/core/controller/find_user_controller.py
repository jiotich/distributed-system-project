import json
from core.services import FindUserService

class FindUserController:
    def handle(self, username):
        find_user_service = FindUserService()
        response = find_user_service.execute(username)
        
        if (response):
            return json.dumps({"data": response, "status_code": "200"})
        else:
            return json.dumps({"data": "unexistent", "status_code": "400"})
            