#!/bin/bash

export REBOOTER_TEST_CMD=./test_internet.py
export REBOOTER_REBOOT_CMD="python3 -c 'import ../auto_linksys/linksys; linksys.reboot()'"
export REBOOTER_RESET_CMD="python3 -c 'import ../auto_linksys/linksys; linksys.reset()'"
export REBOOTER_RETRIES=5
export REBOOTER_REBOOT_WAIT=60
export REBOOTER_RESET_WAIT=30

./router_rebooter.py
