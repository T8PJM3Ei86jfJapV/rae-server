# -*- coding: utf-8 -*-

import string
import random
import urllib2

param = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9000))
url = 'http://jwtech.duapp.com/vip/search.php?search=' + param
respond = urllib2.urlopen(url)
print respond.read()