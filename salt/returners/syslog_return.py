# -*- coding: utf-8 -*-
'''
Return data to the host operating system's syslog facility

Required python modules: syslog, json

The syslog returner simply reuses the operating system's syslog
facility to log return data

To use the syslog returner, append '--return syslog' to the salt command.

.. code-block:: bash

    salt '*' test.ping --return syslog

'''
from __future__ import absolute_import

# Import python libs
import json
try:
    import syslog
    HAS_SYSLOG = True
except ImportError:
    HAS_SYSLOG = False

# Import Salt libs
import salt.utils.jid

# Define the module's virtual name
__virtualname__ = 'syslog'


def __virtual__():
    if not HAS_SYSLOG:
        return False
    return __virtualname__


def returner(ret):
    '''
    Return data to the local syslog
    '''
    syslog.syslog(syslog.LOG_INFO, '{0}'.format(json.dumps(ret)))


def prep_jid(nocache=False, passed_jid=None):  # pylint: disable=unused-argument
    '''
    Do any work necessary to prepare a JID, including sending a custom id
    '''
    return passed_jid if passed_jid is not None else salt.utils.jid.gen_jid()
