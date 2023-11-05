from data import *

# TODO: non-general, game
Transor("PPSSPP",
    {  HG("",
        Metaface(IsasUSR(isas), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.MIPSIII, Up.USR_PVL)}),
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
        ) for isas,kernel in zip(
            [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs],
            [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX])
    }|{HG("",
        Metaface(IsasUSR(Isa_MODERN_ANDROIDs), {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(Isa.MIPSIII, Up.USR_PVL)}),
        # TODO: Android auto generate term?
        term=Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION,
    )},
    Date(2012,3,25), Date.today(), color="#0086B2", license="GPL2",
    desc='''
        https://www.ppsspp.org/
        https://github.com/hrydgard/ppsspp
    ''',
)
