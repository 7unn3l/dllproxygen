class Project:
    def __init__(self,targetdll,outputpath,proxy_functions):
        self.dll = targetdll
        print('setting parameters for vs2019 project')

        self.projectname = self.dll.get_basename().split('.')[0]
        self.arch = self.dll.get_arch()
        self.outputpath = outputpath
        self.proxy_functions = proxy_functions
        

        print(f"solutionname: {self.projectname}")
        print(f"architecture: {self.arch} bit")
        print(f"outputpath  : {self.outputpath}")
    
    def _chk_config(self):
        pass

    def _gen_src_files(self):
        pass
    
    def generate(self):
        pass