########################################################################################################
#                                           Library
########################################################################################################
import urllib3
import platform
from os import environ

#############################  Paths  ##########################################
project_name = 'test'
if platform.system().lower() == 'windows':
    path = "../"
else:
    path = ""
#############################  ConfigFile  #####################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
api_path_prefix = environ['api_prefix']
###############################  Database  ####################################
db_driver = environ['db_driver']
db_address = environ['db_address']
db_port = environ['db_port']
db_name = environ['db_name']
db_username = environ['db_username']
db_password = environ['db_password']
