# [VPYTHON:BEGIN]
# wheel: <
#   name: "infra/python/wheels/yapf-py2_py3"
#   version: "version:0.27.0"
# >
# wheel: <
#   name: "infra/python/wheels/futures-py2_py3"
#   version: "version:3.1.1"
# >
# [VPYTHON:END]

# -*- coding: utf-8 -*-
import re
import sys

from yapf import run_main

if __name__ == '__main__':
    sys.exit(run_main())
