# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('affinitic.core')


def installCore(context):
    if context.readDataFile('affinitic.core-default.txt') is None:
        return

    logger.info('Installing affinitic.core')
