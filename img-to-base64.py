#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import sys
import base64
import mimetypes


class ImgToBase64(object):
    def __init__(self, options=None, file_path=None):
        self.options = options or []
        self.file_path = file_path or ''
        self.file_type = mimetypes.guess_type(file_path, strict=True)[0]
        self.errors = []
        self.result = ''
        self.make_base64()

    def check_errors(self):
        if not os.path.isfile(self.file_path):
            self.errors.append(u'is not file or wrong path')

        if self.errors:
            for error in self.errors:
                print(error)
            sys.exit()

    def make_base64(self):
        self.check_errors()
        result_wrapper = 'base64 is ready! :)\n=======\n{result}\n======='

        with open(self.file_path, 'rb') as f:
            self.result = 'data:{type};base64,{file}'.format(type=self.file_type, file=base64.b64encode(f.read()))

        for option in self.options:
            option_name = '_option_{option}'.format(option=option.replace('-', ''))
            option_run = getattr(self, option_name, None)
            if not hasattr(self, option_name):
                print u'{option} not support'.format(option=option)
                continue
            option_run()

        print result_wrapper.format(result=self.result)

    def _option_css(self):
        self.result = 'background-image: url({string});'.format(string=self.result)


ImgToBase64(options=sys.argv[1:-1], file_path=sys.argv[-1])