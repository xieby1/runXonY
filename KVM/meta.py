from data import *
from Intel_VT.meta import *

KVM = Transor("KVM",
    {  HG("",
        Metaface(IsasUSR_PVL({isa}), {Kernel.LINUX}),
        Metaface(IsasUSR_PVL({isa})),
    ) for isa in Isa_KVMs},
    Date(2007,2,5), Date.today(), color="#000000",
    desc='''
        https://en.wikipedia.org/wiki/VirtualBox
    ''',
)
Connector(Intel_VT, KVM, Date(2007,2,5))
