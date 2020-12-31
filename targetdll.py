# pylint: skip-file
from pefile import PE
from os.path import basename

class Targetdll():
    def __init__(self,dllpath):
        self.dllpath = dllpath
        self.pe = PE(self.dllpath)
        self.pe.parse_data_directories()

    def get_arch(self):
        return 32 if self.pe.FILE_HEADER.Machine == 0x014C else 64 

    def get_basename(self):
        return basename(self.dllpath)

    def get_exports(self):
        for exp in self.pe.DIRECTORY_ENTRY_EXPORT.symbols:
            yield (exp.name.decode(),exp.ordinal)