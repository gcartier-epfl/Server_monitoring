import subprocess
import yaml
import cv2
from color import colored, txt_effect, txt_colors
from time import sleep

SERVER_CONFIG = "server_config.yaml"

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
                # print(info)
                print( colored( f'\t\t{info} : ', txt_colors.ORANGE ), config[c][m][info] )
        print()


def main() -> int :
    config = load_yaml( SERVER_CONFIG )
    refresh_console()
    while True :
        sleep( 0.1 )
        refresh_console()
        display_menu( config )  
    return 0


main()
    