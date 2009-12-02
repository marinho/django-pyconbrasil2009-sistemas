# Author: limodou@gmail.com
# version: 0.2
# Profile request of django
#

import hotshot
import os
import time
from django.conf import settings

PROFILE_DATA_DIR = "./profile"
class ProfileMiddleware(object):
    def process_request(self, request):
        path = getattr(settings, 'PROFILE_DIR', PROFILE_DATA_DIR)
        if not os.path.exists(path):
            os.makedirs(path)
            os.chmod(path, 0755)
#        profname = "%s.%.3f.prof" % (request.path.strip("/").replace('/', '.'), time.time())
        profname = "%s.prof" % (request.path.strip("/").replace('/', '.'))
        profname = os.path.join(PROFILE_DATA_DIR, profname)
        try:
            self.prof = prof = hotshot.Profile(profname)
            prof.start()
        except:
            self.prof = None
        
#    def process_view(self, request, callback, callback_args, callback_kwargs):
#        try:
#            return prof.runcall(callback, request, *callback_args, **callback_kwargs)
#        finally:
#            prof.close()
#            
            
    def process_response(self, request, response):
        if self.prof:
            self.prof.close()
        return response


