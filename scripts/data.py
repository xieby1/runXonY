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

# https://github.com/torvalds/linux/tree/master/arch
Isa_LINUXs: set[Isa] = \
    {Isa.ALPHA, Isa.ARC} | Isa_ARM32s | {Isa.ARM64,
    Isa.CSKY, Isa.HEXAGON, Isa.IA64, Isa.LOONGARCH, Isa.M68K,
    Isa.MICROBLAZE} | Isa_MIPS64s | {Isa.NIOS2, Isa.OPENRISC,
    Isa.PARISC} | Isa_POWERPC64s | Isa_RISCV64s | {Isa.S390,
    Isa.SH} | Isa_SPARC64s | Isa_X86_64s | {Isa.XTENSA}

Isa_KVMs = [Isa.ARM64, Isa.IA64, Isa.X86, Isa.X86_64, Isa.POWERPC64, Isa.S390, Isa.MIPS64, Isa.LA64]

# https://www.freebsd.org/platforms/
Isa_FreeBSDs: set[Isa] = \
    Isa_X86_64s | Isa_X86s | {Isa.AARCH64, Isa.ARM} | \
    Isa_ARMV6s | Isa_ARMV7s | Isa_MIPS64s | Isa_POWERPC64s | \
    Isa_RISCV64s | Isa_SPARC64s
# https://www.openbsd.org/plat.html
Isa_OpenBSDs: set[Isa] = Isa_FreeBSDs | {Isa.ALPHA, Isa.HPPA}
Isa_BSDs: set[Isa] = Isa_FreeBSDs | Isa_OpenBSDs

Isa_MODERN_WINDOWSs: set[Isa] = {Isa.AARCH64, Isa.X86_64, Isa.X86}

Isa_MODERN_MACOSs: set[Isa] = {Isa.AARCH64, Isa.X86_64}

Isa_MODERN_ANDROIDs: set[Isa] = {Isa.X86_64, Isa.AARCH64}

###############################################
#    _  __                 _
#   | |/ /___ _ _ _ _  ___| |
#   | ' </ -_) '_| ' \/ -_) |
#   |_|\_\___|_| |_||_\___|_|
#                           figlet -f small Kernel

Module(Kernel.LINUX.name, set(
    HG(isa.name, Metaface({(isa, Up.USR_PVL)}), Metaface({(isa,Up.USR)}, {Kernel.LINUX}))
for isa in Isa_LINUXs))

Module(Kernel.BSD.name, set(
    HG(isa.name, Metaface({(isa, Up.USR_PVL)}), Metaface({(isa, Up.USR)}, {Kernel.BSD}))
for isa in Isa_BSDs))

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
Module("APPS-WINDOWS", set (
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS, Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs, {App.APPS})
    )
for isa in Isa_MODERN_WINDOWSs))
Module("APPS-WINDOWS-WITH_SYSCALL", set (
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS}, {Syslib.WINDOWS}, Lib_ANYs, Sysapp_ANYs, {App.APPS})
    )
for isa in Isa_MODERN_WINDOWSs))

Module("ANDROID", set(
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs, {App.ANDROID_RUNTIME})
    ) for isa in Isa_MODERN_ANDROIDs) | {
    HG("UNIVERAL",
        Metaface(IsasUSR(Isa_MODERN_ANDROIDs), {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs),
        Metaface({(Isa.NONE, Up.NONE)}, {Kernel.NONE}, {Syslib.NONE}, {Lib.NONE}, {Sysapp.NONE}, {App.ANDROID_RUNTIME})
    )}
)

###############################################
#    ___ _   _ _ _
#   | _ \ |_| (_) |__
#   |   /  _| | | '_ \
#   |_|_\\__|_|_|_.__/
#                           figlet -f small Rtlib

