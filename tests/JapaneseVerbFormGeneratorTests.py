import unittest

from src.JapaneseVerbFormGenerator import *
from src.constants.EnumeratedTypes import Polarity, Formality, VerbClass, Tense

from TestConstants import GodanVerbNomu, IchidanVerbTaberu, IrregularVerbSuru, IrregularVerbKuru

# https://github.com/audreyr/how-to/blob/master/python/use_coverage_with_unittest.rst
# https://github.com/audreyr/how-to/blob/master/python/use_coverage_with_unittest.rst#user-content-set-up-coveralls

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class

        Borrowed from https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases/
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.japaneseVerbFormGenerator = JapaneseVerbFormGenerator()
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

# ---------------------------------------------------------- #
#                    Positive Verb Form Tests                #
# ---------------------------------------------------------- #
class TestPositiveVerbForms(ParametrizedTestCase):
    ''' Tests for each positive verb conjugation form considering
    the permutations of tense and formality. Skipped Tests for 
    Irregular Positive Verbs include:

    - CausativePolitePositive
    - ConditionalPlain
    - ConditionalPolite
    - PassivePolitePositive
    - VolitionalPolitePositive

    This structure of class based test cases and inheriting from 
    ParametrizedTestCase allows testing of different verbs across
    different verb classes. To test a different verb, simply update
    the self.param arg passed to ParametrizedTestCase. 
    '''
    def setUp(self):
        self.polarity = Polarity.POSITIVE
        self.verb = self.param
    
    # Polite Verb Forms Test
    def test_polite_positive_nonpast(self):
        result = self.japaneseVerbFormGenerator.generate_polite_form(self.verb.Verb, self.verb.Verb_Class, Tense.NONPAST, self.polarity)
        self.assertEqual(result, self.verb.PolitePositiveNonpast)

    def test_polite_positive_past(self):
        result = self.japaneseVerbFormGenerator.generate_polite_form(self.verb.Verb, self.verb.Verb_Class, Tense.PAST, self.polarity)
        self.assertEqual(result, self.verb.PolitePositivePast)

    # Plain Verb Forms Test
    def test_plain_positive_nonpast(self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(self.verb.Verb, self.verb.Verb_Class, Tense.NONPAST, self.polarity)
        self.assertEqual(result, self.verb.Verb)

    def test_plain_positive_past (self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(self.verb.Verb, self.verb.Verb_Class, Tense.PAST, self.polarity)
        self.assertEqual(result, self.verb.PlainPositivePast)

    # Te Verb Form Test
    def test_te_form(self):
        result = self.japaneseVerbFormGenerator.generate_te_form(self.verb.Verb, self.verb.Verb_Class)
        self.assertEqual(result, self.verb.TeForm)

    # Conditional Verb Forms Test
    def test_conditional_plain(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_conditional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ConditionalPlain)

    def test_conditional_polite(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_conditional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ConditionalPolite)

    # Volitional Verb Forms Test
    def test_volitional_plain_positive(self):
        # if self.verb.Verb_Class == VerbClass.IRREGULAR:
        #     self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_volitional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.VolitionalPlainPositive)

    def test_volitional_polite_positive(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_volitional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.VolitionalPolitePositive)

    # Potential Verb Forms Test
    def test_potential_plain_positive(self):
        result = self.japaneseVerbFormGenerator.generate_potential_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.PotentialPlainPositive)

    def test_potential_polite_positive(self):
        result = self.japaneseVerbFormGenerator.generate_potential_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.PotentialPolitePositive)

    # Imperative Verb Forms Test
    def test_imperative_plain_positive(self):
        result = self.japaneseVerbFormGenerator.generate_imperative_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ImperativePlainPositive)

    def test_imperative_polite_positive(self):
        result = self.japaneseVerbFormGenerator.generate_imperative_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ImperativePolitePositive)

    # Provisional Verb Forms Test
    def test_provisional_plain_positive(self):
        result = self.japaneseVerbFormGenerator.generate_provisional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ProvisionalPlainPositive)

    def test_provisional_polite_positive(self):
        if self.verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_provisional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ProvisionalPolitePositive)

    # Causative Verb Forms Test
    def test_causative_plain_positive(self):
        result = self.japaneseVerbFormGenerator.generate_causative_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.CausativePlainPositive)

    def test_causative_polite_positive(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_causative_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.CausativePolitePositive)

    # Passive Verb Forms Test
    def test_passive_plain_positive(self):
        result = self.japaneseVerbFormGenerator.generate_passive_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.PassivePlainPositive)

    def test_passive_polite_positive(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_passive_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.PassivePolitePositive)

