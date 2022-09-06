# How do I type hint a method with the type of the enclosing class?
# https://stackoverflow.com/questions/33533148/
from __future__ import annotations
import enum
import typing
import warnings

class App(enum.Enum):
    NONE = enum.auto()
    APPS = ANY = enum.auto()
    END = enum.auto()
App_ANYs = set(App(i) for i in range(App.ANY.value, App.END.value))

class Sysapp(enum.Enum):
    NONE = enum.auto()
    SYSAPPS = ANY = enum.auto()
    END = enum.auto()
Sysapp_ANYs = set(Sysapp(i) for i in range(Sysapp.ANY.value, Sysapp.END.value))

class Lib(enum.Enum):
    NONE = enum.auto()
    LIBS = ANY = enum.auto()
    END = enum.auto()
Lib_ANYs = set(Lib(i) for i in range(Lib.ANY.value, Lib.END.value))

class Syslib(enum.Enum):
    NONE = enum.auto()
    SYSLIBS = ANY = enum.auto()
    END = enum.auto()
Syslib_ANYs = set(Syslib(i) for i in range(Syslib.ANY.value, Syslib.END.value))

class Kernel(enum.Enum):
    NONE = enum.auto()
    KERNELS = ANY = enum.auto()
    SCO_UNIX = enum.auto()
    TRU64 = OSF1 = DIGITAL_UNIX = enum.auto()
    ULTRIX = enum.auto()
    UNIX = enum.auto()
    LINUX = enum.auto()
    DOS = enum.auto()
    WINDOWS3_1 = enum.auto()
    WINDOWS = enum.auto()
    MACOS = enum.auto()
    BSD = enum.auto()
    END = enum.auto()

class Isa(enum.Enum):
    NONE = enum.auto()
    ISAS = ANY = enum.auto()
    I386 = enum.auto()
    I486 = enum.auto()
    I586 = enum.auto()
    I686 = enum.auto()
    X86 = enum.auto()
    X86_64 = enum.auto()

    ARM = enum.auto()
    ARMV5TEL = enum.auto()
    ARMV6L = enum.auto()
    ARMV6M = enum.auto()
    ARMV7L = enum.auto()
    ARMV7M = enum.auto()
    ARMV7A = enum.auto()
    ARMV7R = enum.auto()
    ARMV8M = enum.auto()
    ARMV8A = enum.auto()
    ARMV8R = enum.auto()
    AARCH32 = ARM32 = enum.auto()
    AARCH64 = ARM64 = enum.auto()

    POWERPC = enum.auto()
    POWERPC64 = enum.auto()

    MIPS = enum.auto()
    MIPS64 = enum.auto()

    RISCV32 = enum.auto()
    RISCV64 = enum.auto()

    SPARC = enum.auto()
    SPARC64 = enum.auto()

    # TODO: from qemu tcg

    LA = LA64 = LOONGARCH = LOONGARCH64 = enum.auto()
    S390 = S390X = enum.auto()

    # TODO: from qemu targets

    ALPHA = enum.auto()
    AVR = enum.auto()
    CRIS = enum.auto()
    HEXAGON = enum.auto()
    HPPA = enum.auto()
    M68K = enum.auto()
    MICROBLAZE = enum.auto()
    NIOS2 = enum.auto()
    OPENRISC = enum.auto()
    RX = enum.auto()
    SH = SH4 = enum.auto()
    TRICORE = enum.auto()
    XTENSA = enum.auto()

    # TODO: from linux arch
    ARC = enum.auto()
    CSKY = enum.auto()
    IA64 = enum.auto()
    PARISC = enum.auto()

    END = enum.auto()
