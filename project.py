from os.path import join,exists,dirname,normpath
from os import mkdir
from shutil import rmtree

class Project:
    def __init__(self,targetdll,outputpath,proxy_functions,overwrite):
        self.dll = targetdll
        print('setting parameters for vs2019 project')

        self.projectname = self.dll.get_basename().split('.')[0]
        self.arch = self.dll.get_arch()
        self.outputpath = normpath(join(outputpath,self.projectname))
        self.proxy_functions = proxy_functions
        
        print(f"\nsolutionname: {self.projectname}")
        print(f"architecture: {self.arch}")
        print(f"outputpath  : {self.outputpath}\n")

        self._chk_paths(overwrite)
        self._gen_src_files()
    
    def _chk_paths(self,overwrite):

        if exists(self.outputpath):
            if overwrite:
                print(f'{self.outputpath} already exists, removing.')
                rmtree(self.outputpath)
            else:
                print(f'{self.outputpath} already exists. aborting.')
                print('sepcify --overwrite to overwrite dir')
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

        for exp,_ord in self.dll.get_exports():

            if exp in self.proxy_functions:
                fcache.remove(exp)
                out += f'//#pragma comment(linker,"/export:{exp}={self.projectname}.orig.{exp},@{_ord}")\n'
            else:
                out += f'#pragma comment(linker,"/export:{exp}={self.projectname}.orig.{exp},@{_ord}")\n'
            e += 1
        
        print(f'read {e} exports total')
        
        
        for fname in fcache:
            print(f'WARNING: {fname} function not found in dll exports')

        return out

    def _format_vars(self,text,**kwargs):        
        for k,v in kwargs.items():
            k = k.upper()
            text = text.replace(f'%{k}%',str(v))
        
        return text

    def _gen_functions(self):
        func_decl = ''
        func_def = ''
        def_cont = ''

        for func in self.proxy_functions:
            func_decl += f'{self.projectname}_API int my{func}();\n'
            func_def  += f'int my{func}(){{return 0;}};\n'
            def_cont  += f'\t{func}=my{func}\n'

        return func_decl,func_def,def_cont

    def _gen_src_files(self):
        print('generating source files...')
        files = {'premake.lua':'','proj.def':'','proxy.cpp':'','proxy.h':''}

        rf = lambda f: open(join('templates',f),'r').read()
        wf = lambda f,c: open(join(self.outputpath,f),'w').write(c)

        files['premake5.lua'] = self._format_vars(rf('premake5.lua'),arch=self.arch,proj_name=self.projectname)
        
        fwd_exports = self._gen_fwd_exportlist()
        func_decl,func_def,def_cont = self._gen_functions()

        files['proj.def'] = self._format_vars(rf('proj.def'),proj_name=self.projectname,def_contents=def_cont)
        files['proxy.h'] = self._format_vars(rf('proxy.h'),fwd_exports=fwd_exports,proj_name=self.projectname,functions_header=func_decl)
        files['proxy.cpp'] = self._format_vars(rf('proxy.cpp'),functions=func_def)

        print('creating directory...')
        mkdir(self.outputpath)

        for f in files:
            print(f'writing {f}...')
            wf(f,files[f])

    def generate(self):
        pass