from data import *

Digital_Bridge = Transor("Digital Bridge",
    {  HG("",
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
    )},
    Date(2004), Date(2006), dev=Dev.WCG_LAB, feat="Dynamic + static bt",
    desc='''
        2004: 二进制翻译关键技术研究
        2005: 优化动态二进制翻译器DigitalBridge
    ''',
)
