# How do I type hint a method with the type of the enclosing class?
# https://stackoverflow.com/questions/33533148/
from __future__ import annotations
import enum
import typing
import warnings
from multimethod import multimethod
from itertools import zip_longest
import numpy as np

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

class Src(enum.IntEnum):
    NONE = enum.auto()

    C_SRC = C = enum.auto()
    CPP_SRC = CPP = enum.auto()

    END = enum.auto()
    idx = 8

class Rtapp(enum.IntEnum):
    NONE = enum.auto()

    APPS = ANY = enum.auto()

    END = enum.auto()
    idx = 7

class Rtlib(enum.IntEnum):
    NONE = enum.auto()

    LIBS = ANY = enum.auto()

    END = enum.auto()
    idx = 6

class App(enum.IntEnum):
    NONE = enum.auto()

    APPS = ANY = enum.auto()

    ANDROID_RUNTIME = enum.auto()

    END = enum.auto()
    idx = 5

class Sysapp(enum.IntEnum):
    NONE = enum.auto()
    SYSAPPS = ANY = enum.auto()
    END = enum.auto()
    idx = 4
Sysapp_ANYs = set(Sysapp(i) for i in range(Sysapp.ANY, Sysapp.END))

class Lib(enum.IntEnum):
    NONE = enum.auto()
    LIBS = ANY = enum.auto()
    END = enum.auto()
    idx = 3
Lib_ANYs = set(Lib(i) for i in range(Lib.ANY, Lib.END))

class Syslib(enum.IntEnum):
    NONE = enum.auto()

    SYSLIBS = DEFAULT = enum.auto()

    LINUX_SYSLIBS = LINUX = enum.auto()

    BSD_SYSLIBS = BSD = enum.auto()

    MACOS_SYSLIBS = MACOS = enum.auto()

    WINDOWS_SYSLIBS = WINDOWS = enum.auto()

    END = enum.auto()
    idx = 2

class Kernel(enum.IntEnum):
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
    IOS = enum.auto()

    END = enum.auto()
    idx = 1
# https://en.wikipedia.org/wiki/POSIX
Kernel_POSIXs: set[Kernel] = {Kernel.MACOS, Kernel.BSD, Kernel.LINUX}

class Up(enum.IntEnum):
    NONE = enum.auto()
    USR = USER = UNPVL = UNPRIVILEGE = enum.auto()
    PVL = PRIVILEGE = enum.auto()
    USR_PVL = USER_PRIVILEGE = enum.auto()
    END = enum.auto()
    idx = 0
# dummy class for convenient when calculating toptype
class Usr(enum.IntEnum):
    pass
class UsrPvl(enum.IntEnum):
    pass

class Isa(enum.IntEnum):
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
    IA64 = ITANIUM = enum.auto()
    PARISC = HPPA = enum.auto()

    # VLIW
    DAISY_VLIW = DAISY = enum.auto()
    CRUSOE_VLIW = CRUSOE = enum.auto()
    DENVER_VLIW = DENVER = enum.auto()

    # IR / byte code
    LLVM_IR = LLVM = enum.auto()

    BPF = enum.auto()

    END = enum.auto()
    idx = 0
Isa_ANYs = set(Isa(i) for i in range(Isa.ANY, Isa.END))
Isa_X86s = set(Isa(i) for i in range(Isa.I386, Isa.X86+1))
Isa_X86_64s = set(Isa(i) for i in range(Isa.I386, Isa.X86_64+1))
Isa_ARM32s = set(Isa(i) for i in range(Isa.ARM, Isa.ARM32+1))
Isa_ARMV6s = {Isa.ARMV6L, Isa.ARMV6M}
Isa_ARMV7s = {Isa.ARMV7L, Isa.ARMV7M, Isa.ARMV7A, Isa.ARMV7R}
Isa_POWERPC64s = {Isa.POWERPC, Isa.POWERPC64}
Isa_MIPS64s = set(Isa(i) for i in range(Isa.MIPSI, Isa.MIPS64+1))
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

