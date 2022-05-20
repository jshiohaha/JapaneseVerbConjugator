import unittest

from src.constants.particle_constants import (
    CHISAI_TSU_PARTICLE,
    DA_PARTICLE,
    GU_PARTICLE,
    KU_PARTICLE,
    SU_PARTICLE,
    TA_PARTICLE,
    TSU_PARTICLE,
    U_PARTICLE,
)
from src.utils import *
from TestConstants import (
    GodanVerbNomu,
    IchidanVerbTaberu,
    IrregularVerbKuru,
    IrregularVerbSuru,
)


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.verb_class = VerbClass.GODAN

    def test_handle_irregular_verb_non_irregular_verb_ending(self):
        result = handle_irregular_verb(GodanVerbNomu.Verb)
        # TODO: refactor to throw error
        self.assertIsNone(result)

    # all below this must be godan verb
    def test_base_te_ta_form_CHISAI_TSU(self):
        verb = "使う"
        result = base_te_ta_form(verb, self.verb_class, TA_PARTICLE, DA_PARTICLE)
        self.assertEqual(result, "使った")

    def test_base_te_ta_form_KU_PARTICLE(self):
        verb = "聞く"
        result = base_te_ta_form(verb, self.verb_class, TA_PARTICLE, DA_PARTICLE)
        self.assertEqual(result, "聞いた")

    def test_base_te_ta_form_GU_PARTICLE(self):
        verb = "泳ぐ"
        result = base_te_ta_form(verb, self.verb_class, TA_PARTICLE, DA_PARTICLE)
        self.assertEqual(result, "泳いだ")

    def test_base_te_ta_form_SU_PARTICLE(self):
        verb = "話す"
        result = base_te_ta_form(verb, self.verb_class, TA_PARTICLE, DA_PARTICLE)
        self.assertEqual(result, "話した")

    def test_map_dict_form_to_different_ending_U_PARTICLE(self):
        verb = "使う"
        result = map_dictionary_to_a_ending(verb)
        self.assertEqual(result, "使わ")

    def test_map_dict_form_to_different_ending_TSU_PARTICLE(self):
        verb = "立つ"
        result = map_dictionary_to_a_ending(verb)
        self.assertEqual(result, "立た")

    def test_map_dict_form_to_different_ending_SU_PARTICLE(self):
        verb = "話す"
        result = map_dictionary_to_a_ending(verb)
        self.assertEqual(result, "話さ")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UtilsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
