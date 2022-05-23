import unittest

from src.japverbconj.constants.enumerated_types import Polarity, Tense, VerbClass
from src.japverbconj.constants.particle_constants import KU_PARTICLE
from src.japverbconj.decorators import *
from src.japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg

from .constants import (
    GodanVerbNomu,
    english_with_japanese,
    korean_with_japanese,
    verb_incorrect_particle_ending,
)


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.verb_class = VerbClass.GODAN

    def test_validate_japanese_verb_invalid_length(self):
        with self.assertRaises(InvalidJapaneseVerbLengthError) as expected_exception:
            jvfg.generate_plain_form(
                KU_PARTICLE, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expected_exception.exception),
            "('Invalid Japanese Verb Length', 1, '" + KU_PARTICLE + "')",
        )

    def test_validate_japanese_verb_invalid_japanese_verb_ending(self):
        with self.assertRaises(InvalidJapaneseVerbEndingError) as expected_exception:
            jvfg.generate_plain_form(
                verb_incorrect_particle_ending,
                VerbClass.GODAN,
                Tense.PAST,
                Polarity.NEGATIVE,
            )
        self.assertEqual(
            str(expected_exception.exception),
            "('Invalid Japanese Verb Ending Particle', '"
            + verb_incorrect_particle_ending[-1:]
            + "')",
        )

    def test_validate_japanese_verb_contains_korean_characters(self):
        with self.assertRaises(NonJapaneseCharacterError) as expected_exception:
            jvfg.generate_plain_form(
                korean_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expected_exception.exception),
            "('Non-Japanese Character Found', '" + korean_with_japanese + "')",
        )

    def test_validate_japanese_verb_contains_english_characters(self):
        with self.assertRaises(NonJapaneseCharacterError) as expected_exception:
            jvfg.generate_plain_form(
                english_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE
            )
        self.assertEqual(
            str(expected_exception.exception),
            "('Non-Japanese Character Found', '" + english_with_japanese + "')",
        )

    def test_validate_japanese_verb_valid_verb(self):
        result = jvfg.generate_plain_form(
            GodanVerbNomu.verb,
            GodanVerbNomu.verb_class,
            Tense.NONPAST,
            Polarity.POSITIVE,
        )
        self.assertEqual(result, GodanVerbNomu.verb)


if __name__ == "__main__":
    unittest.main()
