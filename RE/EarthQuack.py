#!/usr/bin/python
#-*-coding:utf-8 -*-
# The data is from http://www.cwb.gov.tw/V7/earthquake/

import sys
import re

def toBig5(text):
    '''
    from utf8 to Big5
    '''
    return text.decode('utf8').encode('Big5')


if len(sys.argv) < 2:
    print "NO INPUT FILE !!"
    sys.exit(0)

filename = sys.argv[1]
#print "filename: {}".format(filename)

content = []
with open(filename) as fd:
    for i in fd.readlines():
#        tmp = i.decode('Big5').strip()
        tmp = i.decode('Big5')
        if len(tmp) > 0:
#            print tmp
#        content.append(i.decode('Big5').encode('utf8'))
            content.append(tmp.encode('utf8'))
#            print repr(tmp)


#for i in content:
#    print i

#result_msg = '期交所地震通報\n'.decode('utf8').encode('Big5')
result_msg = '期交所地震通報\n'

#pattern = toBig5('(?<=相  對  位  置： ).*(?=\s\()')
pattern = '(?<=相  對  位  置： ).*(?=\s\()'
for i in content:
    m1 = re.search(pattern, i)
    if not m1 == None:
        result_msg = result_msg + m1.group(0)
        break


pattern = '(?<=震　源　深　度：).*(\s\d+\.\d*)'
for i in content:
    m1 = re.search(pattern, i)
    if not m1 == None:
        result_msg = result_msg + ', 深度: '+m1.group(1)+'公里'
        break

pattern = '(?<=芮　氏　規　模：).*(\d+\.\d*)'
for i in content:
    m1 = re.search(pattern, i)
    if not m1 == None:
        result_msg = result_msg + ', 規模: '+m1.group(1)
        break

#for i in content:
#    if '地區最大震度' in i:
#        i = i.split('　　　　')
#        for j in i:
#            print "HIT"
#    break


pattern1 = '(\xe3\x80\x80)*(\S+?)地區最大震度\s(\d)級'
result = {}
for i in content:
    m1 = re.findall(pattern1, i)
    if len(m1) > 0 :
#            print m1
        for (j,k,l) in m1:
#            print str(len(j))+">>"+k+": "+l
            result[k] = l

##############################

pattern1 = '(\xe3\x80\x80)*(\S+?)地區最大震度\s(\d)級'
#pattern2 = '\S+(\xe3\x80\x80)*\S*\ \d'
#pattern2 = '(\xe3\x80\x80)+(\S+?\ \d)(\xe3\x80\x80)*'
pattern2 = '([\xe3\x80\x80]+)(\S+?\ \d+)'
#pattern2 = '(.*)(\d)+'
area_info = {}
area_info2 = "" # for area's earthquack > 3
for line, i in enumerate(content):

    if line < 10:
        continue
#    print "line {}: {}\n".format(line+1 ,i)
    m1 = re.findall(pattern1, i)
    if len(m1) > 0:
        PAPA = []
#        print m1
        for z, (j,k,l) in enumerate(m1):
#            print str(len(j))+">>"+k+": "+l
            PAPA.append(k)
            flag_X = True
    else:
        suck_space = 0
#        print "len: ", len(i)
        m1 = re.findall(pattern2, i)
#        print(m1)
        if flag_X:
            for y in range(len(PAPA)):
                area_info[PAPA[y]] = []
            flag_X = False

        for (j,k) in m1:
            suck_space = suck_space + len(j)
#            print "YY"+str(len(j))+"XX"+k+"ZZ"
            if suck_space == 9:
                area_info[PAPA[0]].append(k)
            if suck_space in [54, 42]:
                area_info[PAPA[1]].append(k)
            if suck_space in [75, 99, 87]:
                area_info[PAPA[2]].append(k)

            (n1, n2) = k.split(' ')
            if int(n2) >= 3:
                area_info2 = area_info2 + k + ', '
#            print j
#            for (k,l) in j:

#for i in area_info:
#    result_s = i + ' : '
#    for j in area_info[i]:
#        result_s = result_s +  j+ ', '
#    print result_s.rstrip(', ')

##############################


#find_flag = False
#for i in content:
#    if toBig5('各 地 震 度 級') in i:
#        find_flag = True
#    if not find_flag:
#        continue
#    else:
#        print i

print result_msg

important_city = ['臺北市', '新北市', '臺中市']

for i in result:
    for j in important_city:
        if j in i:
#            print "{}地區最大震度 {}級".format(i, result[i])
            tmp =  "{}地區最大震度 {}級".format(i, result[i])
            if j in area_info.keys():
                for k in area_info[j]:
                    m, n = k.split(' ')
                    if m == j:
#                        print k+'級'
                        tmp = tmp + ', ' +k+'級'
#                print area_info[j][0]+'級'
#                print area_info[j].get(j, 'XX')+"ㄏㄏ"
                print tmp

#print area_info

for i in result:
    if int(result[i]) > 2:
        print "{}地區最大震度{}級".format(i,result[i])

print area_info2.rstrip(', ')
