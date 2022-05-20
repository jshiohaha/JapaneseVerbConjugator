# Local modules
# External Libraries
import romkan

from .constants.enumerated_types import Formality, Polarity, Tense, VerbClass
from .constants.particle_constants import *
from .constants.verb_ending_constants import *


# ---------------------------------------------------------- #
#                UTIL VERB GENERATOR FUNCTIONS               #
# ---------------------------------------------------------- #
def splice_verb(verb, verb_class, should_return_stem=True):
    """Split Japense verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        str: Verb stem or particle endings based on the value of should_return_stem
    """
    num_ending_particles = 1
    if verb_class == VerbClass.IRREGULAR:
        num_ending_particles = 2
    if should_return_stem:
        return verb[: -1 * num_ending_particles]
    return verb[-1 * num_ending_particles :]


def handle_irregular_verb(
    verb,
    append_stem_particle=False,
    suru_ending=None,
    kuru_ending=None,
    kuru_kanji_ending=None,
):
    """Handles irregular verb conjugations depending on suru or kuru verb type.
    Isolates logic of irregular verbs.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        append_stem_particle (bool): verb base particle depends on if the verb is a
            suru or kuru verb. し particle is appended to suru verbs and き is appended
            to kuru verbs. Not all conjugations require these particles to be appended
            to the verb stem.
        suru_ending (:obj: str, optional): suru verb ending based on the conjugation form.
            Defaults to None.
        kuru_ending (:obj: str, optional): kuru verb ending based on the conjugation form.
            Defaults to None.

    Returns:
        str: irregular verb with appropriate particles and ending attached depending
            on verb conjugation
    """
    particle_ending = splice_verb(verb, VerbClass.IRREGULAR, False)
    if particle_ending not in [SURU_ENDING, KURU_ENDING, KURU_KANJI_ENDING]:
        return None

    verb_stem = splice_verb(verb, VerbClass.IRREGULAR)
    ending = ""
    if particle_ending == SURU_ENDING:
        if append_stem_particle:
            ending = SHI_PARTICLE
        ending = "{}{}".format(ending, suru_ending)
    elif particle_ending == KURU_ENDING:
        if append_stem_particle:
            ending = KI_PARTICLE
        ending = "{}{}".format(ending, kuru_ending)
    else:
        if append_stem_particle:
            ending = KURU_KANJI
        ending = "{}{}".format(ending, kuru_kanji_ending)
    return "{}{}".format(verb_stem, ending)


def generate_nai_form(verb, verb_class, is_regular_nai):
    """Generates the nai form of a Japanese verb

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        is_regular_nai (bool): indicates whether to attach nai ending directly
            to verb param or generate the explicit nai form of a verb. Some
            verb conjugations require the nai ending without calculating the
            nai form

    Returns:
        str: nai ending attached to verb param
    """
    verb_stem = splice_verb(verb, verb_class)
    ending = NAI_ENDING

    if not is_regular_nai:
        return "{}{}".format(verb, ending)
    if verb_class == VerbClass.IRREGULAR:
        if splice_verb(verb, verb_class, False) == SURU_ENDING:
            ending = "{}{}".format(SHI_PARTICLE, ending)
        elif splice_verb(verb, verb_class, False) == KURU_ENDING:
            ending = "{}{}".format(KO_PARTICLE, ending)
        else:
            ending = "{}{}".format(KURU_KANJI, ending)
    else:
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_a_ending(verb)
    return "{}{}".format(verb_stem, ending)


def base_te_ta_form(verb, verb_class, *endings):
    """Handle the formation of the -te / -ta form for verbs belonging to
    any verb class. Logic for both forms follows similar logic but differs
    between (-te, -de) and (-ta, -da) based on the last particle of a Godan
    verb.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        *endings: Variable length argument list. Must be in the form (te, de)
        or (ta, da)

        TODO... reformat this logic for *endings

    Returns:
        str: The verb stem plus the -te / -ta particle depending on the
        verb class. Defaults to None.
    """
    if verb_class == VerbClass.IRREGULAR:
        return handle_irregular_verb(verb, True, endings[0], endings[0], endings[0])
    else:
        verb_stem = splice_verb(verb, verb_class)
        verb_ending = ""
        if verb_class == VerbClass.ICHIDAN:
            verb_ending = endings[0]
        else:
            last_kana = splice_verb(verb, verb_class, False)

            if last_kana in [RU_PARTICLE, TSU_PARTICLE, U_PARTICLE]:
                verb_ending = "{}{}".format(CHISAI_TSU_PARTICLE, endings[0])
            elif last_kana in [BU_PARTICLE, MU_PARTICLE, NU_PARTICLE]:
                verb_ending = "{}{}".format(N_PARTICLE, endings[1])
            elif last_kana in [KU_PARTICLE]:
                verb_ending = "{}{}".format(I_PARTICLE, endings[0])
            elif last_kana in [GU_PARTICLE]:
                verb_ending = "{}{}".format(I_PARTICLE, endings[1])
            else:
                verb_ending = "{}{}".format(SHI_PARTICLE, endings[0])
        return "{}{}".format(verb_stem, verb_ending)


def map_dictionary_to_a_ending(verb):
    """Generates Godan verb stem with corresponding -a particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -a particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(
        verb, "a", WA_PARTICLE, TA_PARTICLE, SA_PARTICLE
    )


def map_dictionary_to_e_ending(verb):
    """Generates Godan verb stem with corresponding -e particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -e particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(
        verb, "e", E_PARTICLE, TE_PARTICLE, SE_PARTICLE
    )


def map_dictionary_to_i_ending(verb):
    """Generates Godan verb stem with corresponding -i particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -i particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(
        verb, "i", I_PARTICLE, CHI_PARTICLE, SHI_PARTICLE
    )


def map_dictionary_to_o_ending(verb):
    """Generates Godan verb stem with corresponding -o particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -o particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(
        verb, "o", O_PARTICLE, TO_PARTICLE, SO_PARTICLE
    )


def map_dict_form_to_different_ending(verb, romaji_ending, *special_endings):
    """Generates Godan verb stem and computes the correct particle to attach based on the
    verb's last kana

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        romaji_ending (str): target sound of the particle to append to the verb
        *special_endings: Variable length argument list. Based on the target Godan particle
        class (-a, -e, -i, -o). Order of particles is -u / -tsu / -su.

    Returns:
        str: verb stem with the correct particle attached depending on the last kana particle
    of the Godan verb
    """
    last_kana = splice_verb(verb, VerbClass.GODAN, False)
    verb_stem = splice_verb(verb, VerbClass.GODAN)

    if last_kana == U_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[0])
    elif last_kana == TSU_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[1])
    elif last_kana == SU_PARTICLE:
        return "{}{}".format(verb_stem, special_endings[2])
    else:
        transformed_last_kana_as_romaji = "{}{}".format(
            romkan.to_roma(last_kana)[:-1], romaji_ending
        )
        return "{}{}".format(
            verb_stem, romkan.to_hiragana(transformed_last_kana_as_romaji)
        )
