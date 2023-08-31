import re
# s = betaSignup.txt
s = 'My name is Conrad, and blahblah@gmail.com is my email.'

domain = re.search("@[\w.]+", s)
print domain.group()