class Dev(enum.IntEnum):
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
    SpecOps_Labs = SPECOPS_LABS = enum.auto()
    武成岗组 = WCG_LAB = enum.auto()
    Intel = INTEL = enum.auto()
    Falling_Leaf_System = FALLING_LEAF_SYSTEM = enum.auto()
    Apple = APPLE = enum.auto()
    Oracle = ORACLE = enum.auto()
    上交 = SJ = enum.auto()
    Nvidia = NVIDIA = enum.auto()
    台清华 = TQH = enum.auto()
    台交大 = TJD = enum.auto()
    迪捷软件 = DIGIPROTO = enum.auto()
    Invisible_Things_Lab = INVISIBLE_THINGS_LAB = enum.auto()
    Eltech_Russia = ELTECH_RUSSIA = enum.auto()
    Eltech_Huawei = ELTECH_HUAWEI = enum.auto()
    Microsoft = MICROSOFT = enum.auto()
    Manchester = MANCHESTER = enum.auto()
    Canonical = CANONICAL = enum.auto()
    Valve = VALVE = enum.auto()
    麟卓_国防科大 = LINZHUOTECH = enum.auto()
    统信 = UnionTech = enum.auto()

hierarchy: dict[int, type] = {
    Isa.idx: Isa,
    Kernel.idx: Kernel,
    Syslib.idx: Syslib,
    Lib.idx: Lib,
    Sysapp.idx: Sysapp,
    App.idx: App,
    Rtlib.idx: Rtlib,
    Rtapp.idx: Rtapp,
    Src.idx: Src,
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
        if syslib == Syslib.DEFAULT:
            if kernel ==        Kernel.LINUX:
                self.syslib =   Syslib.LINUX
            elif kernel ==      Kernel.BSD:
                self.syslib =   Syslib.BSD
            elif kernel ==      Kernel.MACOS:
                self.syslib =   Syslib.MACOS
            elif kernel ==      Kernel.WINDOWS:
                self.syslib =   Syslib.WINDOWS
            else:
                self.syslib = syslib
        else:
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
            if ele > 1: # not NONE
                strings += (ele.name,)
        self.name = '-'.join(strings)

    def toptype(self) -> typing.Optional[type]:
        try:
            return self._toptype
        except:
            self._toptype: typing.Optional[type] = None
            for ele,ty in zip(\
                    (self.src, self.rtapp, self.rtlib, self.app, self.sysapp, self.lib, self.syslib, self.kernel),\
                    (     Src,      Rtapp,      Rtlib,      App,      Sysapp,      Lib,      Syslib,      Kernel)):
                if ele > 1: # not NONE
                    self._toptype = ty
                    break
            if self._toptype == None:
                if self.up == Up.USR:
                    self._toptype = Usr
                elif self.up == Up.USR_PVL:
                    self._toptype = UsrPvl
            return self._toptype

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        val: int = 0
        mul: int = 1
        for v,m in zip( \
                (self.isa, self.up, self.kernel, self.syslib, self.lib, self.sysapp, self.app, self.rtlib, self.rtapp, self.src),\
                (Isa.END,  Up.END,  Kernel.END,  Syslib.END,  Lib.END,  Sysapp.END,  App.END,  Rtlib.END,  Rtapp.END,  Src.END)):
            val += v
            mul *= m
        return val

    def __eq__(self, othr: Interface) -> bool:
        if (self.isa, self.up, self.kernel, self.syslib, self.lib, self.sysapp, self.app, self.rtlib, self.rtapp, self.src) == \
           (othr.isa, othr.up, othr.kernel, othr.syslib, othr.lib, othr.sysapp, othr.app, othr.rtlib, othr.rtapp, othr.src):
            return True
        else:
            return False

modules: HashMap[Module] = HashMap()
allhgs: HashMap[HG] = HashMap()
allunihgs: HashMap[UniHG] = HashMap()
allhgs_hashname: HashMap[HG_hashname] = HashMap()
connectors: list[Connector] = list()

class Metaface():
    @multimethod
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
        self.interfaces: set[Interface] = set()
        for isa_up in isas_ups:
            for kernel in kernels:
                for syslib in syslibs:
                    for lib in libs:
                        for sysapp in sysapps:
                            for app in apps:
                                for rtlib in rtlibs:
                                    for rtapp in rtapps:
                                        for src in srcs:
                                            self.interfaces.add(Interface(
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

    @__init__.register
    def _(self, intfc: Interface):
        self.interfaces: set[Interface] = {intfc}

    @__init__.register
    def _(self, intfcs: set[Interface]):
        self.interfaces: set[Interface] = intfcs

    def toptype(self) -> typing.Optional[type]:
        try:
            return self._toptype
        except:
            toptypes: typing.Dict[typing.Optional[type], int] = dict()
            for intfc in self.interfaces:
                t: typing.Optional[type] = intfc.toptype()
                if t not in toptypes:
                    toptypes[t] = 1
                else:
                    toptypes[t] += 1
            maxcnt: int = 0
            self._toptype: typing.Optional[type] = None
            for t in toptypes:
                if toptypes[t] > maxcnt:
                    self._toptype = t
                    maxcnt = toptypes[t]
            return self._toptype

    def __hash__(self) -> int:
        val: int = 0;
        for intfc in self.interfaces:
            val ^= intfc.__hash__()
        return val

    def __eq__(self, other: Metaface) -> bool:
        return self.interfaces == other.interfaces

    def __repr__(self) -> str:
        try:
            return self._repr
        except:
            repr = ','.join(set(intfc.__repr__() for intfc in self.interfaces))
            self._repr: str = '{%s}' % repr
            return self._repr

class Term(enum.IntEnum):
    UNK = UNKNOWN = enum.auto()

    # Transor
    V1_ = TYPE1_VIRTUAL_MACHINE = enum.auto()
    V1B = TYPE1_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION = enum.auto()
    P1_ = TYPE1_PARAVIRTUALIZATION = enum.auto()
    VP1 = TYPE1_VIRTUAL_MACHINE_AND_PARAVIRTUALIZATION = enum.auto()
    V2_ = TYPE2_VIRTUAL_MACHINE = enum.auto()
    V2B = TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION = SYSTEM_LEVEL_BINARY_TRANSLATOR = enum.auto()
    SBT = STATIC_BINARY_TRANSLATOR = enum.auto()
    DSB = DYNAMIC_STATIC_BINARY_TRANSLATOR = enum.auto()
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
    RAP = RTAPP = enum.auto()
    RLB = RTLIB = enum.auto()
    APP = enum.auto()
    SAP = SYSAPP = enum.auto()
    LIB = enum.auto()
    SLB = SYSLIB = enum.auto()
    ISA = enum.auto()
def term2str(term: Term) -> str:
    # Transor
    if term == Term.V1_:
        return "Type1 Virtual Machine"
    if term == Term.V1B:
        return "Type1 Virtual Machine with Binary Translation"
    if term == Term.P1_:
        return "Type1 Paravirtualization"
    if term == Term.VP1:
        return "Type-1 Virtual Machine and Paravirtualization"
    if term == Term.V2_:
        return "Type-2 Virtual Machine"
    if term == Term.V2B:
        return "Type-2 Virtual Machine with Binary Translation"
    if term == Term.SBT:
        return "Static Binary Translator"
    if term == Term.DSB:
        return "Dynamic Static Binary Translator"
    if term == Term.UBT:
        return "User-level Binary Translator"
    if term == Term.UBL:
        return "User-level Binary Translator with Lib Pass-through"
    if term == Term.INS:
        return "Instrumenter"
    if term == Term.OPT:
        return "Optimizer"
    if term == Term.I_O:
        return "Instrumenter and Optimizer"
    if term == Term.SCL:
        return "Syscall Compatible Layer"

    # Module
    if term == Term.OS_:
        return "Kernel"
    if term == Term.CPL:
        return "Compiler"

    # Dummy Module
    if term == Term.RAP:
        return "Runtime App"
    if term == Term.RLB:
        return "Rumtime Libraray"
    if term == Term.APP:
        return "App"
    if term == Term.SAP:
        return "System App"
    if term == Term.LIB:
        return "Libraray"
    if term == Term.SLB:
        return "System Libraray"
    if term == Term.ISA:
        return "ISA"

    return "Unknown"

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
        class Cond(enum.IntEnum):
            IGN = IGNORE = enum.auto()
            EQL = EQUAL = enum.auto()
            NEQ = NOTEQUAL = enum.auto()
        IGN, EQL, NEQ = Cond.IGN, Cond.EQL, Cond.NEQ
        # h none test, default eql
        def hntest_eql(conds: typing.Tuple[Cond, ...]) -> bool:
            h = self.h
            hhs: typing.Tuple[int, ...] = (h.isa, h.up, h.kernel, h.syslib, h.lib, h.sysapp, h.app, h.rtlib, h.rtapp, h.src)
            for hh, cond in zip_longest(hhs, conds):
                if not ((cond==IGN) or ((cond==EQL or cond==None) and hh==1) or (cond==NEQ and hh!=1)):
                    return False
            return True
        # g none test, default eql
        def gntest_eql(conds: typing.Tuple[Cond, ...]) -> bool:
            g = self.g
            ghs: typing.Tuple[int, ...] = (g.isa, g.up, g.kernel, g.syslib, g.lib, g.sysapp, g.app, g.rtlib, g.rtapp, g.src)
            for gh, cond in zip_longest(ghs, conds):
                if not ((cond==IGN) or ((cond==EQL or cond==None) and gh==1) or (cond==NEQ and gh!=1)):
                    return False
            return True
        # h g test, default ign
        def hgtest(conds: typing.Tuple[Cond, ...]) -> bool:
            h = self.h
            hhs: typing.Tuple[int, ...] = (h.isa, h.up, h.kernel, h.syslib, h.lib, h.sysapp, h.app, h.rtlib, h.rtapp, h.src)
            g = self.g
            ghs: typing.Tuple[int, ...] = (g.isa, g.up, g.kernel, g.syslib, g.lib, g.sysapp, g.app, g.rtlib, g.rtapp, g.src)
            for hh, gh, cond in zip(hhs, ghs, conds):
                if not ((cond==IGN) or (cond==EQL and hh==gh) or (cond==NEQ and hh!=gh)):
                    return False
            return True

        if      hntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ, NEQ)) and \
                hgtest((NEQ, EQL, EQL)):
            return Term.USER_LEVEL_BINARY_TRANSLATOR
        if      hntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                hgtest((NEQ, EQL, EQL, EQL, EQL)):
            return Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH
        elif    hntest_eql((NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ)) and \
                hgtest((EQL, EQL)):
            return Term.TYPE1_VIRTUAL_MACHINE
        elif    hntest_eql((NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ)) and \
                hgtest((NEQ, EQL)):
            return Term.TYPE1_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION
        elif    hntest_eql((NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ)) and \
                hgtest((EQL, NEQ)):
            return Term.TYPE1_PARAVIRTUALIZATION
        elif    hntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ)) and \
                hgtest((EQL, NEQ)):
            return Term.TYPE2_VIRTUAL_MACHINE
        elif    hntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ)) and \
                hgtest((NEQ, NEQ)):
            return Term.TYPE2_VIRTUAL_MACHINE_WITH_BINARY_TRANSLATION
        elif    hntest_eql((NEQ, NEQ, NEQ, NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ, NEQ, IGN)) and \
                hgtest((EQL, EQL, NEQ)):
            return Term.SYSCALL_COMPATIBLE_LAYER
        elif    self.h.src==Src.NONE and self.g.src!=Src.NONE:
            return Term.COMPILER
        elif    hntest_eql((NEQ, NEQ)) and \
                gntest_eql((NEQ, NEQ, NEQ)) and \
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
            term: Term = Term.UNKNOWN,
            perfs: list[Perf] = list(),
            add: bool = True,
            ) -> None:
        self.idx = HG.idx
        HG.idx += 1
        self.name = name
        self.h = h
        self.g = g
        self.repr = h.__repr__() + ':' + g.__repr__()
        self.perfs = perfs
        _perfratios = [pf.ratio for pf in perfs]
        self.perfratio: typing.Optional[float] = None
        if len(_perfratios) > 0:
            self.perfratio = np.exp(np.log(_perfratios).mean())
        self.term = term
        self.terms: dict[Term, int] = {term:1} if term!=Term.UNKNOWN else dict()

        if not add:
            return
        hinterfaces =  h.interfaces
        for intfc in hinterfaces:
            record: typing.Optional[Interface] = interfaces.get(intfc)
            if not record:
                interfaces.add(intfc)
                record = intfc
            record.us.add(self)
        ginterfaces = g.interfaces
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

