import argparse
parser = argparse.ArgumentParser()
parser.add_argument('targetdll',help='path of dll file to proxy')
parser.add_argument('outputdir',help='path of the final visual studio project folder')
parser.add_argument('--functions',help='functions to hook, seperated by comma')
parser.add_argument('--overwrite',help='overwrite output directory if already present',action='store_true')

def parse_args():
    args = parser.parse_args()
    args.functions = [x.strip() for x in args.functions.split(',')] if args.functions else []

    return args