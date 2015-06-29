# @SI_Copyright@
#                             www.stacki.com
#                                  v1.0
# 
#      Copyright (c) 2006 - 2015 StackIQ Inc. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#  
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#  
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
#  
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	 "This product includes software developed by StackIQ" 
#  
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY STACKIQ AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# @SI_Copyright@

import os
import time
import pytest
from stack.api import *

NUMRACKS    = 10
RACKSIZE    = 10
ENVIRONMENT = 'pytest'

def setup_module(module):
        for rack in range(1000, 1000 + NUMRACKS):
                for rank in range(0, RACKSIZE):
                        host = 'backend-%d-%d' % (rack, rank)
                        Call('add host %s' % host)
                        Call('set host attr %s attr=environment value=%s' %
                             (host, ENVIRONMENT))
        Call('set environment attr %s attr=key value=value' % ENVIRONMENT)

        result = Call('list host %s' % ENVIRONMENT)
        assert ReturnCode() == 0 and len(result) == (NUMRACKS * RACKSIZE)

                        
def teardown_module(module):
        Call('remove host %s' % ENVIRONMENT)


def test_scale():
        print '...'
        t0 = time.time()
        Call('list host')
        t1 = time.time()
        print 'list host (%.3fs)' % (t1-t0)
        t0 = time.time()
        Call('list host profile', [ 'backend-1000-0' ])
        t1 = time.time()
        print 'list host profile (%.3fs)' % (t1-t0)
        