class Connector:
    def __init__(self,
            startTransor: Transor,
            stopTransor: Transor,
            start: Date,
            stop: Date = Date(),
            ) -> None:
        self.startTransor: Transor = startTransor
        self.stopTransor: Transor = stopTransor
        self.start: Date = start
        self.stop: Date = stop if stop>=start else start
        connectors.append(self)

class Benchmark(enum.IntEnum):
    NONE = enum.auto()
    COREMARK = enum.auto()

class Perf:
    def __init__(self,
            ratio: float,
            benchmark: Benchmark,
            date: Date = Date(),
            info: str = "",
            ) -> None:
        self.ratio: float = ratio
        self.benchmark: Benchmark = benchmark
        self.date: Date = date
        self.info: str = info

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

    def _hgtoptype(self) -> None:
        htoptypes: typing.Dict[typing.Optional[type], int] = dict()
        gtoptypes: typing.Dict[typing.Optional[type], int] = dict()
        for hg in self.hgs:
            ht = hg.h.toptype()
            if ht not in htoptypes:
                htoptypes[ht] = 1
            else:
                htoptypes[ht] += 1
            gt = hg.g.toptype()
            if gt not in gtoptypes:
                gtoptypes[gt] = 1
            else:
                gtoptypes[gt] += 1
        self._htoptype: typing.Optional[type] = None
        maxcnt: int = 0
        for ht in htoptypes:
            if htoptypes[ht] > maxcnt:
                self._htoptype = ht
        self._gtoptype: typing.Optional[type] = None
        maxcnt = 0
        for gt in gtoptypes:
            if gtoptypes[gt] > maxcnt:
                self._gtoptype = gt
    def gtoptype(self) -> typing.Optional[type]:
        try:
            return self._gtoptype
        except:
            self._hgtoptype()
            try:
                return self._gtoptype
            except:
                raise Exception("gtoptype loop?")
    def htoptype(self) -> typing.Optional[type]:
        try:
            return self._htoptype
        except:
            self._hgtoptype()
            try:
                return self._htoptype
            except:
                raise Exception("htoptype loop?")

    def _hgnum(self) -> None:
        self._hnum: int = 0
        self._gnum: int = 0
        for hg in self.hgs:
            self._hnum += len(hg.h.interfaces)
            self._gnum += len(hg.g.interfaces)
    def hnum(self) -> int:
        try:
            return self._hnum
        except:
            self._hgnum()
            try:
                return self._hnum
            except:
                raise Exception("hnum loop?")
    def gnum(self) -> int:
        try:
            return self._gnum
        except:
            self._hgnum()
            try:
                return self._gnum
            except:
                raise Exception("gnum loop?")

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
        self.perfs: list[Perf] = list()
        for hg in hgs:
            self.perfs += hg.perfs
        _perfratios = [pf.ratio for pf in self.perfs]
        self.perfratio: typing.Optional[float] = None
        if len(_perfratios) > 0:
            # https://stackoverflow.com/questions/43099542/python-easy-way-to-do-geometric-mean-in-python
            self.perfratio = np.exp(np.log(_perfratios).mean())
        super().__init__(name, hgs, term=term)

