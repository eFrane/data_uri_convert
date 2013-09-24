#!/usr/bin/env python

import argparse
import io
import mimetypes
import urllib

def textcontent(filename):
    content = ''
    with io.open(filename, 'r') as file:
        content = file.read()
        content = content.encode('utf-8')
    return urllib.quote_plus(content)

def binarycontent(filename):
    content = ''
    with io.open(filename, 'rb') as file:
        content = file.read()
        content = content.encode('base64').replace('\n', '')
    return content

def main():
    parser = argparse.ArgumentParser(description='Convert binary data to data URIs')
    parser.add_argument('inputfile', help='the file to convert')

    args = parser.parse_args()

    mime = mimetypes.guess_type(args.inputfile)

    if (mime[0][0:4] == 'text'):
        print 'data:%(m)s;charset=utf-8,%(c)s' % { 'm': mime[0], 'c': textcontent(args.inputfile) }
    else:
        print 'data:%(m)s;base64,%(c)s' % { 'm': mime[0], 'c': binarycontent(args.inputfile) }

    return 0

if  __name__ == "__main__":
    main()

