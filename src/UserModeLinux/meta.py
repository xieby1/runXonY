from data import *

Transor("User Mode Linux",
    {  HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
        term=Term.SYSCALL_COMPATIBLE_LAYER,
    ) for isa in Isa_LINUXs},
    Date(2001), Date.today(),
    desc="2006: User Mode Linux",
)
