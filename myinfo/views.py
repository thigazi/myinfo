from libs import IMyGeoIP
from zope.component import queryUtility
from os import getcwd
from pyramid.view import view_config
from socket import AF_INET,AF_INET6


def hallo(request):        
    ipx = request.headers['X-Real-Ip']
    
    if len(ipx.split('.')) > 1:
        gi = queryUtility(IMyGeoIP,'GEOIPZ').gi[0]
        
        cix = {
            'rip':ipx,            
            'ipc':gi.country_name_by_addr(ipx),
            'ipcd':gi.country_code_by_addr(ipx),
            'agent':request.user_agent
        }            
        return {'agent': cix['agent'], 'ipx':cix['rip'],'ipc':cix['ipc'],'ipcd':cix['ipcd']}
        
    else:
        gi = queryUtility(IMyGeoIP,'GEOIPZ').gi[1]   
        
        cix = {
            'rip':ipx,            
            'ipc':gi.country_name_by_addr_v6(ipx),
            'ipcd':gi.country_code_by_addr_v6(ipx),
            'agent':request.user_agent
        }            
        
        return {'agent': cix['agent'], 'ipx':cix['rip'],'ipc':cix['ipc'],'ipcd':cix['ipcd']}
    