###############################################
#    ___ _
#   | _ \ |_ __ _ _ __ _ __
#   |   /  _/ _` | '_ \ '_ \
#   |_|_\\__\__,_| .__/ .__/
#                |_|  |_|
#                           figlet -f small Rtapp
Module("APPS-ANDROID", set(
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs, {App.ANDROID_RUNTIME}, {Rtlib.ANY}, {Rtapp.APPS})
    )
    for isa in Isa_MODERN_ANDROIDs) | {
    HG("UNIVERAL",
        Metaface({
            Interface((Isa.NONE, Up.NONE), Kernel.NONE, Syslib.NONE, Lib.NONE, Sysapp.NONE, App.ANDROID_RUNTIME, Rtlib.ANY),
            } | set(
            Interface((isa, Up.USR), Kernel.LINUX_ANDROID, Syslib.DEFAULT, Lib.ANY, Sysapp.ANY, App.ANDROID_RUNTIME, Rtlib.ANY)
        for isa in Isa_MODERN_ANDROIDs)),
        Metaface({(Isa.NONE, Up.NONE)}, {Kernel.NONE}, {Syslib.NONE}, {Lib.NONE}, {Sysapp.NONE}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}, {Rtapp.APPS})
    )}
)

###############################################################
#    _______
#   |__   __|
#      | |_ __ __ _ _ __  ___  ___  _ __ ___
#      | | '__/ _` | '_ \/ __|/ _ \| '__/ __|
#      | | | | (_| | | | \__ \ (_) | |  \__ \
#      |_|_|  \__,_|_| |_|___/\___/|_|  |___/
#                                       figlet -f big Transors

# Template
#Transor("",
#    {  HG("",
#        Metaface(),
#        Metaface(),
#    )},
#    Date(),
#)

import os
curfiledir = os.path.dirname(os.path.abspath(__file__))
for dir in os.listdir(curfiledir):
    filepath = "/".join((curfiledir, dir, "meta.py"))
    if os.path.isfile(filepath):
        exec("from %s.meta import *" % dir)
VMwareWorkstation = Transor("VMware Workstation",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX, Kernel.WINDOWS}, {Syslib.WINDOWS}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
    )},
    Date(1999,5,15), Date.today(), "#F38C00", dev=Dev.VMWARE,
)
Win4Lin = Transor("Win4Lin",
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
    Date(2001), Date(2002,11), dev=Dev.TRANSITIVE_APPLE, term=Term.UBL,
    feat="IR",
    desc='''
        Mail from wine-devel: 2003-August.txt: 17434,
        http://www.transitives.com/tech_faq.htm (need wayback machine)
        https://web.archive.org/web/20021129223838/http://transitives.com:80/
    '''
)
Transor("Tarmac",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2001,3,13), color="#28789E",
    desc='''
        https://davidsharp.com/tarmac/
        https://davidsharp.com/tarmac/tarmacreport.pdf
        https://davidsharp.com/tarmac/tarmacdiary.pdf
    '''
)
Isa_DOSBOXs = {Isa.X86_64, Isa.X86, Isa.MIPS32, Isa.ARM32, Isa.POWERPC}
DOSBox = Transor("DOSBox",
    {  HG("",
        Metaface(IsasUSR(isas), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR_PVL)}),
        term=Term.V2B,
    ) for isas,kernel in zip(
        [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs, Isa_BSDs],
        [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX, Kernel.BSD])},
    Date(2002), Date.today(), "#113466",
    desc="https://sourceforge.net/projects/dosbox/",
)
# TODO:
LLVM = Transor("LLVM",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2003), Date.today(), "#556293",
)
Xen = Transor("Xen",
    {  HG("",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR_PVL)}),
        ) for isa in [Isa.X86, Isa.X86_64]
    } | { HG("Paravirtualized",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR)}),
        ) for isa in [Isa.X86, Isa.X86_64]
    },
    Date(2003), Date.today(), term=Term.TYPE1_VIRTUAL_MACHINE_AND_PARAVIRTUALIZATION,
    desc="https://en.wikipedia.org/wiki/Xen",
)
Transor("IA-32 EL",
    {  HG("",
        Metaface({(Isa.IA64, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.IA32, Up.USR)}, {kernel}),
    ) for kernel in [Kernel.LINUX, Kernel.WINDOWS]},
    Date(2003), Date.today(),
)
# TODO:
Transor("NDISWrapper",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2003), Date.today(),
    desc="github: pgiri/ndiswrapper: manpage: ndiswrapper.8",
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
QEMU_user = Transor("QEMU-user",
    {  HG("linux",
        Metaface(IsasUSR(Isa_QEMU_user_hs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}, {Syslib.LINUX_SYSLIBS}, Lib_ANYs),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
        perfs=[
            Perf(4148.31/23977.99, Benchmark.COREMARK, Date(2023,1,16),
                 "qemu7.1.0, aarch64 on x86_64 linux, clang 13.0.1")
        ],
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

Transor("Project David",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2004), Date(2004), dev=Dev.SPECOPS_LABS,
    desc='''
        Mail from wine-devel: 2004-April.txt: project David
        Turbo Linux: https://web.archive.org/web/20051201013454/http://digital.hmx.net/02contents/pc/linux/fuji.shtml
        http://www.specopslabs.com/david.htm
    ''',
    parent=WINE,
)

Digital_Bridge = Transor("Digital Bridge",
    {  HG("",
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
    )},
    Date(2004), Date(2006), dev=Dev.WCG_LAB, feat="Dynamic + static bt",
    desc='''
        2004: 二进制翻译关键技术研究
        2005: 优化动态二进制翻译器DigitalBridge
    ''',
)

skyeye = Transor("skyeye",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2004,5,26), Date(2013,5,2),
    desc='''
        https://sourceforge.net/projects/skyeye/files/skyeye/
        git://skyeye.git.sourceforge.net/gitroot/skyeye/skyeye
    '''
)

# TODO: non-general, game
Transor("bsnes",
    { HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS, Kernel.BSD}, {Syslib.DEFAULT}, {Lib.ANY}),
        # TODO: Too many old chips!!!
        Metaface(),
    )},
    Date(2004,10,14), Date.today(), "#DC1212",
    desc='''
        https://higan.dev/about
        https://github.com/higan-emu/higan/tree/master/higan/component/processor
    ''',
    renames=[Rename("higan", Date(2012,8,9))],
)

