"""Test suite for mom Listener and Publisher."""

import pytest

from common.lib.communication.mom import Listener, Publisher


def test_create_mom_listener():
    """Test create an abstract listener. Exception should be risen."""
    with pytest.raises(TypeError):
        Listener("listener")


def test_create_mom_publisher():
    """Test create an abstract publisher. Exception should be risen."""
    with pytest.raises(TypeError):
        Publisher("publisher")
