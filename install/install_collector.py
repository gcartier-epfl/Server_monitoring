from os import mkdir, makedirs, chmod, chown, popen 
from os.path import join, exists
from subprocess import check_output
import sys
import yaml
from pwd import getpwnam
from grp import getgrnam
from shutil import copyfile

def load_yaml( file_name ) -> dict : 
    with open( file_name ) as f :
        data = yaml.safe_load( f )
    return data  

def get_uid_from_user( user ) -> int :
    return getpwnam( user ).pw_uid 

def get_guid_from_group( group ) -> int : 
    return getgrnam( group ).gr_gid

def catch_control( command : str ) -> None : 
    try : 
        check_output( command, shell=True, executable="/bin/bash" )
    except Exception as error :
         print( "An exception occurred:", type(error).__name__, ' - ', error )
         sys.exit()



def main() -> None :  
    config = load_yaml( "config.yaml" )
    
    if not exists( config['collector_path'] ) : 
        print(">>> Workspace creation : ", config['collector_path'] )
        makedirs( config['collector_path'] )
    chown( config['workspace'], get_uid_from_user( config['user'] ), get_guid_from_group( config['group'] ) )
    catch_control( f"cp collector/*.py { join(config['workspace'], 'collector/') }" )
    catch_control( 'python3 -m pip install --user virtualenv' )
    catch_control( f"virtualenv { config['venv_name'] }")
    catch_control( f"source { join( config['venv_name'], '/bin/activate' ) }" )



main()