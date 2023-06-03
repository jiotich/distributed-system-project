from core.services import RetrieveFeedService

class RetrieveFeedController:
    def handle(self, username): # retorna um array de posts
        retrieve_feed_service = RetrieveFeedService()
        response = retrieve_feed_service.execute(username)
        
        if (response):
            #gerar o JSON com a resposta positiva
            pass
        else:
            #gerar o JSON com a resposta negativa
            pass