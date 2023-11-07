from data import *

# TODO: non-general, game
Transor("bsnes",
    { HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS, Kernel.BSD}, {Syslib.DEFAULT}, {Lib.ANY}),
        # TODO: Too many old chips!!!
        Metaface(),
    )},
    Date(2004,10,14), Date.today(), "#DC1212",
    desc='''
        https://higan.dev/about
        https://github.com/higan-emu/higan/tree/master/higan/component/processor
    ''',
    renames=[Rename("higan", Date(2012,8,9))],
)
