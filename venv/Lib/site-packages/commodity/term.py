# -*- coding:utf-8; tab-width:4; mode:python -*-

# FIXME: blessings supersedes this module

ESC = chr(27)

BOLD = HIGH = ESC + '[1m'
NORM = ESC + '[m'
CLS = ESC + '[2J' + ESC + '[0;0f'

GREY   = ESC + '[38m'
RED    = ESC + '[31m'
PURPLE = ESC + '[95m'
GREEN  = ESC + '[32m'

LIGHT_RED      = ESC + '[1;91m'
LIGHT_RED_BG   = ESC + '[7;91m'
LIGHT_GREEN_BG = ESC + '[7;32m'
