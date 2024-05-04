#!/bin/bash
set -euo pipefail

redo-ifchange \
  company.json \
  faction.json \
  market.json \
  property.json \
  torn.json \
  user.json \
  torn/all \
;


# vim:set ft=bash:
