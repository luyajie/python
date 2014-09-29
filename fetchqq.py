#!/usr/bin/env python                                                                                                                                                        
#-*-coding: gbk-*-

import re
import os
#try:
#    import xlrd
#    plaintext = 0
#except:
#    plaintext = 1

def getfile(basedir):
    files = []
    for root,dirs,files in os.walk(basedir):                                                                                                      
        for f in files:
            fpath = root + '/' + f 
            if re.findall(r'get_group_member',fpath):
                files.append(fpath)
    return files


def parsefile(files):
    for afile in files:
        print afile
        srcfh = open(afile,'r')
        content = srcfh.read()
        group_name = re.search(r"group_name\":\"(.*?)\"",content).group(1)
        dstfh = open(".\\excel\\{0}.txt".format(group_name),'w')
        members = re.search(r"\[\{(.*)\}\]",content).group(1).split('},{')
        for member in members:
            print member
            nick = member.split(',')[2].split(':')[1]
            uin = member.split(',')[3].split(':')[1]
            dstfh.write("{0}\t: {1}\n".format(uin,nick))
        dstfh.close()
        srcfh.close()


if __name__ == '__main__':
    basedir = raw_input("请输入要查询的目录：")
    if basedir:
        files = getfile(basedir)
        parsefile(files)
