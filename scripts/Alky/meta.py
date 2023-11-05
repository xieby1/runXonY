from data import *

Transor("Alky",
    {  HG("",
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    )},
    Date(2006), Date(2008,1), license="LGPL", dev=Dev.FALLING_LEAF_SYSTEM,
    feat='''
        OpenGL static converter,
        written in python,
        LibAlky is DX10 runtime only work on WinXP
    '''
)
