#!/usr/bin/env python3
from lib import *

# https://github.com/torvalds/linux/tree/master/arch
Isa_LINUXs = {Isa.ALPHA, Isa.ARC} | Isa_ARM32s | {Isa.ARM64,
    Isa.CSKY, Isa.HEXAGON, Isa.IA64, Isa.LOONGARCH, Isa.M68K,
    Isa.MICROBLAZE} | Isa_MIPS64s | {Isa.NIOS2, Isa.OPENRISC,
    Isa.PARISC} | Isa_POWERPC64s | Isa_RISCV64s | {Isa.S390,
    Isa.SH} | Isa_SPARC64s | Isa_X86_64s | {Isa.XTENSA}
Module(Kernel.LINUX.name, set(
    IO(isa.name, Metaface({isa}), Metaface({isa}, {Kernel.LINUX}))
for isa in Isa_LINUXs))

# https://www.freebsd.org/platforms/
Isa_BSDs = Isa_X86_64s | Isa_X86s | {Isa.AARCH64, Isa.ARM} | \
    Isa_ARMV6s | Isa_ARMV7s | Isa_MIPS64s | Isa_POWERPC64s | \
    Isa_RISCV64s | Isa_SPARC64s
# https://www.openbsd.org/plat.html
Isa_BSDs |= {Isa.ALPHA, Isa.HPPA}
Module(Kernel.BSD.name, set(
    IO(isa.name, Metaface({isa}), Metaface({isa}, {Kernel.BSD}))
for isa in Isa_BSDs))

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
        Metaface({Isa.MIPS}, {Kernel.ULTRIX}),
    )},
    Date(1993), dev="Digital",
    desc="1993: Binary Translation by Richard L. Sites"
)

Isa_QEMU_user_is = {
    Isa.AARCH64, Isa.ARM, Isa.X86, Isa.X86_64,
    Isa.LA64, Isa.MIPS,
    Isa.POWERPC, Isa.RISCV64, Isa.S390X, Isa.SPARC,
}
Isa_QEMU_user_os = {
    Isa.ALPHA, Isa.ARM, Isa.AARCH64, Isa.X86, Isa.X86_64,
    Isa.AVR, Isa.CRIS, Isa.HEXAGON, Isa.HPPA, Isa.M68K,
    Isa.MICROBLAZE, Isa.MIPS, Isa.MIPS64, Isa.NIOS2,
    Isa.OPENRISC, Isa.POWERPC, Isa.RISCV64, Isa.RX,
    Isa.S390X, Isa.SH4, Isa.SPARC, Isa.TRICORE, Isa.XTENSA,
}
Transor("QEMU-user",
    {  IO("linux",
        Metaface(Isa_QEMU_user_is & Isa_LINUXs, {Kernel.LINUX}, Syslib_ANYs, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_LINUXs, {Kernel.LINUX})
    ), IO("bsd",
        Metaface(Isa_QEMU_user_is & Isa_BSDs, {Kernel.BSD}, Syslib_ANYs, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_BSDs, {Kernel.BSD})
    ), IO("tci-linux",
        Metaface(Isa_LINUXs, {Kernel.LINUX}, Syslib_ANYs, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_LINUXs, {Kernel.LINUX})
    ), IO("tci-bsd",
        Metaface(Isa_BSDs, {Kernel.BSD}, Syslib_ANYs, Lib_ANYs),
        Metaface(Isa_QEMU_user_os & Isa_BSDs, {Kernel.BSD})
    )},
    Date(2003,2), Date.today(), "#F60", "IR",
    "2005: QEMU, a Fast and Portable Dynamic Translator",
)

addDummyModules()

# printGnucladCsv()
printDot()
# printEdges()
