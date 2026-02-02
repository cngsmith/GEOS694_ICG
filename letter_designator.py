import sys

def _UTMLetterDesignator(lat):
    letter_dict = {
        'C': range(-80, -72),
        'D': range(-72, -64),
        'E': range(-64, -56),
        'F': range(-56, -48),
        'G': range(-48, -40),
        'H': range(-40, -32),
        'J': range(-32, -24),
        'K': range(-24, -16),
        'L': range(-16, -8),
        'M': range(-8, 0),
        'N': range(0, 8),
        'P': range(8, 16),
        'Q': range(16, 24),
        'R': range(24, 32),
        'S': range(32, 40),
        'T': range(40, 48),
        'U': range(48, 56),
        'V': range(56, 64),
        'W': range(64, 72),
        'X': range(72, 85)
        }

    for designator, lat_range in letter_dict.items():
        if lat in lat_range:
            return designator
    
    return 'Z'      #if function is not completed by for return, return Z

lat = float(sys.argv[int(1)])   #defining lat as first argument in command line
print(_UTMLetterDesignator(lat))