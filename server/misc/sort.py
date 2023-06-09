from datetime import datetime

class Sort():
    def convert_to_datetime(self, post):
        order_key = datetime.strptime(post[3] + " " + post[4], '%d/%m/%Y %H:%M:%S')
        return order_key 

    def order_by_date(self, posts):
        ordered = sorted(posts, key=self.convert_to_datetime, reverse=True)
        return ordered
    