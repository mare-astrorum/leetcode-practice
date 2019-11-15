"""
https://leetcode.com/problems/defanging-an-ip-address/
"""

address = "255.100.50.0"
address = "1.1.1.0"

import re

check_num = re.findall("\d+", address)
check_dots = re.findall("\.", address)
if len(check_num) == 4 and len(check_dots) == 3:
    print(address.replace(".", "[.]"))

re.template("255.100.50.0")
re.findall("\d+", address)
re.search("[0-9].[0-9].[0-9].[0-9]", address)
