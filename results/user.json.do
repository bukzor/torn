#!/bin/sh
redo-ifchange hourly.txt
curl -sSL \
  -vv \
  "$TORN_API/user/$TORN_USER_ID?key=$TORN_API_KEY" |
  jq . \
;
