#!/usr/bin/env bash

TEXT=$(<../challenge/twice-cooler.txt)

set -e

while true ; do
    TEXT=$(base32 -d <<< "${TEXT}")
    echo "${TEXT}"
done
