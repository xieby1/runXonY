from data import *

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
