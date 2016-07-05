# -*- coding:utf-8 -*-
class colors:
	'''
	Colors  | Styles             |
	--------|--------------------|
	black   | bold               |
	red     | dark               |
	green   | underline          |
	yellow  | negative           |
	blue    | hide               |
	magenta |                    |
	cyan    |                    |
	white   |                    |

	Params  | Result             |
	--------|--------------------|
	bg_     | background         |
	lg_     | light              |
	bg_lg_  | background & Light |

	PythonColorize.colors.([param][style]_)[name]
	(.) Optional
	'''

	#Prefix
	prefix = '\033['
	nocolor = prefix + '0m'
	b  = 0
	r  = 1
	g  = 2
	y  = 3
	bl = 4
	m  = 5
	c  = 6
	w  = 7

	#Styles
	bold      = 1
	dark      = 2
	underline = 4
	negative  = 7
	hide      = 0

	#Styles >- Types
	color     = 30
	bg_color  = 40
	light     = 90
	bg_light  = 100

	#Colors
	black   = prefix + str(color + b) + 'm'
	red     = prefix + str(color + r) + 'm'
	green   = prefix + str(color + g) + 'm'
	yellow  = prefix + str(color + y) + 'm'
	blue    = prefix + str(color + bl) + 'm'
	magenta = prefix + str(color + m) + 'm'
	cyan    = prefix + str(color + c) + 'm'
	white   = prefix + str(color + w) + 'm'

	#Light Colors
	lg_black   = prefix + str(light + b) + 'm'
	lg_red     = prefix + str(light + r) + 'm'
	lg_green   = prefix + str(light + g) + 'm'
	lg_yellow  = prefix + str(light + y) + 'm'
	lg_blue    = prefix + str(light + bl) + 'm'
	lg_magenta = prefix + str(light + m) + 'm'
	lg_cyan    = prefix + str(light + c) + 'm'
	lg_white   = prefix + str(light + w) + 'm'

	#Background Colors
	bg_black   = prefix + str(bg_color + b) + 'm'
	bg_red     = prefix + str(bg_color + r) + 'm'
	bg_green   = prefix + str(bg_color + g) + 'm'
	bg_yellow  = prefix + str(bg_color + y) + 'm'
	bg_blue    = prefix + str(bg_color + bl) + 'm'
	bg_magenta = prefix + str(bg_color + m) + 'm'
	bg_cyan    = prefix + str(bg_color + c) + 'm'
	bg_white   = prefix + str(bg_color + w) + 'm'

	#Background Light Colors
	bg_lg_black   = prefix + str(bg_light + b) + 'm'
	bg_lg_red     = prefix + str(bg_light + r) + 'm'
	bg_lg_green   = prefix + str(bg_light + g) + 'm'
	bg_lg_yellow  = prefix + str(bg_light + y) + 'm'
	bg_lg_blue    = prefix + str(bg_light + bl) + 'm'
	bg_lg_magenta = prefix + str(bg_light + m) + 'm'
	bg_lg_cyan    = prefix + str(bg_light + c) + 'm'
	bg_lg_white   = prefix + str(bg_light + w) + 'm'

	#Color [ bold ]
	bold_black   = prefix + str(bold) + ';' + str(color + b) + 'm'
	bold_red     = prefix + str(bold) + ';' + str(color + r) + 'm'
	bold_green   = prefix + str(bold) + ';' + str(color + g) + 'm'
	bold_yellow  = prefix + str(bold) + ';' + str(color + y) + 'm'
	bold_blue    = prefix + str(bold) + ';' + str(color + bl) + 'm'
	bold_magenta = prefix + str(bold) + ';' + str(color + m) + 'm'
	bold_cyan    = prefix + str(bold) + ';' + str(color + c) + 'm'
	bold_white   = prefix + str(bold) + ';' + str(color + w) + 'm'

	#Light Colors [ bold ]
	lg_bold_black   = prefix + str(bold) + ';' + str(light + b) + 'm'
	lg_bold_red     = prefix + str(bold) + ';' + str(light + r) + 'm'
	lg_bold_green   = prefix + str(bold) + ';' + str(light + g) + 'm'
	lg_bold_yellow  = prefix + str(bold) + ';' + str(light + y) + 'm'
	lg_bold_blue    = prefix + str(bold) + ';' + str(light + bl) + 'm'
	lg_bold_magenta = prefix + str(bold) + ';' + str(light + m) + 'm'
	lg_bold_cyan    = prefix + str(bold) + ';' + str(light + c) + 'm'
	lg_bold_white   = prefix + str(bold) + ';' + str(light + w) + 'm'

	#Background Colors [ bold ]
	bg_bold_black   = prefix + str(bold) + ';' + str(bg_color + b) + 'm'
	bg_bold_red     = prefix + str(bold) + ';' + str(bg_color + r) + 'm'
	bg_bold_green   = prefix + str(bold) + ';' + str(bg_color + g) + 'm'
	bg_bold_yellow  = prefix + str(bold) + ';' + str(bg_color + y) + 'm'
	bg_bold_blue    = prefix + str(bold) + ';' + str(bg_color + bl) + 'm'
	bg_bold_magenta = prefix + str(bold) + ';' + str(bg_color + m) + 'm'
	bg_bold_cyan    = prefix + str(bold) + ';' + str(bg_color + c) + 'm'
	bg_bold_white   = prefix + str(bold) + ';' + str(bg_color + w) + 'm'

	#Background Light Colors [ bold ]
	bg_lg_bold_black   = prefix + str(bold) + ';' + str(bg_light + b) + 'm'
	bg_lg_bold_red     = prefix + str(bold) + ';' + str(bg_light + r) + 'm'
	bg_lg_bold_green   = prefix + str(bold) + ';' + str(bg_light + g) + 'm'
	bg_lg_bold_yellow  = prefix + str(bold) + ';' + str(bg_light + y) + 'm'
	bg_lg_bold_blue    = prefix + str(bold) + ';' + str(bg_light + bl) + 'm'
	bg_lg_bold_magenta = prefix + str(bold) + ';' + str(bg_light + m) + 'm'
	bg_lg_bold_cyan    = prefix + str(bold) + ';' + str(bg_light + c) + 'm'
	bg_lg_bold_white   = prefix + str(bold) + ';' + str(bg_light + w) + 'm'

	#Color [ dark ]
	dark_black   = prefix + str(dark) + ';' + str(color + b) + 'm'
	dark_red     = prefix + str(dark) + ';' + str(color + r) + 'm'
	dark_green   = prefix + str(dark) + ';' + str(color + g) + 'm'
	dark_yellow  = prefix + str(dark) + ';' + str(color + y) + 'm'
	dark_blue    = prefix + str(dark) + ';' + str(color + bl) + 'm'
	dark_magenta = prefix + str(dark) + ';' + str(color + m) + 'm'
	dark_cyan    = prefix + str(dark) + ';' + str(color + c) + 'm'
	dark_white   = prefix + str(dark) + ';' + str(color + w) + 'm'

	#Light Colors [ dark ]
	lg_dark_black   = prefix + str(dark) + ';' + str(light + b) + 'm'
	lg_dark_red     = prefix + str(dark) + ';' + str(light + r) + 'm'
	lg_dark_green   = prefix + str(dark) + ';' + str(light + g) + 'm'
	lg_dark_yellow  = prefix + str(dark) + ';' + str(light + y) + 'm'
	lg_dark_blue    = prefix + str(dark) + ';' + str(light + bl) + 'm'
	lg_dark_magenta = prefix + str(dark) + ';' + str(light + m) + 'm'
	lg_dark_cyan    = prefix + str(dark) + ';' + str(light + c) + 'm'
	lg_dark_white   = prefix + str(dark) + ';' + str(light + w) + 'm'

	#Background Colors [ dark ]
	bg_dark_black   = prefix + str(dark) + ';' + str(bg_color + b) + 'm'
	bg_dark_red     = prefix + str(dark) + ';' + str(bg_color + r) + 'm'
	bg_dark_green   = prefix + str(dark) + ';' + str(bg_color + g) + 'm'
	bg_dark_yellow  = prefix + str(dark) + ';' + str(bg_color + y) + 'm'
	bg_dark_blue    = prefix + str(dark) + ';' + str(bg_color + bl) + 'm'
	bg_dark_magenta = prefix + str(dark) + ';' + str(bg_color + m) + 'm'
	bg_dark_cyan    = prefix + str(dark) + ';' + str(bg_color + c) + 'm'
	bg_dark_white   = prefix + str(dark) + ';' + str(bg_color + w) + 'm'

	#Background Light Colors [ dark ]
	bg_lg_dark_black   = prefix + str(dark) + ';' + str(bg_light + b) + 'm'
	bg_lg_dark_red     = prefix + str(dark) + ';' + str(bg_light + r) + 'm'
	bg_lg_dark_green   = prefix + str(dark) + ';' + str(bg_light + g) + 'm'
	bg_lg_dark_yellow  = prefix + str(dark) + ';' + str(bg_light + y) + 'm'
	bg_lg_dark_blue    = prefix + str(dark) + ';' + str(bg_light + bl) + 'm'
	bg_lg_dark_magenta = prefix + str(dark) + ';' + str(bg_light + m) + 'm'
	bg_lg_dark_cyan    = prefix + str(dark) + ';' + str(bg_light + c) + 'm'
	bg_lg_dark_white   = prefix + str(dark) + ';' + str(bg_light + w) + 'm'

	#Color [ underline ]
	underline_black   = prefix + str(underline) + ';' + str(color + b) + 'm'
	underline_red     = prefix + str(underline) + ';' + str(color + r) + 'm'
	underline_green   = prefix + str(underline) + ';' + str(color + g) + 'm'
	underline_yellow  = prefix + str(underline) + ';' + str(color + y) + 'm'
	underline_blue    = prefix + str(underline) + ';' + str(color + bl) + 'm'
	underline_magenta = prefix + str(underline) + ';' + str(color + m) + 'm'
	underline_cyan    = prefix + str(underline) + ';' + str(color + c) + 'm'
	underline_white   = prefix + str(underline) + ';' + str(color + w) + 'm'

	#Light Colors [ underline ]
	lg_underline_black   = prefix + str(underline) + ';' + str(light + b) + 'm'
	lg_underline_red     = prefix + str(underline) + ';' + str(light + r) + 'm'
	lg_underline_green   = prefix + str(underline) + ';' + str(light + g) + 'm'
	lg_underline_yellow  = prefix + str(underline) + ';' + str(light + y) + 'm'
	lg_underline_blue    = prefix + str(underline) + ';' + str(light + bl) + 'm'
	lg_underline_magenta = prefix + str(underline) + ';' + str(light + m) + 'm'
	lg_underline_cyan    = prefix + str(underline) + ';' + str(light + c) + 'm'
	lg_underline_white   = prefix + str(underline) + ';' + str(light + w) + 'm'

	#Background Colors [ underline ]
	bg_underline_black   = prefix + str(underline) + ';' + str(bg_color + b) + 'm'
	bg_underline_red     = prefix + str(underline) + ';' + str(bg_color + r) + 'm'
	bg_underline_green   = prefix + str(underline) + ';' + str(bg_color + g) + 'm'
	bg_underline_yellow  = prefix + str(underline) + ';' + str(bg_color + y) + 'm'
	bg_underline_blue    = prefix + str(underline) + ';' + str(bg_color + bl) + 'm'
	bg_underline_magenta = prefix + str(underline) + ';' + str(bg_color + m) + 'm'
	bg_underline_cyan    = prefix + str(underline) + ';' + str(bg_color + c) + 'm'
	bg_underline_white   = prefix + str(underline) + ';' + str(bg_color + w) + 'm'

	#Background Light Colors [ underline ]
	bg_lg_underline_black   = prefix + str(underline) + ';' + str(bg_light + b) + 'm'
	bg_lg_underline_red     = prefix + str(underline) + ';' + str(bg_light + r) + 'm'
	bg_lg_underline_green   = prefix + str(underline) + ';' + str(bg_light + g) + 'm'
	bg_lg_underline_yellow  = prefix + str(underline) + ';' + str(bg_light + y) + 'm'
	bg_lg_underline_blue    = prefix + str(underline) + ';' + str(bg_light + bl) + 'm'
	bg_lg_underline_magenta = prefix + str(underline) + ';' + str(bg_light + m) + 'm'
	bg_lg_underline_cyan    = prefix + str(underline) + ';' + str(bg_light + c) + 'm'
	bg_lg_underline_white   = prefix + str(underline) + ';' + str(bg_light + w) + 'm'

	#Color [ negative ]
	negative_black   = prefix + str(negative) + ';' + str(color + b) + 'm'
	negative_red     = prefix + str(negative) + ';' + str(color + r) + 'm'
	negative_green   = prefix + str(negative) + ';' + str(color + g) + 'm'
	negative_yellow  = prefix + str(negative) + ';' + str(color + y) + 'm'
	negative_blue    = prefix + str(negative) + ';' + str(color + bl) + 'm'
	negative_magenta = prefix + str(negative) + ';' + str(color + m) + 'm'
	negative_cyan    = prefix + str(negative) + ';' + str(color + c) + 'm'
	negative_white   = prefix + str(negative) + ';' + str(color + w) + 'm'

	#Light Colors [ negative ]
	lg_negative_black   = prefix + str(negative) + ';' + str(light + b) + 'm'
	lg_negative_red     = prefix + str(negative) + ';' + str(light + r) + 'm'
	lg_negative_green   = prefix + str(negative) + ';' + str(light + g) + 'm'
	lg_negative_yellow  = prefix + str(negative) + ';' + str(light + y) + 'm'
	lg_negative_blue    = prefix + str(negative) + ';' + str(light + bl) + 'm'
	lg_negative_magenta = prefix + str(negative) + ';' + str(light + m) + 'm'
	lg_negative_cyan    = prefix + str(negative) + ';' + str(light + c) + 'm'
	lg_negative_white   = prefix + str(negative) + ';' + str(light + w) + 'm'

	#Background Colors [ negative ]
	bg_negative_black   = prefix + str(negative) + ';' + str(bg_color + b) + 'm'
	bg_negative_red     = prefix + str(negative) + ';' + str(bg_color + r) + 'm'
	bg_negative_green   = prefix + str(negative) + ';' + str(bg_color + g) + 'm'
	bg_negative_yellow  = prefix + str(negative) + ';' + str(bg_color + y) + 'm'
	bg_negative_blue    = prefix + str(negative) + ';' + str(bg_color + bl) + 'm'
	bg_negative_magenta = prefix + str(negative) + ';' + str(bg_color + m) + 'm'
	bg_negative_cyan    = prefix + str(negative) + ';' + str(bg_color + c) + 'm'
	bg_negative_white   = prefix + str(negative) + ';' + str(bg_color + w) + 'm'

	#Background Light Colors [ negative ]
	bg_lg_negative_black   = prefix + str(negative) + ';' + str(bg_light + b) + 'm'
	bg_lg_negative_red     = prefix + str(negative) + ';' + str(bg_light + r) + 'm'
	bg_lg_negative_green   = prefix + str(negative) + ';' + str(bg_light + g) + 'm'
	bg_lg_negative_yellow  = prefix + str(negative) + ';' + str(bg_light + y) + 'm'
	bg_lg_negative_blue    = prefix + str(negative) + ';' + str(bg_light + bl) + 'm'
	bg_lg_negative_magenta = prefix + str(negative) + ';' + str(bg_light + m) + 'm'
	bg_lg_negative_cyan    = prefix + str(negative) + ';' + str(bg_light + c) + 'm'
	bg_lg_negative_white   = prefix + str(negative) + ';' + str(bg_light + w) + 'm'

	#Color [ hide ]
	hide_black   = prefix + str(hide) + ';' + str(color + b) + 'm'
	hide_red     = prefix + str(hide) + ';' + str(color + r) + 'm'
	hide_green   = prefix + str(hide) + ';' + str(color + g) + 'm'
	hide_yellow  = prefix + str(hide) + ';' + str(color + y) + 'm'
	hide_blue    = prefix + str(hide) + ';' + str(color + bl) + 'm'
	hide_magenta = prefix + str(hide) + ';' + str(color + m) + 'm'
	hide_cyan    = prefix + str(hide) + ';' + str(color + c) + 'm'
	hide_white   = prefix + str(hide) + ';' + str(color + w) + 'm'

	#Light Colors [ hide ]
	lg_hide_black   = prefix + str(hide) + ';' + str(light + b) + 'm'
	lg_hide_red     = prefix + str(hide) + ';' + str(light + r) + 'm'
	lg_hide_green   = prefix + str(hide) + ';' + str(light + g) + 'm'
	lg_hide_yellow  = prefix + str(hide) + ';' + str(light + y) + 'm'
	lg_hide_blue    = prefix + str(hide) + ';' + str(light + bl) + 'm'
	lg_hide_magenta = prefix + str(hide) + ';' + str(light + m) + 'm'
	lg_hide_cyan    = prefix + str(hide) + ';' + str(light + c) + 'm'
	lg_hide_white   = prefix + str(hide) + ';' + str(light + w) + 'm'

	#Background Colors [ hide ]
	bg_hide_black   = prefix + str(hide) + ';' + str(bg_color + b) + 'm'
	bg_hide_red     = prefix + str(hide) + ';' + str(bg_color + r) + 'm'
	bg_hide_green   = prefix + str(hide) + ';' + str(bg_color + g) + 'm'
	bg_hide_yellow  = prefix + str(hide) + ';' + str(bg_color + y) + 'm'
	bg_hide_blue    = prefix + str(hide) + ';' + str(bg_color + bl) + 'm'
	bg_hide_magenta = prefix + str(hide) + ';' + str(bg_color + m) + 'm'
	bg_hide_cyan    = prefix + str(hide) + ';' + str(bg_color + c) + 'm'
	bg_hide_white   = prefix + str(hide) + ';' + str(bg_color + w) + 'm'

	#Background Light Colors [ hide ]
	bg_lg_hide_black   = prefix + str(hide) + ';' + str(bg_light + b) + 'm'
	bg_lg_hide_red     = prefix + str(hide) + ';' + str(bg_light + r) + 'm'
	bg_lg_hide_green   = prefix + str(hide) + ';' + str(bg_light + g) + 'm'
	bg_lg_hide_yellow  = prefix + str(hide) + ';' + str(bg_light + y) + 'm'
	bg_lg_hide_blue    = prefix + str(hide) + ';' + str(bg_light + bl) + 'm'
	bg_lg_hide_magenta = prefix + str(hide) + ';' + str(bg_light + m) + 'm'
	bg_lg_hide_cyan    = prefix + str(hide) + ';' + str(bg_light + c) + 'm'
	bg_lg_hide_white   = prefix + str(hide) + ';' + str(bg_light + w) + 'm'

