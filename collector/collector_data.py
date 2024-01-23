import platform
import os
import json  
from datetime import datetime


def dump_json_to_file( dict, filename ) -> None :  
    with open( filename, 'w' ) as outputfile : 
        json.dump( dict, outputfile )  


def main() -> None : 
    CWD = os.getcwd()
    OUTPUT_FILE = "collected_data.json"
    timestamp = datetime.now().strftime( "%d/%m/%Y %H:%M:%S" )
    platform_info = platform.uname()
    dump_json_to_file( { 'hostname' : platform_info.node, 'timestamp' : timestamp, 'system' : { 'os': platform_info.system, 'os_distri': platform_info.version, 'kernel': platform_info.release }, 'path' : os.path.join( CWD, OUTPUT_FILE ) }, os.path.join( CWD, OUTPUT_FILE ) )


main()