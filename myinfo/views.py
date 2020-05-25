from .libs import IMyGeoIP
from zope.component import getUtility
from os import getcwd
from pyramid.view import view_config


def hallo(request):
    if request.client_addr in ('127.0.0.1','::1'):
        #testaddress for NL ipv6 address
        ipx = '2001:610:1a08:292:129:125:2:51'
        
    else:
        ipx = request.client_addr
    
    gi = getUtility(IMyGeoIP)    
    response = gi.Reader.country(ipx)    
    
    cix = {
        'rip':ipx,            
        'ipc':response.country.name,
        'ipcd':response.country.iso_code,
        'agent':request.user_agent
    }            
    return {'agent': cix['agent'], 'ipx':cix['rip'],'ipc':cix['ipc'],'ipcd':cix['ipcd']}