#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.data = []

    def startElement(self, name, attrs):
        if name == "root-layout":
            self.width = attrs.get("width", "")
            self.height = attrs.get("height", "")
            self.background_color = attrs.get("background-color", "")
            self.data.append({"name": name, "width": self.width,
                              "height": self.height,
                              "background-color": self.background_color})

        elif name == "region":
            self.id = attrs.get("id", "")
            self.top = attrs.get("top", "")
            self.bottom = attrs.get("bottom", "")
            self.left = attrs.get("left", "")
            self.right = attrs.get("right", "")
            self.data.append({"name": name, "id": self.id, "top": self.top,
                              "bottom": self.bottom, "left": self.left,
                              "right": self.right})

        elif name == "img":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur")
            self.data.append({"name": name, "src": self.src,
                              "region": self.region, "begin": self.begin,
                              "dur": self.dur})

        elif name == "audio":
            self.src = attrs.get("src", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.data.append({"name": name, "src": self.src,
                              "begin": self.begin, "dur": self.dur})

        elif name == "textstream":

            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.data.append({"name": name, "src": self.src,
                              "region": self.region})

    def get_tags(self):
        return self.data


if __name__ == '__main__':

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.argv[1]))
    data = sHandler.get_tags()
    print(data)
