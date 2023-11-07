from data import *
from KVM.meta import *

multipass = Transor("multipass",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX}),
        term=Term.V2_,
    )},
    Date(2017,12,7), Date.today(), color="#E95420", license="GPL3", dev=Dev.CANONICAL,
    desc="https://github.com/canonical/multipass",
)
# TODO: windows:hyper-v, macos:hyperkit
Connector(KVM, multipass, Date(2017,12,7))
