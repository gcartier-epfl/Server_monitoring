import platform
import json  
from datetime import datetime


def dump_json_to_file( dict, filename ) -> None :  
    with open( filename, 'w' ) as outputfile : 
        json.dump( dict, outputfile )  


def main() -> None : 
    data_file = "/var/Server_monitoring/collector/collected_data.json"
    timestamp = datetime.now().strftime( "%d/%m/%Y %H:%M:%S" )
    platform_info = platform.uname()
    dump_json_to_file( { 'hostname' : platform_info.node, 'timestamp' : timestamp, 'system' : { 'os': platform_info.system, 'os_distri': platform_info.version, 'kernel': platform_info.release }}, data_file )


main()