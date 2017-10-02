#! /bin/sh

set -ex

python generate_config.py

exec ./veneur -f config.yaml
