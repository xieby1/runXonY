from data import *

Dynamo = Transor("Dynamo",
    {  HG("",
        Metaface({(Isa.PARISC, Up.USR)}, {Kernel.UNIX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.PARISC, Up.USR)}, {Kernel.UNIX}),
        term=Term.OPT,
    )},
    Date(1999), Date(2000), dev=Dev.HP,
    desc='''
        1999: Transparent Dynamic Optimization: The Design and Implementation of Dynamo
        2000: Dynamo: A Transparent Dynamic Optimization System
    ''',
)
