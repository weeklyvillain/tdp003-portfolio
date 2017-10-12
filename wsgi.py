#!/usr/bin/python3
import os

virtenv = os.environ['var/lib/openshift/59df606679c0532a7c000576/app-root/runtime/repo'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
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

import os
os.chdir(os.environ['var/lib/openshift/59df606679c0532a7c000576/app-root/'])

from server import app as application
