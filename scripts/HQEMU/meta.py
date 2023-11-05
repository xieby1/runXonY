from data import *
from QEMU_user.meta import *
from LLVM.meta import *

HQEMU = Transor("HQEMU",
    {  HG("",
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.ARM64, Isa.POWERPC64}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.ARM, Isa.ARM64}), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    )},
    Date(2012), Date(2018), color="#F60", parent=QEMU_user, dev=Dev.TQH,
    feat="multi thread opt",
    desc='''
        2012: HQEMU: A Multi-Threaded and Retargetable Dynamic Binary Translator on Multicores
        2013: Efficient and Retargetable Dynamic Binary Translation on Multicores
        2018: HQEMU v2.5.2 Technical Report
    ''',
)
Connector(LLVM, HQEMU, Date(2012))
