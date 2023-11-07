from data import *

Xen = Transor("Xen",
    {  HG("",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR_PVL)}),
        ) for isa in [Isa.X86, Isa.X86_64]
    } | { HG("Paravirtualized",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR)}),
        ) for isa in [Isa.X86, Isa.X86_64]
    },
    Date(2003), Date.today(), term=Term.TYPE1_VIRTUAL_MACHINE_AND_PARAVIRTUALIZATION,
    desc="https://en.wikipedia.org/wiki/Xen",
)
