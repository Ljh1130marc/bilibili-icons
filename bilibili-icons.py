import os
from urllib.request import urlretrieve,urlopen
import urllib.request
import gzip
import io
import json
import time
import urllib.parse

FILE_URL='http://www.bilibili.com/index/index-icon.json'
response = urllib.request.urlopen(FILE_URL)
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)
Json=decompressed_file.read()
NewIcons=json.loads(Json)
for a in NewIcons['fix']:
    for i in range(0,len(a['links'])):
        a['links'][i]=urllib.parse.unquote(a['links'][i])
        if a['icon'][0:2] == '//':
            a['icon'] = 'http:' + a['icon']
#print(icons)
isExists=os.path.exists('gif')
if not isExists:
        os.makedirs('gif')
OldIcons = json.load(open('index-icon.json',encoding='utf-8'))
for a in NewIcons['fix']:
    for b in OldIcons['fix']:
        filename = 'gif/' + a['title'] + '.gif'
        filesize = os.path.getsize(filename)
        if not os.path.exists(filename) or filesize==0:
            f = open(filename, 'wb')
            if a['icon'][0:2] == '//':
                a['icon'] = 'http:' + a['icon']
            img = urllib.request.urlopen(a['icon']).read()
            f.write(img)
            f.close()
            time.sleep(4)
        if a['title']==b['title']:
            NewTitle = False
            for i in len(a):
                if a['deltime']!=b['deltime'] or a['edittime']!=b['edittime'] or a['icon']!=b['icon'] or a['id']!=b['id'] or a['links']!=b['links'] or a['posttime']!=b['posttime'] or a['state']!=b['state'] or a['sttime']!=b['sttime'] or a['type']!=b['type'] or a['weight']!=b['weight']:
                    NewTitle=True
    if NewTitle==True:
        f = open(filename, 'wb')
        if a['icon'][0:2] == '//':
            a['icon'] = 'http:' + a['icon']
        img = urllib.request.urlopen(a['icon']).read()
        f.write(img)
        f.close()
        time.sleep(4)
