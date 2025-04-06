# ict4310-02-pub-sub
Chapter 2 example from van Steen &amp; Tanenbaum using redis rather than Linda

This example uses Redis for publish-subscribe (rather than Linda tuple space)

The new Python 'pip' command only wants to work with virtual environments, and this example uses the redis module for Python.

This will use 3 different Terminal / Command Prompts
All should use this directory as the current directory

1) Start the redis server in the 1st window: redis-server

2) To to the 2nd window
3) Create a virtual environment: python3 -m venv 02venv      
4) Source the activation for the environmnet: source 02venv/bin/activate
   Your prompt should reflect the virtual environment
5) Add  the redis module: python3 -m pip install redis
6) Run the listener: python3 02-listener.py

7) go to the 3rd window
8) Source the activation for the environment:
9) Run the client: python3 02-pub-sub.py

You should have a series of received messages in the listener window, Michael's postings, based on topics of interest (Jazz)
Running the client 02-pub-sub.py multiple times will have that effect

You can also interact with the server through a standard redis client.
To do that, create a new Terminal window, change to the working directory, activate the virtual environment, and issue the command:
python3 -c "import redis, code; code.interact(local=locals())"

This will create a cli environment with the module redis already imported.
You can connect with redis:
    my_redis = redis.Redis(host='localhost', port=6379, db=0)
    my_pubsub = my_redis.pubsub()
    my_pubsub.subscribe('Jazz')
    my_pubsub.publish('Folk','Arlo Guthrie')
and so forth

