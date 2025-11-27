"""
Basic functionality tests for Enigma Hashcat
"""

import unittest
import tempfile
import os
from pathlib import Path

# Add the project root to Python path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from python.hashcat_like.core import parse_hash_line, load_hashes, SimpleHashTarget
from python.hashcat_like.attacks import wordlist_candidates, mask_candidates, DEFAULT_CHARSETS


class TestBasicFunctionality(unittest.TestCase):
    """Test basic hashcat functionality."""
    
    def test_hash_parsing(self):
        """Test hash parsing functionality."""
        # Test simple hash
        target = parse_hash_line("sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f")
        self.assertIsInstance(target, SimpleHashTarget)
        self.assertEqual(target.algorithm, "sha256")
        
        # Test with salt
        target = parse_hash_line("sha256:salt:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f")
        self.assertEqual(target.algorithm, "sha256")
        self.assertEqual(target.salt, b"salt")
    
    def test_wordlist_candidates(self):
        """Test wordlist candidate generation."""
        # Create temporary wordlist
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("password\n123456\nadmin\n")
            wordlist_path = f.name
        
        try:
            candidates = list(wordlist_candidates([wordlist_path], mutate_mode="none"))
            self.assertIn("password", candidates)
            self.assertIn("123456", candidates)
            self.assertIn("admin", candidates)
        finally:
            os.unlink(wordlist_path)
    
    def test_mask_candidates(self):
        """Test mask candidate generation."""
        candidates = list(mask_candidates("?d?d?d", DEFAULT_CHARSETS))
        self.assertIn("000", candidates)
        self.assertIn("123", candidates)
        self.assertIn("999", candidates)
        self.assertEqual(len(candidates), 1000)
    
    def test_hash_loading(self):
        """Test loading hashes from file."""
        # Create temporary hash file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("# This is a comment\n")
            f.write("sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f\n")
            f.write("sha1:5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8\n")
            hash_file_path = f.name
        
        try:
            targets = load_hashes([], [hash_file_path], default_algorithm=None)
            self.assertEqual(len(targets), 2)
            self.assertEqual(targets[0].algorithm, "sha256")
            self.assertEqual(targets[1].algorithm, "sha1")
        finally:
            os.unlink(hash_file_path)


if __name__ == '__main__':
    unittest.main()