import geoip2.database
from os import getcwd
from zope.interface import Interface,implements

class IMyGeoIP(Interface):
    pass

class MyGeoIP(object):
    implements(IMyGeoIP)
    
    def __init__(self):
        self.Reader = geoip2.database.Reader(getcwd()+'/GeoLite2-Country.mmdb')
        #self.Reader.country(ip_address)
        
    def __delete__(self):
        self.Reader.close()