# How do I type hint a method with the type of the enclosing class?
# https://stackoverflow.com/questions/33533148/
from __future__ import annotations
import enum

class App(enum.Enum):
    NONE = enum.auto()
    ANY = enum.auto()
    END = enum.auto()
App_ANYs = set(App(i) for i in range(App.ANY.value, App.END.value))

class Sysapp(enum.Enum):
    NONE = enum.auto()
    ANY = enum.auto()
    END = enum.auto()
Sysapp_ANYs = set(Sysapp(i) for i in range(Sysapp.ANY.value, Sysapp.END.value))

class Lib(enum.Enum):
    NONE = enum.auto()
    ANY = enum.auto()
    END = enum.auto()
Lib_ANYs = set(Lib(i) for i in range(Lib.ANY.value, Lib.END.value))

class Syslib(enum.Enum):
    NONE = enum.auto()
    ANY = enum.auto()
    END = enum.auto()
Syslib_ANYs = set(Syslib(i) for i in range(Syslib.ANY.value, Syslib.END.value))

class Kernel(enum.Enum):
    NONE = enum.auto()
    LINUX = enum.auto()
    WINDOWS = enum.auto()
    MACOS = enum.auto()
    BSD = enum.auto()
    END = enum.auto()

class Isa(enum.Enum):
    NONE = enum.auto()
    ANY = enum.auto()
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

    LA = LA64 = enum.auto()
    S390X = enum.auto()

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
    SH4 = enum.auto()
    TRICORE = enum.auto()
    XTENSA = enum.auto()

    END = enum.auto()
Isa_ANYs = set(Isa(i) for i in range(Isa.ANY.value, Isa.END.value))
Isa_X86 = set(Isa(i) for i in range(Isa.I386.value, Isa.X86.value+1))
Isa_X86_64s = set(Isa(i) for i in range(Isa.I386.value, Isa.X86_64.value+1))
Isa_ARM32s = set(Isa(i) for i in range(Isa.ARM.value, Isa.ARM32.value+1))


# TODO: use hashmap
#       though currently there will be no collision
interfaces: dict[int, Interface] = dict()

class Interface:
    def __init__(self,
            isa:    Isa     = Isa.NONE,
            kernel: Kernel  = Kernel.NONE,
            syslib: Syslib  = Syslib.NONE,
            lib:    Lib     = Lib.NONE,
            sysapp: Sysapp  = Sysapp.NONE,
            app:    App     = App.NONE,
            ) -> None:
        self.isa    = isa
        self.kernel = kernel
        self.syslib = syslib
        self.lib    = lib
        self.sysapp = sysapp
        self.app    = app
        # higher, lower modules
        self.ls: set[IO] = set()
        self.hs: set[IO] = set()
        self.repr = ''
        for ele in (isa, kernel, syslib, lib, sysapp, app):
            self.repr += ele.name[0] + '|'

    def __repr__(self) -> str:
        return self.repr

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

    def __repr__(self) -> str:
        return self.repr

class IO:
    def __init__(self,
            name: str,
            i: Metaface,
            o: Metaface,
            # TODO: add efficiency
            # eff,
            ) -> None:
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

    # make type checker happy,
    # or type checker will alert self.module not exists
    def _set_module(self, module: Module) -> None:
        self.module = module

    def __repr__(self) -> str:
        return self.repr

import datetime

class Date(datetime.date):
    def __new__(cls, year: int = 1, month: int = 1, day: int = 1) -> Date:
        return super().__new__(cls, year, month, day)

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
            start: Date,
            stop: Date = Date(),
            color: str = '',
            # TODO: enum licenses
            license: str = '',
            # TODO: enum devs
            dev: str = '',
            feat: str = '',
            desc: str = '',
            renames: list[Rename] = list(),
            ) -> None:
        self.name = name
        self.ios = ios
        self.start = start
        self.stop = stop
        self.color = color
        self.license = license
        self.dev = dev
        self.feat = feat
        self.desc = desc
        self.renames = renames
        for io in ios:
            io.module = self
        modules[name] = self

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, other: Module) -> bool:
        return self.name == other.name


def printEdges() -> None:
    for intfc in interfaces.values():
        for l in intfc.ls:
            for h in intfc.hs:
                print('"%s" -> "%s"' % (l.name, h.name))

def printGnucladCsv() -> None:
    for module in modules.values():
        print("#, name, color, parent, start, stop, icon, desc, renames...")
        print('"%s","%s","%s","%s","%s","%s","%s","%s"' % (
            "N", module.name, module.color, "",
            module.start.strftime("%Y.%m.%d"),
            module.stop.strftime("%Y.%m.%d"),
            "", module.desc
            ))
