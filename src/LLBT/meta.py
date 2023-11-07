from data import *

Transor("LLBT",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface({(Isa.ARM, Up.USR)}, {Kernel.LINUX}),
        term=Term.STATIC_BINARY_TRANSLATOR,
    )},
    Date(2012), Date(2014), dev=Dev.TJD,
    desc='''
        2012: LLBT: An LLVM-based Static Binary Translator
        2013: Automatic Validation for Static Binary Translation
        2014: A Retargetable Static Binary Translator for the ARM Architecture
    ''',
)
