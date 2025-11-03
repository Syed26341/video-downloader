import imp
import os
import sys

# Ensure current directory is in path
sys.path.insert(0, os.path.dirname(__file__))

# Load Flask app
wsgi = imp.load_source('wsgi', 'app.py')
application = wsgi.app
