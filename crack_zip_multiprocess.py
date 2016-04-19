# -*- coding: utf-8 -*-
import zipfile
from multiprocessing import Process
import time

def extract_file(passwords):
    zip_file = zipfile.ZipFile(r"C:\Users\Ming\Documents\test.zip")
    for password in passwords:
        try:
            zip_file.extractall(pwd=password.strip('\n'))
            print "The possword is %s" % password
            print 'use time %d' % (time.time() - start_time)
            os._exit(0)
        except Exception, e:
            # traceback.print_exc(e)
            continue

if __name__ == '__main__':
    N_PROC = 8
    pwds = open("dict.txt")
    passwords = pwds.readlines()
    size = len(passwords) / N_PROC
    for i in range(N_PROC):
        p = Process(target=extract_file, args=[passwords[i::N_PROC]])
        p.start()