def colorize(text=None, color=None, style=None, light=None, background=None):
	'''
	Colors  | Styles             |
	--------|--------------------|
	black   | bold               |
	red     | dark               |
	green   | underline          |
	yellow  | negative           |
	blue    | hide               |
	magenta |                    |
	cyan    |                    |
	white   |                    |

	PythonColorize.colorize(text=[text], color=[color], style=[style], light=[True|False], background=[True|False])
	'''

	param = colors.color
	param_color = 7
	param_style = 0
	if text == None:
		text = ''
		
	if color:
		if color == 'black':
			param_color = colors.b
		elif color == 'red':
			param_color = colors.r
		elif color == 'green':
			param_color = colors.g
		elif color == 'yellow':
			param_color = colors.y
		elif color == 'blue':
			param_color = colors.bl
		elif color == 'magenta':
			param_color = colors.m
		elif color == 'cyan':
			param_color = colors.c
		elif color == 'white':
			param_color = colors.w
		else:
			param_color = color

	if style:
		if style == 'bold':
			param_style = colors.bold
		elif style == 'dark':
			param_style = colors.dark
		elif style == 'underline':
			param_style = colors.underline
		elif style == 'negative':
			param_style = colors.negative
		elif param_style == 'hide':
			param_style == colors.hide
		else:
			param_style = style

	if light:
		if background:
			param = colors.bg_light
		else:
			param = colors.light
	elif background:
		param = colors.bg_color

	apply_text = '{n1}{text}{n2}'.format(n1=colors.prefix + str(param_style) +\
										';' + str(param + param_color) + 'm',
										text=text, n2=colors.nocolor)

	return apply_text