# return True for added, False for not add
DMargs = tuple[tuple[Isa, Up], Kernel, Syslib, Lib, Sysapp, App, Rtlib, Rtapp]
def addDummyModule(args: DMargs, hierarchyIdx: int) -> bool:
    term: Term
    if hierarchyIdx == Isa.idx:
        term = Term.ISA
    elif hierarchyIdx == Kernel.idx:
        term = Term.KERNEL
    elif hierarchyIdx == Syslib.idx:
        term = Term.SYSLIB
    elif hierarchyIdx == Lib.idx:
        term = Term.LIB
    elif hierarchyIdx == Sysapp.idx:
        term = Term.SYSAPP
    elif hierarchyIdx == App.idx:
        term = Term.APP
    elif hierarchyIdx == Rtlib.idx:
        term = Term.RTLIB
    elif hierarchyIdx == Rtapp.idx:
        term = Term.RTAPP
    else:
        term = Term.UNKNOWN

    if hierarchyIdx == Isa.idx:
        hintfc = Interface()
        gintfc = Interface((args[0][0], Up.USR_PVL))
    elif hierarchyIdx == Kernel.idx:
        hintfc = Interface((args[0][0], Up.USR_PVL))
        gintfc = Interface(*(args[:hierarchyIdx+1])) # type: ignore
    else:
        hintfc = Interface(*(args[:hierarchyIdx])) # type: ignore
        gintfc = Interface(*(args[:hierarchyIdx+1])) # type: ignore
    unihg = UniHG(hintfc, gintfc, False)
    if hintfc != gintfc and hintfc in interfaces and gintfc in interfaces:
        if unihg not in allunihgs:
            # print(args)
            # print("%d - %d" % (hierarchyIdx, hierarchyIdx+1))
            # print("%s - %s" % (hintfc.name, gintfc.name))
            DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
        return False
    if hierarchyIdx == Isa.idx:
        if args[Isa.idx][0] > Isa.ANY: # type: ignore
            DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Kernel.idx:
        if args[Kernel.idx] > Kernel.NO_KERNEL and args[Isa.idx][0] > Isa.ANY: # type: ignore
            DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Syslib.idx:
        if args[Kernel.idx] > Kernel.ANY: # type: ignore
            DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
        else:
            return False
    elif hierarchyIdx == Lib.idx:
        DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
    elif hierarchyIdx == Sysapp.idx:
        DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
    elif hierarchyIdx == App.idx:
        DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
    elif hierarchyIdx == Rtlib.idx:
        DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
    elif hierarchyIdx == Rtapp.idx:
        DummyModule(gintfc.name, {HG("", Metaface(hintfc), Metaface(gintfc), term)})
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
    for i in range(toptype.idx+1, App.idx+1): # [toptype+1, App]
        if not addDummyModule(args, i):
            break
    # downward
    for i in reversed(range(Isa.idx, toptype.idx+1)): # reversed([Isa, toptype])
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

    # sort transors by start date
    transors: list[Transor] = []
    for module in modules:
        if isinstance(module, Transor):
            transors.append(module)
    sorted_transors: list[Transor] = sorted(transors, key=lambda transor: transor.start)

    for transor in sorted_transors:
        if isinstance(transor, Transor):
            f.write('"%s","%s","%s","%s","%s","%s","%s","%s"' % (
                "N", transor.name, transor.color,
                transor.parent.name if transor.parent else "",
                transor.start, transor.stop, "", transor.desc
            ))
            for rename in transor.renames:
                f.write(',"%s","%s","%s"' % (
                    rename.rename, rename.date, rename.desc
                ))
            f.write('\n')
    for conn in connectors:
        f.write('"C","%s","%s","%s","%s","%s","%s"\n' % (
        conn.start, conn.startTransor.name,
        conn.stop, conn.stopTransor.name,
        2, conn.startTransor.color,
    ))

