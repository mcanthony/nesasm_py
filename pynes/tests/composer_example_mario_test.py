# -*- coding: utf-8 -*-

import unittest

from pynes.tests import ComposerTestCase

class ComposerMarioTest(ComposerTestCase):

    def test_mario(self):
        self.path = 'fixtures/nesasm/scrolling/'
        f = open('pynes/examples/mario.py')
        code = f.read()
        f.close()
        (
            self.assert_asm_from(code)
                .has('.bank 0')
                .and_then('WAITVBLANK:')
                .and_then('RESET:')
                .and_then('JSR WAITVBLANK')
                .and_then('CLEARMEM:')
                .and_then('JSR WAITVBLANK')
                .and_then('LoadPalettes:')
                #TODO: why? .and_then('LDA #%10000000') #just nmi
                .and_then('STA $2000')
                #TODO: why? .and_then('LDA #%00010000') #just sprite
                .and_then('STA $2001')

                .and_then('NMI:')
                .and_then('.bank 1')
                .and_then('palette:')
                .and_then('tinymario:')
                .and_then('mario:')
        )