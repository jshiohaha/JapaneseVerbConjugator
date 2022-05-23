# Japanese Verb Conjugator

Japanese Verb Conjugator is a Python library for conjugating Japanese verbs. 
This fork is used to fix some Issues in the usage of the base package.
Changes will be recorded in CHANGELOG.md

### What forms will Japanese Verb Conjugator conjugate?

Japanese Verb Conjugator conjugates the following verb forms:

* plain form
* polite form
* ~te form
* conditional form
* volitional form
* potential form
* imperative form
* provisional form
* causative form
* passive form

Japanese Verb Conjugator conjugates verbs based on `verb class`, `tense`, `formality`, and `polarity` parameters. Depending on the conjugation and [verb class](https://wtawa.people.amherst.edu/jvrules/index.php?form=groups), the parameters for conjugation methods may vary. 

**Example**

`generate_plain_form` requires `verb class`, `tense`, and `formality` parameters.

`generate_volitional_form` requires `verb class`, `tense`, and `polarity` parameters.

Similarily the conjugations of the copula だ/です can be generated.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `japanese-verb-conjugator-v2`. If you want to install `japanese-verb-conjugator-v2` and its dependencies in a virtual environment, first create and activiate a virtual environment. If you want to change the virtual environment name to someting other than `venv`, replace the second `venv` with your desired name. Use that same name to replace `venv` in the second command.

```python
python3 -m venv venv
source venv/bin/activate
```

If you run into trouble, see the [Python Virtual Environment tutorial](https://docs.python.org/3/tutorial/venv.html). 

### Method 1: Pypi
After installing and activating the virtual environment, run the following commands to install `japanese-verb-conjugator-v2` and its dependencies.

```bash
pip install japanese-verb-conjugator-v2
```
#### Note
Pip may display an error during installation that includes the following message. 

```
No matching distribution found for romkan (from JapaneseVerbConjugator)
```

In this case, run the command `pip install romkan` and then run `pip install japanese-verb-conjugator-v2` again.

You should be good to go! See the **Usage** section on how to get started using the library.

### Method 2: Clone this repository

Go to the directory you want to clone this repository and run the following command.

```bash
git clone https://github.com/Bel-Shazzar/JapaneseVerbConjugator.git
```


To install the Library use the following command

```bash
pip install .
```

To run the library you should install the dependencies in `requirements.txt`.

```bash
pip install -r requirements.txt
```

You should be good to go! See the **Usage** section on how to get started using the library.

## Usage

Here is an example of how to import the library and use it.

```python
from japverbconj.constants.enumerated_types import Formality, Polarity, Tense, VerbClass
from japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg

jvfg.generate_plain_form("飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.POSITIVE) # returns '飲む'
jvfg.generate_plain_form("飲む", VerbClass.GODAN, Formality.POLITE, Polarity.NEGATIVE) # returns '飲まない'
```

The library will try to help validate the correctness of the verb by checking for invalid verb lengths, non-Japanese characters, and invalid verb endings. **Limitation**: this library cannot identify Chinese words with valid Japanese particle endings or nonexistent Japanese verbs.

AHere is an example of how to use the copula generator-

```python 
from japverbconj.constants.enumerated_types import Formality, Polarity, Tense, VerbClass
from japverbconj.verb_form_gen import JapaneseVerbFormGenerator as jvfg

jvfg.copula.generate_plain_form(Tense.NONPAST, Polarity.POSITIVE) # returns 'だ'
jvfg.copula.generate_presumptive_form(Tense.NONPAST, Polarity.POSITIVE) # returns 'ではないでしょう'
```

## Tests
The coverage package is used to run the unittests. The configuration is defined in `.coveragerc`
To run the tests, first install the testing requirements

```bash
pip install -r test/requirements.txt
```

### Run tests
You can run the tests like this

```bash
coverage run -m unittest
```

#### View coverage report
After running the tests with coverage you can show the coverage report like this

```bash
coverage report
```

Alternativly you can generate an html representation like this

```bash
coverage html
```

You can open the html in a browser like this

```bash
open htmlcov/index.html
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project uses a Python package named `romkan`, which has a BSD license. This project therefore has a [BSD](https://choosealicense.com/licenses/bsd/) license.