def outputRelplot(output: str):
    import matplotlib.pyplot as plt
    plt.rcParams['svg.fonttype'] = 'none'
    f: plt.Figure
    ax: plt.Axes
    # figsize, see
    #   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    f, ax = plt.subplots(figsize=(12, 40))

    types = (UsrPvl, Usr, Kernel, Syslib, Lib, Sysapp, App, Rtlib, Rtapp, Src)
    htype_cnt: typing.Dict[type, int] = dict()
    gtype_cnt: typing.Dict[type, int] = dict()
    type_cnt: typing.Dict[type, int] = dict()
    xmin: int = Date.today().toordinal()
    xmax: int = 0
    for ty in types:
        htype_cnt[ty] = 1
        gtype_cnt[ty] = 1
    for module in modules:
        if isinstance(module, Transor):
            ht: typing.Optional[type] = module.htoptype()
            gt: typing.Optional[type] = module.gtoptype()
            if ht == None or gt == None:
                continue
            htype_cnt[ht] += 1
            gtype_cnt[gt] += 1
            _xh = module.start.toordinal()
            if _xh < xmin:
                xmin = _xh
            _xg = module.stop.toordinal()
            if _xg > xmax:
                xmax = _xg
    xmin -= 365

    for ty in types:
        type_cnt[ty] = max(htype_cnt[ty], gtype_cnt[ty])

    htype_idx: typing.Dict[type, int] = dict()
    gtype_idx: typing.Dict[type, int] = dict()
    type_idx: typing.Dict[type, int] = dict()
    htype_floor: typing.Dict[type, int] = dict()
    gtype_floor: typing.Dict[type, int] = dict()
    type_floor: typing.Dict[type, int] = dict()
    htype_celling: typing.Dict[type, int] = dict()
    gtype_celling: typing.Dict[type, int] = dict()
    type_celling: typing.Dict[type, int] = dict()
    _tf: int = 0
    for ty in types:
        htype_floor[ty] = _tf
        htype_idx[ty] = _tf + 1
        htype_celling[ty] = htype_idx[ty] + htype_cnt[ty]

        gtype_floor[ty] = _tf
        gtype_idx[ty] = _tf + 1
        gtype_celling[ty] = gtype_idx[ty] + gtype_cnt[ty]

        type_floor[ty] = _tf
        type_idx[ty] = _tf + 1
        _tf += type_cnt[ty] + 1
        type_celling[ty] = _tf

    ymax: float = type_celling[types[len(types)-1]] # last element of gtype_celling

    # draw background bands
    _cbool: bool = True
    for _f,_c in zip(type_floor.values(), type_celling.values()):
        ax.add_patch(plt.Polygon([
            (xmin, _f), (xmin, _c),
            (xmax, _c), (xmax, _f),
        ], color='white' if _cbool else 'gray', alpha=0.2))
        _cbool = not _cbool

    # make sure start and stop position uniformly distributes among background band
    # hg True for h, False for g
    def linearFix(hg:bool, t:type, y:float) -> float:
        hc: float = htype_celling[t]
        hf: float = htype_floor[t]
        gc: float = gtype_celling[t]
        gf: float = gtype_floor[t]
        _c: float = type_celling[t]
        _f: float = type_floor[t]
        yratiol: float # y ratio lower
        yratioh: float # y ratio higher
        if hg: # h
            yratiol = (y-hf)/(hc-hf)
            yratioh = (hc-y)/(hc-hf)
        else: # g
            yratiol = (y-gf)/(gc-gf)
            yratioh = (gc-y)/(gc-gf)
        return yratioh*_f + yratiol*_c

    import math
    for module in modules:
        if isinstance(module, Transor):
            ht: typing.Optional[type] = module.htoptype()
            gt: typing.Optional[type] = module.gtoptype()
            if ht == None or gt == None:
                continue

            # prepare data
            ## Host/Start
            _herr: float = math.log10(module.hnum())
            _hidx: int = htype_idx[ht]
            _xh = module.start.toordinal()
            #print("%s\t%s\t%s" %(module.start.toordinal(), ht, module.name))
            htype_idx[ht] += 1
            ## Guest/Stop
            _gerr: float = math.log10(module.gnum())
            _gidx: int = gtype_idx[gt]
            _xg = module.stop.toordinal()
            #print("%s\t%s\t%s" %(module.start.toordinal(), gt, module.name))
            gtype_idx[gt] += 1

            # add transor band
            _yh: float = linearFix(True, ht, _hidx)
            _yg: float = linearFix(False, gt, _gidx)
            ax.add_patch(plt.Polygon([
                (_xh, _yh - _herr/2), (_xh, _yh + _herr/2),
                (_xg, _yg + _gerr/2), (_xg, _yg - _gerr/2),
            ], color=module.color, alpha=0.4))

            # add text
            ax.text(_xh, _yh, module.name, va='center', ha='right', color=module.color)
            ax.text(_xg, _yg, module.name, va='center', ha='left',  color=module.color)

    # x axis
    years: typing.List[int] = list(range(Date.fromordinal(xmin).year, Date.fromordinal(xmax).year + 1))
    xs: typing.List[int] = list(map(lambda y: Date(y).toordinal(), years))
    ax.xaxis.set_ticks(xs, years, rotation=90)
    # y axis
    ys: typing.List[float] = list(map(lambda l,h: (l+h)/2, [0]+list(type_celling.values()), type_celling.values()))
    names: typing.List[str] = list(map(lambda t: t.__name__, types))
    ax.yaxis.set_ticks(ys, names)

    ax.set(xlim=(xmin, xmax), ylim=(0, ymax))
    if output=="window":
        plt.show()
    else:
        plt.savefig(output, bbox_inches="tight")

