from lib import *

###############################################################
#    __  __           _       _
#   |  \/  | ___   __| |_   _| | ___  ___
#   | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#   | |  | | (_) | (_| | |_| | |  __/\__ \
#   |_|  |_|\___/ \__,_|\__,_|_|\___||___/
#                                       figlet -f big modules

###############################################
#    ___
#   |_ _|___ __ _
#    | |(_-</ _` |
#   |___/__/\__,_|
#                           figlet -f small Isa

###############################################
#    _  __                 _
#   | |/ /___ _ _ _ _  ___| |
#   | ' </ -_) '_| ' \/ -_) |
#   |_|\_\___|_| |_||_\___|_|
#                           figlet -f small Kernel

# https://github.com/torvalds/linux/tree/master/arch
Isa_LINUXs: set[Isa] = \
    {Isa.ALPHA, Isa.ARC} | Isa_ARM32s | {Isa.ARM64,
    Isa.CSKY, Isa.HEXAGON, Isa.IA64, Isa.LOONGARCH, Isa.M68K,
    Isa.MICROBLAZE} | Isa_MIPS64s | {Isa.NIOS2, Isa.OPENRISC,
    Isa.PARISC} | Isa_POWERPC64s | Isa_RISCV64s | {Isa.S390,
    Isa.SH} | Isa_SPARC64s | Isa_X86_64s | {Isa.XTENSA}
Module(Kernel.LINUX.name, set(
    HG(isa.name, Metaface({(isa, Up.USR_PVL)}), Metaface({(isa,Up.USR)}, {Kernel.LINUX}))
for isa in Isa_LINUXs))

# https://www.freebsd.org/platforms/
Isa_BSDs: set[Isa] = \
    Isa_X86_64s | Isa_X86s | {Isa.AARCH64, Isa.ARM} | \
    Isa_ARMV6s | Isa_ARMV7s | Isa_MIPS64s | Isa_POWERPC64s | \
    Isa_RISCV64s | Isa_SPARC64s
# https://www.openbsd.org/plat.html
Isa_BSDs |= {Isa.ALPHA, Isa.HPPA}
Module(Kernel.BSD.name, set(
    HG(isa.name, Metaface({(isa, Up.USR_PVL)}), Metaface({(isa, Up.USR)}, {Kernel.BSD}))
for isa in Isa_BSDs))

Isa_MODERN_WINDOWSs: set[Isa] = {Isa.AARCH64, Isa.X86_64, Isa.X86}

###############################################
#    ___         _ _ _
#   / __|_  _ __| (_) |__
#   \__ \ || (_-< | | '_ \
#   |___/\_, /__/_|_|_.__/
#        |__/
#                           figlet -f small Syslib

Syslib_POSIXs: set[Syslib] = {Syslib.LINUX, Syslib.BSD, Syslib.MACOS}

###############################################
#    _    _ _
#   | |  (_) |__
#   | |__| | '_ \
#   |____|_|_.__/
#                           figlet -f small Lib
Module("-".join((Lib.ANY.name, Syslib.WINDOWS.name, Kernel.NO_SYSCALL.name)), set (
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS, Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs)
    )
for isa in Isa_MODERN_WINDOWSs))

###############################################
#    ___
#   / __|_  _ ___ __ _ _ __ _ __
#   \__ \ || (_-</ _` | '_ \ '_ \
#   |___/\_, /__/\__,_| .__/ .__/
#        |__/         |_|  |_|
#                           figlet -f small Sysapp
Module("-".join((Sysapp.ANY.name, Lib.ANY.name, Syslib.WINDOWS.name, Kernel.NO_SYSCALL.name)), set (
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS, Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs)
    )
for isa in Isa_MODERN_WINDOWSs))

###############################################
#      _
#     /_\  _ __ _ __
#    / _ \| '_ \ '_ \
#   /_/ \_\ .__/ .__/
#         |_|  |_|
#                           figlet -f small App
Module("APPS-WINDOWS-NO_SYSCALL", set (
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS, Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs, App_ANYs)
    )
for isa in Isa_MODERN_WINDOWSs))

###############################################################
#    _______
#   |__   __|
#      | |_ __ __ _ _ __  ___  ___  _ __ ___
#      | | '__/ _` | '_ \/ __|/ _ \| '__/ __|
#      | | | | (_| | | | \__ \ (_) | |  \__ \
#      |_|_|  \__,_|_| |_|___/\___/|_|  |___/
#                                       figlet -f big Transors

