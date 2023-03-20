#!/usr/bin/env bash
set -ex
UNIQUE_ID=$1 nextpnr-ice40 --up5k --package sg48 --json icebreaker_pnr.json --run patch_id.py
icepack icebreaker_patched.asc icebreaker_patched.bin
iceprog -t
iceprog icebreaker_patched.bin
