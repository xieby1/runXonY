# How do I type hint a method with the type of the enclosing class?
# https://stackoverflow.com/questions/33533148/
from __future__ import annotations
import enum
import typing
import warnings

HashItem = typing.TypeVar("HashItem", bound=typing.Hashable)

class HashMap(typing.Generic[HashItem]):
    def __init__(self) -> None:
        self.buckets: dict[int, list[HashItem]] = dict()

    def _common(self, item: HashItem, add: bool, replace: bool) -> typing.Optional[HashItem]:
        found: typing.Optional[HashItem] = None
        hash = item.__hash__()
        if hash in self.buckets:
            bucket: list[HashItem] = self.buckets[hash]
            for i, record in enumerate(bucket):
                if record == item:
                    found = record
                    if replace:
                        bucket[i] = item
                    break
            if not found and add:
                bucket.append(item)
        elif add: # hash not in self.buckets
            self.buckets[hash] = [item]
        return found

    def add(self, item: HashItem) -> None:
        self._common(item, True, False)

    def get(self, item: HashItem) -> typing.Optional[HashItem]:
        return self._common(item, False, False)

    def copy(self) -> HashMap[HashItem]:
        copied = HashMap[HashItem]()
        copied.buckets = self.buckets.copy()
        return copied

    def __contains__(self, item: HashItem) -> bool:
        return bool(self.get(item))

    def __iter__(self) -> HashMap[HashItem]:
        self.buckets_iter: typing.Iterator[int] = self.buckets.__iter__()
        self.item_iter: typing.Iterator[HashItem] = list().__iter__()
        return self

    def __next__(self) -> HashItem:
        try:
            return self.item_iter.__next__()
        except StopIteration:
            try:
                hash: int = self.buckets_iter.__next__()
                self.item_iter = self.buckets[hash].__iter__()
                return self.__next__()
            except StopIteration:
                raise StopIteration

class Src(enum.Enum):
    NONE = enum.auto()

    C_SRC = C = enum.auto()
    CPP_SRC = CPP = enum.auto()

    END = enum.auto()
    idx = 6

class App(enum.Enum):
    NONE = enum.auto()
    APPS = ANY = enum.auto()
    END = enum.auto()
    idx = 5
App_ANYs = set(App(i) for i in range(App.ANY.value, App.END.value))

class Sysapp(enum.Enum):
    NONE = enum.auto()
    SYSAPPS = ANY = enum.auto()
    END = enum.auto()
    idx = 4
Sysapp_ANYs = set(Sysapp(i) for i in range(Sysapp.ANY.value, Sysapp.END.value))

class Lib(enum.Enum):
    NONE = enum.auto()
    LIBS = ANY = enum.auto()
    END = enum.auto()
    idx = 3
Lib_ANYs = set(Lib(i) for i in range(Lib.ANY.value, Lib.END.value))

class Syslib(enum.Enum):
    NONE = enum.auto()

    SYSLIBS = DEFAULT = enum.auto()

    LINUX_SYSLIBS = LINUX = enum.auto()

    BSD_SYSLIBS = BSD = enum.auto()

    MACOS_SYSLIBS = MACOS = enum.auto()

    WINDOWS_SYSLIBS = WINDOWS = enum.auto()

    END = enum.auto()
    idx = 2

class Kernel(enum.Enum):
    NONE = enum.auto()
    KERNELS = ANY = enum.auto()

    NO_SYSCALL = NO_KERNEL = enum.auto()

    OPENVMS = VMS = enum.auto()

    SCO_UNIX = enum.auto()
    TRU64 = OSF1 = DIGITAL_UNIX = enum.auto()
    ULTRIX = enum.auto()
    SUNOS5_UNIX = enum.auto()
    UNIX = enum.auto()

    SUNOS4_BSD = enum.auto()
    BSD = enum.auto()

    LINUX = enum.auto()

    DOS = enum.auto()
    WINDOWS3_1 = enum.auto()
    WINDOWS_NT4_0 = enum.auto()
    WINDOWS = enum.auto()

    MACOS = enum.auto()

    END = enum.auto()
    idx = 1
