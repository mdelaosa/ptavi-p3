#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.data = []

    def startElement(self, name, attrs):
        if name == "root-layout":
            root_attrs = {'name': name}
            for attr in ['width', 'height', 'background_color']:
                if attr in attrs:
                    root_attrs[attr] = attrs[attr]
            self.data.append(root_attrs)

        elif name == "region":
            region_attrs = {'name': name}
            for attr in ['id', 'top', 'bottom', 'left', 'right']:
                if attr in attrs:
                    region_attrs[attr] = attrs[attr]
            self.data.append(region_attrs)

        elif name == "img":
            img_attrs = {'name': name}
            for attr in ['src', 'region', 'begin', 'dur']:
                if attr in attrs:
                    img_attrs[attr] = attrs[attr]
            self.data.append(img_attrs)

        elif name == "audio":
            audio_attrs = {'name': name}
            for attr in ['src', 'begin', 'dur']:
                if attr in attrs:
                    audio_attrs[attr] = attrs[attr]
            self.data.append(audio_attrs)

        elif name == "textstream":
            text_attrs = {'name': name}
            for attr in ['src', 'region']:
                if attr in attrs:
                    text_attrs[attr] = attrs[attr]
            self.data.append(text_attrs)

    def get_tags(self):
        return self.data


if __name__ == '__main__':

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.argv[1]))
    data = sHandler.get_tags()
    print(data)
