from pytest_bdd import scenario, given, when

@scenario("test_basic_call.feature", "SIP Call flow")
def test_basic_sip_call():
    """ basic SIP to SIP Call flow """
    assert True

@when("Configure vega for testcall")
def Config_vega(Login):
    Login.write(b"set sip.accept_non_proxy_invites=1\n")
    Login.write(b"apply\n")
    Login.write(b"apply\n")
    Login.write(b"apply\n")
    Login.write(b"save\n")
    Login.write(b"save\n")
    Login.write(b"save\n")

    Login.write(b"exit\n")