# https://en.wikipedia.org/wiki/POSIX
Kernel_POSIXs: set[Kernel] = {Kernel.MACOS, Kernel.BSD, Kernel.LINUX}

class Up(enum.Enum):
    NONE = enum.auto()
    USR = USER = UNPVL = UNPRIVILEGE = enum.auto()
    PVL = PRIVILEGE = enum.auto()
    USR_PVL = USER_PRIVILEGE = enum.auto()
    END = enum.auto()
    idx = 0

class Isa(enum.Enum):
    NONE = enum.auto()
    ISAS = ANY = enum.auto()

    VAX = enum.auto()

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

    # TODO
    UMIPSV = enum.auto()

    MIPSI = enum.auto()
    MIPSII = enum.auto()
    MIPSIII = enum.auto()
    MIPSIV = enum.auto()
    MIPSV = enum.auto()
    MIPS32 = enum.auto()
    MIPS64 = enum.auto()

    RISCV32 = enum.auto()
    RISCV64 = enum.auto()

    SPARCV8 = enum.auto()
    SPARCV9 = enum.auto()
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
    idx = 0
Isa_ANYs = set(Isa(i) for i in range(Isa.ANY.value, Isa.END.value))
Isa_X86s = set(Isa(i) for i in range(Isa.I386.value, Isa.X86.value+1))
Isa_X86_64s = set(Isa(i) for i in range(Isa.I386.value, Isa.X86_64.value+1))
Isa_ARM32s = set(Isa(i) for i in range(Isa.ARM.value, Isa.ARM32.value+1))
Isa_ARMV6s = {Isa.ARMV6L, Isa.ARMV6M}
Isa_ARMV7s = {Isa.ARMV7L, Isa.ARMV7M, Isa.ARMV7A, Isa.ARMV7R}
Isa_POWERPC64s = {Isa.POWERPC, Isa.POWERPC64}
Isa_MIPS64s = set(Isa(i) for i in range(Isa.MIPSI.value, Isa.MIPS64.value+1))
Isa_RISCV64s = {Isa.RISCV32, Isa.RISCV64}
Isa_SPARC64s = {Isa.SPARC, Isa.SPARC64}
def IsasUp(isas: set[Isa], up: Up) -> set[typing.Tuple[Isa, Up]]:
    return set((isa, up) for isa in isas)
def IsasUSR(isas: set[Isa]) -> set[typing.Tuple[Isa, Up]]:
    return IsasUp(isas, Up.USR)
def IsasPVL(isas: set[Isa]) -> set[typing.Tuple[Isa, Up]]:
    return IsasUp(isas, Up.PVL)
def IsasUSR_PVL(isas: set[Isa]) -> set[typing.Tuple[Isa, Up]]:
    return IsasUp(isas, Up.USR_PVL)

hierarchy: dict[int, type] = {
    Isa.idx.value: Isa,
    Kernel.idx.value: Kernel,
    Syslib.idx.value: Syslib,
    Lib.idx.value: Lib,
    Sysapp.idx.value: Sysapp,
    App.idx.value: App,
    Src.idx.value: Src,
}

interfaces: HashMap[Interface] = HashMap()

class Interface:
    idx: int = 0
    def __init__(self,
            isa_up: typing.Tuple[Isa, Up] = (Isa.NONE, Up.NONE),
            kernel: Kernel  = Kernel.NONE,
            syslib: Syslib  = Syslib.NONE,
            lib:    Lib     = Lib.NONE,
            sysapp: Sysapp  = Sysapp.NONE,
            app:    App     = App.NONE,
            src:    Src     = Src.NONE,
            ) -> None:
        self.idx = Interface.idx
        Interface.idx += 1
        isa, up = isa_up
        self.isa    = isa
        self.up     = up
        self.kernel = kernel
        self.syslib = syslib
        self.lib    = lib
        self.sysapp = sysapp
        self.app    = app
        self.src    = src
        # upper, lower modules
        self.ls: set[HG] = set()
        self.us: set[HG] = set()
        strings = ()
        for ele in (src, app, sysapp, lib, syslib, kernel, isa, up):
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
        val += self.up.value * mul
        mul += Up.END.value
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
        val += self.src.value * mul
        mul *= Src.END.value
        return val

    def __eq__(self, other: Interface) -> bool:
        if \
                self.isa == other.isa and \
                self.up == other.up and \
                self.kernel == other.kernel and \
                self.syslib == other.syslib and \
                self.lib == other.lib and \
                self.sysapp == other.sysapp and \
                self.app == other.app and \
                self.src == other.src:
            return True
        else:
            return False

