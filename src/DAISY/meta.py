from data import *

Transor("DAISY",
    {  HG("",
        Metaface({(Isa.DAISY_VLIW, Up.USR_PVL)}),
        Metaface({(Isa.POWERPC, Up.USR_PVL)}),
    )},
    Date(1998), Date(2001), dev=Dev.IBM,
    desc = '''
        1997: DAISY dynamic compilation for 100% architecutral compatibility
        2000: Binary Translation and Architecture Convergence Issues for IBM System/390
        2000: full system binary translation RISC to VLIW
        2000: simulation and debugging of full system bianry translation
        2001: Dynamic binary translation and optimization
    '''
)
