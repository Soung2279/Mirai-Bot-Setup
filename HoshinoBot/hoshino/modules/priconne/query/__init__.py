from hoshino import Service, priv

sv = Service('pcr-query', visible=True, manage_priv=priv.ADMIN)

from .query import *
from .whois import *
from .miner import *
