from data import *
from QEMU_user.meta import *
from LLVM.meta import *

REV_NG = Transor("REV.NG",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
    )},
    Date(2017), Date.today(), color="#E92B29", parent=QEMU_user,
    term=Term.DYNAMIC_STATIC_BINARY_TRANSLATOR,
    desc='''
        2017: REV.NG :A Unified Binary Analysis Framework to Recover CFGs and Function Boundaries
        2018: rev.ng: A Multi-Architecture Framework for Reverse Engineering and Vulnerability Discovery
        2019: Performance, Correctness, Exceptions: Pick Three
''',
)
Connector(LLVM, REV_NG, Date(2017))
