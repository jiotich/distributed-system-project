from core.services import CreatePostService

class CreatePostController:
    def handle(self, username, description, image):
        create_post_service = CreatePostService()
        response = create_post_service.execute(username, description, image)
        
        print(response)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass