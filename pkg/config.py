import os
import yaml

def getConfig(config_file):
    # Read YAML file
    with open(config_file, 'r') as stream:
        config = yaml.safe_load(stream)

    s3_bucket = config['aws']['s3']['bucket']

    # Set the OS Enviroment
    os.environ['AWS_ACCESS_KEY_ID'] = config['aws']['credential']['access_key']
    os.environ['AWS_SECRET_ACCESS_KEY'] = config['aws']['credential']['secret_key']
    os.environ['AWS_DEFAULT_REGION'] = config['aws']['credential']['region']

    conf = {
        "s3_bucket": s3_bucket
    }

    return conf