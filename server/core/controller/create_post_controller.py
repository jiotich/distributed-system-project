import json
from core.services import CreatePostService

class CreatePostController:
    def handle(self, username, description, image):
        create_post_service = CreatePostService()
        response = create_post_service.execute(username, description, image)
        
        if (response):
            return json.dumps({
                "message": "success",
                "status_code": 200
            })

        else:
            return json.dumps({
                "message": "failed", 
                "status_code": 400
            })
