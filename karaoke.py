#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser


if __name__ == '__main__':

    if len(sys.argv) != 2:
            print("Usage: python3 karaoke.py file.smil.")
    else:
        file = sys.argv[1]
        karaokesmill = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(karaokesmill)
        parser.parse(open(file))
        data = karaokesmill.get_tags()

        fichjson = ''
        if fichjson == '':
            fichjson = file.replace('.smil', '.json')

        with open(fichjson, 'w') as cambiojson:
            json.dump(data, cambiojson, indent=3)

        for datos in data:
            for atributo, valor in datos.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        archivo = valor.split('/')[-1]
                        urllib.request.urlretrieve(valor)
                        valor = archivo
                if atributo == 'name':
                    print(valor, end='\t')
                if valor != '' and atributo != 'name':
                    print(atributo, "=", "'", valor, "'", end='\t')
            print(end='\n')
