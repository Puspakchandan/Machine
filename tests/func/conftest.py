from pytest_bdd import given
from pytest import fixture 

import getpass
import sys
import telnetlib
import socket
import os

@fixture(scope="session")
def Login():
    """ Login vega with username and passowrd """
    Host = "192.168.3.254"
    user = "admin"
    password = "admin"

    tn = telnetlib.Telnet(Host)

    tn.read_until(b"Username: ")
    tn.write((user.encode("ascii") + b"\n"))

    if password:
       tn.read_until(b"Password: ")
       tn.write((password.encode("ascii") + b"\n"))
    
    return tn


@given("Login vega with username and password")
def login_vega(Login):
    """ Login vega with valid username and passoword """


