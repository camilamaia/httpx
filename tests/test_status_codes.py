import httpx


def test_status_code_as_int():
    assert httpx.codes.NOT_FOUND == 404
    assert str(httpx.codes.NOT_FOUND) == "404"


def test_lowercase_status_code():
    assert httpx.codes.not_found == 404  # type: ignore


def test_reason_phrase_for_status_code():
    assert httpx.codes.get_reason_phrase(404) == "Not Found"


def test_reason_phrase_for_unknown_status_code():
    assert httpx.codes.get_reason_phrase(499) == ""
