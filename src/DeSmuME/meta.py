from data import *

# TODO: non-general, game
Transor("DeSmuME",
    {  HG("",
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR_PVL)}),
    )},
    Date(2006,4,6), Date.today(), "#A4A8FF", "GPL2",
    feat='''
        peripherals,
        bios (loading and executing ROMs) (able to run external bios)
    ''',
    desc='''
        https://desmume.org/
        https://github.com/TASEmulators/desmume
        http://wiki.desmume.org/index.php?title=Faq
    ''',
)
