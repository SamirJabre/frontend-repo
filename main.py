import sys
sys.path.append('..')
from config_reader import load_config

config = load_config()
if config['run_localhost']:
    print("Running in localhost mode")
else:
    print("Running in production mode")