modules: HashMap[Module] = HashMap()
allhgs: HashMap[HG] = HashMap()

class Metaface:
    @classmethod
    # Meta-lize an Interface
    def metalize(cls, intfc: Interface) -> Metaface:
        return cls(
            {(intfc.isa, intfc.up)},
            {intfc.kernel},
            {intfc.syslib},
            {intfc.lib},
            {intfc.sysapp},
            {intfc.app},
            {intfc.src},
        )

    def __init__(self,
            isas_ups:   set[typing.Tuple[Isa, Up]] = {(Isa.NONE, Up.NONE)},
            kernels:    set[Kernel] = {Kernel.NONE},
            syslibs:    set[Syslib] = {Syslib.NONE},
            libs:       set[Lib]    = {Lib.NONE},
            sysapps:    set[Sysapp] = {Sysapp.NONE},
            apps:       set[App]    = {App.NONE},
            srcs:       set[Src]    = {Src.NONE},
            ) -> None:
        self.isas_ups:  set[typing.Tuple[Isa, Up]] = isas_ups
        self.kernels:   set[Kernel] = kernels
        self.syslibs:   set[Syslib] = syslibs
        self.libs:      set[Lib]    = libs
        self.sysapps:   set[Sysapp] = sysapps
        self.apps:      set[App]    = apps
        self.srcs:      set[Src]    = srcs
        self.repr = ''
        for isa, up in isas_ups:
            self.repr += isa.name[0] + up.name[0]
        for set in (kernels, syslibs, libs, sysapps, apps, srcs):
            self.repr += '|'
            for ele in set:
                self.repr += ele.name[0]

    def getInterfaces(self) -> set[Interface]:
        _interfaces = set()
        for isa_up in self.isas_ups:
            for kernel in self.kernels:
                for syslib in self.syslibs:
                    for lib in self.libs:
                        for sysapp in self.sysapps:
                            for app in self.apps:
                                for src in self.srcs:
                                    _interfaces.add(Interface(
                                        isa_up,
                                        kernel,
                                        syslib,
                                        lib,
                                        sysapp,
                                        app,
                                        src,
                                    ))
        return _interfaces

    def __hash__(self) -> int:
        val = 0
        mul = 1
        for isa, up in self.isas_ups:
            val ^= hash(isa.value * up.value* mul)
        mul *= Isa.END.value * Up.END.value
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
        for src in self.srcs:
            val ^= hash(src.value * mul)
        mul *= Src.END.value
        return val

    def __eq__(self, other: Metaface) -> bool:
        if \
                self.isas_ups == other.isas_ups and \
                self.kernels == other.kernels and \
                self.syslibs == other.syslibs and \
                self.libs == other.libs and \
                self.sysapps == other.sysapps and \
                self.apps == other.apps and \
                self.srcs == other.srcs:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return self.repr

class HG:
    idx: int = 0
    def __init__(self,
            name: str,
            h: Metaface, # Host
            g: Metaface, # Guest
            # TODO: add efficiency
            # eff,
            add: bool = True,
            ) -> None:
        self.idx = HG.idx
        HG.idx += 1
        self.name = name
        self.h = h
        self.g = g
        self.repr = h.repr + ':' + g.repr

        if not add:
            return
        hinterfaces =  h.getInterfaces()
        for intfc in hinterfaces:
            record: typing.Optional[Interface] = interfaces.get(intfc)
            if not record:
                interfaces.add(intfc)
                record = intfc
            record.us.add(self)
        ginterfaces = g.getInterfaces()
        for intfc in ginterfaces:
            record: typing.Optional[Interface] = interfaces.get(intfc)
            if not record:
                interfaces.add(intfc)
                record = intfc
            record.ls.add(self)

    def setmodule_then_addhg(self, module: Module) -> None:
        self.module = module
        if len(self.name):
            self.name = "-".join((module.name, self.name))
        else:
            self.name = module.name
        if self in allhgs:
            warnings.warn("io %s has been defined!" % self.name)
        else:
            allhgs.add(self)

    def __hash__(self) -> int:
        # make h and g not commutative
        return hash(self.h.__hash__()) ^ self.g.__hash__()

    def __eq__(self, other: HG) -> bool:
        if self.h == other.h and self.g == other.g:
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
            ios: set[HG],
            ) -> None:
        self.name = name
        self.ios = ios
        record: typing.Optional[Module] = modules.get(self)
        if record:
            warnings.warn("module %s has been defined!" % name)
        modules.add(self)
        for io in ios:
            io.setmodule_then_addhg(self)
    def __repr__(self) -> str:
        return self.name
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, other: Module) -> bool:
        return self.name == other.name

