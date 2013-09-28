#!/usr/bin/env python3
"""
License: BSD

Copyright (c) 2013, Stefan Graupner. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer. Redistributions in
binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution. THIS SOFTWARE IS
PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import argparse
import io
import mimetypes
import urllib

def textcontent(filename):
    content = ''
    with io.open(filename, 'r') as file:
        content = file.read()
        content = content.encode('utf-8')
    return urllib.parse.quote_plus(content)

def binarycontent(filename):
    content = ''
    with io.open(filename, 'rb') as file:
        content = file.read()
        content = content.encode('base64').replace('\n', '')
    return content

def main():
    parser = argparse.ArgumentParser(description='Convert files to data URIs')
    parser.add_argument('inputfile', help='the file to convert')

    args = parser.parse_args()

    mime = mimetypes.guess_type(args.inputfile)

    if (mime[0][0:4] == 'text'):
        print('data:%(m)s;charset=utf-8,%(c)s' % { 'm': mime[0], 'c': textcontent(args.inputfile) })
    else:
        print('data:%(m)s;base64,%(c)s' % { 'm': mime[0], 'c': binarycontent(args.inputfile) })

    return 0

if  __name__ == "__main__":
    main()

