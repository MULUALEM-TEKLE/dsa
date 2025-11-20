class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1 
        self.user_tweets[userId].append([self.timestamp , tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        users_to_check = self.follow_map[userId].union({userId})

        feed = []
        MAX_TWEETS = 10
        for followeeId in users_to_check : 
            timeline = self.user_tweets[followeeId]
            for ts,tid in timeline[-MAX_TWEETS :] : 
                heappush(feed , [-ts , tid])
        res = []
        for i in range(10) : 
            if feed : 
                ts , tid = heappop(feed)
                res.append(tid)
            else : 
                break
        return res 
 
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId : 
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follow_map[followerId] : 
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)