Isa_ANYs = set(Isa(i) for i in range(Isa.ANY.value, Isa.END.value))
Isa_X86s = set(Isa(i) for i in range(Isa.I386.value, Isa.X86.value+1))
Isa_X86_64s = set(Isa(i) for i in range(Isa.I386.value, Isa.X86_64.value+1))
Isa_ARM32s = set(Isa(i) for i in range(Isa.ARM.value, Isa.ARM32.value+1))
Isa_ARMV6s = {Isa.ARMV6L, Isa.ARMV6M}
Isa_ARMV7s = {Isa.ARMV7L, Isa.ARMV7M, Isa.ARMV7A, Isa.ARMV7R}
Isa_POWERPC64s = {Isa.POWERPC, Isa.POWERPC64}
Isa_MIPS64s = {Isa.MIPS, Isa.MIPS64}
Isa_RISCV64s = {Isa.RISCV32, Isa.RISCV64}
Isa_SPARC64s = {Isa.SPARC, Isa.SPARC64}


# TODO: use hashmap
#       though currently there will be no collision
interfaces: dict[int, Interface] = dict()

class Interface:
    idx: int = 0
    def __init__(self,
            isa:    Isa     = Isa.NONE,
            kernel: Kernel  = Kernel.NONE,
            syslib: Syslib  = Syslib.NONE,
            lib:    Lib     = Lib.NONE,
            sysapp: Sysapp  = Sysapp.NONE,
            app:    App     = App.NONE,
            ) -> None:
        self.idx = Interface.idx
        Interface.idx += 1
        self.isa    = isa
        self.kernel = kernel
        self.syslib = syslib
        self.lib    = lib
        self.sysapp = sysapp
        self.app    = app
        # higher, lower modules
        self.ls: set[IO] = set()
        self.hs: set[IO] = set()
        strings = ()
        for ele in (app, sysapp, lib, syslib, kernel, isa):
            if ele.value > 1: # not NONE
                strings += (ele.name,)
        self.name = '-'.join(strings)

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        val = 0
        mul = 1
        val += self.isa.value * mul
        mul *= Isa.END.value
        val += self.kernel.value * mul
        mul *= Kernel.END.value
        val += self.syslib.value * mul
        mul *= Syslib.END.value
        val += self.lib.value * mul
        mul *= Lib.END.value
        val += self.sysapp.value * mul
        mul *= Sysapp.END.value
        val += self.app.value * mul
        mul *= App.END.value
        return val

    def __eq__(self, other: Interface) -> bool:
        if \
                self.isa == other.isa and \
                self.kernel == other.kernel and \
                self.syslib == other.syslib and \
                self.lib == other.lib and \
                self.sysapp == other.sysapp and \
                self.app == other.app:
            return True
        else:
            return False

modules: dict[str, Module] = dict()
allios: dict[str, IO] = dict()

class Metaface:
    def __init__(self,
            isas:       set[Isa]    = {Isa.NONE},
            kernels:    set[Kernel] = {Kernel.NONE},
            syslibs:    set[Syslib] = {Syslib.NONE},
            libs:       set[Lib]    = {Lib.NONE},
            sysapps:    set[Sysapp] = {Sysapp.NONE},
            apps:       set[App]    = {App.NONE},
            ) -> None:
        self.isas:      set[Isa]    = isas
        self.kernels:   set[Kernel] = kernels
        self.syslibs:   set[Syslib] = syslibs
        self.libs:      set[Lib]    = libs
        self.sysapps:   set[Sysapp] = sysapps
        self.apps:      set[App]    = apps
        self.repr = ''
        for set in (isas, kernels, syslibs, libs, sysapps, apps):
            for ele in set:
                self.repr += ele.name[0]
            self.repr += '|'

    def getInterfaces(self) -> set[Interface]:
        _interfaces = set()
        for isa in self.isas:
            for kernel in self.kernels:
                for syslib in self.syslibs:
                    for lib in self.libs:
                        for sysapp in self.sysapps:
                            for app in self.apps:
                                _interfaces.add(Interface(
                                    isa,
                                    kernel,
                                    syslib,
                                    lib,
                                    sysapp,
                                    app
                                ))
        return _interfaces

    def __hash__(self) -> int:
        val = 0
        mul = 1
        for isa in self.isas:
            val ^= hash(isa.value * mul)
        mul *= Isa.END.value
        for kernel in self.kernels:
            val ^= hash(kernel.value * mul)
        mul *= Kernel.END.value
        for syslib in self.syslibs:
            val ^= hash(syslib.value * mul)
        mul *= Syslib.END.value
        for lib in self.libs:
            val ^= hash(lib.value * mul)
        mul *= Lib.END.value
        for sysapp in self.sysapps:
            val ^= hash(sysapp.value * mul)
        mul *= Sysapp.END.value
        for app in self.apps:
            val ^= hash(app.value * mul)
        mul *= App.END.value
        return val

    def __eq__(self, other: Metaface) -> bool:
        if \
                self.isas == other.isas and \
                self.kernels == other.kernels and \
                self.syslibs == other.syslibs and \
                self.libs == other.libs and \
                self.sysapps == other.sysapps and \
                self.apps == other.apps:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return self.repr

