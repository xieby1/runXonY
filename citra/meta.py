from data import *
from skyeye.meta import *

# TODO: non-general, game
citra = Transor("citra",
    {  HG("",
        Metaface(),
        # TODO: 3DS
        Metaface(),
    )},
    Date(2013,8,30), Date.today(), color="#FF8E03",
    desc="https://github.com/citra-emu/citra",
)
Connector(skyeye, citra, Date(2013,5,2), Date(2013,9,18))
