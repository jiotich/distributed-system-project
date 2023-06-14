import json
from core.services import UpdateUserService

class UpdateUserController:
    def handle(self, username, data, column):
        update_user_service = UpdateUserService()
        response = update_user_service.execute(username, data, column)
        
        return response
        
        # if (response):
        #     return json.dumps({
        #         "message": "success", "status_code": 200
        #     })
        # else:
        #     return json.dumps({
        #         "message": "failed", "status_code": 400
        #     })
        