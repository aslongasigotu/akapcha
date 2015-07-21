#-*- coding: utf-8 -*-
import urllib2
import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')

rus_alp = u"абвгдежзийклмнопрстуфхцчшщъыьэюя"
eng_alp = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"

q_cnt = 10000
q_len = 12

q_line = "http://yandex.ru/search/?lr=213&text=%s"

for i in xrange(q_cnt):
    q = ""
    for i in xrange(q_len):
        w_list = random.choice((rus_alp,eng_alp,digits))
        q += random.choice(w_list)
    print "q : " + q
    resp = urllib2.urlopen(q_line % q)
    html = resp.read()
    if "captcha" in html:
        print html
        break
