# ==================================================
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : KimHuang
# @Organization : SDUST
# @E-mail: kim.huang.j@qq.com
# @Site : 
# @Time : 2021/5/12 21:07
# @File : update_package.py
# @Software: PyCharm
# @Desc : 
# ==================================================

import pkg_resources
from subprocess import call

for packages in [dist.project_name for dist in pkg_resources.working_set]:
    call("pip3 install --upgrade " + ''.join(packages) + ' --user', shell=True)
