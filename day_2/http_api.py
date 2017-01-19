 <!-- Consumes an API From Http lib -->
 <!-- Assuming the site has been blocked -->
import httplib
conn = httplib.HTTPSConnection("www.youtube.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
200 ok
data1 = r1.read()
conn.request("GET", "/")
r2 = conn.getresponse()
print r2.status, r2.reason
404 Not Found
data2 = r2.read()
conn.close()
<!--brought up error-->
