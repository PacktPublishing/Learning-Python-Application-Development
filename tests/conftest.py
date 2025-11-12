"""
Shared pytest fixtures for the Learning Python Design Patterns project.

This module provides common fixtures that can be used across all test modules.
"""

import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, MagicMock
import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory that is cleaned up after the test."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture 
def temp_file():
    """Create a temporary file that is cleaned up after the test."""
    temp_fd, temp_path = tempfile.mkstemp()
    temp_path_obj = Path(temp_path)
    yield temp_path_obj
    temp_path_obj.unlink(missing_ok=True)


@pytest.fixture
def mock_config():
    """Provide a mock configuration object."""
    config = {
        'debug': False,
        'verbose': False,
        'timeout': 30,
        'max_retries': 3,
        'test_mode': True
    }
    return config


@pytest.fixture
def sample_data():
    """Provide sample test data for game units."""
    return {
        'knight': {
            'name': 'Sir Lancelot',
            'health': 100,
            'attack_power': 15
        },
        'orc': {
            'name': 'Grimjaw',
            'health': 80,
            'attack_power': 12
        },
        'hut': {
            'number': 1,
            'occupant': None,
            'is_acquired': False
        }
    }


@pytest.fixture
def mock_logger():
    """Provide a mock logger object."""
    logger = Mock()
    logger.info = Mock()
    logger.error = Mock()
    logger.warning = Mock()
    logger.debug = Mock()
    return logger


@pytest.fixture
def mock_file_system():
    """Provide a mock file system for testing file operations."""
    fs = MagicMock()
    fs.exists.return_value = True
    fs.read_text.return_value = "mock file content"
    fs.write_text.return_value = None
    fs.mkdir.return_value = None
    return fs


@pytest.fixture
def game_unit_data():
    """Provide test data for game unit testing."""
    return {
        'valid_unit': {
            'name': 'Test Unit',
            'max_hp': 100,
            'hp': 100,
            'attack': 10
        },
        'damaged_unit': {
            'name': 'Damaged Unit', 
            'max_hp': 100,
            'hp': 50,
            'attack': 8
        },
        'dead_unit': {
            'name': 'Dead Unit',
            'max_hp': 100,
            'hp': 0,
            'attack': 0
        }
    }


@pytest.fixture(scope="session")
def project_root():
    """Provide the project root directory path."""
    return Path(__file__).parent.parent


@pytest.fixture
def capture_stdout():
    """Capture stdout for testing print statements."""
    import io
    import sys
    from contextlib import contextmanager
    
    @contextmanager
    def _capture():
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            yield buffer
        finally:
            sys.stdout = old_stdout
    
    return _capture