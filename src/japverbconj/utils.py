from .constants.enumerated_types import VerbClass
from .constants.particle_constants import *
from .constants.verb_ending_constants import *
from .exceptions import NonIrregularVerbError


# ---------------------------------------------------------- #
#                UTIL VERB GENERATOR FUNCTIONS               #
# ---------------------------------------------------------- #
def splice_verb(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        tuple: Verb stem and particle ending
    """
    num_ending_particles = 1
    if verb_class == VerbClass.IRREGULAR:
        num_ending_particles = 2
    return verb[: -1 * num_ending_particles], verb[-1 * num_ending_particles :]


def get_verb_stem(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        str: Verb stem
    """
    return splice_verb(verb, verb_class)[0]


def get_ending_particle(verb, verb_class):
    """Split Japanese verb between stem and ending particle(s). The number of ending
    particles returned depends on the verb class (i.e. godan / ichidan will return one
    particle while irregular verbs will return two particles)

    Args:
        verb (str): Japanese verb in kanji and/or kana
        verb_class (enum): VerbClass enum representing the Japanese verb class

    Returns:
        tuple: Particle ending
    """
    return splice_verb(verb, verb_class)[1]


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
        kuru_kanji_ending (:obj: str, optional): kuru as kanji verb ending based on the conjugation form.
            Defaults to None.

    Returns:
        str: irregular verb with appropriate particles and ending attached depending
            on verb conjugation
    """
    verb_stem, particle_ending = splice_verb(verb, VerbClass.IRREGULAR)
    if particle_ending not in [SURU_ENDING, KURU_ENDING, KURU_KANJI_ENDING]:
        raise NonIrregularVerbError("Non-Irregular Verb Ending Found", particle_ending)
    stem_particle = ""
    if particle_ending == SURU_ENDING:
        if append_stem_particle:
            stem_particle = SHI_PARTICLE
        ending = suru_ending
    elif particle_ending == KURU_ENDING:
        if append_stem_particle:
            stem_particle = KI_PARTICLE
        ending = kuru_ending
    else:
        if append_stem_particle:
            stem_particle = KURU_KANJI
        ending = kuru_kanji_ending
    return f"{verb_stem}{stem_particle}{ending}"


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
    if not is_regular_nai:
        return f"{verb}{NAI_ENDING}"
    verb_stem, particle_ending = splice_verb(verb, verb_class)
    stem_particle = ""
    if verb_class == VerbClass.IRREGULAR:
        if particle_ending == SURU_ENDING:
            stem_particle = SHI_PARTICLE
        elif particle_ending == KURU_ENDING:
            stem_particle = KO_PARTICLE
        else:
            stem_particle = KURU_KANJI
    else:
        if verb_class == VerbClass.GODAN:
            verb_stem = map_dictionary_to_a_ending(verb)
    return f"{verb_stem}{stem_particle}{NAI_ENDING}"


def base_te_ta_form(verb, verb_class, regular_ending, dakuten_ending):
    """Handle the formation of the -te / -ta form for verbs belonging to
    any verb class. Logic for both forms follows similar logic but differs
    between (-te, -de) and (-ta, -da) based on the last particle of a Godan
    verb.

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        verb_class (enum): VerbClass Enum representing the verb class
            to which the verb belongs
        regular_ending (str): ending without dakuten
        dakuten_ending (str): ending with dakuten

        TODO... reformat this logic for endings

    Returns:
        str: The verb stem plus the -te / -ta particle depending on the
        verb class.
    """
    if verb_class == VerbClass.IRREGULAR:
        return handle_irregular_verb(
            verb, True, regular_ending, regular_ending, regular_ending
        )
    else:
        verb_stem, particle_ending = splice_verb(verb, verb_class)
        if verb_class == VerbClass.ICHIDAN:
            verb_ending = regular_ending
        else:
            if particle_ending in [RU_PARTICLE, TSU_PARTICLE, U_PARTICLE]:
                verb_ending = f"{CHISAI_TSU_PARTICLE}{regular_ending}"
            elif particle_ending in [BU_PARTICLE, MU_PARTICLE, NU_PARTICLE]:
                verb_ending = f"{N_PARTICLE}{dakuten_ending}"
            elif particle_ending in [KU_PARTICLE]:
                verb_ending = f"{I_PARTICLE}{regular_ending}"
            elif particle_ending in [GU_PARTICLE]:
                verb_ending = f"{I_PARTICLE}{dakuten_ending}"
            else:
                verb_ending = f"{SHI_PARTICLE}{regular_ending}"
        return f"{verb_stem}{verb_ending}"


def map_dictionary_to_a_ending(verb):
    """Generates Godan verb stem with corresponding -a particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -a particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, A_PARTICLE)


def map_dictionary_to_e_ending(verb):
    """Generates Godan verb stem with corresponding -e particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -e particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, E_PARTICLE)


def map_dictionary_to_i_ending(verb):
    """Generates Godan verb stem with corresponding -i particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -i particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, I_PARTICLE)


def map_dictionary_to_o_ending(verb):
    """Generates Godan verb stem with corresponding -o particle attached

    Args:
        verb (str): Japanese verb in kana, might contain kanji

    Returns:
        str: verb stem with the correct -o particle attached (Godan verbs only)
    """
    return map_dict_form_to_different_ending(verb, O_PARTICLE)


def map_dict_form_to_different_ending(verb, desired_ending):
    """Generates Godan verb stem and computes the correct particle to attach based on the
    verb's last kana

    Args:
        verb (str): Japanese verb in kana, might contain kanji
        desired_ending (str): target base_particle

    Returns:
        str: verb stem with the correct particle attached depending on the last kana particle
    of the Godan verb
    """
    verb_stem, particle_ending = splice_verb(verb, VerbClass.GODAN)

    return f"{verb_stem}{ENDING_DICT[particle_ending][desired_ending]}"
