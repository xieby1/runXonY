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
Merge = Transor("Merge",
    {  HG("",
        Metaface({(Isa.I386, Up.USR)}, {Kernel.SCO_UNIX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.I386, Up.USR_PVL)})
    )},
    Date(1985,10,9), Date(2000),
    feat="run DOS/Windows 3.1",
    desc="https://en.wikipedia.org/wiki/Merge_(software)"
)
Transor("mx",
    {  HG("",
        Metaface({(Isa.ALPHA, Up.USR)}, {Kernel.OSF1}),
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.ULTRIX}),
    )},
    Date(1993), dev=Dev.DIGITAL,
    desc="1993: Binary Translation by Richard L. Sites"
)
Transor("Shade",
    {  HG("MIPS.V8",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.UMIPSV, Up.USR), (Isa.MIPSI, Up.USR)}, {Kernel.SUNOS4_BSD}),
    ), HG("V8.V8-BSD",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    ), HG("V9.V8-BSD",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS4_BSD}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV9, Up.USR)}, {Kernel.SUNOS4_BSD}),
    ), HG("V8.V8-UNIX",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    ), HG("V9.V8-UNIX",
        Metaface({(Isa.SPARCV8, Up.USR)}, {Kernel.SUNOS5_UNIX}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.SPARCV9, Up.USR)}, {Kernel.SUNOS5_UNIX}),
    )},
    Date(1993), dev=Dev.SUN,
    desc="1994: Shade: a fast instruction-set simulator for execution profiling"
)
Transor("VEST",
    {  HG("",
        Metaface({(Isa.ALPHA, Up.USR)}, {Kernel.OPENVMS}, {Syslib.DEFAULT}, Lib_ANYs),
        Metaface({(Isa.VAX, Up.USR)}, {Kernel.OPENVMS}),
    )},
    Date(1993), dev=Dev.DIGITAL,
    desc="1993: Binary Translation by Richard L. Sites",
)
# TODO: Android
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
    Date(1996), dev=Dev.DIGITAL,
    desc = '''
        1997: DIGITAL FX!32: Combining Emulation and Binary Translation
        1998: FX!32 A Profile-Directed Binary Translator
    '''
)
Transor("DAISY",
    {  HG("",
        Metaface({(Isa.DAISY_VLIW, Up.USR_PVL)}),
        Metaface({(Isa.POWERPC, Up.USR_PVL)}),
    )},
    Date(1998), Date(2001), dev=Dev.IBM,
    desc = '''
        1997: DAISY dynamic compilation for 100% architecutral compatibility
        2000: Binary Translation and Architecture Convergence Issues for IBM System/390
        2000: full system binary translation RISC to VLIW
        2000: simulation and debugging of full system bianry translation
        2001: Dynamic binary translation and optimization
    '''
)
Transor("MinGW",
    {  HG("",
        Metaface(IsasUSR(Isa_MODERN_WINDOWSs), {Kernel.WINDOWS}),
        Metaface({(Isa.NONE, Up.NONE)}, {Kernel.NONE}, {Syslib.WINDOWS}, srcs={Src.C, Src.CPP}),
    )},
    Date(1998,7,1), Date.today(), "#71B21F",
    feat='''
        Run on MSVC runtime
        Can be compiled on Win and Linux
    '''
)
Dynamo = Transor("Dynamo",
    {  HG("",
        Metaface({(Isa.PARISC, Up.USR)}, {Kernel.UNIX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.PARISC, Up.USR)}, {Kernel.UNIX}),
        term=Term.OPT,
    )},
    Date(1999), Date(2000), dev=Dev.HP,
    desc='''
        1999: Transparent Dynamic Optimization: The Design and Implementation of Dynamo
        2000: Dynamo: A Transparent Dynamic Optimization System
    ''',
)
# TODO: Android
Transor("DynamoRIO",
    {  HG('-'.join((kernel.name, isa.name)),
        Metaface(IsasUSR({isa}), {kernel}, {syslib}, {Lib.ANY}),
        Metaface(IsasUSR({isa}), {kernel}),
        term=Term.I_O,
    ) for isa in [Isa.X86, Isa.X86_64, Isa.ARM32, Isa.AARCH64]
      for kernel, syslib in zip([Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS], [Syslib.WINDOWS, Syslib.LINUX, Syslib.MACOS])},
    Date(2000), Date.today(), dev=Dev.HP,
    desc="https://dynamorio.org/index.html",
    parent=Dynamo,
    renames=[Rename("DynamoRIO(VMware)", Date(2007), "")]
)
Transor("VMware Workstation",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX, Kernel.WINDOWS}, {Syslib.WINDOWS}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
    )},
    Date(1999,5,15), Date.today(), "#F38C00", dev=Dev.VMWARE,
)
Transor("Win4Lin",
    {  HG("",
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR_PVL)})
    )},
    Date(2000), Date(2008,6,4), dev=Dev.WIN4LIN,
    feat="run  Windows 9x, Windows 2000 or Windows XP",
    desc='''
        http://freshmeat.sourceforge.net/projects/win4lin
        https://en.wikipedia.org/wiki/Win4Lin
        2005: SUSE™ Linux 10 Unleashed: Chapter 11
    ''',
    parent=Merge,
    renames=[Rename("Win4Lin 9x", Date(2005,3),
        desc="https://web.archive.org/web/20050318033645/http://www.win4lin.com:80/"
    )],
)
Transor("Code Morphing",
    {  HG("",
        Metaface({(Isa.CRUSOE_VLIW, Up.USR_PVL)}),
        Metaface({(Isa.X86, Up.USR_PVL)}),
    )},
    Date(2000), Date(2009), dev=Dev.TRANSMETA,
    desc='''
        2003: The Transmeta Code Morphing Software: Using Speculation, Recovery, and Adaptive Retranslation to Address Real-Life Challenges
        https://en.wikipedia.org/wiki/Transmeta
    ''',
)
Transor("Aries",
    {  HG("",
        Metaface({(Isa.IA64, Up.USR)}, {Kernel.UNIX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.PARISC, Up.USR)}, {Kernel.UNIX}),
    )},
    Date(2000), dev=Dev.HP,
    desc='''
        2000: PA-RISC to IA-64: Transparent Execution, No Recompilatio
    ''',
)
Transor("WineX",
    set(),
    Date(2000,12,27), Date(2016), "#800000", dev=Dev.TRANSGAMING_NVIDIA,
    feat="Support DirectX",
    desc='''
        Mail from wine-devel: 2004-August.txt: 22697
        https://web.archive.org/web/20010331041916/http://www.transgaming.com/news.php
    ''',
    parent=WINE,
    renames=[
        Rename("Cedega", Date(2004,6,22), "https://en.wikipedia.org/wiki/Cedega_(software)"),
        Rename("GameTree Linux", Date(2011,2,28), ""),
    ],
)
Transor("User Mode Linux",
    {  HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
        term=Term.SYSCALL_COMPATIBLE_LAYER,
    ) for isa in Isa_LINUXs},
    Date(2001), Date.today(),
    desc="2006: User Mode Linux",
)
Transor("Dynamite",
    {  HG("",
        Metaface(IsasUSR({hisa}), {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface(IsasUSR({gisa}), {Kernel.LINUX}),
        ) for hisa,gisa in zip([Isa.MIPS32, Isa.MIPS32, Isa.X86],[Isa.ARM32, Isa.X86, Isa.POWERPC])
    } | { HG("",
        Metaface(IsasUSR({hisa}), {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface(IsasUSR({gisa}), {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        ) for hisa,gisa in zip([Isa.MIPS32, Isa.MIPS32, Isa.X86],[Isa.ARM32, Isa.X86, Isa.POWERPC])
    },
    Date(2001), Date(2002,11), dev=Dev.TRANSITIVE_APPLE, feat="IR",
    desc='''
        Mail from wine-devel: 2003-August.txt: 17434,
        http://www.transitives.com/tech_faq.htm (need wayback machine)
        https://web.archive.org/web/20021129223838/http://transitives.com:80/
    '''
)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)


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
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    ), HG("bsd",
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_BSDs), {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_BSDs), {Kernel.BSD}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    ), HG("tci-linux",
        Metaface(IsasUSR(Isa_LINUXs), {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    ), HG("tci-bsd",
        Metaface(IsasUSR(Isa_BSDs), {Kernel.BSD}, {Syslib.BSD_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_BSDs), {Kernel.BSD}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    )},
    Date(2003,2), Date.today(), "#F60", "IR",
    desc="2005: QEMU, a Fast and Portable Dynamic Translator",
)

# Lastly, add dummy modules after all modules are added
addDummyModules()
