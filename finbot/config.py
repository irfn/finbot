import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    PERSIST_DIRECTORY=(str, "./db/chroma")
)
# reading .env file
environ.Env.read_env()

CONFLUENCE_SPACE_NAME = env('CONFLUENCE_SPACE_NAME')
CONFLUENCE_SPACE_KEY = env('CONFLUENCE_SPACE_KEY')
CONFLUENCE_USERNAME = env('CONFLUENCE_USERNAME')
CONFLUENCE_API_KEY = env('CONFLUENCE_API_KEY')
PERSIST_DIRECTORY  = env('PERSIST_DIRECTORY')