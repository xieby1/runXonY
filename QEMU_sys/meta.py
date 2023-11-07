from data import *
from QEMU_user.meta import *

QEMU_sys = Transor("QEMU-sys",
    {  HG(Kernel.LINUX.name,
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface(IsasUSR_PVL(Isa_QEMU_user_gs)),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    ), HG(Kernel.MACOS.name,
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_MODERN_MACOSs), {Kernel.MACOS}, {Syslib.MACOS}, {Lib.ANY}),
        Metaface(IsasUSR_PVL(Isa_QEMU_user_gs)),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    ), HG(Kernel.WINDOWS.name,
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_MODERN_WINDOWSs), {Kernel.WINDOWS}, {Syslib.WINDOWS}, {Lib.ANY}),
        Metaface(IsasUSR_PVL(Isa_QEMU_user_gs)),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    ), HG(Kernel.BSD.name,
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_BSDs), {Kernel.BSD}, {Syslib.BSD}, {Lib.ANY}),
        Metaface(IsasUSR_PVL(Isa_QEMU_user_gs)),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    )},
    Date(2003,10), Date.today(), "#F60", "IR", parent=QEMU_user,
    desc='''
        2005: QEMU, a Fast and Portable Dynamic Translator
        gitL v0.5.0
    ''',
)
