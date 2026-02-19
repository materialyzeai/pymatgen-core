from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(autouse=True)
def setup_teardown() -> Generator:
    """Use tempdir for all tests."""
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        yield tmpdir
        os.chdir(cwd)


@pytest.fixture(autouse=True)
def test_files_dir() -> Path:
    return Path(__file__).parent.parent / "pymatgen-test-files"
