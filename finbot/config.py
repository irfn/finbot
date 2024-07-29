import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    INIT_DB=(bool, False),
    PERSIST_DIRECTORY=(str, "./db/chroma")
)
# reading .env file
environ.Env.read_env()
environ.Env.read_env()
#import ipdb; ipdb.set_trace()

class Config:
    def __init__(self):
        self.INIT_DB = env('INIT_DB')
        self.CONFLUENCE_URL = env('CONFLUENCE_URL')
        self.CONFLUENCE_SPACE_NAME = env('CONFLUENCE_SPACE_NAME')
        self.CONFLUENCE_SPACE_KEY = env('CONFLUENCE_SPACE_KEY')
        self.CONFLUENCE_USERNAME = env('CONFLUENCE_USERNAME')
        self.CONFLUENCE_API_KEY = env('CONFLUENCE_API_KEY')
        self.PERSIST_DIRECTORY  = env('PERSIST_DIRECTORY')

