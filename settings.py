from definitions.accounts import definitions as accounts

DOMAIN = {'accounts': accounts}

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = ''
MONGO_PORT = 

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = ''
MONGO_PASSWORD = ''

MONGO_DBNAME = ''
