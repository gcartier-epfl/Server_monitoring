#!/bin/python3

import os
import subprocess
import platform
import yaml
from color import colored, txt_effect, txt_colors
from time import sleep

SERVER_CONFIG = "server_config.yaml"
TXT_COLORS = [txt_colors.PURPLE, txt_colors.ORANGE, txt_colors.GREEN, txt_colors.CYAN, txt_colors.RED]
TXT_EFFECTS = [txt_effect.BOLD, txt_effect.UNDERLINE]


def load_yaml( file_name ) -> dict : 
    with open( file_name ) as f :
        yaml_f = yaml.safe_load( f )
    return yaml_f

def refresh_console() -> None :
    subprocess.call( "clear" )

def display_menu( config ) -> None : 
    for c in config : 
        print( colored( f'{c} :', txt_colors.PURPLE, txt_effect.BOLD) )
        for m in config[c] :
            print( colored( f'\t{m} :', txt_colors.GREEN, txt_effect.UNDERLINE) )
            for info in config[c][m] : 
                print( colored( f'\t\t{info} : ', txt_colors.ORANGE ), config[c][m][info] )
        print()

def display_menu_rec( config, index = None ) -> None :
    i = 0 if index == None else index+1
    for c in config :
        if type( config[c] ) != dict :
            print( i*'\t', colored( f'{c} :', TXT_COLORS[i], TXT_EFFECTS[i] if i<2 else None), f'{config[c]}' ) 
        else :
            print( i*'\t', colored( f'{c} :', TXT_COLORS[i], TXT_EFFECTS[i] if i<2 else None) )
            display_menu_rec( config[c], i )


def main() -> int :
    config = load_yaml( SERVER_CONFIG )
    refresh_console()
    while True :
        sleep( 0.1 )
        refresh_console()
        display_menu_rec( config )
        print( platform.uname() )
        print( platform.version() )


# main()