class IO:
    idx: int = 0
    def __init__(self,
            name: str,
            i: Metaface,
            o: Metaface,
            # TODO: add efficiency
            # eff,
            ) -> None:
        self.idx = IO.idx
        IO.idx += 1
        self.name = name
        self.i = i
        self.o = o
        self.repr = i.repr + ':' + o.repr

        iinterfaces =  i.getInterfaces()
        for intfc in iinterfaces:
            hash = intfc.__hash__()
            if hash not in interfaces:
                interfaces[hash] = intfc
            interfaces[hash].hs.add(self)
        ointerfaces = o.getInterfaces()
        for intfc in ointerfaces:
            hash = intfc.__hash__()
            if hash not in interfaces:
                interfaces[hash] = intfc
            interfaces[hash].ls.add(self)

    def setmodule_then_addio(self, module: Module) -> None:
        self.module = module
        if len(self.name):
            self.name = "-".join((module.name, self.name))
        else:
            self.name = module.name
        if self.name in allios:
            warnings.warn("io %s has been defined!" % self.name)
        else:
            allios[self.name] = self

    def __hash__(self) -> int:
        # make i and o not commutative
        return hash(self.i.__hash__()) ^ self.o.__hash__()

    def __eq__(self, other: IO) -> bool:
        if self.i == other.i and self.o == other.o:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return self.repr

import datetime

class Date(datetime.date):
    def __new__(cls, year: int = 1, month: int = 1, day: int = 1) -> Date:
        return super().__new__(cls, year, month, day)
    def __str__(self) -> str:
        return self.strftime("%Y.%m.%d")

class Rename:
    def __init__(self,
            rename: str,
            date: Date,
            desc: str = '',
            ) -> None:
        self.rename = rename
        self.date = date,
        self.desc = desc

class Module:
    def __init__(self,
            name: str,
            ios: set[IO],
            ) -> None:
        self.name = name
        self.ios = ios
        if name in modules and \
                not isinstance(modules[name], DummyModule):
            warnings.warn("module %s has been defined!" % name)
        modules[name] = self
        for io in ios:
            io.setmodule_then_addio(modules[name])
    def __repr__(self) -> str:
        return self.name
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, other: Module) -> bool:
        return self.name == other.name

class DummyModule(Module):
    def __init__(self,
            name: str,
            ios: set[IO],
            ) -> None:
        self.name = name
        self.ios = ios
        if name not in modules:
            modules[name] = self
        for io in ios:
            io.setmodule_then_addio(modules[name])

class Transor(Module):
    def __init__(self,
            name: str,
            ios: set[IO],
            start: Date,
            stop: Date = Date(),
            color: str = '#000',
            # TODO: enum licenses
            license: str = '',
            # TODO: enum devs
            dev: str = '',
            feat: str = '',
            desc: str = '',
            renames: list[Rename] = list(),
            ) -> None:
        self.start = start
        if stop < start:
            self.stop = start
        else:
            self.stop = stop
        self.color = color
        self.license = license
        self.dev = dev
        self.feat = feat
        self.desc = desc
        self.renames = renames
        super().__init__(name, ios)


