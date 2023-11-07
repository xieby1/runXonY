from data import *
from Dynamo.meta import *

# TODO: Android
Transor("DynamoRIO",
    {  HG('-'.join((kernel.name, isa.name)),
        Metaface(IsasUSR({isa}), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({isa}), {kernel}),
        term=Term.I_O,
    ) for isa in [Isa.X86, Isa.X86_64, Isa.ARM32, Isa.AARCH64]
      for kernel in [Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS]},
    Date(2000), Date.today(), dev=Dev.HP,
    desc="https://dynamorio.org/index.html",
    parent=Dynamo,
    renames=[Rename("DynamoRIO(VMware)", Date(2007), "")]
)
