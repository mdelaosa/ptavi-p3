#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:53:07 2018

@author: mdelaosa
"""
import sys
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

        for atributo in data:
            for datos in atributo:
                if atributo[datos] != '':
                    print(datos, "=", "'", atributo[datos], "'", end='\t')
            print(end='\n')
