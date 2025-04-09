from __future__ import annotations

from identity_containers import IdentityDefaultDict


def test_access_nonexistent_key():
    iddict = IdentityDefaultDict(list)

    foo = iddict["foo"]

    assert len(iddict) == 1
    assert "foo" in iddict
    assert iddict["foo"] is foo


def test_access_existing_key():
    foo = [1, 2, 3]
    iddict = IdentityDefaultDict(list, {"foo": foo})

    assert len(iddict) == 1
    assert iddict["foo"] is foo
