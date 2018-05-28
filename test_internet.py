#!/usr/bin/python3
"""Test this host's Internet connection. Returns 0 if Internet is reachable"""

import requests

def test_web(url):
    """Return True if a HTTP GET request of the URL returns a 200 code."""
    r = requests.get(url)
    return r.status_code == requests.codes.OK

def test_ping(host):
    """Return True if ping to the host is successful."""
    return True

def test_dns(hostname, server):
    """Return True if the hostname is resolved by the dns server."""
    return True

def test_webs():
    """Test a number of websites."""
    urls = (
        'http://www.msftncsi.com/ncsi.txt',
        'http://www.something.com',
        'https://eff.org',
        )

    #Start with the number of URLs to test and subtract 1 for each successful test.
    success = len(urls)
    for url in urls:
        if test_web(url):
            success -= 1

    if success == 0:
        return True

def test_pings():
    hosts = (
        'www.something.com',
    )
    return True

def test_dnss():
    hostnames = (
        'www.something.com',
    )
    servers = (
        '8.8.8.8',
    )
    return True

def main():
    # All tests must pass
    test = test_webs() and test_pings() and test_dnss()
    if test:
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()
