from toolsx import MyGeoIP,IMyGeoIP
from zope.component import getGlobalSiteManager

try:
    gsmx
    
except:
    gsmx = getGlobalSiteManager()
    gsmx.registerUtility(MyGeoIP(),IMyGeoIP,'GEOIPZ')