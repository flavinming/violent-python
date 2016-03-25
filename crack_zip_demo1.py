# -*- coding: utf-8 -*-
"""
函数版破解zip文件密码
"""
import zipfile
import time


def extract_file(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return password
    except:
        return

if __name__ == '__main__':
    start_time = time.time()
    # 密码: xcvb
    zip_file = zipfile.ZipFile("C:\Users\Ming\Documents\dsf.zip")
    pwds = open("dict.txt")
    for pwd in pwds.readlines():
        password = extract_file(zip_file, pwd.strip('\n'))
        if password:
            print "Password is %s" % password
            break

    print 'use time %d' % (time.time() - start_time)

"""
    Password is xcvb
    use time 52
"""