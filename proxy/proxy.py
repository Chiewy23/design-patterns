from abc import abstractmethod


class TwitterBase:
    @abstractmethod
    def display_tweets(self):
        pass


class RealTimeTweets(TwitterBase):
    def __init__(self, twitter_handle):
        self.twitter_handle = twitter_handle

    def display_tweets(self):
        print(f"Displaying tweets for {self.twitter_handle}")


class ProxyServer(TwitterBase):
    real_time_tweets = None

    def __init__(self, twitter_handle, password):
        self.twitter_handle = twitter_handle
        self.password = password

    def display_tweets(self):
        if self.password == "Pass123":
            if self.real_time_tweets is None:
                self.real_time_tweets = RealTimeTweets(self.twitter_handle)

            self.real_time_tweets.display_tweets()
