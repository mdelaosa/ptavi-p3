#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import smallsmilhandler
from xml.sax import make_parser


def convertirjson(self, filesmil, filejson=''):
    if filejson == '':
        filejson = filesmil.replace('.smil', '.json')

    with open(filejson, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=3)


if __name__ == '__main__':

    if len(sys.argv) != 2:
            print("Usage: python3 karaoke.py file.smil.")
    else:
        karaokesmill = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(karaokesmill)
        parser.parse(open(sys.argv[1]))
        data = karaokesmill.get_tags()

        for datos in data:
            for atributo, valor in datos.items():
                if atributo == 'name':
                    print(valor, end='\t')
                if valor != '' and atributo != 'name':
                    print(atributo, "=", "'", valor, "'", end='\t')
            print(end='\n')