Transor("Pin", set(
    HG("",
        Metaface({(Isa.X86, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {kernel}),
    )
    for kernel in (Kernel.LINUX, Kernel.WINDOWS, Kernel.MACOS)),
    Date(2005), Date.today(), dev=Dev.INTEL, term=Term.INSTRUMENTER,
    feat="PinCRT",
    desc='''
        2005: Pin: Building Customized Program Analysis Tools with Dynamic Instrumentation
    ''',
)

Win4Lin_Pro = Transor("Win4Lin Pro",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2005), Date(2010,3), parent=Win4Lin,
    desc="https://en.wikipedia.org/wiki/Win4Lin",
)
Connector(QEMU_sys, Win4Lin_Pro, Date(2005))

IntelVT = Transor("Intel VT", set(  HG("",
        Metaface({(isa, Up.USR_PVL)}),
        Metaface({(isa, Up.USR_PVL)}),
    )
    for isa in (Isa.X86, Isa.X86_64)),
    Date(2006), Date.today(), "#0071C5", dev=Dev.INTEL,
    desc="Intel ® Virtualization Technology: Hardware Support for Efficient Processor Virtualization",
)

Transor("Alky",
    {  HG("",
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    )},
    Date(2006), Date(2008,1), license="LGPL", dev=Dev.FALLING_LEAF_SYSTEM,
    feat='''
        OpenGL static converter,
        written in python,
        LibAlky is DX10 runtime only work on WinXP
    '''
)

Transor("Digital Bridge 2",
    {  HG("",
        Metaface({(Isa.MIPS32, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH
    )},
    Date(2006), parent=Digital_Bridge, dev=Dev.WCG_LAB,
    feat='''
        Dynamic + static bt
        lib wrapper
    ''',
    desc="2006: 二进制翻译中的库函数处理",
)

Transor("Linuxulator", set(
    HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.BSD}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
    )
    for isa in Isa_FreeBSDs),
    Date(2006), Date.today(),
    desc='''
        Mail from wine-devel: 2004-August.txt: 26171: `kernel compatibility layer`
        2006: Linux emulation in FreeBSD
    '''
)

Transor("Rosetta",
    {  HG("",
        Metaface({(Isa.X86, Up.USR)}, {Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.POWERPC, Up.USR)}, {Kernel.MACOS}),
    )},
    Date(2006), Date(2011), "#525152", dev=Dev.APPLE,
    desc="https://en.wikipedia.org/wiki/Rosetta_%28software%29",
)

# TODO: non-general, game
Transor("DeSmuME",
    {  HG("",
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR_PVL)}),
    )},
    Date(2006,4,6), Date.today(), "#A4A8FF", "GPL2",
    feat='''
        peripherals,
        bios (loading and executing ROMs) (able to run external bios)
    ''',
    desc='''
        https://desmume.org/
        https://github.com/TASEmulators/desmume
        http://wiki.desmume.org/index.php?title=Faq
    ''',
)

