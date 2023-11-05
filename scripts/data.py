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
