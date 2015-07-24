#!/usr/bin/env python2.7
import sys, base64, mimetypes

def encode(fp):
	ft = mimetypes.guess_type(fp, strict=True)[0]
	with open(fp, 'rb') as f:
		return 'data:{type};base64, {file}'.format(type = ft, file = base64.b64encode(f.read())) 


if len(sys.argv) == 2:
	fp = sys.argv[1]
	print encode(fp)