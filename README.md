# Japanese Verb Conjugator

Japanese Verb Conjugator is a Python library for conjugating Japanese verbs.

### What forms will Japanese Verb Conjugator conjugate?

Japanese Verb Conjugator conjugates the following verb forms:

- plain form
- polite form
- ~te form
- conditional form
- volitional form
- potential form
- imperative form
- provisional form
- causative form
- passive form

Japanese Verb Conjugator conjugates verbs based on `verb class`, `tense`, `formality`, and `polarity` parameters. Depending on the conjugation and [verb class](https://wtawa.people.amherst.edu/jvrules/index.php?form=groups), the parameters for conjugation methods may vary.

**Example**

`generate_plain_form` requires `verb class`, `tense`, and `formality` parameters.

`generate_volitional_form` requires `verb class`, `tense`, and `polarity` parameters.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `japaneseverbconjugator`. If you want to install `japaneseverbconjugator` and its dependencies in a virtual environment, first create and activiate a virtual environment. If you want to change the virtual environment name to someting other than `venv`, replace the second `venv` with your desired name. Use that same name to replace `venv` in the second command.

```python
python3 -m venv venv
source venv/bin/activate
```

If you run into trouble, see the [Python Virtual Environment tutorial](https://docs.python.org/3/tutorial/venv.html).

### Method 1: Pip

After installing and activating the virtual environment, run the following commands to install `japaneseverbconjugator` and its dependencies.

```bash
pip install japaneseverbconjugator
```

#### Note

Pip may display an error during installation that includes the following message.

```
No matching distribution found for romkan (from JapaneseVerbConjugator)
```

In this case, run the command `pip install romkan` and then run `pip install japaneseverbconjugator` again.

You should be good to go! See the **Usage** section on how to get started using the library.

### Method 2: Clone this repository

Go to the directory you want to clone this repository and run the following command.

```bash
git clone https://github.com/jShiohaha/JapaneseVerbConjugator.git
```

After installing the library, install the library dependencies via pip with the following command. The dependencies in `requirements.txt` will allow you to run the library and tests.

```bash
pip install -r requirements.txt
```

You should be good to go! See the **Usage** section on how to get started using the library.

## Usage

Here is an example of how to import the library and use it.

```python
from japaneseverbconjugator.src import JapaneseVerbFormGenerator as japaneseVerbFormGenerator
from japaneseverbconjugator.src.constants.EnumeratedTypes import VerbClass, Tense, Polarity

jvfg = japaneseVerbFormGenerator.JapaneseVerbFormGenerator() # creates JapaneseVerbFormGenerator instance
jvfg.generate_plain_form("飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.POSITIVE) # returns '飲む'
jvfg.generate_plain_form("飲む", VerbClass.GODAN, Tense.NONPAST, Polarity.NEGATIVE) # returns '飲まない'
```

The library will try to help validate the correctness of the verb by checking for invalid verb lengths, non-Japanese characters, and invalid verb endings. **Limitation**: this library cannot identify Chinese words with valid Japanese particle endings or nonexistent Japanese verbs.

## Tests

Running tests should be done from `japaneseverbsconjugator` directory. Otherwise, you will get errors saying that Python cannot find certain modules needed for import.

The script named `RunTests.sh` makes it easy to run all the tests for this library. This repository includes the `coverage` package to track code coverage, and `RunTests.sh` will use this package if you instruct it to do so.

#### Run tests and view HTML coverage report

Use the following commands to run the tests and see the HTML coverage report in a browser.

```bash
./RunTests.sh html
```

**Note**: If this doesn't work, you can manually create and open the report with the following commands.

```bash
coverage html
open htmlcov/index.html
```

#### Run tests and view command line coverage report

Use the following commands to run the tests and see the coverage report on command line.

```bash
./RunTests.sh report
```

#### Run tests

Use the following commands to only run the tests with the `unittest` framework.

```bash
./RunTests.sh
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project uses a Python package named `romkan`, which has a BSD license. This project therefore has a [BSD](https://choosealicense.com/licenses/bsd/) license.
