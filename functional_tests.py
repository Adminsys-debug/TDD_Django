#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 21:51
# @Author  : mr.chen
# @File    : functional_tests
# @Software: PyCharm
# @Email   : 794281961@qq.com

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.br = webdriver.Chrome()
        # 隐式等待3s
        self.br.implicitly_wait(3)

    def tearDown(self):
        self.br.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.br.get("http://localhost:8000")
        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.br.title)
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings="ignore")
