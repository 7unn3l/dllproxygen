from cmdline import parse_args
from targetdll import Targetdll
from project import Project

def main():
    args = parse_args()
    
    dll = Targetdll(args.targetdll)
    proj = Project(dll,args.outputdir,args.functions)
    proj.generate()


if __name__ == '__main__':
    main()
