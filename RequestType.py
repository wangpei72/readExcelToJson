#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
from enum import Enum, unique


@unique
class RequestType(Enum):
    isHeader = 0
    isBody = 1
