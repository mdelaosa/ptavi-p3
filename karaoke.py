#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser


class KaraokeLocal:

    def __init__(self, file):
        try:
            karaokesmill = smallsmilhandler.SmallSMILHandler()
            parser = make_parser()
            parser.setContentHandler(karaokesmill)
            parser.parse(open(file))
            self.data = karaokesmill.get_tags()

        except FileNotFoundError:
            sys.exit("Usage: python3 karaoke.py file.smil.")

    def __str__(self):
        for datos in self.data:
            for atributo, valor in datos.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        url = valor.split('/')[-1]
                        valor = url
                if atributo == 'name':
                    resultado = valor
                elif valor != '' and atributo != 'name':
                    resultado += '\t' + atributo + "= '" + valor + "'"
            return resultado

    def do_local(self):
        for datos in self.data:
            for atributo, valor in datos.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        url = valor.split('/')[-1]
                        urllib.request.urlretrieve(valor, url)
                        valor = url

    def to_json(self, file, fichjson=''):
        if fichjson == '':
            fichjson = file.replace('.smil', '.json')

        with open(fichjson, 'w') as to_json:
            json.dump(self.data, to_json, indent=3)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("file.smil is not found")
    else:
        file = sys.argv[1]
        karaoke = KaraokeLocal(file)
        print(karaoke.__str__())
        karaoke.to_json(file)
        karaoke.do_local()
        karaoke.to_json(file, 'local.json')
        print(karaoke)
