import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)    # store a list of [time, tweetId]
        self.followMap = defaultdict(set)    # store a set of unique followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1   # More Negative Time = More Recent

    def getNewsFeed(self, userId: int) -> list[int]:
        self.minHeap = []
        heapq.heapify(self.minHeap)

        # Make sure that the user follows themselves
        self.followMap[userId].add(userId)
        # For every followeeId, add the most recent tweet to the MinHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                recent_index = len(self.tweetMap[followeeId])-1
                time, tweetId = self.tweetMap[followeeId][recent_index]
                next_position_to_look = recent_index-1
                heapq.heappush(self.minHeap, [time, tweetId, followeeId, next_position_to_look])

        result = []
        while self.minHeap and len(result) < 10:
            time, tweetId, followeeId, recent_position = heapq.heappop(self.minHeap)
            result.append(tweetId)
            # If the same user has more tweets, add the recent one to the MinHeap
            if recent_position >= 0:
                time, tweetId = self.tweetMap[followeeId][recent_position]
                next_position_to_look = recent_position - 1
                heapq.heappush(self.minHeap, [time, tweetId, followeeId, next_position_to_look])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)