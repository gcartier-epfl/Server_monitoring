#!/bin/python3

import yaml
import requests
from os import mkdir
from os.path import join, exists

SERVER_PORT = 8000

CWD = os.getcwd()
SERVER_DIR = "server_info"
MENU_DIR = "menu_info"

######## Thread harvesting data ########  

def load_yaml( file_name ) -> dict : 
    with open( file_name ) as f :
        data = yaml.safe_load( f )
    return data  

def request_usage( ip_address ) -> None :
    address = f'http://{ip_address}:{SERVER_PORT}'
    return requests.get( address ).text

def request_system_info( ip_address ) -> None :
    address = f'http://{ip_address}:{SERVER_PORT}/system_info'
    return requests.get( address ).text

# def harvest_info( config ) :  
#     for 

#########################################

def main() -> None : 
    config = load_yaml( "config.yaml" )
    
    if not exists( join( CWD, SERVER_DIR ) ) : mkdir( join( CWD, SERVER_DIR ) )
    if not exists( join( CWD, MENU_DIR ) ) : mkdir( join( CWD, MENU_DIR ) )

    print( request_usage( config['myVM']['ip'] ) )
    print( request_system_info( config['myVM']['ip'] ) )

main()