Transor("playonlinux",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2007), Date.today(), parent=WINE,
    desc="zorin os",
)

Transor("MagiXen",
    {  HG("",
        Metaface({(Isa.ITANIUM, Up.USR_PVL)}),
        Metaface({(Isa.IA32, Up.USR_PVL)}),
    )},
    Date(2007), dev=Dev.HP, parent=Xen,
    desc="2007: MagiXen: Combining Binary Translation and Virtualization",
)

VirtualBox = Transor("VirtualBox",
    {  HG("",
        Metaface(IsasUSR({isa}), {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR_PVL({isa})),
    ) for isa in [Isa.X86, Isa.X86_64]},
    Date(2007,1,17), Date.today(), color="#2F61B4", dev=Dev.ORACLE,
    desc="https://en.wikipedia.org/wiki/VirtualBox",
)
Connector(IntelVT, VirtualBox, Date(2007,1,17))

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
Connector(IntelVT, KVM, Date(2007,2,5))

Transor("VMware Player",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
    ) for kernel in [Kernel.WINDOWS, Kernel.LINUX]},
    Date(2008,6,6), Date.today(), color="#FFE839", dev=Dev.VMWARE, parent=VMwareWorkstation,
    desc="https://en.wikipedia.org/wiki/VMware_Workstation_Player",
)

QEMU_KVM = Transor("QEMU-KVM",
    {  HG("",
        Metaface(IsasUSR({isa}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR_PVL({isa})),
    ) for isa in Isa_KVMs},
    Date(2008,11,6), Date.today(), color="#F60", parent=QEMU_sys,
    desc="Git commit: 7ba1e61953f459: Add KVM support to QEMU",
)
Connector(KVM, QEMU_KVM, Date(2008,11,6))

Transor("DistriBit",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2009), Date(2012), dev=Dev.SJ,
    feat='''
        Server-client,
        2-level code cache,
        Server predicts client’s needing code
    ''',
    desc="2010: DistriBit: A Distributed Dynamic Binary Translator System for Thin Client Computing",
)

proot = Transor("proot",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2010,5,22), Date.today(),
    feat="fs isolation",
    desc="https://github.com/proot-me/proot.git",
)

Transor("DOSBox-X",
    {  HG("",
        Metaface(IsasUSR(isas), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR_PVL)}),
        term=Term.V2B,
    ) for isas,kernel in zip(
        [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs, Isa_BSDs],
        [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX, Kernel.BSD])},
    Date(2011), Date.today(), color="#113466", parent=DOSBox,
)

Transor("Denver",
    {  HG("",
        Metaface({(Isa.DENVER, Up.USR_PVL)}),
        Metaface({(Isa.ARM64, Up.USR_PVL)}),
    )},
    Date(2011,3,4), Date(2014,10,15), dev=Dev.NVIDIA,
    desc="https://en.wikipedia.org/wiki/Project_Denver",
)

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

HQEMU = Transor("HQEMU",
    {  HG("",
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.ARM64, Isa.POWERPC64}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.ARM, Isa.ARM64}), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR,
    )},
    Date(2012), Date(2018), color="#F60", parent=QEMU_user, dev=Dev.TQH,
    feat="multi thread opt",
    desc='''
        2012: HQEMU: A Multi-Threaded and Retargetable Dynamic Binary Translator on Multicores
        2013: Efficient and Retargetable Dynamic Binary Translation on Multicores
        2018: HQEMU v2.5.2 Technical Report
    ''',
)
Connector(LLVM, HQEMU, Date(2012))

