#!/bin/bash
set -euo pipefail

redo-ifchange \
  company.json \
  faction.json \
  market.json \
  property.json \
  torn.json \
  user.json \
;


# vim:set ft=bash:
