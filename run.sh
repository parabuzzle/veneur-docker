#! /bin/sh

set -ex

python generate_config.py

exec /build/veneur -f config.yaml
