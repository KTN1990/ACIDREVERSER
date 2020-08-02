# -*- coding: utf-8 -*
#!/usr/bin/python
#pip install http-request-randomizer
#####################################
##KILL THE NET##
##############[LIBS]###################
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import sys
while 1:
    try:
        ip = sys.argv[1]
        api = 'http://api.hackertarget.com/reverseiplookup/?q='+ip
        req_proxy = RequestProxy()
        try:
            request = req_proxy.generate_proxied_request(api)
            if request:
                if 'error' in request.text or 'No DNS' in request.text:
                    break
                if 'API count exceeded' in request.text or 'Bad Request' in request.text:
                    continue
                else:
                    open(ip+'.txt','a').write(request.text+'\n')
                    open('ALL-SITES.txt','a').write(request.text+'\n')
                    break
        except:
            pass
    except Exception as e:
        print(e)
        break
