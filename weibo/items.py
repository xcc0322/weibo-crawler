# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class UserProfileItem(Item):
    # Store some features to signal the probability of anomaly
    uid = Field()
    number_of_fans = Field()
    number_of_followings = Field()
    number_of_interactions_in_most_recent_posts = Field()
    pass

class UserConnectionItem(Item):
    # Store connections of users
    uid = Field()
    type_of_connections = Field() # 0 for fans, 1 for followings
    uid_list = Field()
    pass
