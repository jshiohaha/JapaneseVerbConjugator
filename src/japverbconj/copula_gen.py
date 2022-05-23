from .constants.enumerated_types import Formality, Polarity, Tense
from .constants.particle_constants import RA_PARTICLE
from .constants.verb_ending_constants import (
    CONDITIONAL_DA_PLAIN_POSITIVE_ENDING,
    PAST_DA_PLAIN_NEGATIVE_ENDING,
    PAST_DA_PLAIN_POSITIVE_ENDING,
    PAST_DA_POLITE_POSITIVE_ENDING,
    PLAIN_DA_NEGATIVE_ENDING,
    PLAIN_DA_POSITIVE_ENDING,
    POLITE_DA_NEGATIVE_ENDING,
    POLITE_DA_POSITIVE_ENDING,
    PRESUMPTIVE_DA_PLAIN_POSITIVE_ENDING,
    PRESUMPTIVE_DA_POLITE_POSITIVE_ENDING,
    TE_FORM_DA_PLAIN_POSITIVE_ENDING,
    TE_FORM_DA_POLITE_POSITIVE_ENDING,
)


class Copula:
    @classmethod
    def generate_plain_form(cls, tense, polarity):
        if polarity == Polarity.POSITIVE:
            if tense == Tense.NONPAST:
                return PLAIN_DA_POSITIVE_ENDING
            else:
                return PAST_DA_PLAIN_POSITIVE_ENDING
        else:
            if tense == Tense.NONPAST:
                return PLAIN_DA_NEGATIVE_ENDING
            else:
                return PAST_DA_PLAIN_NEGATIVE_ENDING

    @classmethod
    def generate_polite_form(cls, tense, polarity):
        if polarity == Polarity.POSITIVE:
            if tense == Tense.NONPAST:
                return POLITE_DA_POSITIVE_ENDING
            else:
                return PAST_DA_POLITE_POSITIVE_ENDING
        else:
            if tense == Tense.NONPAST:
                return POLITE_DA_NEGATIVE_ENDING
            else:
                return f"{POLITE_DA_NEGATIVE_ENDING}{PAST_DA_POLITE_POSITIVE_ENDING}"

    @classmethod
    def generate_conditional_form(cls):
        return CONDITIONAL_DA_PLAIN_POSITIVE_ENDING

    @classmethod
    def generate_presumptive_form(cls, formality, polarity):
        if polarity == Polarity.POSITIVE:
            stem = ""
        else:
            stem = PLAIN_DA_NEGATIVE_ENDING
        if formality == Formality.PLAIN:
            ending = PRESUMPTIVE_DA_PLAIN_POSITIVE_ENDING
        else:
            ending = PRESUMPTIVE_DA_POLITE_POSITIVE_ENDING
        return f"{stem}{ending}"

    @classmethod
    def generate_te_form(cls, formality):
        if formality == Formality.PLAIN:
            return TE_FORM_DA_PLAIN_POSITIVE_ENDING
        else:
            return TE_FORM_DA_POLITE_POSITIVE_ENDING

    @classmethod
    def generate_tara_form(cls, formality):
        if formality == Formality.PLAIN:
            return (
                f"{cls.generate_plain_form(Tense.PAST,Polarity.POSITIVE)}{RA_PARTICLE}"
            )
        else:
            return (
                f"{cls.generate_polite_form(Tense.PAST,Polarity.POSITIVE)}{RA_PARTICLE}"
            )
