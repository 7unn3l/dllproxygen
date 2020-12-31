from os.path import join,exists,dirname,normpath
class Project:
    def __init__(self,targetdll,outputpath,proxy_functions):
        self.dll = targetdll
        print('setting parameters for vs2019 project')

        self.projectname = self.dll.get_basename().split('.')[0]
        self.arch = self.dll.get_arch()
        self.outputpath = normpath(join(outputpath,self.projectname))
        self.proxy_functions = proxy_functions
        
        print(f"\nsolutionname: {self.projectname}")
        print(f"architecture: {self.arch} bit")
        print(f"outputpath  : {self.outputpath}\n")

        self._chk_paths()
        self._gen_fwd_exportlist()
    
    def _chk_paths(self):

        if exists(self.outputpath):
            print(f'{self.outputpath} already exists. aborting.')
            exit(-1)

        pdir = dirname(self.outputpath)
        if not exists(pdir) and pdir:
            print(f'parent directory {pdir} does not exist. aborting.')
            exit(-1)

    def _gen_fwd_exportlist(self):   
        print('generating linker comments for export forwarding...')
        fcache = self.proxy_functions.copy()
        out = ''
        e = 0
        bname = self.dll.get_basename()

        for exp,_ord in self.dll.get_exports():

            if exp in self.proxy_functions:
                fcache.remove(exp)
                out += f'//#pragma comment(linker,"/export:{exp}={bname}.orig.{exp},@{_ord}")\n'
            else:
                out += f'#pragma comment(linker,"/export:{exp}={bname}.orig.{exp},@{_ord}")\n'
            e += 1
        
        print(f'read {e} exports total')
        
        
        for fname in fcache:
            print(f'WARNING: {fname} function not found in dll exports')

        return out

    def _gen_src_files(self):
        pass
    
    def generate(self):
        pass

    pass