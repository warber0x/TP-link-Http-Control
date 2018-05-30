# TP-link WIFI Interface Control

This python code will allow you  to enable or disable your TP-link TL-WR940N wireless interface. This is useful when you need to control your WIFI radio signal by a third party device or sometimes to reduce its negative effects by turn it off. The code uses the known python library urllib2 for every http requests done here.

When the code is executed, it will try to open a valid session on the access point by sending HTTP request with a prepared cookie. The cookie is combination of Ascii login & MD5 hash encoded into a base64 scheme. The program must have a valid login and password that you gotta fill in the code. The access point  will get a result whether is valid or not. The success of the request depends on the parsed html response, and mainly when there is a valid token. If the final url string compared with the correct pattern and respect all the criteria, then the WIFI radio signal will shutdown. 

The code is yours. So, Have fun ...



