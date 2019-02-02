import unittest

from src.JapaneseVerbFormGenerator import JapaneseVerbFormGenerator
from src.Decorators import *
from src.constants.EnumeratedTypes import VerbClass, Tense, Polarity
from src.constants.ParticleConstants import CHISAI_TSU_PARTICLE, KU_PARTICLE, GU_PARTICLE, SU_PARTICLE, U_PARTICLE, TSU_PARTICLE, TA_PARTICLE, DA_PARTICLE, PU_PARTICLE

from TestConstants import GodanVerbNomu, korean_with_japanese, english_with_japanese, verb_incorrect_particle_ending

class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.verb_class = VerbClass.GODAN
        self.japaneseVerbFormGenerator = JapaneseVerbFormGenerator()

    def test_validateJapaneseVerbDecorator_InvalidLength(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(KU_PARTICLE, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE)
        self.assertEqual(str(expectedException.exception), '(\'Invalid Japanese Verb Length\', 1, \'' + KU_PARTICLE + '\')')
        
    # "Invalid Japanese Verb Ending Particle", verb[-1:]
    def test_validateJapaneseVerbDecorator_InvalidJapaneseEndingParticle(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(verb_incorrect_particle_ending, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE)
        self.assertEqual(str(expectedException.exception), '(\'Invalid Japanese Verb Ending Particle\', \'' + verb_incorrect_particle_ending[-1:] + '\')')

    def test_validateJapaneseVerbDecorator_ContainsKoreanCharacters(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(korean_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE)
        self.assertEqual(str(expectedException.exception), '(\'Non-Japanese Character Found\', \'' + korean_with_japanese + '\')')

    def test_validateJapaneseVerbDecorator_ContainsEnglishCharacters(self):
        with self.assertRaises(Exception) as expectedException:
            self.japaneseVerbFormGenerator.generate_plain_form(english_with_japanese, VerbClass.GODAN, Tense.PAST, Polarity.NEGATIVE)
        self.assertEqual(str(expectedException.exception), '(\'Non-Japanese Character Found\', \'' + english_with_japanese + '\')')

    def test_validateJapaneseVerbDecorator_ValidVerb(self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(GodanVerbNomu.Verb, GodanVerbNomu.Verb_Class, Tense.NONPAST, Polarity.POSITIVE)
        self.assertEqual(result, GodanVerbNomu.Verb)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UtilsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)