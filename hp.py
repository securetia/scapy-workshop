from pprint import pprint
from http_parser.parser import HttpParser

'''
 'execute',
 'get_errno',
 'get_fragment',
 'get_headers',
 'get_method',
 'get_path',
 'get_query_string',
 'get_status_code',
 'get_url',
 'get_version',
 'get_wsgi_environ',
 'is_chunked',
 'is_headers_complete',
 'is_message_begin',
 'is_message_complete',
 'is_partial_body',
 'is_upgrade',
 'maybe_parse_url',
 'recv_body',
 'recv_body_into',
 'should_keep_alive']
'''

request = '''GET http://werkzeug.pocoo.org/docs/0.14/http/ HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-AR,en-US;q=0.7,en;q=0.3
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Host: werkzeug.pocoo.org
\r\n\r\n'''

response = '''HTTP/1.1 200 OK
Server: nginx
Date: Sat, 22 Sep 2018 00:49:36 GMT
Content-Type: text/html
Content-Length: 66552
Last-Modified: Fri, 25 May 2018 07:51:42 GMT
Connection: keep-alive
ETag: "5b07c08e-103f8"
Accept-Ranges: bytes


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
'''

for item in [request, response]:


    p = HttpParser()

    #pprint(dir(p))

    p.execute(item.encode(), len(item))


    print('headers:', p.get_headers())
    print('method:', p.get_method())
    print('path:', p.get_path())
    print('qs:', p.get_query_string())
    print('sc:', p.get_status_code())
    print('url:', p.get_url())
    print('version:', p.get_version())

    print('ff:', p.get_fragment())
    print('body:', p.recv_body())


