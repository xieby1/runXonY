from data import *

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
