#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#


# @lc code=start
class User:
    user_id: int
    followers: set[int]

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.followers = set()

    def follow(self, followee_id: int):
        if followee_id in self.followers:
            return
        self.followers.add(followee_id)

    def unfollow(self, followee_id: int):
        if followee_id not in self.followers:
            return
        self.followers.remove(followee_id)


class Post:
    tweet_id: int
    user: User

    def __init__(self, tweet_id: int, user: User):
        self.tweet_id = tweet_id
        self.user = user


class Twitter:
    posts: list[Post]
    users: dict[str, User]

    def __init__(self):
        self.posts = []
        self.users = {}

    def getUser(self, userId: int) -> User:
        self.users[userId] = self.users.get(userId, User(userId))
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUser(userId)
        self.posts.insert(0, Post(tweetId, user))

    def getNewsFeed(self, userId: int) -> list[int]:
        return [
            post.tweet_id for post in self.posts
            if post.user.user_id == userId or userId in post.user.followers
        ][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        followee = self.getUser(followeeId)
        followee.follow(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followee = self.getUser(followeeId)
        followee.unfollow(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(1, 5)
# r = obj.getNewsFeed(1)
# print(r)
# obj.follow(1, 2)
# obj.postTweet(2, 6)
# r = obj.getNewsFeed(1)
# print(r)
# obj.unfollow(1, 2)
# r = obj.getNewsFeed(1)
# print(r)
# @lc code=end
