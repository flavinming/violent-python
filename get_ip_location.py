# -*- coding: utf-8 -*-
import requests
import re


def get_location(ip):
    location = ''
    try:
        r = requests.get('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query='+ip+r'&co=&resource_id=6006&t=1434376542742&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110209716921530198306_1434374205566&_=1434374205616')
        js =  r.content[r.content.find('{"'):-2]
        match = re.search('(?<=location":")[^"]+', js)
        if match:
            location = match.group()
        print 'ip: %s , location:%s' % (ip, location.decode("gbk"))
    except Exception, e:
        print 'ip: %s , location:%s' % (ip, location)
        pass

if __name__=="__main__":
    with open("ip.txt") as f:
        #IP 120.52.168.66
        for line in f:
            m = re.search("(?<=IP) \d+.\d+.\d+.\d+", line)
            if m:
                ip = m.group()
                get_location(ip)
