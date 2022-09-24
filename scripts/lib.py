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
    idx = 8

class Rtapp(enum.Enum):
    NONE = enum.auto()

    APPS = ANY = enum.auto()

    END = enum.auto()
    idx = 7

class Rtlib(enum.Enum):
    NONE = enum.auto()

    LIBS = ANY = enum.auto()

    END = enum.auto()
    idx = 6

class App(enum.Enum):
    NONE = enum.auto()

    APPS = ANY = enum.auto()

    ANDROID_RUNTIME = enum.auto()

    END = enum.auto()
    idx = 5

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
    LINUX_ANDROID = enum.auto()

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
    X86 = IA32 = enum.auto()
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
    PARISC = HPPA = enum.auto()

    DAISY_VLIW = DAISY = enum.auto()

    CRUSOE_VLIW = CRUSOE = enum.auto()

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

class Dev(enum.Enum):
    NONE = enum.auto()
    Digital = DIGITAL = enum.auto()
    SUN = enum.auto()
    IBM = enum.auto()
    VMware = VMWARE = enum.auto()
    Win4Lin = WIN4LIN = enum.auto()
    Transmeta = TRANSMETA = enum.auto()
    HP = enum.auto()
    TransGaming_Nvidia = TRANSGAMING_NVIDIA = enum.auto()
    Transitive_Apple = TRANSITIVE_APPLE = enum.auto()

