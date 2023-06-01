from core.services import CreateUserService

class CreateUserController:
    def handle(self, username, password):
        createUserService = CreateUserService()
        response = createUserService.execute(username, password)
        
        if (response):
            
            #gerar o JSON com a resposta positiva
            
            pass
        else:
            
            #gerar o JSON com a resposta negativa
            
            pass