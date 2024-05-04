#!/bin/bash
set -euo pipefail
selection="$2"

curl -sSL \
  -v \
  "$TORN_API/torn/?key=$TORN_API_KEY&selections=$selection" |
  jq . \
;


# vim:set ft=bash:
