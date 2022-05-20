import unittest

from .constants import english_with_japanese
from .constants import GodanVerbNomu
from .constants import korean_with_japanese
from .constants import verb_incorrect_particle_ending
from src.japverbconj.constants.enumerated_types import Polarity
from src.japverbconj.constants.enumerated_types import Tense
from src.japverbconj.constants.enumerated_types import VerbClass
from src.japverbconj.constants.particle_constants import KU_PARTICLE
from src.japverbconj.decorators import *
from src.japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.verb_class = VerbClass.GODAN

    def test_validateJapaneseVerbDecorator_InvalidLength(self):
        with self.assertRaises(Exception) as expectedException:
            jvfg.generate_plain_form(
                KU_PARTICLE, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Invalid Japanese Verb Length', 1, '" + KU_PARTICLE + "')",
        )

    # "Invalid Japanese Verb Ending Particle", verb[-1:]
    def test_validateJapaneseVerbDecorator_InvalidJapaneseEndingParticle(self):
        with self.assertRaises(Exception) as expectedException:
            jvfg.generate_plain_form(
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
            jvfg.generate_plain_form(
                korean_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Non-Japanese Character Found', '" + korean_with_japanese + "')",
        )

    def test_validateJapaneseVerbDecorator_ContainsEnglishCharacters(self):
        with self.assertRaises(Exception) as expectedException:
            jvfg.generate_plain_form(
                english_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expectedException.exception),
            "('Non-Japanese Character Found', '" + english_with_japanese + "')",
        )

    def test_validateJapaneseVerbDecorator_ValidVerb(self):
        result = jvfg.generate_plain_form(
            GodanVerbNomu.Verb,
            GodanVerbNomu.Verb_Class,
            Tense.NONPAST,
            Polarity.POSITIVE,
        )
        self.assertEqual(result, GodanVerbNomu.Verb)


if __name__ == "__main__":
    unittest.main()
