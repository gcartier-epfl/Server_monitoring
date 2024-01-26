from os import mkdir, makedirs 
import yaml

def load_yaml( file_name ) -> dict : 
    with open( file_name ) as f :
        data = yaml.safe_load( f )
    return data  

def main() -> None :  
    config = load_yaml( "config.yaml" )
    makedirs( config['workspace' ] )


main()