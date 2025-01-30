# In another window, run this file under python

# Every message read from a PubSub instance will be a dictionary with the following keys.
##  type: one of the following: "subscribe", "unsubscribe", "psubscribe",
##                              "punsubscribe", "message", "pmessage"
##  channel: The channel [un]subscribed to or the channel a message was published to
##  pattern: The pattern that matched a published message's channel.
##           Will be None in all cases except for 'pmessage' types.
##  data: The message data.
##        With [un]subscribe messages, this value will be the number of channels and patterns
##        the connection is currently subscribed to.
##        With [p]message messages, this value will be the actual published message.

# NOTE: Published messages are only available to clients who have subscribed _before_
#       the messages were published.
# NOTE: The b'data' denotes an encoded byte array

"""This is an extremely basic pub/sub example."""

import redis

michael_redis = redis.Redis(host='localhost', port=6379, db=0)
# Create a pubsub connection to redis
michael_pubsub = michael_redis.pubsub()

# subscribe to Jazz "channel"
michael_pubsub.subscribe('Jazz')

# We'll ignore subscribe messages
count = 1
for michael_playlist in michael_pubsub.listen():
    playlist = michael_playlist
    print(playlist)
    if playlist['type'] == "message":
        print(f"Michael next message (data only): {count}: {str(playlist['data'].decode('utf-8'))}")
        print(f"    Oooh! I just love {str(playlist['data'].decode('utf-8'))}")
        count += 1
        if count == 10:
            michael_pubsub.unsubscribe()
        if count == 11:
            break;

print("Done.")
