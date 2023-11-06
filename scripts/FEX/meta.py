from data import *

Transor("FEX",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64, Isa.ARM64}), {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86_64, Isa.X86}), {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2018,11,16), Date.today(), license="MIT",
    feat='''
        Interp,
        JIT,
        LLVM disasm,
        thunklib: guest ↔ host
    ''',
    desc='''
        https://github.com/FEX-Emu/FEX
        git commit 5efab55ea9b: remove problematic LLVM JIT
    ''',
)
