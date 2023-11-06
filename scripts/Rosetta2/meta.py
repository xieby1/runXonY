from data import *

Transor("Rosetta 2",
    {  HG("",
        Metaface({(Isa.AARCH64, Up.USR)}, {Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.MACOS}),
    )},
    Date(2020), Date.today(), color="#525152", dev=Dev.APPLE,
    desc="https://en.wikipedia.org/wiki/Rosetta_%28software%29",
)
