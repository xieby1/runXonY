from data import *

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
