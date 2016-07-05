#!/usr/bin/env python3
# setup.py

from distutils.core import setup

setup(name='PythonColorize',
		version ='0.2',
		description = 'Simple module to colorize text on terminal',
		long_description = '''
		PythonColorize
		==============

		Simple module to colorize text on terminal

		Install ::

			sudo pip3 install PythonColorize

		DOC
		===

		Colors  | Styles
		--------|--------------------
		black   | bold
		red     | dark
		green   | underline
		yellow  | negative
		blue    | hide
		magenta |
		cyan    |
		white   |

		Params  | Result
		--------|--------------------
		bg_     | background
		lg_     | light
		bg_lg_  | background & Light

		Module function
		===============

		Get color ::

			PythonColorize.colors.<[param][style]_>[name]

		<.> Optional

		Colorize ::

			PythonColorize.colorize(text=[text], color=[color], style=[style], light=[True|False], background=[True|False])
		''',
		author = 'Tiago Danin',
		author_email = 'TiagoDanin@outlook.com',
		license = 'GPLv3',
		url = 'https://TiagoDanin.github.io/PythonColorize/',
		py_modules = ['PythonColorize'],
		classifiers = [
			'Development Status :: 4 - Beta',
			'Environment :: Console',
			'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			'Natural Language :: English',
			'Operating System :: MacOS',
			'Operating System :: Unix',
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.0',
			'Programming Language :: Python :: 3.1',
			'Programming Language :: Python :: 3.2',
			'Programming Language :: Python :: 3.3',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: 3.5',
			'Topic :: Software Development :: Libraries :: Python Modules',
			'Topic :: System :: Shells',
			'Topic :: Terminals',
			'Topic :: Utilities',
		],
		keywords = 'shell terminal python3 python2 color colorize',)