def _canonicalize_folder_name(name: str) -> str:
    return name.replace(' ', '_').\
                replace('-', '_').\
                replace('!', '').\
                replace('(', '_').\
                replace(')', '').\
                replace('.', '_')

def outputSUMMARY() -> None:
    f = open("src/SUMMARY.md", "w")
    f.write("# Summary\n\n")
    f.write("* [Home](./README.md)\n")
    f.write("* [Timeline](./timeline.md)\n")
    f.write("* [X-Y Relplot](./relplot.md)\n")

    f.write("\n# All RunXonY Projects\n\n")

    # sort transors by name (case insensitive)
    transors: list[Transor] = []
    for module in modules:
        if isinstance(module, Transor):
            transors.append(module)
    sorted_transors: list[Transor] = sorted(transors, key=lambda transor: transor.name.lower())

    f.write("* [Listed by Name (%d)](./list/byName.md)\n" % len(sorted_transors))

    for transor in sorted_transors:
        import os
        canonical_folder_name: str = _canonicalize_folder_name(transor.name)
        canonical_folder_name_README: str = canonical_folder_name + "/README.md"
        if not os.path.exists("src/" + canonical_folder_name_README):
            print("outputListByName error: File %s not exists" % canonical_folder_name_README)
        f.write("  * [%s](%s/README.md),\n" % (transor.name, canonical_folder_name))
    f.close()

