#!/bin/bash

export REBOOTER_TEST_CMD=/bin/false
export REBOOTER_REBOOT_CMD=/bin/false
export REBOOTER_RESET_CMD=/bin/true
export REBOOTER_RETRIES=1
export REBOOTER_REBOOT_WAIT=5
export REBOOTER_RESET_WAIT=1
export REBOOTER_VERBOSE=1

./router_rebooter.py
