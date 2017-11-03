import os
import base64
import json
import getpass

template = """
{
   "kernel_python_credentials" : {
     "username": "{USERNAME}",
     "base64_password": "{BASE64ENCODEDPASSWORD}",
     "url": "https://{CLUSTERDNSNAME}.azurehdinsight.net/livy"
   },
   "kernel_scala_credentials" : {
     "username": "{USERNAME}",
     "base64_password": "{BASE64ENCODEDPASSWORD}",
     "url": "https://{CLUSTERDNSNAME}.azurehdinsight.net/livy"
   },
   "heartbeat_refresh_seconds": 5,
   "livy_server_heartbeat_timeout_seconds": 60,
   "heartbeat_retry_seconds": 1
 }
"""


def encode_pw(pw):
    return base64.b64encode(bytes(pw, 'utf-8')).decode('ascii')


def get_user_parameters():
    cluster_dns_name = input('1) Please enter the DNS name or IP Address of your HDInsight cluster: \n')
    user_name = input('2) Please enter your cluster username: \n')
    pw = encode_pw(getpass.getpass('3) Please enter your password: \n'))
    return cluster_dns_name, user_name, pw


def build_config():
    dns, user, pw = get_user_parameters()
    j = json.loads(template)

    # replace usernames
    j['kernel_python_credentials']['username'] = user
    j['kernel_scala_credentials']['username'] = user

    # replace passwords
    j['kernel_python_credentials']['base64_password'] = pw
    j['kernel_scala_credentials']['base64_password'] = pw

    # replace urls
    uri = 'https://{CLUSTERDNSNAME}.azurehdinsight.net/livy'.replace('{CLUSTERDNSNAME}', dns)
    j['kernel_python_credentials']['url'] = uri
    j['kernel_scala_credentials']['url'] = uri

    return j


def apply_config(config):
    user_directory = os.path.expanduser('~')
    sparkmagic_dir = user_directory + '\.sparkmagic'
    spark_config_file = sparkmagic_dir + '\config.json'

    # Create .sparkmagic directory if not exists
    if not os.path.exists(sparkmagic_dir):
        print('Creating directory {}'.format(sparkmagic_dir))
        os.makedirs(sparkmagic_dir)

    # Create json config file if not exists
    if not os.path.isfile(spark_config_file):
        print('Creating configuration file {}'.format(spark_config_file))
        with open(spark_config_file, 'w') as f:
            f.write(json.dumps(config, indent=4))

# Main
print('*' * 40)
print('Local Jupyter Notebook HDInsight Spark Configuration')
print('*' * 40 + '\n')

user_config = build_config()
apply_config(user_config)

print('*' * 40)
print('Configuration Complete!')
print('*' * 40 + '\n')