import unittest

from japverbgen.constants.enumerated_types import Polarity, Tense, VerbClass
from japverbgen.constants.particle_constants import (
    CHISAI_TSU_PARTICLE,
    DA_PARTICLE,
    GU_PARTICLE,
    KU_PARTICLE,
    PU_PARTICLE,
    SU_PARTICLE,
    TA_PARTICLE,
    TSU_PARTICLE,
    U_PARTICLE,
)
from japverbgen.decorators import *
from japverbgen.verb_form_gen import JapaneseVerbFormGenerator
from TestConstants import (
    GodanVerbNomu,
    english_with_japanese,
    korean_with_japanese,
    verb_incorrect_particle_ending,
)


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.verb_class = VerbClass.GODAN
        self.japaneseVerbFormGenerator = JapaneseVerbFormGenerator()

    def test_validateJapaneseVerbDecorator_InvalidLength(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(
                KU_PARTICLE, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Invalid Japanese Verb Length', 1, '" + KU_PARTICLE + "')",
        )

    # "Invalid Japanese Verb Ending Particle", verb[-1:]
    def test_validateJapaneseVerbDecorator_InvalidJapaneseEndingParticle(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(
                verb_incorrect_particle_ending,
                VerbClass.GODAN,
                Tense.PAST,
                Polarity.NEGATIVE,
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Invalid Japanese Verb Ending Particle', '"
            + verb_incorrect_particle_ending[-1:]
            + "')",
        )

    def test_validateJapaneseVerbDecorator_ContainsKoreanCharacters(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(
                korean_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Non-Japanese Character Found', '" + korean_with_japanese + "')",
        )

    def test_validateJapaneseVerbDecorator_ContainsEnglishCharacters(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(
                english_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Non-Japanese Character Found', '" + english_with_japanese + "')",
        )

    def test_validateJapaneseVerbDecorator_ValidVerb(self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(
            GodanVerbNomu.Verb,
            GodanVerbNomu.Verb_Class,
            Tense.NONPAST,
            Polarity.POSITIVE,
        )
        self.assertEqual(result, GodanVerbNomu.Verb)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UtilsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