Transor("LLBT",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface({(Isa.ARM, Up.USR)}, {Kernel.LINUX}),
        term=Term.STATIC_BINARY_TRANSLATOR,
    )},
    Date(2012), Date(2014), dev=Dev.TJD,
    desc='''
        2012: LLBT: An LLVM-based Static Binary Translator
        2013: Automatic Validation for Static Binary Translation
        2014: A Retargetable Static Binary Translator for the ARM Architecture
    ''',
)

# TODO: non-general, game
Transor("PPSSPP",
    {  HG("",
        Metaface(IsasUSR(isas), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.MIPSIII, Up.USR_PVL)}),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
        ) for isas,kernel in zip(
            [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs],
            [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX])
    }|{HG("",
        Metaface(IsasUSR(Isa_MODERN_ANDROIDs), {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(Isa.MIPSIII, Up.USR_PVL)}),
        # TODO: Android auto generate term?
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    )},
    Date(2012,3,25), Date.today(), color="#0086B2", license="GPL2",
    desc='''
        https://www.ppsspp.org/
        https://github.com/hrydgard/ppsspp
    ''',
)

Transor("Arm-js",
    {  HG("",
        # TODO:
        Metaface(),
        Metaface({(Isa.ARM, Up.USR_PVL)}),
    )},
    Date(2012,5,20), Date(2014,2,11),
    desc="https://github.com/ozaki-r/arm-js",
)

Transor("skyeye(Commercial)",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2013), Date.today(), parent=skyeye, dev=Dev.DIGIPROTO,
    desc="https://www.digiproto.com/product/24.html",
)

# TODO: non-general, game
citra = Transor("citra",
    {  HG("",
        Metaface(),
        # TODO: 3DS
        Metaface(),
    )},
    Date(2013,8,30), Date.today(), color="#FF8E03",
    desc="https://github.com/citra-emu/citra",
)
Connector(skyeye, citra, Date(2013,5,2), Date(2013,9,18))

Transor("Qubes OS",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
        Metaface({(Isa.X86_64, Up.USR)}),
    )},
    Date(2013,9,3), Date.today(), color="#3874D8", dev=Dev.INVISIBLE_THINGS_LAB, parent=Xen,
    desc="https://en.wikipedia.org/wiki/Qubes_OS",
)

exagear_strategies = Transor("exagear strategies",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    )},
    Date(2014), Date(2020), dev=Dev.ELTECH_RUSSIA,
    desc="https://4pda.to/forum/index.php?showtopic=992239",
)
Connector(exagear_strategies, WINE, Date(2014))

Transor("WINE-Android",
    {  HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    ) for isa in Isa_MODERN_ANDROIDs},
    Date(2014,2), Date.today(), color="#800000", parent=WINE,
    desc="https://wiki.winehq.org/Android",
)

# non-general
Transor("firebird",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2014,4,26), Date.today(), color="#FA0430", license="GPL3",
    desc="https://github.com/nspire-emus/firebird",
)

Transor("VisUAL",
    {  HG("",
        Metaface(IsasUSR(isas), {kenerl}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM, Up.USR)}),
    ) for isas,kenerl in zip(
        [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs],
        [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX]
    )},
    Date(2015), Date.today(), color="#3A9878",
    feat="visualization",
    desc="https://salmanarif.bitbucket.io/visual/about.html",
)

unicorn = Transor("unicorn",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2015,8,21), Date.today(), color="#E62129", parent=QEMU_sys,
    feat="Framework",
    desc="https://github.com/unicorn-engine/unicorn",
)

# a Unix-like operating system
# actually, not a transor
Transor("browsix",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2015,9,26), Date.today(), color="#6D6B91",
    desc='''
        https://browsix.org/
        https://github.com/plasma-umass/browsix
    ''',
)

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

Transor("Limbo",
    {  HG("",
        Metaface(IsasUSR(Isa_MODERN_ANDROIDs), {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface(),
    )},
    Date(2016), Date(2022), color="#383838", parent=QEMU_sys,
)

Anbox = Transor("Anbox",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}),
    ) for isa in [Isa.X86_64, Isa.ARM64]},
    Date(2016,4,11), Date.today(), color="#009688", license="GPL3",
)

