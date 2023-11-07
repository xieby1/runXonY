from data import *

Transor("Pin", set(
    HG("",
        Metaface({(Isa.X86, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {kernel}),
    )
    for kernel in (Kernel.LINUX, Kernel.WINDOWS, Kernel.MACOS)),
    Date(2005), Date.today(), dev=Dev.INTEL, term=Term.INSTRUMENTER,
    feat="PinCRT",
    desc='''
        2005: Pin: Building Customized Program Analysis Tools with Dynamic Instrumentation
    ''',
)
