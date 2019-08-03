import os

# grab the folder of the top-level directory of this project
basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

class Config(object):
    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY') or ''