from data import *
from KVM.meta import *

captive = Transor("captive",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
        Metaface({(Isa.ARM32, Up.USR_PVL)}),
    )},
    Date(2016), Date(2019),
    desc='''
        2016: Hardware-Accelerated Cross-Architecture Full-System Virtualization
        2017: Efficient Cross-architecture Hardware Virtualisation
        2019: A Retargetable System-Level DBT Hypervisor
    ''',
)
Connector(KVM, captive, Date(2016))
