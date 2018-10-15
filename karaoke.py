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
        karaokesmill = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(karaokesmill)
        parser.parse(open(sys.argv[1]))
        data = karaokesmill.get_tags()

        fichsmil = sys.argv[1]
        fichjson = ''
        if fichjson == '':
            fichjson = fichsmil.replace('.smil', '.json')

        with open(fichjson, 'w') as cambiojson:
            json.dump(data, cambiojson, indent=3)

        for datos in data:
            for atributo, valor in datos.items():
                if atributo == 'name':
                    print(valor, end='\t')
                if atributo == 'src':
                    if valor.startswith('http://'):
                        archivo = valor.split('/')
                        descarga = urllib.request.urlretrieve(valor, archivo)
                        valor = descarga
                if valor != '' and atributo != 'name':
                    print(atributo, "=", "'", valor, "'", end='\t')
            print(end='\n')
