# -*- coding: utf-8 -*-

import unittest

from nesasm.compiler import lexical, syntax, semantic


class RtiTest(unittest.TestCase):

    def test_rti_sngl(self):
        tokens = list(lexical('RTI'))
        self.assertEquals(1, len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        ast = syntax(tokens)
        self.assertEquals(1, len(ast))
        self.assertEquals('S_IMPLIED', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x40])