class DummyModule(Module):
    def __init__(self,
            name: str,
            hgs: set[HG],
            ) -> None:
        self.name = name
        self.hgs = hgs
        record: typing.Optional[Module] = modules.get(self)
        if not record:
            modules.add(self)
            record = self
        for hg in hgs:
            hg.setmodule_then_addhg(self)

class Transor(Module):
    def __init__(self,
            name: str,
            hgs: set[HG],
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
        self.feat = feat.replace("\n", r"\n")
        self.desc = desc.replace("\n", r"\n")
        self.renames = renames
        super().__init__(name, hgs)

# return True for added, False for not add
DMargs = tuple[tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App]
def addDummyModule(args: DMargs, hierarchyIdx: int) -> bool:
    if hierarchyIdx == Isa.idx.value:
        hintfc = Interface()
        gintfc = Interface((args[0][0], Up.USR_PVL))
    elif hierarchyIdx == Kernel.idx.value:
        hintfc = Interface((args[0][0], Up.USR_PVL))
        gintfc = Interface(*(args[:hierarchyIdx+1]))
    else:
        hintfc = Interface(*(args[:hierarchyIdx]))
        gintfc = Interface(*(args[:hierarchyIdx+1]))
    hg = HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), False)
    if hintfc != gintfc and hintfc in interfaces and gintfc in interfaces:
        if hg not in allhgs:
            # print(args)
            # print("%d - %d" % (hierarchyIdx, hierarchyIdx+1))
            # print("%s - %s" % (hintfc.name, gintfc.name))
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
        return False
    if hierarchyIdx == Isa.idx.value:
        if args[Isa.idx.value][0].value > Isa.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
        else:
            return False
    elif hierarchyIdx == Kernel.idx.value:
        if args[Kernel.idx.value].value > Kernel.NO_KERNEL.value and \
                args[Isa.idx.value][0].value > Isa.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
        else:
            return False
    elif hierarchyIdx == Syslib.idx.value:
        if args[Kernel.idx.value].value > Kernel.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
        else:
            return False
    elif hierarchyIdx == Lib.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
    elif hierarchyIdx == Sysapp.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
    elif hierarchyIdx == App.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc))})
    else:
        warnings.warn("addDummyModule unknown hierarchyIdx %d" % hierarchyIdx)
    return True

Intfctype = typing.Union[tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Src]
intfctypes = (tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Src)
def addDummyModulesByIntfc(intfc: Interface) -> None:
    toptype: type
    if intfc.src != Src.NONE:
        return
    if intfc.app != App.NONE:
        toptype = App
    elif intfc.sysapp != Sysapp.NONE:
        toptype = Sysapp
    elif intfc.lib != Lib.NONE:
        toptype = Lib
    elif intfc.syslib != Syslib.NONE:
        toptype = Syslib
    elif intfc.kernel != Kernel.NONE:
        toptype = Kernel
    elif intfc.isa != Isa.NONE:
        toptype = Isa
    else:
        return
    args = (
        (intfc.isa, intfc.up),
        intfc.kernel,
        Syslib.DEFAULT if intfc.syslib==Syslib.NONE else intfc.syslib,
        Lib.ANY if intfc.lib==Lib.NONE else intfc.lib,
        Sysapp.ANY if intfc.sysapp==Sysapp.NONE else intfc.sysapp,
        App.ANY if intfc.app==App.NONE else intfc.app,
    )

    # upwards
    for i in range(toptype.idx.value+1, App.idx.value+1): # [toptype+1, App]
        if not addDummyModule(args, i):
            break
    # downward
    for i in reversed(range(Isa.idx.value, toptype.idx.value+1)): # reversed([Isa, toptype])
        if not addDummyModule(args, i):
            break

