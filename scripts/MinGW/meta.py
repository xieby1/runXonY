from data import *

Transor("MinGW",
    {  HG("",
        Metaface(IsasUSR(Isa_MODERN_WINDOWSs), {Kernel.WINDOWS}),
        Metaface({(Isa.NONE, Up.NONE)}, {Kernel.NONE}, {Syslib.WINDOWS}, srcs={Src.C, Src.CPP}),
    )},
    Date(1998,7,1), Date.today(), "#71B21F",
    feat='''
        Run on MSVC runtime
        Can be compiled on Win and Linux
    '''
)
