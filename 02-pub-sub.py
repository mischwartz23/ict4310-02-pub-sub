# REDIS pub/sub example
# Author: Michael Schwartz
# File: 02-pub-sub.py

# Usage:
# Start redis-server in a command prompt or terminal window
#    redis-server

# You must have redis python interface available
#   Use pip (pip3) to install it if it is not avaiable
#     You will know if there is an error on the import statement)
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

# connect with redis server as Pat (Port 6379 is the default for Redis)
pat_redis = redis.Redis(host='localhost', port=6379, db=0)
# Create a pubsub connection to redis
pat_pubsub = pat_redis.pubsub()
# subscribe to Jazz "channel"
pat_pubsub.subscribe('Jazz')

# Freddy can also subscribe to the Jazz channel
freddy_redis = redis.Redis(host='localhost', port=6379, db=0)
freddy_pubsub = freddy_redis.pubsub()
freddy_pubsub.subscribe('Jazz')

# connect with redis server as Alex
alex_redis = redis.Redis(host='localhost', port=6379, db=0)
# publish new music in the channel Jazz
alex_redis.publish('Jazz', 'Milt Jackson')
print("Alex publishes Milt Jackson")

# Using get_message, Pat can see what has been published
# Pat's subscription message will be provided as a list
message = pat_pubsub.get_message()
print(f"Pat's subscription message: {str(message)}")

# Pat can see what Alex published as well
new_music = pat_pubsub.get_message()
print(f"Pat's next message: {str(new_music)}")

# Alex can publish more of the collection:
alex_redis.publish('Jazz', 'Dizzy Gillespie')
alex_redis.publish('Jazz', 'Ella Fitzgerald')
print("Alex publishes Dizzy Gillespie and Ella Fitzgerald")

# Pat can see what Alex published as well
new_music = pat_pubsub.get_message()['data']
print(f"Pat's next message: (data only): {str(new_music.decode('utf-8'))}")
new_music = pat_pubsub.get_message()['data']
print(f"Pat's next message: (data only): {str(new_music.decode('utf-8'))}")

# Publish one more to Alex's collection
alex_redis.publish('Jazz', 'Freddy Hubbard')
print("Alex publishes Freddy Hubbard")

# Freddy can also retrieve things from the Jazz channel
# We'll ignore subscribe messages
while freddy_playlist := freddy_pubsub.get_message():
    if freddy_playlist['type'] == "message":
        print(f"Freddy next message (data only): {str(freddy_playlist['data'].decode('utf-8'))}")

print("Done.")
