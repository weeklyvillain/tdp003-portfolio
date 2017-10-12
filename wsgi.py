#!/usr/bin/python3


virtualenv = 'bin/activate_this.py'
try:
    with open(virtualenv) as f:
        code = compile(f.read(), virtualenv, 'exec')
        exec(code, global_vars, local_vars)
except IOError:
     pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#



from main import app as application

