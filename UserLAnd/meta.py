from data import *
from proot.meta import *

Transor("UserLAnd",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs, Sysapp_ANYs, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, Lib_ANYs),
    )},
    Date(2018,3,21), Date.today(), color="#221F1F", parent=proot,
    feat="No-privilege fs isolation",
    desc="https://github.com/CypherpunkArmory/UserLAnd.git",
)
