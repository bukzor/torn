#!/bin/bash
set -euo pipefail
redo-ifchange hourly.txt

curl -sSL \
  -vv \
  "$TORN_API/faction?key=$TORN_API_KEY" |
  jq . \
;


# vim:set ft=bash:
