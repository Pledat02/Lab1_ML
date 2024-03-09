class Account:
    def __init__(self, name, country, friends, listAccs,listPosts):
        self.name = name
        self.country = country
        self.friends = friends
        self.listAccs = listAccs
        self.listPosts = listPosts

    def __repr__(self):
        return self.name + ", " + self.country + ", " + str(self.friends) + ", " + str(self.listAccs)

    def get_country(self):
        return self.country

    def get_friends(self):
        return self.friends

    def getMaxLikePostByFriend(self):
        return max(self.listPosts)

class Post:
    def __init__(self, content, subject, like):
        self.content = content
        self.subject = subject
        self.like = like
class AccountManager:
    def __init__(self, listAccs):
        self.listAccs = listAccs
