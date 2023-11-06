from data import *
from citra.meta import *
from unicorn.meta import *

yuzu = Transor("yuzu",
    {  HG("",
        Metaface(),
        # Nintendo Switch
        Metaface(),
    )},
    Date(2017,10,10), Date.today(), color="#5C93ED", parent=citra,
    desc='''
        https://github.com/yuzu-emu/yuzu
        Git commit: d15e15bd058f93f16
    ''',
)
Connector(unicorn, yuzu, Date(2017,10,10))
