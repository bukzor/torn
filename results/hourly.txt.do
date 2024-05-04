#!/bin/bash
set -euo pipefail

redo-always
date -Ihours |
  tee >(redo-stamp)
