from libs import IMyGeoIP
from zope.component import getUtility
from os import getcwd
from pyramid.view import view_config


def hallo(request):
    if request.client_addr == '127.0.0.1':
        ipx = '138.201.227.75'
        
    else:
        ipx = request.client_addr
    
    gi = getUtility(IMyGeoIP)    
    response = gi.Reader.country(ipx)
    print response.country.name    
    
    cix = {
        'rip':ipx,            
        'ipc':response.country.name,
        'ipcd':response.country.iso_code,
        'agent':request.user_agent
    }            
    return {'agent': cix['agent'], 'ipx':cix['rip'],'ipc':cix['ipc'],'ipcd':cix['ipcd']}