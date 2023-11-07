from data import *
from QEMU_sys.meta import *

unicorn = Transor("unicorn",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2015,8,21), Date.today(), color="#E62129", parent=QEMU_sys,
    feat="Framework",
    desc="https://github.com/unicorn-engine/unicorn",
)
