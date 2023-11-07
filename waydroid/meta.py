from data import *
from Anbox_halium.meta import *

Transor("waydroid",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}),
    ) for isa in [Isa.X86_64, Isa.ARM64]},
    Date(2021,8,27), Date.today(), color="#F0AD4E", parent=Anbox_halium,
    desc='''
        https://www.reddit.com/r/Ubports/comments/oovy13/anbox_for_halium9_aka_new_anbox_update/
        https://github.com/waydroid/waydroid
    ''',
)
