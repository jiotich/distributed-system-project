from core.repositories import PostRepository
from core.repositories import UserRepository
from core.repositories import RelationshipRepository

from misc.sort  import Sort

#TODO: fazer os posts virem em ordem de data

class RetrieveFeedService:
    def execute(self, username, posts_limit):
        
        user_repository         = UserRepository()
        post_repository         = PostRepository()
        relationship_repository = RelationshipRepository()

        sort = Sort()

        user_exist = user_repository.find_one(username)
        
        if (user_exist):
            response = []
            posts = []
            user_id  = user_exist[0]

            followed_users = relationship_repository.list_followers(user_id)

            for index in range(len(followed_users)):
                user_id = followed_users[index][0]

                
                fetched_posts = post_repository.find(user_id)

                for index2 in range(len(fetched_posts)):
                    response.append(fetched_posts[index2])

            if (response):
                if (posts_limit != 0):
                    if (len(response) < posts_limit):
                        limit = len(response)
                    else:
                        limit = posts_limit

                    for index in range(limit):
                        posts.append(response[index])
                else:
                    posts = response

                # ordered_posts = sort.order_by_date(posts)

                return posts
            else:
                return False
        else:
            return False
        
        