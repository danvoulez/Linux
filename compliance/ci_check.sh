#!/bin/sh
DIR="$(dirname "$0")"
"$DIR/license_validator.sh"
"$DIR/sbom_generator.py"
