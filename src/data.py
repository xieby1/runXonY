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

# Lastly, add dummy modules after all modules are added
addDummyModules()
