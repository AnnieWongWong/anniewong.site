from datetime import datetime
from mod_python import apache

#  Print HTML header
print('Cache-Control: no-cache')
print('Content-type: text/html\n')
print('<html><head><title>Hello Python</title></head>')

print('<body><h1 align=center>Annie was here - Hello HTML World</h1> <hr/>')

print('<p>This page was generated with the Python programming langauge</p>')

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("<p>Current Time: " +  dt_string + " </p>")
print(req.get_remote_host(apache.REMOTE_NOLOOKUP))
# print("<p>Your IP Address: " + os.environ['REMOTE_ADDR'] + " </p>")

print("</body>")
print("</html>")