# -*- coding: utf-8 -*-
import sys 1

def main(): 2
    print 'Hello there', sys.argv[1] 3
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

if __name__ == '__main__': 4
    main()