dynarmic = Transor("dynarmic",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.ANY}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.ARM64, Isa.ARM32})),
    )},
    Date(2016,7,1), Date.today(),
    feat="Framework",
)
Connector(dynarmic, citra, Date(2016,9,2))

Transor("WSL",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
    ) for isa in Isa_MODERN_WINDOWSs},
    Date(2016,8,2), Date.today(), color="#0C2AAE", dev=Dev.MICROSOFT,
    desc="https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux",
)

MAMBO_X64 = Transor("MAMBO-X64",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR)}, {Kernel.LINUX}),
    )},
    Date(2017), Date.today(), dev=Dev.MANCHESTER,
    desc='''
        2017: Low Overhead Dynamic Binary Translation on ARM
    ''',
)
HyperMAMBO_X64 = Transor("HyperMAMBO-X64",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR_PVL)}),
    )},
    Date(2017), parent=MAMBO_X64, dev=Dev.MANCHESTER,
    desc="2017: HyperMAMBO-X64: Using Virtualization to Support High-Performance Transparent Binary Translation",
)
Connector(KVM, HyperMAMBO_X64, Date(2017))

REV_NG = Transor("REV.NG",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR(Isa_QEMU_user_gs) & IsasUSR(Isa_LINUXs), {Kernel.LINUX}),
    )},
    Date(2017), Date.today(), color="#E92B29", parent=QEMU_user,
    term=Term.DYNAMIC_STATIC_BINARY_TRANSLATOR,
    desc='''
        2017: REV.NG :A Unified Binary Analysis Framework to Recover CFGs and Function Boundaries
        2018: rev.ng: A Multi-Architecture Framework for Reverse Engineering and Vulnerability Discovery
        2019: Performance, Correctness, Exceptions: Pick Three
''',
)
Connector(LLVM, REV_NG, Date(2017))

yuzu = Transor("yuzu",
    {  HG("",
        Metaface(),
        # Nintendo Switch
        Metaface(),
    )},
    Date(2017,10,10), Date.today(), color="#5C93ED", parent=citra,
    desc='''
        https://github.com/yuzu-emu/yuzu
        Git commit: d15e15bd058f93f16
    ''',
)
Connector(unicorn, yuzu, Date(2017,10,10))

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

box86 = Transor("box86",
    {  HG("",
        Metaface({(Isa.ARM32, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2018), Date.today(), color="#B5E853",
    feat="lib warp",
    desc="https://github.com/ptitSeb/box86",
)

# non-general game
Ryujinx = Transor("Ryujinx",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        # Nintendo switch
        Metaface(),
    )},
    Date(2018,2,5), Date.today(), color="#FF5F55", license="MIT",
    desc="https://github.com/Ryujinx/Ryujinx/",
)
Transor("ChocolArm64",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}),
    )},
    Date(2018,2,21), Date(2019,11,1), color="#FF5F55", parent=Ryujinx, license="Unlicense",
    feat="Framework",
    desc='''
        https://github.com/Ryujinx/Ryujinx/
        https://github.com/Ryujinx/ChocolArm64
    ''',
)

Transor("UserLAnd",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs),
    )},
    Date(2018,3,21), Date.today(), color="#221F1F", parent=proot,
    feat="No-privilege fs isolation",
    desc="https://github.com/CypherpunkArmory/UserLAnd.git",
)

Transor("Proton",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2018,8,21), Date.today(), parent=WINE, dev=Dev.VALVE,
    desc="https://github.com/ValveSoftware/Proton",
)

Transor("xDroid",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2018,8,21), Date.today(), color="#009688", parent=Anbox, dev=Dev.LINZHUOTECH,
    desc='''
        https://www.linzhuotech.com/index.php/home/index/article.html?page=4&id=2
        https://zhuanlan.zhihu.com/p/213300936
    ''',
)

