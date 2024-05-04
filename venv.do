#!/bin/bash -x
set -euo pipefail
exec >&2  # we're not building a file from stdout

redo-ifchange requirements.txt

python3.12 -m venv --upgrade-deps venv
pip install -r requirements.txt


# vim:ft=bash:
