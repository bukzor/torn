#!/bin/bash
set -euxo pipefail

cat selections.list |
  sed 's/$/.json/' |
  xargs redo-ifchange


# vim:set ft=bash:
