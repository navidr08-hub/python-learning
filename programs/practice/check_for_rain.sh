#!/usr/bin/env bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv exec python3 $HOME/projects/python-learning/programs/practice/check_for_rain.py >> $HOME/projects/python-learning/logs/check_for_rain.log 2>&1