def addDummyModules() -> None:
    _interfaces = interfaces.copy()
    for intfc in _interfaces:
        addDummyModulesByIntfc(intfc)

def outputDot(f: typing.TextIO) -> None:
    def prefix(x: object) -> str:
        return x.__class__.__name__[0]
    f.write('digraph {\nnode[shape=box];\n')
    # nodes (IOs and Interfaces)
    for hg in allhgs:
        ## Transors' IOs
        if isinstance(hg.module, Transor):
            f.write('%s%d[label="%s", style=filled, fontcolor=white, fillcolor=black];\n' %(prefix(hg.module), hg.idx, hg.name))
        ## DummyModules' IOs
        elif isinstance(hg.module, DummyModule):
            f.write('%s%d[label="%s", style="dotted"];\n' % (prefix(hg.module), hg.idx, hg.name))
        ## Other Modules' IOs
        else:
            f.write('%s%d[label="%s"];\n' %(prefix(hg.module), hg.idx, hg.name))
    ## Interfaces
    for intfc in interfaces:
        if len(intfc.name):
            f.write('%s%d[label="%s", style=rounded];\n' %(prefix(intfc), intfc.idx, intfc.name))
    # edges
    for intfc in interfaces:
        if len(intfc.name):
            for l in intfc.ls:
                f.write('%s%d -> %s%d\n' % (prefix(l.module), l.idx, prefix(intfc), intfc.idx))
            for u in intfc.us:
                f.write('%s%d -> %s%d\n' % (prefix(intfc), intfc.idx, prefix(u.module), u.idx))
    f.write("}\n")

def outputJson(f: typing.TextIO) -> None:
    def prefix(x: object) -> str:
        return x.__class__.__name__[0]
    f.write('{\n')
    # nodes (IOs and Interfaces)
    f.write('"nodes": {\n')
    num: int = 0
    for hg in allhgs:
        if num>0:
            f.write(',')
        else:
            f.write(' ')
        num += 1
        f.write(' "%s%d": "%s"\n' %(prefix(hg.module), hg.idx, hg.name))
    ## Interfaces
    for intfc in interfaces:
        if len(intfc.name):
            if num>0:
                f.write(',')
            else:
                f.write(' ')
            num += 1
            f.write(' "%s%d": "%s"\n' %(prefix(intfc), intfc.idx, intfc.name))
    f.write('},\n')
    # edges
    f.write('"edges": [\n')
    num = 0
    for intfc in interfaces:
        if len(intfc.name):
            for l in intfc.ls:
                if num>0:
                    f.write(',')
                else:
                    f.write(' ')
                num += 1
                f.write(' ["%s%d", "%s%d"]\n' % (prefix(l.module), l.idx, prefix(intfc), intfc.idx))
            for u in intfc.us:
                if num>0:
                    f.write(',')
                else:
                    f.write(' ')
                num += 1
                f.write(' ["%s%d", "%s%d"]\n' % (prefix(intfc), intfc.idx, prefix(u.module), u.idx))
    f.write(']\n')
    f.write('}\n')

def outputEdges(f: typing.TextIO) -> None:
    f.write('digraph {\n')
    for intfc in interfaces:
        if len(intfc.name):
            for l in intfc.ls:
                f.write('"%s" -> "intfc:%s"\n' % (l.name, intfc.name))
            for u in intfc.us:
                f.write('"intfc:%s" -> "%s"\n' % (intfc.name, u.name))
    f.write("}\n")

def outputGnucladCsv(f: typing.TextIO) -> None:
    f.write("#, name, color, parent, start, stop, icon, desc, renames...\n")
    for module in modules:
        if isinstance(module, Transor):
            f.write('"%s","%s","%s","%s","%s","%s","%s","%s"\n' % (
                "N", module.name, module.color, "",
                module.start, module.stop, "", module.desc
            ))