Transor("FEX",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64, Isa.ARM64}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86_64, Isa.X86}), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2018,11,16), Date.today(), license="MIT",
    feat='''
        Interp,
        JIT,
        LLVM disasm,
        thunklib: guest ↔ host
    ''',
    desc='''
        https://github.com/FEX-Emu/FEX
        git commit 5efab55ea9b: remove problematic LLVM JIT
    ''',
)

# Firmware, actually not a transor
edk2_sagit = Transor("edk2-sagit",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2019,2,22), Date(2020,5,25),
)

Transor("McSema",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.AARCH64}), {Kernel.LINUX}),
        term=Term.STATIC_BINARY_TRANSLATOR,
    )},
    Date(2019), Date(2022,4,26), color="#9C1B45", parent=LLVM,
    desc='''
        https://github.com/lifting-bits/mcsema
        2019: DECOMPILING BINARIES INTO LLVM IR USING MCSEMA AND DYNINST
    ''',
)

Transor("MCTOLL",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR({Isa.X86_64, Isa.AARCH64}), {Kernel.LINUX}),
    )},
    Date(2019), Date.today(), dev=Dev.MICROSOFT, parent=LLVM,
    desc='''
        https://github.com/microsoft/llvm-mctoll
        2019: Raising Binaries to LLVM IR with MCTOLL (WIP Paper)
    ''',
)

Transor("UTM",
    {  HG("",
        Metaface({(Isa.AARCH64, Up.USR)}, {Kernel.IOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(),
    )},
    Date(2019), Date.today(), color="#1D63EA", parent=QEMU_sys,
)

Transor("WSL2",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR_PVL)}),
    ) for isa in Isa_MODERN_WINDOWSs},
    Date(2019,5), Date.today(), color="#0C2AAE", dev=Dev.MICROSOFT,
    desc="https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux",
)

Transor("ARMeilleure",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}),
    )},
    Date(2019,8,9), Date.today(), color="#FF5F55", parent=Ryujinx,
    feat="Framework",
    desc="https://github.com/Ryujinx/Ryujinx/",
)

Transor("Rosetta 2",
    {  HG("",
        Metaface({(Isa.AARCH64, Up.USR)}, {Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.MACOS}),
    )},
    Date(2020), Date.today(), color="#525152", dev=Dev.APPLE,
    desc="https://en.wikipedia.org/wiki/Rosetta_%28software%29",
)

Transor("exagear",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.LINUX}),
    )},
    Date(2020), Date.today(), parent=exagear_strategies, dev=Dev.ELTECH_HUAWEI,
)

# Firmware, actually not a transor
Transor("edk2-sdm845",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2020,5,25), Date.today(), parent=edk2_sagit,
    desc="Enable to run Win11, Support graphics card, can play ff14",
)

Transor("box64",
    {  HG("DynaRec",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
        perfs=[
            Perf(3763.83/10024.33, Benchmark.COREMARK, Date(2023,1,15),
                 "box64 0.1.8, x86_64 on raspberrypi4, gcc 11.3.0"),
        ],
    ), HG("without-DynaRec",
        Metaface(IsasUSR({Isa.ARM64, Isa.LA64, Isa.RISCV64, Isa.POWERPC64, Isa.X86_64}), {Kernel.LINUX}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2020,12,1), Date.today(), color="#B5E853", parent=box86,
    desc="https://github.com/ptitSeb/box64",
)

Anbox_halium = Transor("Anbox-halium",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2021,4,16), Date(2021,8,27), color="#009688", parent=Anbox,
    desc="Mirror: https://github.com/my-helps/anbox-halium",
)

Transor("Deepin Android Runtime",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2021,6,29), Date.today(), dev=Dev.UnionTech,
    desc="https://www.deepin.org/zh/2021/06/29/deepin-20-2-2/",
)

Transor("waydroid",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}),
    ) for isa in [Isa.X86_64, Isa.ARM64]},
    Date(2021,8,27), Date.today(), color="#F0AD4E", parent=Anbox_halium,
    desc='''
        https://www.reddit.com/r/Ubports/comments/oovy13/anbox_for_halium9_aka_new_anbox_update/
        https://github.com/waydroid/waydroid
    ''',
)
# Lastly, add dummy modules after all modules are added
addDummyModules()
