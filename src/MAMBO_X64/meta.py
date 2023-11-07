from data import *

MAMBO_X64 = Transor("MAMBO-X64",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR)}, {Kernel.LINUX}),
    )},
    Date(2017), Date.today(), dev=Dev.MANCHESTER,
    desc='''
        2017: Low Overhead Dynamic Binary Translation on ARM
    ''',
)
