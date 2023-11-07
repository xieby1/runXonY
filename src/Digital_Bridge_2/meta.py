from data import *
from Digital_Bridge.meta import *

Transor("Digital Bridge 2",
    {  HG("",
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH
    )},
    Date(2006), parent=Digital_Bridge, dev=Dev.WCG_LAB,
    feat='''
        Dynamic + static bt
        lib wrapper
    ''',
    desc="2006: 二进制翻译中的库函数处理",
)
