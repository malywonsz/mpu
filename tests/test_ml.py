#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

# core modules
import unittest

# internal modules
import mpu.ml


class MLTest(unittest.TestCase):

    def test_negative_class_number(self):
        with self.assertRaises(ValueError):
            mpu.ml.indices2one_hot([0, 1, 1], 0)