import GeoIP
from os import getcwd
from zope.interface import Interface,implements

class IMyGeoIP(Interface):
    pass

class MyGeoIP(object):
    implements(IMyGeoIP)
    
    def __init__(self):
        fpath = [
            '%s/GeoIP.dat' % (getcwd()),
            '%s/GeoIPv6.dat' % (getcwd())
        ]
        
        self.gi = [
            GeoIP.open(fpath[0],GeoIP.GEOIP_STANDARD),
            GeoIP.open(fpath[1],GeoIP.GEOIP_STANDARD)
        ]
    