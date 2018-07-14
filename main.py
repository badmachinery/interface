# -*- coding: utf-8 -*-
import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import interface.builder as builder
from interface.interface import app

def main():
    builder.buildAll()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
