from data import *

Transor("Linuxulator", set(
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.BSD}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
    )
    for isa in Isa_FreeBSDs),
    Date(2006), Date.today(),
    desc='''
        Mail from wine-devel: 2004-August.txt: 26171: `kernel compatibility layer`
        2006: Linux emulation in FreeBSD
    '''
)