# ---------------------------------------------------------- #
#                    Negative Verb Form Tests                #
# ---------------------------------------------------------- #
class TestNegativeVerbForms(ParametrizedTestCase):
    ''' Tests for each negative verb conjugation form considering
    the permutations of tense and formality. Skipped Tests for 
    Irregular Negative Verbs include:

    - CausativePlainNegative for する verbs
    - CausativePoliteNegative for する verbs
    - PassivePlainNegative
    - PassivePoliteNegative
    - ProvisionalPoliteNegative

    This structure of class based test cases and inheriting from 
    ParametrizedTestCase allows testing of different verbs across
    different verb classes. To test a different verb, simply update
    the self.param arg passed to ParametrizedTestCase. 
    '''
    def setUp(self):
        self.polarity = Polarity.NEGATIVE
        self.verb = self.param

    # Formal Verb Forms Test
    def test_polite_negative_nonpast(self):
        result = self.japaneseVerbFormGenerator.generate_polite_form(self.verb.Verb, self.verb.Verb_Class, Tense.NONPAST, self.polarity)
        self.assertEqual(result, self.verb.PoliteNegativeNonpast)

    def test_polite_negative_past(self):
        result = self.japaneseVerbFormGenerator.generate_polite_form(self.verb.Verb, self.verb.Verb_Class, Tense.PAST, self.polarity)
        self.assertEqual(result, self.verb.PoliteNegativePast)

    # Plain Verb Forms Test
    def test_plain_negative_nonpast (self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(self.verb.Verb, self.verb.Verb_Class, Tense.NONPAST, self.polarity)
        self.assertEqual(result, self.verb.PlainNegativeNonpast)

    def test_plain_negative_past (self):
        result = self.japaneseVerbFormGenerator.generate_plain_form(self.verb.Verb, self.verb.Verb_Class, Tense.PAST, self.polarity)
        self.assertEqual(result, self.verb.PlainNegativePast)

    # Conditional Verb Forms Test
    def test_conditional_plain(self):
        if self.verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_conditional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ConditionalPlainNegative)

    def test_conditional_polite(self):
        if self.verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = self.japaneseVerbFormGenerator.generate_conditional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ConditionalPoliteNegative)

    # Volitional Verb Forms Test
    def test_volitional_plain_negative(self):
        result = self.japaneseVerbFormGenerator.generate_volitional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.VolitionalPlainNegative)

    def test_volitional_polite_negative(self):
        result = self.japaneseVerbFormGenerator.generate_volitional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.VolitionalPoliteNegative)

    # Potential Verb Forms Test
    def test_potential_plain_negative(self):
        result = self.japaneseVerbFormGenerator.generate_potential_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.PotentialPlainNegative)

    def test_potential_polite_negative(self):
        result = self.japaneseVerbFormGenerator.generate_potential_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.PotentialPoliteNegative)

    # Imperative Verb Forms Test
    def test_imperative_plain_negative(self):
        result = self.japaneseVerbFormGenerator.generate_imperative_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ImperativePlainNegative)

    def test_imperative_polite_negative(self):
        result = self.japaneseVerbFormGenerator.generate_imperative_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ImperativePoliteNegative)

    # Provisional Verb Forms Test
    def test_provisional_plain_negative(self):
        result = self.japaneseVerbFormGenerator.generate_provisional_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.ProvisionalPlainNegative)

    def test_provisional_polite_negative(self):
        if self.verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not required for non-irregular verbs")
        result = self.japaneseVerbFormGenerator.generate_provisional_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.ProvisionalPoliteNegative)

    # Causative Verb Forms Test
    def test_causative_plain_negative(self):
        if self.verb.Verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = self.japaneseVerbFormGenerator.generate_causative_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.CausativePlainNegative)

    def test_causative_polite_negative(self):
        if self.verb.Verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = self.japaneseVerbFormGenerator.generate_causative_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.CausativePoliteNegative)

    # Passive Verb Forms Test
    def test_passive_plain_negative(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not required for irregular verbs")
        result = self.japaneseVerbFormGenerator.generate_passive_form(self.verb.Verb, self.verb.Verb_Class, Formality.PLAIN, self.polarity)
        self.assertEqual(result, self.verb.PassivePlainNegative)

    def test_passive_polite_negative(self):
        if self.verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not required for irregular verbs")
        result = self.japaneseVerbFormGenerator.generate_passive_form(self.verb.Verb, self.verb.Verb_Class, Formality.POLITE, self.polarity)
        self.assertEqual(result, self.verb.PassivePoliteNegative)

# ---------------------------------------------------------- #
#     Register Positive and Negative Verb Form Test Suites   #
# ---------------------------------------------------------- #
def create_positive_verb_form_suite(suite):
    ''' Adds all positive verb form generator tests for each specified method. 
        The current verbs tested are:
         
        1. Godan Verb [Nomu / のむ]
        2. Ichidan Verb [Taberu / たベる]
        3. Irregular Verb [Suru / する]
        4. Irregular Verb [Kuru / くる]
    '''
    suite.addTest(ParametrizedTestCase.parametrize(TestPositiveVerbForms, param=GodanVerbNomu))
    suite.addTest(ParametrizedTestCase.parametrize(TestPositiveVerbForms, param=IchidanVerbTaberu))
    suite.addTest(ParametrizedTestCase.parametrize(TestPositiveVerbForms, param=IrregularVerbSuru))
    suite.addTest(ParametrizedTestCase.parametrize(TestPositiveVerbForms, param=IrregularVerbKuru))

    return suite

def create_negative_verb_form_suite(suite):
    ''' Adds all negative verb form generator tests for each specified method. 
        The current verbs tested are:

        1. Godan Verb [Nomu / のむ]
        2. Ichidan Verb [Taberu / たベる]
        3. Irregular Verb [Suru / する]
        4. Irregular Verb [Kuru / くる]
    '''
    suite.addTest(ParametrizedTestCase.parametrize(TestNegativeVerbForms, param=GodanVerbNomu))
    suite.addTest(ParametrizedTestCase.parametrize(TestNegativeVerbForms, param=IchidanVerbTaberu))
    suite.addTest(ParametrizedTestCase.parametrize(TestNegativeVerbForms, param=IrregularVerbSuru))
    suite.addTest(ParametrizedTestCase.parametrize(TestNegativeVerbForms, param=IrregularVerbKuru))

    return suite

if __name__ == '__main__':
    suite = unittest.TestSuite()
    create_positive_verb_form_suite(suite)
    create_negative_verb_form_suite(suite)

    unittest.TextTestRunner(verbosity=2).run(suite)