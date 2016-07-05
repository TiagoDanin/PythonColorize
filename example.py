#!/usr/bin/env python
# -*- coding:utf-8 -*-
import PythonColorize as _
print('{}Test\t1{}'.format(_.colors.red, _.colors.nocolor))
print(_.colorize(text='Test\t2', color='blue', light=True, background=True))
print(_.colorize(text='Test\t3', color='green', light=False, background=True))
print(_.colorize(text='Test\t4', color='white', light=True, background=False))

from PythonColorize import *
print('{}Test\t5{}'.format(colors.blue, colors.nocolor))
print(colorize(text='Test\t6', color='blue', light=True, background=True))
print(colorize(text='Test\t7', color='green', light=False, background=True))
print(colorize(text='Test\t8', color='white', light=True, background=False))
