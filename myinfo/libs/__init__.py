from toolsx import MyGeoIP,IMyGeoIP
from zope.component import getGlobalSiteManager

gsmx = getGlobalSiteManager()
gsmx.registerUtility(MyGeoIP(),IMyGeoIP)