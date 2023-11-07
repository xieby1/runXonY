from data import *

Kernel_WINEs_str: set[str] = {Kernel.LINUX.name, Kernel.MACOS.name, Kernel.BSD.name}
Kernel_WINEs: set[Kernel] = set(Kernel[name] for name in Kernel_WINEs_str)
Syslib_WINEs: set[Syslib] = set(Syslib[name] for name in Kernel_WINEs_str)
WINE = Transor("WINE",
    set(HG(
        "-".join((kname, isa.name)),
        Metaface({(isa, Up.USR)}, {Kernel[kname]}, {Syslib[kname]}, Lib_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    ) for isa in Isa_MODERN_WINDOWSs for kname in Kernel_WINEs_str),
    Date(1993,7,4), Date.today(), "#800000", "LGPL",
)
