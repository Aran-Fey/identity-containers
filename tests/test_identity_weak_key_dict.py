from __future__ import annotations

import gc

import pytest

from identity_containers import IdentityWeakKeyDict


class Weakrefable:
    pass


def test_access_nonexistent_key():
    wkdict = IdentityWeakKeyDict()

    with pytest.raises(KeyError):
        wkdict["foo"]


def test_access_existing_key():
    wkdict = IdentityWeakKeyDict()

    foo = Weakrefable()
    wkdict[foo] = 123


def test_key_death():
    wkdict = IdentityWeakKeyDict()

    foo = Weakrefable()
    wkdict[foo] = 123

    del foo
    gc.collect()

    assert len(wkdict) == 0


def test_key_death_during_iteration():
    wkdict = IdentityWeakKeyDict()

    foo = Weakrefable()
    wkdict[foo] = 123

    bar = Weakrefable()
    wkdict[bar] = 123

    num_loops = 0
    for _ in wkdict:
        num_loops += 1

        foo = bar = None
        gc.collect()

    assert num_loops == 2


def test_repr():
    class Reprable:
        def __init__(self, name: str):
            self.repr = name

        def __repr__(self) -> str:
            return self.repr

    key1 = Reprable("[]")
    key2 = Reprable("'b'")
    wkdict = IdentityWeakKeyDict([(key1, "a"), (key2, {})])
    assert repr(wkdict) == "IdentityWeakKeyDict([([], 'a'), ('b', {})])"