def outputMetaMd() -> None:
    for module in modules:
        if isinstance(module, Transor):
            transor: Transor = module

            import os
            canonical_folder_name: str = _canonicalize_folder_name(transor.name)
            if not os.path.exists("src/" + canonical_folder_name):
                print("outputListByName error: Folder %s not exists" % canonical_folder_name)

            with open("src/" + canonical_folder_name + "/meta.md", "w") as metamd:
                metamd.write("* **Date**: %s - " % transor.start)
                if transor.stop < Date.today():
                    metamd.write("%s\n" % transor.stop)
                else:
                    metamd.write("today\n")
                if transor.license != '':
                    metamd.write("* **License**: %s\n" % transor.license)
                if transor.dev != Dev.NONE:
                    metamd.write("* **Development**: %s\n" % transor.dev)
                if transor.term != Term.UNKNOWN:
                    metamd.write("* **Category**: %s\n" % term2str(transor.term))
                if transor.parent:
                    metamd.write("* **Parent**: %s\n" % transor.parent.name)

                if len(transor.renames) > 0:
                    metamd.write("* **Renames**:")
                    for rename in transor.renames:
                        metamd.write(" %s(%s)," % (rename.rename, rename.date))
                    metamd.write("\n")

                metamd.write("\n")
                metamd.write("| Name | Run **X** | On **Y** |\n")
                metamd.write("| ---- | --------- | -------- |\n")
                def _canonicalize_hg(hg: str) -> str:
                    import re
                    hg = re.sub(r'[^-,]*SYSAPPS-', '', hg)
                    hg = re.sub(r'[^-,]*LIBS-', '', hg)
                    return hg.replace(",", ", ").\
                              replace("{", "").\
                              replace("}", "")
                for hg in transor.hgs:
                    metamd.write("| %s | %s | %s |\n" % (
                        hg.name,
                        _canonicalize_hg(hg.g.__repr__()),
                        _canonicalize_hg(hg.h.__repr__())
                    ))

def outputByTermMd() -> None:
    f = open("src/SUMMARY.md", "a")

    termed_transors: dict[Term, list[Transor]] = {}
    for term in Term:
        termed_transors[term] = list()

    len_transors: int = 0
    for module in modules:
        if isinstance(module, Transor):
            transor: Transor = module
            termed_transors[transor.term].append(transor)
            len_transors += 1

    f.write("* [List by Category (%d)](./list/byTerm.md)\n" % len_transors)

    for term in Term:
        transors: list[Transor] = termed_transors[term]
        if len(transors) > 0:
            sorted_transors: list[Transor] = sorted(transors, key=lambda transor: transor.name.lower())
            f.write("  * [%s (%d)](list/byTerm/%s.md)\n" % (term2str(term), len(sorted_transors), term.name))
            for transor in sorted_transors:
                canonical_folder_name: str = _canonicalize_folder_name(transor.name)
                f.write("    * [%s](%s/README.md)\n" % (transor.name, canonical_folder_name))
    f.close()
