from os import mkdir, makedirs, chmod, chown, popen 
from os.path import join, exists
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



def main() -> None :  
    config = load_yaml( "config.yaml" )
    
    if not exists( config['workspace'] ) : makedirs( config['workspace' ] )
    chown( config['workspace'], get_uid_from_user( config['user'] ), get_guid_from_group( config['group'] ) )
    popen( f"cp collector/*.py { join(config['workspace'], 'collector/') }" )
    popen( 'python3 -m pip install virtualenv' )
    popen( f"virtualenv { config['venv_name'] }")
    popen( f"source { join( config['venv_name'], '/bin/activate' ) }" )



main()