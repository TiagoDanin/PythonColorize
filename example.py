#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import PythonColorize as _
print('{}Test{}'.format(_.colors.red, _.colors.nocolor))
print(_.colorize(text='Test', color='red', light=True))

from PythonColorize import *
print('{}Test{}'.format(colors.blue, colors.nocolor))
print(colorize(text='Test', color='blue', light=True))
