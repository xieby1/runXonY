from data import *

Transor("BPF(JIT)",
    {  HG("",
        Metaface(IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
        Metaface({(Isa.BPF, Up.USR)}),
    )},
    Date(2011,4), Date.today(),
    renames=[Rename(
        "eBPF",
        Date(2014,9,4),
        "https://lwn.net/Articles/740157/ : commit daedfb22451d in 2014, the eBPF virtual machine was exposed directly to user space."
    )],
)
