from data import *
from Merge.meta import *

Win4Lin = Transor("Win4Lin",
    {  HG("",
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}, {Syslib.LINUX}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR_PVL)})
    )},
    Date(2000), Date(2008,6,4), dev=Dev.WIN4LIN,
    feat="run  Windows 9x, Windows 2000 or Windows XP",
    desc='''
        http://freshmeat.sourceforge.net/projects/win4lin
        https://en.wikipedia.org/wiki/Win4Lin
        2005: SUSE™ Linux 10 Unleashed: Chapter 11
    ''',
    parent=Merge,
    renames=[Rename("Win4Lin 9x", Date(2005,3),
        desc="https://web.archive.org/web/20050318033645/http://www.win4lin.com:80/"
    )],
)
