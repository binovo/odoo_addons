# -*- coding: utf-8 -*-
# (C) 2020 Smile (<https://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


def s2human(time):
    """
    Copy from https://github.com/odoo/odoo-extra/blob/master/runbot/runbot.py
    """
    for delay, desc in [(86400, 'd'), (3600, 'h'), (60, 'm')]:
        if time >= delay:
            return str(int(time / delay)) + desc
    return str(int(time)) + "s"
