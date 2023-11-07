from data import *
from edk2_sagit.meta import *

# Firmware, actually not a transor
Transor("edk2-sdm845",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2020,5,25), Date.today(), parent=edk2_sagit,
    desc="Enable to run Win11, Support graphics card, can play ff14",
)
