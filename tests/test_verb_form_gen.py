import unittest

from parameterized import parameterized

from src.japverbconj.constants.enumerated_types import (Formality, Polarity,
                                                        Tense, VerbClass)
from src.japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg
from src.japverbconj.verb_form_gen import *

from .constants import PARAMETER_LIST


# ---------------------------------------------------------- #
#                    Positive Verb Form Tests                #
# ---------------------------------------------------------- #
class TestPositiveVerbForms(unittest.TestCase):
    """Tests for each positive verb conjugation form considering
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
    """

    def setUp(self):
        self.polarity = Polarity.POSITIVE

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_positive_nonpast(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.Verb, verb.Verb_Class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.PolitePositiveNonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_positive_past(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.Verb, verb.Verb_Class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.PolitePositivePast)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_positive_nonpast(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.Verb, verb.Verb_Class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.Verb)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_positive_past(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.Verb, verb.Verb_Class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.PlainPositivePast)

    @parameterized.expand(PARAMETER_LIST)
    def test_te_form(self, _, verb):
        result = jvfg.generate_te_form(verb.Verb, verb.Verb_Class)
        self.assertEqual(result, verb.TeForm)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_plain(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ConditionalPlain)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_polite(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ConditionalPolite)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_plain_positive(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.VolitionalPlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_polite_positive(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_volitional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.VolitionalPolitePositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_plain_positive(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.PotentialPlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_polite_positive(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.PotentialPolitePositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_plain_positive(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ImperativePlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_polite_positive(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ImperativePolitePositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_plain_positive(self, _, verb):
        result = jvfg.generate_provisional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ProvisionalPlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_polite_positive(self, _, verb):
        if verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_provisional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ProvisionalPolitePositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_plain_positive(self, _, verb):
        result = jvfg.generate_causative_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.CausativePlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_polite_positive(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_causative_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.CausativePolitePositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_plain_positive(self, _, verb):
        result = jvfg.generate_passive_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.PassivePlainPositive)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_polite_positive(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_passive_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.PassivePolitePositive)


# ---------------------------------------------------------- #
#                    Negative Verb Form Tests                #
# ---------------------------------------------------------- #
class TestNegativeVerbForms(unittest.TestCase):
    """Tests for each negative verb conjugation form considering
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
    """

    def setUp(self):
        self.polarity = Polarity.NEGATIVE

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_negative_nonpast(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.Verb, verb.Verb_Class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.PoliteNegativeNonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_negative_past(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.Verb, verb.Verb_Class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.PoliteNegativePast)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_negative_nonpast(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.Verb, verb.Verb_Class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.PlainNegativeNonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_negative_past(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.Verb, verb.Verb_Class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.PlainNegativePast)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_plain(self, _, verb):
        if verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ConditionalPlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_polite(self, _, verb):
        if verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ConditionalPoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_plain_negative(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.VolitionalPlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_polite_negative(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.VolitionalPoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_plain_negative(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.PotentialPlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_polite_negative(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.PotentialPoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_plain_negative(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ImperativePlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_polite_negative(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ImperativePoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_plain_negative(self, _, verb):
        result = jvfg.generate_provisional_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.ProvisionalPlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_polite_negative(self, _, verb):
        if verb.Verb_Class is not VerbClass.IRREGULAR:
            self.skipTest("Not required for non-irregular verbs")
        result = jvfg.generate_provisional_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.ProvisionalPoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_plain_negative(self, _, verb):
        if verb.Verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = jvfg.generate_causative_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.CausativePlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_polite_negative(self, _, verb):
        if verb.Verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = jvfg.generate_causative_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.CausativePoliteNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_plain_negative(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not required for irregular verbs")
        result = jvfg.generate_passive_form(
            verb.Verb, verb.Verb_Class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.PassivePlainNegative)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_polite_negative(self, _, verb):
        if verb.Verb_Class == VerbClass.IRREGULAR:
            self.skipTest("Not required for irregular verbs")
        result = jvfg.generate_passive_form(
            verb.Verb, verb.Verb_Class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.PassivePoliteNegative)


if __name__ == "__main__":
    unittest.main()