def addDummyModule(intfc: Interface) -> None:
    name = intfc.isa.name
    iargs = ()
    oargs = ({intfc.isa},)
    if name not in allios and \
            intfc.isa.value > Isa.ANY.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})
    name = '-'.join((intfc.kernel.name, name))
    iargs = oargs
    oargs += ({intfc.kernel},)
    if name not in allios and \
            intfc.kernel.value > Kernel.ANY.value and \
            intfc.isa.value > Isa.ANY.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})
    name = '-'.join((intfc.syslib.name, name))
    iargs = oargs
    oargs += ({intfc.syslib},)
    if name not in allios and \
            intfc.syslib.value > Syslib.NONE.value and \
            intfc.kernel.value > Kernel.ANY.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})
    name = '-'.join((intfc.lib.name, name))
    iargs = oargs
    oargs += ({intfc.lib},)
    if name not in allios and \
            intfc.lib.value > Lib.NONE.value and \
            intfc.syslib.value > Syslib.NONE.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})
    name = '-'.join((intfc.sysapp.name, name))
    iargs = oargs
    oargs += ({intfc.sysapp},)
    if name not in allios and \
            intfc.sysapp.value > Sysapp.NONE.value and \
            intfc.lib.value > Lib.NONE.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})
    name = '-'.join((intfc.app.name, name))
    iargs = oargs
    oargs += ({intfc.app},)
    if name not in allios and \
            intfc.app.value > App.NONE.value and \
            intfc.sysapp.value > Sysapp.NONE.value:
        DummyModule(name, {IO("", Metaface(*iargs), Metaface(*oargs))})

def addDummyModules() -> None:
    _interfaces = interfaces.copy()
    for intfc in _interfaces.values():
        addDummyModule(intfc)

def outputDot(f: typing.TextIO) -> None:
    def prefix(x: object) -> str:
        return x.__class__.__name__[0]
    f.write('digraph {\nnode[shape=box];\n')
    # nodes (IOs and Interfaces)
    for io in allios.values():
        ## Transors' IOs
        if isinstance(io.module, Transor):
            f.write('%s%d[label="%s", style=filled, fontcolor=white, fillcolor=black];\n' %(prefix(io.module), io.idx, io.name))
        ## DummyModules' IOs
        elif isinstance(io.module, DummyModule):
            f.write('%s%d[label="%s", style="dotted"];\n' % (prefix(io.module), io.idx, io.name))
        ## Other Modules' IOs
        else:
            f.write('%s%d[label="%s"];\n' %(prefix(io.module), io.idx, io.name))
    ## Interfaces
    for intfc in interfaces.values():
        if len(intfc.name):
            f.write('%s%d[label="%s", style=rounded];\n' %(prefix(intfc), intfc.idx, intfc.name))
    # edges
    for intfc in interfaces.values():
        if len(intfc.name):
            for l in intfc.ls:
                f.write('%s%d -> %s%d\n' % (prefix(l.module), l.idx, prefix(intfc), intfc.idx))
            for h in intfc.hs:
                f.write('%s%d -> %s%d\n' % (prefix(intfc), intfc.idx, prefix(h.module), h.idx))
    f.write("}\n")

def outputEdges(f: typing.TextIO) -> None:
    f.write('digraph {\n')
    for intfc in interfaces.values():
        if len(intfc.name):
            for l in intfc.ls:
                f.write('"%s" -> "intfc:%s"\n' % (l.name, intfc.name))
            for h in intfc.hs:
                f.write('"intfc:%s" -> "%s"\n' % (intfc.name, h.name))
    f.write("}\n")

def outputGnucladCsv(f: typing.TextIO) -> None:
    f.write("#, name, color, parent, start, stop, icon, desc, renames...\n")
    for module in modules.values():
        if isinstance(module, Transor):
            f.write('"%s","%s","%s","%s","%s","%s","%s","%s"\n' % (
                "N", module.name, module.color, "",
                module.start, module.stop, "", module.desc
            ))
