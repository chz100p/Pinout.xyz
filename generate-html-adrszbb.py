#!/usr/bin/env python

import os
import re
import sys
import unicodedata
import glob

try:
    import markdown
except ImportError:
    exit("This script requires the Markdown module\nInstall with: sudo pip install Markdown")

import markjaml
import pinout
import urlmapper

import json

reload(sys)
sys.setdefaultencoding('utf8')

DEBUG_LEVEL = 1
GROUND_PINS = [6,9,14,20,25,30,34,39]

lang = "en"
default_strings = {
    'home': 'Home',
    'boards': 'Boards',
    'details': 'Details',
    'pin_header': '{} pin header',
    'form_undefined': 'Undefined',
    'group_other': 'other',
    'type_hat': 'HAT form-factor',
    'type_phat': 'pHAT form-factor',
    'type_classic': 'Classic form-factor',
    'eeprom_detect': 'Uses VID/PID',
    'eeprom_setup': 'Uses EEPROM',
    'uses_5v_and_3v3': 'Needs 5v and 3v3 power',
    'uses_5v': 'Needs 5v power',
    'uses_3v3': 'Needs 3v3 power',
    'uses_i2c': 'Uses I2C',
    'uses_spi': 'Uses SPI',
    'uses_n_gpio_pins': 'Uses {} GPIO pins',
    'bcm_pin_rev1_pi': 'BCM pin {} on Rev 1 ( very early ) Pi',
    'physical_pin_n': 'Physical pin {}',
    'wiring_pi_pin': 'Wiring Pi pin {}',
    'made_by': 'Made by {manufacturer}',
    'more_information': 'More Information',
    'github_repository': 'GitHub Repository',
    'board_schematic': 'Schematic',
    'buy_now': 'Buy Now',
    'translate_msg': '<a href="https://github.com/gadgetoid/Pinout.xyz">This page needs translating, can you help?</a><br><br>',
    'browse_addons': 'Browse more HATs, pHATs and add-ons',
    'return_home': 'Return to the Raspberry Pi GPIO Pinout',
    'boards_title': 'Raspberry Pi HATs, pHATs &amp; Add-ons',
    'boards_subtitle': 'Click on a HAT, pHAT or add-on for more details and to see which pins it uses!'
}



'''
Main Program Flow
'''

if len(sys.argv) > 1:
    lang = sys.argv[1]

alternate_urls = urlmapper.generate_urls(lang)

pinout.load(lang)

overlays = glob.glob("src/{}/overlay/*.md".format(lang)) + glob.glob("src/{}/translate/*.md".format(lang))

strings = pinout.get_string('strings', {})

if type(strings) == list:
    _strings = {}
    for item in strings:
        _strings[item.keys()[0]] = item.values()[0]
    strings = _strings

for key, val in default_strings.items():
    if key not in strings:
        strings[key] = val

base_url = pinout.get_setting('base_url', '/pinout/')  # '/pinout-tr/pinout/'
resource_url = pinout.get_setting('resource_url', '/resources/')  # '/pinout-tr/resources/'
url_suffix = pinout.get_setting('url_suffix', '')  # '.html'


template_adrszbb = open('common/adrszbb.html'.format(lang)).read()

if not os.path.isdir('output'):
    try:
        os.mkdir('output')
    except OSError:
        exit('Failed to create output dir')
if not os.path.isdir('output/{}'.format(lang)):
    try:
        os.mkdir('output/{}'.format(lang))
    except OSError:
        exit('Failed to create output/{} dir'.format(lang))
if not os.path.isdir('output/{}/Pinout.xyz'.format(lang)):
    try:
        os.mkdir('output/{}/Pinout.xyz'.format(lang))
    except OSError:
        exit('Failed to create output/{}/Pinout.xyz dir'.format(lang))

boards = map(lambda overlay: markjaml.load(overlay)['data'], overlays)
html = template_adrszbb.replace('{{data}}', json.dumps(boards))
html = html.replace('{{resource_url}}', resource_url)
url = 'adrszbb'

url = os.path.join('Pinout.xyz', url)

with open(os.path.join('output', lang, '{}.html'.format(url)), 'w') as f:
    f.write(html)

print('\nAll done!')
