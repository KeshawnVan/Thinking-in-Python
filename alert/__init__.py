#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

a = "1000025:iHR5DffcRLuOSfZUU5eYgSfQkR8PyOBYKb3-v0eOLkg"
b = base64.b64encode(a.encode('utf-8'))
print(str(b,'utf-8'))