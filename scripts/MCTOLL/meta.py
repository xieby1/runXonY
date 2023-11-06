from data import *
from LLVM.meta import *

Transor("MCTOLL",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR({Isa.X86_64, Isa.AARCH64}), {Kernel.LINUX}),
    )},
    Date(2019), Date.today(), dev=Dev.MICROSOFT, parent=LLVM,
    desc='''
        https://github.com/microsoft/llvm-mctoll
        2019: Raising Binaries to LLVM IR with MCTOLL (WIP Paper)
    ''',
)
