from data import *

Intel_VT = Transor("Intel VT", set(  HG("",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR_PVL)}),
    )
    for isa in (Isa.X86, Isa.X86_64)),
    Date(2006), Date.today(), "#0071C5", dev=Dev.INTEL,
    desc="Intel ® Virtualization Technology: Hardware Support for Efficient Processor Virtualization",
)
