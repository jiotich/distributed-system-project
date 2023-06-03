from core.services import CreateUserService

class CreateUserController:
    def handle(self, username, password):
        create_user_service = CreateUserService()
        response = create_user_service.execute(username, password)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass