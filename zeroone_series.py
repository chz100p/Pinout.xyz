import requests
from bs4 import BeautifulSoup
from io import open # for python2
import re
import time
import json

import subprocess

from PersistentDict import PersistentDict

zeroone = PersistentDict('zeroone.json', format='json')
top = PersistentDict('top.json', 'r', format='json')
github = PersistentDict('github.json', 'r', format='json')
btoshop = PersistentDict('btoshop.json', 'r', format='json')

# zeroone.update(merge(top,github,btoshop))
zeroone.update({pn:{'{}_{}'.format(pre, k):v for pre, dic in (('top',top[pn] if pn in top else {}), ('github',github[pn] if pn in github else {}), ('btoshop',btoshop[pn] if pn in btoshop else {})) for k, v in dic.items()} for pn in github})

# 間違えて収集しちゃった情報を修正
for pn,xpn in (('adrszei','adrszel'),('adrszgp','adrszdgp')):
    zeroone[pn].update({'{}_{}'.format(pre, k):v for pre, dic in (('top',top[xpn] if xpn in top else {}), ('btoshop',btoshop[xpn] if xpn in btoshop else {})) for k, v in dic.items()})
zeroone['adrszei']['top_bittradeone_zeroone_name']=u'adrszei'
zeroone['adrszgp']['top_bittradeone_zeroone_name']=u'adrszgp'
zeroone['adrszgp']['top_url']=u'http://bit-trade-one.co.jp/adrszgp/'


# zeroone['.index']
zeroone['.index'] = sorted(zeroone, key=lambda k: int(zeroone[k]['github_bittradeone_zeroone_no']))
zeroone['.top_index'] = sorted(zeroone, key=lambda k: int(zeroone[k]['top_bittradeone_zeroone_no'] if 'top_bittradeone_zeroone_no' in zeroone[k] else 99))

# 製品の説明文を拾ってきて必要なところだけmarkdownに変換
for pn in zeroone['.index']:
    print '{}:{}: {}'.format(zeroone[pn]['github_bittradeone_zeroone_no'], pn, zeroone[pn]['top_url']) if 'top_bittradeone_zeroone_no' in zeroone[pn] else '{}:{}: '.format(zeroone[pn]['github_bittradeone_zeroone_no'], pn)
    if 'top_url' in zeroone[pn]:
        response = requests.get(zeroone[pn]['top_url'])
        response.encoding = response.apparent_encoding
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        left_col = bs.find(id='left_col')
        yarpp_related = left_col.find(class_='yarpp-related').extract()
        html2md = subprocess.Popen(('node', 'html2md.js'), stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        html2md.stdin.write(str(left_col))
        html2md.stdin.close()
        md = html2md.stdout.read()
        ret = html2md.wait()
        zeroone[pn]['top_md'] = md if isinstance(md, unicode) else unicode(md, encoding='utf-8')

'''
for pn in zeroone['.index']:
    if 'top_md' in zeroone[pn] and not isinstance(zeroone[pn]['top_md'], unicode):
        zeroone[pn]['top_md'] = unicode(zeroone[pn]['top_md'], encoding='utf-8')

'''

mj_template = u'''<!--
---
name: {name_}
class: {class_}
type: {type_}
formfactor: {formfactor_}
manufacturer: {manufacturer_}
description: {description_}
url: {url_}
github: {github_}
buy: {buy_}
image: '{image_}'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Enable
    mode: output
    active: high
i2c:
  '0x00':
    name: device display name
    device: chip name
-->
{md_}
'''

for pn in zeroone['.index']:
    p = zeroone[pn]
    mj = mj_template.format(
        name_ = p['top_bittradeone_zeroone_name'] if 'top_bittradeone_zeroone_name' in p else "''",
        class_ = 'board',
        type_ = 'other',
        formfactor_ = 'pHAT',
        manufacturer_ = 'BitTradeOne',
        description_ = p['top_name'] if 'top_name' in p else "''",
        url_ = p['top_url'] if 'top_url' in p else "''",
        github_ = p['github_url'] if 'github_url' in p else "''",
        buy_ = p['btoshop_url'] if 'btoshop_url' in p else "''",
        image_ = '{}.png'.format(pn),
        md_ = p['top_md'] if 'top_md' in p else pn
        )
    with open('draft/overlay/{}.md'.format(pn), 'w', encoding='utf-8') as f:
        f.write(mj)


import os
import shutil
for pn in zeroone['.index']:
    pn_png = 'draft/boards/{}.png'.format(pn)
    if not os.path.exists(pn_png):
        shutil.copy('draft/boards/template.png', pn_png)


'''
top_url = 'http://bit-trade-one.co.jp/product/module/zeroone01top/'
top_response = requests.get(top_url)
top_response.encoding = top_response.apparent_encoding

top_response_html = top_response.text

with open('top.html', 'w', encoding='utf-8') as f:
    f.write(top_response_html)
'''
with open('top.html', 'r', encoding='utf-8') as f:
    top_response_html = f.read()

top_bs = BeautifulSoup(top_response_html, 'html.parser')

anker = top_bs.find(id='page_content').find_all('a')

top = {}
bittradeone_zeroone_no = 0
for a in anker:
    url = a.get('href')
    if '/adrsz' in url and not a.find_parent(class_='yarpp-related'):
        bittradeone_zeroone_no = bittradeone_zeroone_no + 1
        bittradeone_zeroone_name = re.search(r'adrsz[a-z]*', url).group()
        name = a.get_text(separator=u' ')
        print bittradeone_zeroone_no, bittradeone_zeroone_name, name, url
        top[bittradeone_zeroone_name] = {
            'bittradeone_zeroone_no': bittradeone_zeroone_no,
            'bittradeone_zeroone_name': bittradeone_zeroone_name,
            'name': name,
            'url': url
            }


'''
github_url = 'https://github.com/bit-trade-one/RasPi-Zero-One-Series'
github_response = requests.get(github_url)
github_response.encoding = github_response.apparent_encoding

github_response_html = github_response.text

with open('github.html', 'w', encoding='utf-8') as f:
    f.write(github_response_html)
'''
with open('github.html', 'r', encoding='utf-8') as f:
    github_response_html = f.read()

github_bs = BeautifulSoup(github_response_html, 'html.parser')

anker = github_bs.find(id='readme').find_all('a')

github = {}
bittradeone_zeroone_no = 0
for a in anker:
    name = a.get_text(separator=u',')
    m = re.search(r'adrsz[a-z]*', name, re.IGNORECASE)
    if m:
        bittradeone_zeroone_no = bittradeone_zeroone_no + 1
        bittradeone_zeroone_name = m.group().lower()
        url = a.get('href')
        print bittradeone_zeroone_no, bittradeone_zeroone_name, name, url
        github[bittradeone_zeroone_name] = {
            'bittradeone_zeroone_no': bittradeone_zeroone_no,
            'bittradeone_zeroone_name': bittradeone_zeroone_name,
            'name': name,
            'url': url
            }



'''
zeroone_series = sorted(top, key=lambda k: int(top[k]['bittradeone_zeroone_no']))

btoshop = {}
for zeroone in zeroone_series:
    print zeroone
    time.sleep(1)
    btoshop_s_url = r'http://btoshop.jp/?s={}'.format(zeroone)
    btoshop_s_response = requests.get(btoshop_s_url)
    btoshop_s_response.encoding = btoshop_s_response.apparent_encoding
    btoshop_s_response_html = btoshop_s_response.text
    btoshop_s_bs = BeautifulSoup(btoshop_s_response_html, 'html.parser')
    anker = btoshop_s_bs.find(id='content').find_all('a')
    btoshop_urls = [a.get('href') for a in anker]
    if len(btoshop_urls) == 1:
        btoshop_url = btoshop_urls[0]
    elif len(btoshop_urls) > 1:
        btoshop_url = btoshop_s_url
    else:
        btoshop_url = ''
    btoshop[zeroone] = {
        'btoshop_s_response_html': btoshop_s_response_html,
        'urls': btoshop_urls,
        'url': btoshop_url
        }

with open('btoshop.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(btoshop).decode('utf-8'))

with open('top.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(top).decode('utf-8'))

with open('github.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(github).decode('utf-8'))


with open('adrszbm.html', 'r', encoding='utf-8') as f:
    adrszbm_html = f.read()

adrszbm_bs = BeautifulSoup(adrszbm_html, 'html.parser')

left_col=adrszbm_bs.find(id='left_col')
left_col.find(class_='yarpp-related').extract()

html2md = subprocess.Popen(('node', 'html2md.js'), stdin = subprocess.PIPE, stdout = subprocess.PIPE)
html2md.stdin.write(str(left_col))
html2md.stdin.close()
md = html2md.stdout.read()
ret = html2md.wait()
print('ret={0}'.format(ret))
print(md)

#[k for k in btoshop]
#[k for k in btoshop if r'?s=' in btoshop[k]['url']]
#[k for k in btoshop if 0 == len(btoshop[k]['url'])]

'''

'''
bittradeone-zeroone-name
bittradeone-zeroone-no
name
description
url
github
buy
image
md
'''

