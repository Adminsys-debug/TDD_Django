#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 21:51
# @Author  : mr.chen
# @File    : functional_tests
# @Software: PyCharm
# @Email   : 794281961@qq.com

from selenium import webdriver
import pytest

br = webdriver.Chrome()
br.get("http://localhost:8000")
assert 'Django' in br.title
br.quit()


