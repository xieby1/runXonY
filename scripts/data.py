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
    IO(isa.name, Metaface({isa}), Metaface({isa}, {Kernel.LINUX}))
for isa in Isa_LINUXs))

# https://www.freebsd.org/platforms/
Isa_BSDs: set[Isa] = \
    Isa_X86_64s | Isa_X86s | {Isa.AARCH64, Isa.ARM} | \
    Isa_ARMV6s | Isa_ARMV7s | Isa_MIPS64s | Isa_POWERPC64s | \
    Isa_RISCV64s | Isa_SPARC64s
# https://www.openbsd.org/plat.html
Isa_BSDs |= {Isa.ALPHA, Isa.HPPA}
Module(Kernel.BSD.name, set(
    IO(isa.name, Metaface({isa}), Metaface({isa}, {Kernel.BSD}))
for isa in Isa_BSDs))

Isa_MODERN_WINDOWSs: set[Isa] = {Isa.AARCH64, Isa.X86_64, Isa.X86}

###############################################
#    ___         _ _ _
#   / __|_  _ __| (_) |__
#   \__ \ || (_-< | | '_ \
#   |___/\_, /__/_|_|_.__/
#        |__/
#                           figlet -f small Syslib

###############################################
#    _    _ _
#   | |  (_) |__
#   | |__| | '_ \
#   |____|_|_.__/
#                           figlet -f small Lib
Module("-".join((Lib.ANY.name, Syslib.WINDOWS.name, Kernel.NO_KERNEL.name)), set (
    IO(isa.name,
        Metaface({isa}, {Kernel.WINDOWS, Kernel.NO_KERNEL}, {Syslib.WINDOWS}),
        Metaface({isa}, {Kernel.NO_KERNEL}, {Syslib.WINDOWS}, Lib_ANYs)
    )
for isa in Isa_MODERN_WINDOWSs))

###############################################
#    ___
#   / __|_  _ ___ __ _ _ __ _ __
#   \__ \ || (_-</ _` | '_ \ '_ \
#   |___/\_, /__/\__,_| .__/ .__/
#        |__/         |_|  |_|
#                           figlet -f small Sysapp
Module("-".join((Sysapp.ANY.name, Lib.ANY.name, Syslib.WINDOWS.name, Kernel.NO_KERNEL.name)), set (
    IO(isa.name,
        Metaface({isa}, {Kernel.WINDOWS, Kernel.NO_KERNEL}, {Syslib.WINDOWS}, Lib_ANYs),
        Metaface({isa}, {Kernel.NO_KERNEL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs)
    )
for isa in Isa_MODERN_WINDOWSs))

###############################################
#      _
#     /_\  _ __ _ __
#    / _ \| '_ \ '_ \
#   /_/ \_\ .__/ .__/
#         |_|  |_|
#                           figlet -f small App
Module("-".join((App.ANY.name, Sysapp.ANY.name, Lib.ANY.name, Syslib.WINDOWS.name, Kernel.NO_KERNEL.name)), set (
    IO(isa.name,
        Metaface({isa}, {Kernel.WINDOWS, Kernel.NO_KERNEL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs),
        Metaface({isa}, {Kernel.NO_KERNEL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs, App_ANYs)
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
#    {  IO("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
Transor("Merge",
    {  IO("",
        Metaface({Isa.I386}, {Kernel.SCO_UNIX}),
        Metaface({Isa.I386}, {Kernel.DOS, Kernel.WINDOWS3_1})
    )},
    Date(1985,10,9), Date(2000),
    desc="https://en.wikipedia.org/wiki/Merge_(software)"
)
Transor("mx",
    {  IO("",
        Metaface({Isa.ALPHA}, {Kernel.OSF1}),
        Metaface({Isa.MIPS32}, {Kernel.ULTRIX}),
    )},
    Date(1993), dev="Digital",
    desc="1993: Binary Translation by Richard L. Sites"
)
Transor("Shade",
    {  IO("MIPS.V8",
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.UMIPSV, Isa.MIPSI}, {Kernel.SUNOS4_BSD}),
    ), IO("V8.V8-BSD",
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS4_BSD}),
    ), IO("V9.V8-BSD",
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.SPARCV9}, {Kernel.SUNOS4_BSD}),
    ), IO("V8.V8-UNIX",
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS5_UNIX}),
    ), IO("V9.V8-UNIX",
        Metaface({Isa.SPARCV8}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.SPARCV9}, {Kernel.SUNOS5_UNIX}),
    )},
    Date(1993), dev="SUN",
    desc="1994: Shade: a fast instruction-set simulator for execution profiling"
)
Transor("VEST",
    {  IO("",
        Metaface({Isa.ALPHA}, {Kernel.OPENVMS}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({Isa.VAX}, {Kernel.OPENVMS}),
    )},
    Date(1993), dev="Digital",
    desc="1993: Binary Translation by Richard L. Sites",
)
# TODO: Android
Kernel_WINEs_str: set[str] = {Kernel.LINUX.name, Kernel.MACOS.name, Kernel.BSD.name}
Kernel_WINEs: set[Kernel] = set(Kernel[name] for name in Kernel_WINEs_str)
Syslib_WINEs: set[Syslib] = set(Syslib[name] for name in Kernel_WINEs_str)
Transor("WINE",
    set(IO(
        "-".join((kname, isa.name)),
        Metaface({isa}, {Kernel[kname]}, {Syslib[kname]}, Lib_ANYs),
        Metaface({isa}, {Kernel.NO_KERNEL}, {Syslib.WINDOWS}),
    ) for isa in Isa_MODERN_WINDOWSs for kname in Kernel_WINEs_str),
    Date(1993,7,4), Date.today(), "#800000", "LGPL",
)


# TODO: user-mode linux
Isa_QEMU_user_is: set[Isa] = {
    Isa.AARCH64, Isa.ARM, Isa.X86, Isa.X86_64,
    Isa.LA64, Isa.MIPS32, Isa.MIPS64,
    Isa.POWERPC, Isa.RISCV64, Isa.S390X, Isa.SPARC,
}
Isa_QEMU_user_os: set[Isa] = {
    Isa.ALPHA, Isa.ARM, Isa.AARCH64, Isa.X86, Isa.X86_64,
    Isa.AVR, Isa.CRIS, Isa.HEXAGON, Isa.HPPA, Isa.M68K,
    Isa.MICROBLAZE, Isa.MIPS32, Isa.MIPS64, Isa.NIOS2,
    Isa.OPENRISC, Isa.POWERPC, Isa.RISCV64, Isa.RX,
    Isa.S390X, Isa.SH4, Isa.SPARC, Isa.TRICORE, Isa.XTENSA,
}
Transor("QEMU-user",
    {  IO("linux",
        Metaface(Isa_QEMU_user_is & Isa_LINUXs, {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_LINUXs, {Kernel.LINUX})
    ), IO("bsd",
        Metaface(Isa_QEMU_user_is & Isa_BSDs, {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_BSDs, {Kernel.BSD})
    ), IO("tci-linux",
        Metaface(Isa_LINUXs, {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_LINUXs, {Kernel.LINUX})
    ), IO("tci-bsd",
        Metaface(Isa_BSDs, {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_BSDs, {Kernel.BSD})
    )},
    Date(2003,2), Date.today(), "#F60", "IR",
    "2005: QEMU, a Fast and Portable Dynamic Translator",
)

# Lastly, add dummy modules after all modules are added
addDummyModules()
