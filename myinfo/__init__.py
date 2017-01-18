import libs,tpx
from pyramid.config import Configurator
from views import hallo
from os import getcwd

def main(global_config, **settings):    
    config = Configurator(settings=settings)    
    config.include('pyramid_jinja2')    
    config.add_route('hallo','/')
    config.add_view(hallo,route_name='hallo',renderer='tpx/infox.jinja2')
    config.add_static_view(name='static', path=getcwd()+'/myinfo/static')
    config.scan()
    return config.make_wsgi_app()