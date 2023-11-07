from data import *
from QEMU_sys.meta import *
from KVM.meta import *

QEMU_KVM = Transor("QEMU-KVM",
    {  HG("",
        Metaface(IsasUSR({isa}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR_PVL({isa})),
    ) for isa in Isa_KVMs},
    Date(2008,11,6), Date.today(), color="#F60", parent=QEMU_sys,
    desc="Git commit: 7ba1e61953f459: Add KVM support to QEMU",
)
Connector(KVM, QEMU_KVM, Date(2008,11,6))
