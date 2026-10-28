#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_anatomy_figures info
PYTHONPATH=src python -m gbt_anatomy_figures check --payload '{}'
PYTHONPATH=src python -m gbt_anatomy_figures run   --payload '{}'
