import heapq

class Twitter:

    def __init__(self):
        self.user_dict = {}
        self.time_stamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_dict:
            self.user_dict[userId] = {"tweets": [], "following": set()}
        self.time_stamp += 1
        tweet_content = (-self.time_stamp, tweetId)
        self.user_dict[userId]["tweets"].append(tweet_content)
        print("tweet added")

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_dict:
            self.user_dict[userId] = {"tweets": [], "following": set()}
        feed = []
        heap = []
        candidates = self.user_dict[userId]["following"] | {userId}
        for uid in candidates:
            if uid not in self.user_dict:
                self.user_dict[uid] = {"tweets": [], "following": set()}
            tweet = self.user_dict[uid]['tweets']
            if tweet:
                idx = len(tweet) - 1
                neg_ts, tid = tweet[idx]
                heapq.heappush(heap, (neg_ts, tid, uid, idx))
        # print(tweets)
        while heap and len(feed) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                idx -= 1
                neg_ts, tid = self.user_dict[uid]['tweets'][idx]
                heapq.heappush(heap, (neg_ts, tid, uid, idx))
    
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
        
