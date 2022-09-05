#!/usr/bin/env python3
from lib import *

qemu_user_i = {
    Isa.AARCH64, Isa.ARM, Isa.X86, Isa.X86_64,
    Isa.LA64, Isa.MIPS,
    Isa.POWERPC, Isa.RISCV64, Isa.S390X, Isa.SPARC,
}
qemu_user_o = {
    Isa.ALPHA, Isa.ARM, Isa.AARCH64, Isa.X86, Isa.X86_64,
    Isa.AVR, Isa.CRIS, Isa.HEXAGON, Isa.HPPA, Isa.M68K,
    Isa.MICROBLAZE, Isa.MIPS, Isa.MIPS64, Isa.NIOS2,
    Isa.OPENRISC, Isa.POWERPC, Isa.RISCV64, Isa.RX,
    Isa.S390X, Isa.SH4, Isa.SPARC, Isa.TRICORE, Isa.XTENSA,
}
Module(
    # name
    "QEMU-user",
    # ios: set[IO]
    {  IO(
        "linux",
        Metaface(qemu_user_i, {Kernel.LINUX}, Syslib_ANYs, Lib_ANYs),
        Metaface(qemu_user_o, {Kernel.LINUX})
    ), IO(
        "bsd",
        Metaface(qemu_user_i, {Kernel.BSD}, Syslib_ANYs, Lib_ANYs),
        Metaface(qemu_user_o, {Kernel.BSD})
    ), IO(
        "tci-linux",
        Metaface(Isa_ANYs, {Kernel.LINUX}, Syslib_ANYs, Lib_ANYs),
        Metaface(qemu_user_o, {Kernel.LINUX})
    ), IO(
        "tci-bsd",
        Metaface(Isa_ANYs, {Kernel.BSD}, Syslib_ANYs, Lib_ANYs),
        Metaface(qemu_user_o, {Kernel.BSD})
    )},
    Date(2003,2),
    Date.today(),
    "#F60",
    "IR",
    "2005: QEMU, a Fast and Portable Dynamic Translator",
)

printGnucladCsv()
