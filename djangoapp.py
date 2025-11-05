import sys

sys.path.insert(0, "./hello_world")
from hello_world import wsgi

app = wsgi.application
