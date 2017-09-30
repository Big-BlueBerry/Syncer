import os 
import argparse

# set arguments to synchronize
parser = argparse.ArgumentParser()
parser.add_argument('--first', help='First dir to synchronize')
parser.add_argument('--second', help='Second dir to synchronize')
args = parser.parse_args()


if __name__ == '__main__':
    first = args.first
    second = args.second

    

