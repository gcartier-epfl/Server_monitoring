
class txt_colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'

class txt_effect :
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def colored( txt, color, effect=None ) -> str :  
    return f'{color}{"" if effect == None else effect}{txt}{txt_effect.ENDC}'


test =  colored( "Header", txt_colors.PURPLE, txt_effect.BOLD ) + \
        colored( "OKBLUE", txt_colors.BLUE ) + \
        colored( "OKCYAN", txt_colors.CYAN ) + \
        colored( "OKGREEN", txt_colors.GREEN, txt_effect.UNDERLINE ) + \
        colored( "WARNING", txt_colors.ORANGE ) + \
        colored( "FAIL", txt_colors.RED )

# print( test )