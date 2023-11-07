from data import *
from Ryujinx.meta import *

Transor("ChocolArm64",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}),
    )},
    Date(2018,2,21), Date(2019,11,1), color="#FF5F55", parent=Ryujinx, license="Unlicense",
    feat="Framework",
    desc='''
        https://github.com/Ryujinx/Ryujinx/
        https://github.com/Ryujinx/ChocolArm64
    ''',
)