#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
Transor("Merge",
    {  HG("",
        Metaface({(Isa.I386, Up.USR)}, {Kernel.SCO_UNIX}),
        Metaface({(Isa.I386, Up.USR)}, {Kernel.DOS, Kernel.WINDOWS3_1})
    )},
    Date(1985,10,9), Date(2000),
    desc="https://en.wikipedia.org/wiki/Merge_(software)"
)
Transor("mx",
    {  HG("",
        Metaface({(Isa.ALPHA, Up.USR)}, {Kernel.OSF1}),
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.ULTRIX}),
    )},
    Date(1993), dev="Digital",
    desc="1993: Binary Translation by Richard L. Sites"
)
Transor("Shade",
    {  HG("MIPS.V8",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.UMIPSV, Up.USR), (Isa.MIPSI, Up.USR)}, {Kernel.SUNOS4_BSD}),
    ), HG("V8.V8-BSD",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}),
    ), HG("V9.V8-BSD",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV9, Up.USR)}, {Kernel.SUNOS4_BSD}),
    ), HG("V8.V8-UNIX",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}),
    ), HG("V9.V8-UNIX",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV9, Up.USR)}, {Kernel.SUNOS5_UNIX}),
    )},
    Date(1993), dev="SUN",
    desc="1994: Shade: a fast instruction-set simulator for execution profiling"
)
Transor("VEST",
    {  HG("",
        Metaface({(Isa.ALPHA, Up.USR)}, {Kernel.OPENVMS}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.VAX, Up.USR)}, {Kernel.OPENVMS}),
    )},
    Date(1993), dev="Digital",
    desc="1993: Binary Translation by Richard L. Sites",
)
# TODO: Android
Kernel_WINEs_str: set[str] = {Kernel.LINUX.name, Kernel.MACOS.name, Kernel.BSD.name}
Kernel_WINEs: set[Kernel] = set(Kernel[name] for name in Kernel_WINEs_str)
Syslib_WINEs: set[Syslib] = set(Syslib[name] for name in Kernel_WINEs_str)
Transor("WINE",
    set(HG(
        "-".join((kname, isa.name)),
        Metaface({(isa, Up.USR)}, {Kernel[kname]}, {Syslib[kname]}, Lib_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    ) for isa in Isa_MODERN_WINDOWSs for kname in Kernel_WINEs_str),
    Date(1993,7,4), Date.today(), "#800000", "LGPL",
)
Transor("Cygwin",
    {  HG("",
        Metaface(IsasUSR(Isa_MODERN_WINDOWSs), {Kernel.WINDOWS}),
        Metaface({(Isa.NONE, Up.NONE)}, {Kernel.NONE}, Syslib_POSIXs, srcs={Src.C, Src.CPP}),
    )},
    Date(1995,10,18), Date.today(), "#99003F",
)
Transor("FX!32",
    {  HG("",
        Metaface({(Isa.ALPHA, Up.USR)}, {Kernel.WINDOWS_NT4_0}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.WINDOWS_NT4_0}),
    )},
    Date(1996), dev="Digital",
    desc = '''1997: DIGITAL FX!32: Combining Emulation and Binary Translation
1998: FX!32 A Profile-Directed Binary Translator'''
)
Transor("DAISY",
    {  HG("",
        Metaface({(Isa.DAISY_VLIW, Up.USR_PVL)}),
        Metaface({(Isa.POWERPC, Up.USR_PVL)}),
    )},
    Date(1998), Date(2001), dev="IBM",
    desc = '''
        1997: DAISY dynamic compilation for 100% architecutral compatibility
        2000: Binary Translation and Architecture Convergence Issues for IBM System/390
        2000: full system binary translation RISC to VLIW
        2000: simulation and debugging of full system bianry translation
        2001: Dynamic binary translation and optimization
    '''
)


# TODO: user-mode linux
Isa_QEMU_user_hs: set[Isa] = {
    Isa.AARCH64, Isa.ARM, Isa.X86, Isa.X86_64,
    Isa.LA64, Isa.MIPS32, Isa.MIPS64,
    Isa.POWERPC, Isa.RISCV64, Isa.S390X, Isa.SPARC,
}
Isa_QEMU_user_gs: set[Isa] = {
    Isa.ALPHA, Isa.ARM, Isa.AARCH64, Isa.X86, Isa.X86_64,
    Isa.AVR, Isa.CRIS, Isa.HEXAGON, Isa.HPPA, Isa.M68K,
    Isa.MICROBLAZE, Isa.MIPS32, Isa.MIPS64, Isa.NIOS2,
    Isa.OPENRISC, Isa.POWERPC, Isa.RISCV64, Isa.RX,
    Isa.S390X, Isa.SH4, Isa.SPARC, Isa.TRICORE, Isa.XTENSA,
}
Transor("QEMU-user",
    {  HG("linux",
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX})
    ), HG("bsd",
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_BSDs), {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_BSDs), {Kernel.BSD})
    ), HG("tci-linux",
        Metaface(IsasUSR(Isa_LINUXs), {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX})
    ), HG("tci-bsd",
        Metaface(IsasUSR(Isa_BSDs), {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_BSDs), {Kernel.BSD})
    )},
    Date(2003,2), Date.today(), "#F60", "IR",
    "2005: QEMU, a Fast and Portable Dynamic Translator",
)

# Lastly, add dummy modules after all modules are added
addDummyModules()
