from data import *

Transor("DistriBit",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2009), Date(2012), dev=Dev.SJ,
    feat='''
        Server-client,
        2-level code cache,
        Server predicts client’s needing code
    ''',
    desc="2010: DistriBit: A Distributed Dynamic Binary Translator System for Thin Client Computing",
)
