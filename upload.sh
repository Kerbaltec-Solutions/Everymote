#!/usr/bin/env bash
for file in *; do
    if [[ $file != *"upload.sh"* ]]; then
        mpremote fs cp $file :$file
    fi
done

mpremote fs ls