import json
from core.services import CreateUserService

class CreateUserController:
    def handle(self, username, password, description):
        create_user_service = CreateUserService()
        response = create_user_service.execute(username, password, description)
        
        if (response):
            return json.dumps({ 
                "message": "success", "status_code": 200 
            })
            
        else:
            return json.dumps({ 
                "message": "failed", "status_code": 400 
            })
            