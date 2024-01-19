import subprocess
from time import sleep

def main() :
    subprocess.call( "clear" )
    i = 0
    while 1 :
        print( i )
        i += 1
        sleep( 0.01 )
        subprocess.call( "clear" )

main()
    