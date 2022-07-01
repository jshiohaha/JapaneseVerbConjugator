import unittest

from parameterized import parameterized
from src.japverbconj.constants.enumerated_types import (
    Formality,
    Polarity,
    Tense,
    VerbClass,
)
from src.japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg
from src.japverbconj.verb_form_gen import *

from .constants import PARAMETER_LIST, CopulaDa


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
            verb.verb, verb.verb_class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.polite_positive_nonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_positive_past(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.verb, verb.verb_class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.polite_positive_past)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_positive_nonpast(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.verb, verb.verb_class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.verb)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_positive_past(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.verb, verb.verb_class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.plain_positive_past)

    @parameterized.expand(PARAMETER_LIST)
    def test_te_form(self, _, verb):
        result = jvfg.generate_te_form(verb.verb, verb.verb_class)
        self.assertEqual(result, verb.te_form)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_plain(self, _, verb):
        if verb.verb_class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.conditional_plain)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_polite(self, _, verb):
        if verb.verb_class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.conditional_polite)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_plain_positive(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.volitional_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_polite_positive(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.volitional_polite_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_plain_positive(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.potential_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_polite_positive(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.potential_polite_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_plain_positive(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.imperative_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_polite_positive(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.imperative_polite_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_plain_positive(self, _, verb):
        result = jvfg.generate_provisional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.provisional_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_polite_positive(self, _, verb):
        if verb.verb_class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_provisional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.provisional_polite_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_plain_positive(self, _, verb):
        result = jvfg.generate_causative_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.causative_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_polite_positive(self, _, verb):
        if verb.verb_class == VerbClass.IRREGULAR:
            self.skipTest("Not Required for Irregular Verbs")
        result = jvfg.generate_causative_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.causative_polite_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_plain_positive(self, _, verb):
        result = jvfg.generate_passive_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.passive_plain_positive)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_polite_positive(self, _, verb):
        result = jvfg.generate_passive_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.passive_polite_positive)


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
            verb.verb, verb.verb_class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.polite_negative_nonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_polite_negative_past(self, _, verb):
        result = jvfg.generate_polite_form(
            verb.verb, verb.verb_class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.polite_negative_past)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_negative_nonpast(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.verb, verb.verb_class, Tense.NONPAST, self.polarity
        )
        self.assertEqual(result, verb.plain_negative_nonpast)

    @parameterized.expand(PARAMETER_LIST)
    def test_plain_negative_past(self, _, verb):
        result = jvfg.generate_plain_form(
            verb.verb, verb.verb_class, Tense.PAST, self.polarity
        )
        self.assertEqual(result, verb.plain_negative_past)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_plain(self, _, verb):
        if verb.verb_class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.conditional_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_conditional_polite(self, _, verb):
        if verb.verb_class is not VerbClass.IRREGULAR:
            self.skipTest("Not Required for Non-Irregular Verbs")
        result = jvfg.generate_conditional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.conditional_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_plain_negative(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.volitional_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_volitional_polite_negative(self, _, verb):
        result = jvfg.generate_volitional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.volitional_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_plain_negative(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.potential_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_potential_polite_negative(self, _, verb):
        result = jvfg.generate_potential_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.potential_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_plain_negative(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.imperative_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_imperative_polite_negative(self, _, verb):
        result = jvfg.generate_imperative_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.imperative_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_plain_negative(self, _, verb):
        result = jvfg.generate_provisional_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.provisional_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_provisional_polite_negative(self, _, verb):
        if verb.verb_class is not VerbClass.IRREGULAR:
            self.skipTest("Not required for non-irregular verbs")
        result = jvfg.generate_provisional_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.provisional_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_plain_negative(self, _, verb):
        if verb.verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = jvfg.generate_causative_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.causative_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_causative_polite_negative(self, _, verb):
        if verb.verb[-2:] == "する":
            self.skipTest("Not required for する verbs")
        result = jvfg.generate_causative_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.causative_polite_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_plain_negative(self, _, verb):
        result = jvfg.generate_passive_form(
            verb.verb, verb.verb_class, Formality.PLAIN, self.polarity
        )
        self.assertEqual(result, verb.passive_plain_negative)

    @parameterized.expand(PARAMETER_LIST)
    def test_passive_polite_negative(self, _, verb):
        result = jvfg.generate_passive_form(
            verb.verb, verb.verb_class, Formality.POLITE, self.polarity
        )
        self.assertEqual(result, verb.passive_polite_negative)


class TestCopula(unittest.TestCase):
    @parameterized.expand(
        [
            ("pos", Tense.NONPAST, Polarity.POSITIVE, CopulaDa.plain_positive),
            ("pos past", Tense.PAST, Polarity.POSITIVE, CopulaDa.plain_past),
            ("neg", Tense.NONPAST, Polarity.NEGATIVE, CopulaDa.plain_negative),
            ("neg past", Tense.PAST, Polarity.NEGATIVE, CopulaDa.plain_past_negative),
        ]
    )
    def test_copula_plain(self, _, tense, polarity, expected_copula):
        self.assertEqual(
            jvfg.copula.generate_plain_form(tense, polarity), expected_copula
        )

    @parameterized.expand(
        [
            ("pos", Tense.NONPAST, Polarity.POSITIVE, CopulaDa.polite_positive),
            ("pos past", Tense.PAST, Polarity.POSITIVE, CopulaDa.polite_past),
            ("neg", Tense.NONPAST, Polarity.NEGATIVE, CopulaDa.polite_negative),
            ("neg past", Tense.PAST, Polarity.NEGATIVE, CopulaDa.polite_past_negative),
        ]
    )
    def test_copula_polite(self, _, tense, polarity, expected_copula):
        self.assertEqual(
            jvfg.copula.generate_polite_form(tense, polarity), expected_copula
        )

    def test_copula_conditional(self):
        self.assertEqual(jvfg.copula.generate_conditional_form(), CopulaDa.conditional)

    @parameterized.expand(
        [
            ("pla pos", Formality.PLAIN, Polarity.POSITIVE, CopulaDa.presumptive_plain),
            (
                "pol pos",
                Formality.POLITE,
                Polarity.POSITIVE,
                CopulaDa.presumptive_polite,
            ),
            (
                "pla neg",
                Formality.PLAIN,
                Polarity.NEGATIVE,
                CopulaDa.presumptive_plain_negative,
            ),
            (
                "pol neg",
                Formality.POLITE,
                Polarity.NEGATIVE,
                CopulaDa.presumptive_polite_negative,
            ),
        ]
    )
    def test_copula_presumptive(self, _, formality, polarity, expected_copula):
        self.assertEqual(
            jvfg.copula.generate_presumptive_form(formality, polarity), expected_copula
        )

    @parameterized.expand(
        [
            ("pla", Formality.PLAIN, CopulaDa.te_form_plain),
            ("pol", Formality.POLITE, CopulaDa.te_form_polite),
        ]
    )
    def test_copula_te_form(self, _, formality, expected_copula):
        self.assertEqual(jvfg.copula.generate_te_form(formality), expected_copula)

    @parameterized.expand(
        [
            ("pla", Formality.PLAIN, CopulaDa.tara_plain),
            ("pol", Formality.POLITE, CopulaDa.tara_polite),
        ]
    )
    def test_copula_tara_form(self, _, formality, expected_copula):
        self.assertEqual(jvfg.copula.generate_tara_form(formality), expected_copula)


if __name__ == "__main__":
    unittest.main()