hierarchy: dict[int, type] = {
    Isa.idx.value: Isa,
    Kernel.idx.value: Kernel,
    Syslib.idx.value: Syslib,
    Lib.idx.value: Lib,
    Sysapp.idx.value: Sysapp,
    App.idx.value: App,
    Rtlib.idx.value: Rtlib,
    Rtapp.idx.value: Rtapp,
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
            rtlib:  Rtlib   = Rtlib.NONE,
            rtapp:  Rtapp   = Rtapp.NONE,
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
        self.rtlib  = rtlib
        self.rtapp  = rtapp
        self.src    = src
        # upper, lower modules
        self.ls: set[HG] = set()
        self.us: set[HG] = set()
        strings = ()
        for ele in (src, rtapp, rtlib, app, sysapp, lib, syslib, kernel, isa, up):
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
        val += self.rtlib.value * mul
        mul *= Rtlib.END.value
        val += self.rtapp.value * mul
        mul *= Rtapp.END.value
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
                self.rtlib == other.rtlib and \
                self.rtapp == other.rtapp and \
                self.src == other.src:
            return True
        else:
            return False

modules: HashMap[Module] = HashMap()
allhgs: HashMap[HG] = HashMap()
allunihgs: HashMap[UniHG] = HashMap()
allhgs_hashname: HashMap[HG_hashname] = HashMap()

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
            {intfc.rtlib},
            {intfc.rtapp},
            {intfc.src},
        )

    def __init__(self,
            isas_ups:   set[typing.Tuple[Isa, Up]] = {(Isa.NONE, Up.NONE)},
            kernels:    set[Kernel] = {Kernel.NONE},
            syslibs:    set[Syslib] = {Syslib.NONE},
            libs:       set[Lib]    = {Lib.NONE},
            sysapps:    set[Sysapp] = {Sysapp.NONE},
            apps:       set[App]    = {App.NONE},
            rtlibs:     set[Rtlib]  = {Rtlib.NONE},
            rtapps:     set[Rtapp]  = {Rtapp.NONE},
            srcs:       set[Src]    = {Src.NONE},
            ) -> None:
        self.isas_ups:  set[typing.Tuple[Isa, Up]] = isas_ups
        self.kernels:   set[Kernel] = kernels
        self.syslibs:   set[Syslib] = syslibs
        self.libs:      set[Lib]    = libs
        self.sysapps:   set[Sysapp] = sysapps
        self.apps:      set[App]    = apps
        self.rtlibs:    set[Rtlib]  = rtlibs
        self.rtapps:    set[Rtapp]  = rtapps
        self.srcs:      set[Src]    = srcs
        self.repr = ''
        for isa, up in isas_ups:
            self.repr += isa.name[0] + up.name[0]
        for set in (kernels, syslibs, libs, sysapps, apps, rtlibs, rtapps, srcs):
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
                                for rtlib in self.rtlibs:
                                    for rtapp in self.rtapps:
                                        for src in self.srcs:
                                            _interfaces.add(Interface(
                                                isa_up,
                                                kernel,
                                                syslib,
                                                lib,
                                                sysapp,
                                                app,
                                                rtlib,
                                                rtapp,
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
        for rtlib in self.rtlibs:
            val ^= hash(rtlib.value * mul)
        mul *= Rtlib.END.value
        for rtapp in self.rtapps:
            val ^= hash(rtapp.value * mul)
        mul *= Rtapp.END.value
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
                self.rtlibs == other.rtlibs and \
                self.rtapps == other.rtapps and \
                self.srcs == other.srcs:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return self.repr

class Term(enum.Enum):
    UNK = UNKNOWN = enum.auto()

    # Transor
    V1_ = TYPE1_VIRTUAL_MACHINE = enum.auto()
    V1B = TYPE1_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION = enum.auto()
    P1_ = TYPE1_PARAVIRTUALIZATION = enum.auto()
    VP1 = TYPE1_VIRTUAL_MACHINE_AND_PARAVIRTUALIZATION = enum.auto()
    V2_ = TYPE2_VIRTUAL_MACHINE = enum.auto()
    V2B = TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION = \
    SBT = SYSTEM_LEVEL_BINARY_TRANSLATOR = enum.auto()
    UBT = USER_LEVEL_BINARY_TRANSLATOR = enum.auto()
    UBL = USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH = enum.auto()
    INS = INSTRUMENTER = enum.auto()
    OPT = OPTIMIZER = enum.auto()
    I_O = INSTRUMENTER_AND_OPTIMIZER = enum.auto()
    SCL = SYSCALL_COMPATIBLE_LAYER = enum.auto()

    # Module
    OS_ = KERNEL = OPERATING_SYSTEM = enum.auto()
    CPL = COMPILER = enum.auto()

    # Dummy Module
    APP = SYSAPP = enum.auto()
    LIB = SYSLIB = enum.auto()
    ISA = enum.auto()

# UniHG help addDummyModule to determine whether a dummy module has a counterpart module?
# E.g.
#       +---+     +---+
#       | O |     | F |
#       +---+     +---+
#           \     /   ?
#            \   /     ?
#            +---+     +---+
#            | A |     | B |
#            +---+     +---+
#                \     ?
#                 \   ? 
#                 +---+
#                 | T |
#                 +---+
#
# HG_B should not be added.
# HG_A={OF,T} are HG_B={F,T} are diff, therefore class UniHG is added.
# UniHG only contain one H, one G.
class UniHG:
    def __init__(self, h: Interface, g: Interface, add: bool = True) -> None:
        self.h = h
        self.g = g
        if add:
            allunihgs.add(self)

    def term(self) -> Term:
        class Cond(enum.Enum):
            IGN = IGNORE = enum.auto()
            EQL = EQUAL = enum.auto()
            NEQ = NOTEQUAL = enum.auto()
        IGN, EQL, NEQ = Cond.IGN, Cond.EQL, Cond.NEQ
        # h none test, default eql
        def hntest(conds: typing.Tuple[Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond]) -> bool:
            hhs = (self.h.isa, self.h.up, self.h.kernel, self.h.syslib, self.h.lib, self.h.sysapp, self.h.app, self.h.rtlib, self.h.rtapp, self.h.src)
            for hh, cond in zip(hhs, conds):
                if not ((cond==IGN) or (cond==EQL and hh.value==1) or (cond==NEQ and hh.value!=1)):
                    return False
            return True
        # g none test
        def gntest(conds: typing.Tuple[Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond, Cond]) -> bool:
            ghs = (self.g.isa, self.g.up, self.g.kernel, self.g.syslib, self.g.lib, self.g.sysapp, self.g.app, self.g.rtlib, self.g.rtapp, self.g.src)
            for gh, cond in zip(ghs, conds):
                if not ((cond==IGN) or (cond==EQL and gh.value==1) or (cond==NEQ and gh.value!=1)):
                    return False
            return True
        # h g test
        def hgtest(conds: typing.Tuple[Cond, ...]) -> bool:
            hhs = (self.h.isa, self.h.up, self.h.kernel, self.h.syslib, self.h.lib, self.h.sysapp, self.h.app, self.h.src)
            ghs = (self.g.isa, self.g.up, self.g.kernel, self.g.syslib, self.g.lib, self.g.sysapp, self.g.app, self.g.src)
            for hh, gh, cond in zip(hhs, ghs, conds):
                if not ((cond==IGN) or (cond==EQL and hh==gh) or (cond==NEQ and hh!=gh)):
                    return False
            return True

        if      hntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((NEQ, EQL, EQL)):
            return Term.USER_LEVEL_BINARY_TRANSLATOR
        if      hntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((NEQ, EQL, EQL, EQL, EQL)):
            return Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH
        elif    hntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((EQL, EQL)):
            return Term.TYPE1_VIRTUAL_MACHINE
        elif    hntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((NEQ, EQL)):
            return Term.TYPE1_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION
        elif    hntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((EQL, NEQ)):
            return Term.TYPE1_PARAVIRTUALIZATION
        elif    hntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((EQL, NEQ)):
            return Term.TYPE2_VIRTUAL_MACHINE
        elif    hntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((NEQ, NEQ)):
            return Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION
        elif    hntest((NEQ, NEQ, NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, NEQ, IGN, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((EQL, EQL, NEQ)):
            return Term.SYSCALL_COMPATIBLE_LAYER
        elif    self.h.src==Src.NONE and self.g.src!=Src.NONE:
            return Term.COMPILER
        elif    hntest((NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                gntest((NEQ, NEQ, NEQ, EQL, EQL, EQL, EQL, EQL, EQL, EQL)) and \
                hgtest((EQL,)):
            return Term.OS_
        else:
            return Term.UNKNOWN

    def __hash__(self) -> int:
        return hash(self.h.__hash__()) ^ self.g.__hash__()

    def __eq__(self, other: UniHG) -> bool:
        return  self.h == other.h and self.g == other.g

class HG:
    idx: int = 0
    def __init__(self,
            name: str,
            h: Metaface, # Host
            g: Metaface, # Guest
            # TODO: add efficiency
            # eff,
            term: Term = Term.UNKNOWN,
            add: bool = True,
            ) -> None:
        self.idx = HG.idx
        HG.idx += 1
        self.name = name
        self.h = h
        self.g = g
        self.repr = h.repr + ':' + g.repr
        self.term = term
        self.terms: dict[Term, int] = {term:1} if term!=Term.UNKNOWN else dict()

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
        # UniHG
        for hintfc in hinterfaces:
            for gintfc in ginterfaces:
                unihg = UniHG(hintfc, gintfc)
                if term==Term.UNKNOWN:
                    allunihgs.add(unihg)
                    if unihg.term() not in self.terms:
                        self.terms[unihg.term()] = 1
                    else:
                        self.terms[unihg.term()] += 1
        if len(self.terms) > 1:
            warnings.warn("hg %s has more than one terms %s"
                    %(self.name, self.terms))
        if term==Term.UNKNOWN:
            maxcnt: int = 0
            for t in self.terms:
                if self.terms[t] > maxcnt:
                    self.term = t
                    maxcnt = self.terms[t]
                elif self.terms[t] == maxcnt:
                    warnings.warn("hg term %s and %s has same count %d" %
                            (self.term.name, t.name, maxcnt))

    def setmodule_then_addhg(self, module: Module) -> None:
        self.module = module
        if len(self.name):
            self.name = "-".join((module.name, self.name))
        else:
            self.name = module.name
        if isinstance(module, DummyModule) and self in allhgs:
            warnings.warn("hg %s from Dummy Module has been defined!" % self.name)
        elif not isinstance(module, DummyModule) and HG_hashname(self) in allhgs_hashname:
            warnings.warn("hg %s has been defined!" % self.name)
        else:
            allhgs.add(self)
            allhgs_hashname.add(HG_hashname(self))

    def __hash__(self) -> int:
        # make h and g not commutative
        return hash(self.h.__hash__()) ^ self.g.__hash__()

    def __eq__(self, other: HG) -> bool:
        return self.h == other.h and self.g == other.g

    def __repr__(self) -> str:
        return self.repr
class HG_hashname:
    def __init__(self, hg: HG) -> None:
        self.hg = hg
    def __hash__(self) -> int:
        return hash(self.hg.name) ^ self.hg.__hash__()
    def __eq__(self, other: HG_hashname) -> bool:
        return self.hg==other.hg and self.hg.name==other.hg.name

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
        self.rename: str = rename
        self.date: Date = date
        self.desc: str = desc

class Module:
    def __init__(self,
            name: str,
            hgs: set[HG],
            term: Term = Term.UNKNOWN,
            dummy: bool = False,
            ) -> None:
        self.name = name
        self.hgs = hgs
        self.term = term
        self.terms: dict[Term, int] = {term:1} if term!=Term.UNKNOWN else dict()
        record: typing.Optional[Module] = modules.get(self)
        if dummy:
            if not record:
                modules.add(self)
                record = self
        else:
            if record:
                warnings.warn("module %s has been defined!" % name)
            modules.add(self)
            record = self
        for hg in hgs:
            hg.setmodule_then_addhg(record)
            if term==Term.UNKNOWN:
                for t in hg.terms:
                    if t not in self.terms:
                        self.terms[t] = hg.terms[t]
                    else:
                        self.terms[t] += hg.terms[t]
        if len(self.terms) == 0:
            self.terms = {Term.UNKNOWN: 1}
        elif len(self.terms) > 1:
            warnings.warn("module %s has more than one terms %s"
                    %(self.name, self.terms))
        if term==Term.UNKNOWN:
            maxcnt: int = 0
            for t in self.terms:
                if self.terms[t] > maxcnt:
                    self.term = t
                    maxcnt = self.terms[t]
                elif self.terms[t] == maxcnt:
                    warnings.warn("module %s term %s and %s has same count %d" %
                            (self.name, self.term.name, t.name, maxcnt))

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
        super().__init__(name, hgs, dummy=True)

def fixMultiLineString(s: str) -> str:
    res: str
    if len(s)>0 and s[0] == '\n':
        res = s[1:].replace(' '*4, '')
    else:
        res = s
    return res.replace('\n', r'\n')
class Transor(Module):
    def __init__(self,
            name: str,
            hgs: set[HG],
            start: Date,
            stop: Date = Date(),
            color: str = '#000',
            # TODO: enum licenses
            license: str = '',
            dev: Dev = Dev.NONE,
            term: Term = Term.UNKNOWN,
            feat: str = '',
            desc: str = '',
            parent: typing.Optional[Transor] = None,
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
        self.feat = fixMultiLineString(feat)
        self.desc = fixMultiLineString(desc)
        self.parent = parent
        self.renames = renames
        super().__init__(name, hgs, term=term)

# return True for added, False for not add
DMargs = tuple[tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Rtlib, Rtapp]
def addDummyModule(args: DMargs, hierarchyIdx: int) -> bool:
    term: Term
    if hierarchyIdx == Isa.idx.value:
        term = Term.ISA
    elif hierarchyIdx == Kernel.idx.value:
        term = Term.KERNEL
    elif hierarchyIdx == Syslib.idx.value or hierarchyIdx == Lib.idx.value:
        term = Term.LIB
    elif hierarchyIdx == Sysapp.idx.value or hierarchyIdx == App.idx.value:
        term = Term.APP
    else:
        term = Term.UNKNOWN

    if hierarchyIdx == Isa.idx.value:
        hintfc = Interface()
        gintfc = Interface((args[0][0], Up.USR_PVL))
    elif hierarchyIdx == Kernel.idx.value:
        hintfc = Interface((args[0][0], Up.USR_PVL))
        gintfc = Interface(*(args[:hierarchyIdx+1]))
    else:
        hintfc = Interface(*(args[:hierarchyIdx]))
        gintfc = Interface(*(args[:hierarchyIdx+1]))
    unihg = UniHG(hintfc, gintfc, False)
    if hintfc != gintfc and hintfc in interfaces and gintfc in interfaces:
        if unihg not in allunihgs:
            # print(args)
            # print("%d - %d" % (hierarchyIdx, hierarchyIdx+1))
            # print("%s - %s" % (hintfc.name, gintfc.name))
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
        return False
    if hierarchyIdx == Isa.idx.value:
        if args[Isa.idx.value][0].value > Isa.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Kernel.idx.value:
        if args[Kernel.idx.value].value > Kernel.NO_KERNEL.value and \
                args[Isa.idx.value][0].value > Isa.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Syslib.idx.value:
        if args[Kernel.idx.value].value > Kernel.ANY.value:
            DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Lib.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
    elif hierarchyIdx == Sysapp.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
    elif hierarchyIdx == App.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
    elif hierarchyIdx == Rtlib.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
    elif hierarchyIdx == Rtapp.idx.value:
        DummyModule(gintfc.name, {HG("", Metaface.metalize(hintfc), Metaface.metalize(gintfc), term)})
    else:
        warnings.warn("addDummyModule unknown hierarchyIdx %d" % hierarchyIdx)
    return True

Intfctype = typing.Union[tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Src]
intfctypes = (tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Rtlib, Rtapp, Src)
def addDummyModulesByIntfc(intfc: Interface) -> None:
    toptype: type
    autofill: bool = True
    if intfc.src != Src.NONE:
        return
    if intfc.rtapp != Rtapp.NONE:
        toptype = Rtapp
        autofill = False
    elif intfc.rtlib != Rtlib.NONE:
        toptype = Rtlib
        autofill = False
    elif intfc.app != App.NONE:
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
        Syslib.DEFAULT if intfc.syslib==Syslib.NONE and autofill else intfc.syslib,
        Lib.ANY if intfc.lib==Lib.NONE and autofill else intfc.lib,
        Sysapp.ANY if intfc.sysapp==Sysapp.NONE and autofill else intfc.sysapp,
        App.ANY if intfc.app==App.NONE and autofill else intfc.app,
        intfc.rtlib,
        intfc.rtapp,
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

def prefix(x: object) -> str:
    return x.__class__.__name__[0]
def nodeNameHG(hg: HG) -> str:
    return "%s%s%d" % (prefix(hg.module), hg.term.name, hg.idx)
def outputDot(f: typing.TextIO) -> None:
    f.write('digraph {\nnode[shape=box];\n')
    # nodes (IOs and Interfaces)
    for hg_hn in allhgs_hashname:
        hg = hg_hn.hg
        ## Transors' IOs
        if isinstance(hg.module, Transor):
            f.write('%s[label="%s", style=filled, fontcolor=white, fillcolor=black];\n' %(nodeNameHG(hg), hg.name))
        ## DummyModules' IOs
        elif isinstance(hg.module, DummyModule):
            f.write('%s[label="%s", style="dotted"];\n' % (nodeNameHG(hg), hg.name))
        ## Other Modules' IOs
        else:
            f.write('%s[label="%s"];\n' %(nodeNameHG(hg), hg.name))
    ## Interfaces
    for intfc in interfaces:
        if len(intfc.name):
            f.write('%s%d[label="%s", style=rounded];\n' %(prefix(intfc), intfc.idx, intfc.name))
    # edges
    for intfc in interfaces:
        if len(intfc.name):
            for l in intfc.ls:
                f.write('%s -> %s%d\n' % (nodeNameHG(l), prefix(intfc), intfc.idx))
            for u in intfc.us:
                f.write('%s%d -> %s\n' % (prefix(intfc), intfc.idx, nodeNameHG(u)))
    f.write("}\n")

def outputJson(f: typing.TextIO) -> None:
    f.write('{\n')
    # nodes (IOs and Interfaces)
    f.write('"nodes": {\n')
    num: int = 0
    for hg_hn in allhgs_hashname:
        hg = hg_hn.hg
        if num>0:
            f.write(',')
        else:
            f.write(' ')
        num += 1
        f.write(' "%s": "%s"\n' %(nodeNameHG(hg), hg.name))
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
                f.write(' ["%s", "%s%d"]\n' % (nodeNameHG(l), prefix(intfc), intfc.idx))
            for u in intfc.us:
                if num>0:
                    f.write(',')
                else:
                    f.write(' ')
                num += 1
                f.write(' ["%s%d", "%s"]\n' % (prefix(intfc), intfc.idx, nodeNameHG(u)))
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
            f.write('"%s","%s","%s","%s","%s","%s","%s","%s"' % (
                "N", module.name, module.color,
                module.parent.name if module.parent else "",
                module.start, module.stop, "", module.desc
            ))
            for rename in module.renames:
                f.write(',"%s","%s","%s"' % (
                    rename.rename, rename.date, rename.desc
                ))
            f.write('\n')
