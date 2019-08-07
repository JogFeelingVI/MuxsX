#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-08-08 07:08
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: Colortable

class colortable:
	mode = [x for x in range(8)]
	fg = [x for x in range(30, 38)]
	bg = [x for x in range(40, 48)]

	@staticmethod
	def Coloring(m: int = 0, f: int = 30, b: int = 40, s=None) -> str:
		# \033[mode,f,bm
		md = m if m in colortable.mode else 0
		fc = f if f in colortable.fg or f is 0 else 30
		bc = b if b in colortable.bg or f is 0 else 40
		msg = str(s)
		code = ';'.join([str(md), str(fc), str(bc)])
		return '\x1b[{code}m {t} \x1b[0m'.format(code=code, t=msg)

	@staticmethod
	def legend():
		for style in range(8):
			for fg in range(30, 38):
				s1 = ''
				for bg in range(40, 48):
					format = ';'.join([str(style), str(fg), str(bg)])
					s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
				print(s1)
			print('\n')

	@staticmethod
	def legend_no_bg():
		for style in range(8):
			for fg in range(30, 38):
				format = ';'.join([str(style), str(fg)])
				s1 = '\x1b[%sm %s \x1b[0m' % (format, format)
				print(s1)
			print('\n')


def main():
	colortable.legend_no_bg()

if __name__ == '__main__':
	main()