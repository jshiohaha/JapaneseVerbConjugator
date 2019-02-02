#!/bin/bash
japaneseVerbFormGeneratorTests="JapaneseVerbFormGeneratorTests.py"
utilsTests="UtilsTests.py"
decoratorsTests="DecoratorsTests.py"
if [ $# -gt 0 ]
  then
    srcdir = "src"
    coverage run -a --source $srcdir "tests/$japaneseVerbFormGeneratorTests"
    coverage run -a --include "$srcdir/Utils.py" "tests/$utilsTests"
    coverage run -a --include "$srcdir/Decorators.py" "tests/$decoratorsTests"
    if [ $1 == "report" ]
    then
      coverage report -m # prints to console
    elif [ $1 == "html" ]
    then
      coverage html # this will create a dir named htmlcov/ which contains html coverage data
      open htmlcov/index.html
    fi
else
  python "tests/$japaneseVerbFormGeneratorTests"  
  python "tests/$utilsTests"
  python "tests/$decoratorsTests"
fi