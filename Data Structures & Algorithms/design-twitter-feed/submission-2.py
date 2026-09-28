from collections import OrderedDict, defaultdict
class Twitter:

    def __init__(self):
        self.posts = OrderedDict()
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[tweetId] = userId
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for key, val in reversed(self.posts.items()):
            if len(res) == 10:
                break
            if (userId in self.follows and  val in self.follows[userId]) or val == userId:
                res.append(key)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
