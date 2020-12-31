# pylint: skip-file
from pefile import PE
from os.path import basename

class Targetdll():
    def __init__(self,dllpath):
        print(f'parsing {dllpath}')
        self.dllpath = dllpath
        try:
            self.pe = PE(self.dllpath)
            self.pe.parse_data_directories()
        except Exception as e:
            print(f'could not parse dll: {e}')
            exit(-1)

    def get_arch(self):
        return "x86" if self.pe.FILE_HEADER.Machine == 0x014C else "x86_64" 

    def get_basename(self):
        return basename(self.dllpath)

    def get_exports(self):
        for exp in self.pe.DIRECTORY_ENTRY_EXPORT.symbols:
            yield (exp.name.decode(),exp.ordinal)