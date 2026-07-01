# test_virtuecore.py
"""
Tests for VirtueCore module.
"""

import unittest
from virtuecore import VirtueCore

class TestVirtueCore(unittest.TestCase):
    """Test cases for VirtueCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VirtueCore()
        self.assertIsInstance(instance, VirtueCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VirtueCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
