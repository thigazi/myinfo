from pyramid.paster import get_app,setup_logging
from os import getcwd

ini_path = getcwd()+'/development.ini'
setup_logging(ini_path)
application = get_app(ini_path,'main')