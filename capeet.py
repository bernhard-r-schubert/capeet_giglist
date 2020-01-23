import urllib.request, urllib.parse, urllib.error

fin = urllib.request.urlopen('http://www.capeet.com/gigs_list.html')
#for line in fin:
#    try:
#        print(line.decode())
#    except:
#        continue
#gigs=fin.decode()
#print(gigs)
fout = open('cleaned.html', 'w')
counts=0

for line in fin:
    try: #alles lesen was geht
        #print(type(line))
        #print(type(line.decode()))
        if 'Wien' not in line.decode():
            continue
        else:
            counts=counts+1
            fout.write(line.decode())
            fout.write('</p>')
    except: #fehlerhafte infos lesen
        #try:
        #    y=line.decode()
        #    print(y)
        #except:
        #    print('error')
        #    continue
        #print(type(line))
        if 'Wien' not in str(line):
            continue
        else:
            counts=counts+1
            fout.write(str(line))
            fout.write('</p>')

print(counts)
fout.close()
