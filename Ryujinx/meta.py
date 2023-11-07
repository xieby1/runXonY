from data import *

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
