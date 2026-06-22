import heapq

class Twitter:

    def __init__(self):
        self.user_dict = {}
        self.time_stamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_dict:
            self.user_dict[userId] = {"tweets": [], "following": set()}
        self.time_stamp += 1
        tweet_content = (self.time_stamp, tweetId)
        self.user_dict[userId]["tweets"].append(tweet_content)
        print("tweet added")

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.user_dict)
        if userId not in self.user_dict:
            self.user_dict[userId] = {"tweets": [], "following": set()}
        feed = []
        tweets = []
        candidates = self.user_dict[userId]["following"] | {userId}
        n = 0
        for uid in candidates:
            if uid not in self.user_dict:
                self.user_dict[userId] = {"tweets": [], "following": set()}
            tweet = self.user_dict[uid]["tweets"][:]
            tweets.append(tweet)
            n += len(tweet)
        j = 0
        print(tweets)
        while j < 10 and j < n:
            latest_tid_time = -1
            index = 0
            for i in range(0, len(tweets)):
                if len(tweets[i]):
                    time, tid = tweets[i][-1]
                    if time > latest_tid_time:
                        latest_tid_time = time
                        index = i
            feed.append(tweets[index][-1][1])
            tweets[index].pop()
            j += 1
        
        print("feed generated")
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_dict:
            self.user_dict[followerId] = {"tweets": [], "following": set()}
        if followeeId not in self.user_dict:
            self.user_dict[followeeId] = {"tweets": [], "following": set()}
        self.user_dict[followerId]["following"].add(followeeId)
        print("followed")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_dict:
            self.user_dict[followerId] = {"tweets": [], "following": set()}
        if followeeId not in self.user_dict:
            self.user_dict[followeeId] = {"tweets": [], "following": set()}
        self.user_dict[followerId]["following"].discard(followeeId)
        print("unfollowed")
        
