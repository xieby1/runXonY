from data import *

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
