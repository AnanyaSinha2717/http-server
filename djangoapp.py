from hello_world import wsgi
import sys

sys.path.insert(0, "./hello_world")
# from hello_world...

app = wsgi.application
