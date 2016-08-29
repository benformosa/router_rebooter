#!/usr/bin/python3
"""If the Internet is unreachable, attempt to gracefully reset the router.
After a number of failed attempts, reboot the router."""
#Ben Formosa 2016-08-29

import os
import subprocess
import sys
import time

#A program which will return a 0 exit code when the internet connection is OK.
test_env = 'REBOOTER_TEST_CMD'
test_cmd = os.getenv(test_env, False)
if not test_cmd:
    raise ValueError('Test command not specified. Environment variable {} not set'.format(test_env))

#A program which will attempt to restart the router.
reboot_env = 'REBOOTER_REBOOT_CMD'
reboot_cmd = os.getenv(reboot_env, False)
if not reboot_cmd:
    raise ValueError('Reboot command not specified. Environment variable {} not set'.format(reboot_env))

#A program which will attempt to gracefully reset the router.
#If not specified, use the reboot command
reset_env = 'REBOOTER_RESET_CMD'
reset_cmd = os.getenv(reset_env, reboot_env)

#How many times to try resetting the router before giving up.
#If this is set to 0, one reset will be attempted.
retry_attempts_env = 'REBOOTER_RETRIES'
retry_attempts = int(os.getenv(retry_attempts_env, '5'))
if retry_attempts < 0:
    raise ValueError('number of retries must be non-negative')

#How many seconds to wait after a reboot.
reboot_wait_env = 'REBOOTER_REBOOT_WAIT'
reboot_wait = int(os.getenv(reboot_wait_env, 60))

#How many seconds to wait after a graceful reset.
reset_wait_env = 'REBOOTER_RESET_WAIT'
reset_wait = int(os.getenv(reset_wait_env, 30))

verbose_env = 'REBOOTER_VERBOSE'
verbose = int(os.getenv(verbose_env, False))

retry = 0
#Add another attempt if a reboot command was specified
if not reset_cmd == reboot_cmd:
    reboot = True
    retry_attempts +=1

while retry <= retry_attempts:
    verbose and print('## test attempt {}'.format(retry))
    OK = subprocess.call(test_cmd)
    verbose and print('## Test result - {}'.format(OK))
    if OK == 0:
        verbose and print('## Everything is fine.')
        sys.exit(0)
    elif retry < retry_attempts:
        if reboot and retry == retry_attempts:
            verbose and print('## rebooting.')
            subprocess.call(reboot_cmd)
            time.sleep(reboot_wait)
            retry += 1
        else:
            verbose and print('## reset attempt {}'.format(retry))
            subprocess.call(reset_cmd)
            time.sleep(reset_wait)
            retry += 1
    else:
        print('Giving up after {} attempts'.format(retry))
        exit(1)


#else:
    #If a different command is specified for reboot, run it now.
 #   if not reset_cmd == reboot_cmd:
        #verbose and print('## rebooting.')
        #subprocess.call(reboot_cmd)
        #time.sleep(reboot_wait)
        #OK = subprocess.call(test_cmd)
        #if OK == 0:
            #verbose and print('## Everything is fine.')
            #sys.exit(0)
    #print('Giving up after {} attempts'.format(retry))
    #exit(1)




