"""
Infrastructure validation tests to ensure the testing setup works correctly.

These tests validate that:
1. pytest is working
2. fixtures are available 
3. test markers work
4. coverage reporting works
5. mocking capabilities work
"""

import pytest
from unittest.mock import Mock, patch
import tempfile
from pathlib import Path


class TestInfrastructureValidation:
    """Test class to validate the testing infrastructure setup."""
    
    def test_basic_assertion(self):
        """Test basic pytest functionality."""
        assert True
        assert 1 + 1 == 2
        assert "hello" in "hello world"
    
    def test_fixtures_work(self, temp_dir, mock_config, sample_data):
        """Test that shared fixtures are available and working."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test mock_config fixture
        assert isinstance(mock_config, dict)
        assert 'debug' in mock_config
        assert 'test_mode' in mock_config
        assert mock_config['test_mode'] is True
        
        # Test sample_data fixture
        assert 'knight' in sample_data
        assert 'orc' in sample_data
        assert sample_data['knight']['name'] == 'Sir Lancelot'
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that the unit marker works."""
        assert True
    
    @pytest.mark.integration  
    def test_integration_marker(self):
        """Test that the integration marker works."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that the slow marker works."""
        import time
        time.sleep(0.01)  # Very brief sleep for slow test simulation
        assert True
    
    def test_mock_functionality(self, mock_logger):
        """Test that mocking works correctly."""
        # Test the mock logger fixture
        mock_logger.info("Test message")
        mock_logger.info.assert_called_once_with("Test message")
        
        # Test manual mocking
        mock_obj = Mock()
        mock_obj.method.return_value = "mocked"
        assert mock_obj.method() == "mocked"
    
    def test_file_operations(self, temp_dir, temp_file):
        """Test file operations with fixtures."""
        # Test temp_dir
        test_file = temp_dir / "test.txt"
        test_file.write_text("test content")
        assert test_file.read_text() == "test content"
        
        # Test temp_file
        assert temp_file.exists()
    
    @patch('builtins.print')
    def test_patching_works(self, mock_print):
        """Test that patching functionality works."""
        print("This should be mocked")
        mock_print.assert_called_once_with("This should be mocked")
    
    def test_exception_handling(self):
        """Test exception handling in tests."""
        with pytest.raises(ValueError):
            raise ValueError("Test exception")
        
        with pytest.raises(TypeError, match="can only concatenate str"):
            "string" + 5
    
    def test_parametrized_test_example(self):
        """Example of how parametrized tests would work."""
        test_data = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
        ]
        
        for a, b, expected in test_data:
            assert a + b == expected
    
    def test_game_unit_fixture(self, game_unit_data):
        """Test game-specific fixture data."""
        valid_unit = game_unit_data['valid_unit']
        assert valid_unit['name'] == 'Test Unit'
        assert valid_unit['hp'] == valid_unit['max_hp']
        
        damaged_unit = game_unit_data['damaged_unit']
        assert damaged_unit['hp'] < damaged_unit['max_hp']
        
        dead_unit = game_unit_data['dead_unit']
        assert dead_unit['hp'] == 0
    
    def test_project_root_fixture(self, project_root):
        """Test project root fixture."""
        assert project_root.exists()
        assert project_root.is_dir()
        assert (project_root / "pyproject.toml").exists()
    
    def test_capture_stdout_fixture(self, capture_stdout):
        """Test stdout capturing fixture."""
        with capture_stdout() as output:
            print("Hello, World!")
        
        captured = output.getvalue()
        assert "Hello, World!" in captured


def test_function_level_test():
    """Test that function-level tests work (not just class methods)."""
    assert "pytest" == "pytest"


@pytest.mark.unit
def test_standalone_unit_test():
    """Standalone unit test with marker."""
    result = 2 ** 3
    assert result == 8


@pytest.mark.integration
def test_standalone_integration_test():
    """Standalone integration test with marker.""" 
    # This would normally test integration between components
    components = ['component1', 'component2']
    assert len(components) == 2