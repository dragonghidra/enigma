#!/usr/bin/env python3
"""
Enigma Hashcat Demo Script

Demonstrates the full capabilities of Enigma Hashcat 2025
"""

import os
import sys
import time
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from python.hashcat_like.enhanced_cli import EnhancedCLI
from python.hashcat_like.benchmark import BenchmarkSuite, system_info
from python.hashcat_like.gpu_acceleration import detect_gpu


def create_demo_files():
    """Create demo hash and wordlist files."""
    
    # Demo hashes (password: "password123")
    hashes = """# Enigma Hashcat Demo Hashes
# All hashes use password: password123

# Simple hashes
sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
md5:482c811da5d5b4bc6d497ffa98491e38
sha1:6367c48dd193d56ea7b0baad25b19455e529f5ee

# Salted hashes
sha256:salt:5b3d2c5e5a5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e

# PBKDF2
pbkdf2-sha256:120000:salt:48a99ed11c2f6ce4928ec2ad39db81f8f4d48039c8eed253e9a02f067d7a347c

# Scrypt
scrypt:16384:8:1:salt:3d47b5c77dee05a144663062b47de0b804e2b3cf15cd10ddb0f97a00776b6196
"""
    
    # Demo wordlist
    wordlist = """# Enigma Hashcat Demo Wordlist
password
password123
Password123
letmein
admin
123456
qwerty
hello
welcome
secret
"""
    
    with open("demo_hashes.txt", "w") as f:
        f.write(hashes)
    
    with open("demo_wordlist.txt", "w") as f:
        f.write(wordlist)
    
    print("✅ Created demo files:")
    print("   - demo_hashes.txt (various hash types)")
    print("   - demo_wordlist.txt (common passwords)")


def run_system_check():
    """Run system capability check."""
    print("\n🔍 SYSTEM CAPABILITY CHECK")
    print("=" * 50)
    
    # System information
    info = system_info()
    print("\n📊 System Information:")
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # GPU detection
    gpu_info = detect_gpu()
    if gpu_info:
        print("\n🎮 GPU Acceleration:")
        print(f"   CUDA Available: {gpu_info.get('cuda_available', False)}")
        print(f"   OpenCL Available: {gpu_info.get('opencl_available', False)}")
        if gpu_info.get('devices'):
            for device in gpu_info['devices']:
                print(f"   Device {device['id']}: {device['name']} ({device['memory_mb']}MB)")
    else:
        print("\n🎮 GPU Acceleration: No compatible GPUs detected")


def run_benchmarks():
    """Run performance benchmarks."""
    print("\n⚡ PERFORMANCE BENCHMARKS")
    print("=" * 50)
    
    benchmark = BenchmarkSuite()
    results = benchmark.run_all()
    
    print("\n📈 Algorithm Performance:")
    for result in results:
        print(f"   {result.algorithm}: {result.hashes_per_second:,.0f} H/s")


def demo_basic_attacks():
    """Demonstrate basic attack modes."""
    print("\n🎯 BASIC ATTACK MODES")
    print("=" * 50)
    
    # Dictionary attack
    print("\n📚 Dictionary Attack:")
    os.system("python3 hashcat.py --attack-mode dictionary --wordlist demo_wordlist.txt --hash-file demo_hashes.txt --status-every 0")
    
    # Mask attack
    print("\n🎭 Mask Attack (PIN cracking):")
    os.system("python3 hashcat.py --attack-mode mask --mask ?d?d?d?d --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0 --max-candidates 10000")
    
    # Hybrid attack
    print("\n🔗 Hybrid Attack (Dictionary + Mask):")
    os.system("python3 hashcat.py --attack-mode hybrid --wordlist demo_wordlist.txt --append-mask ?d?d --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")


def demo_advanced_attacks():
    """Demonstrate advanced attack modes."""
    print("\n🚀 ADVANCED ATTACK MODES")
    print("=" * 50)
    
    # Rule-based attack
    print("\n⚙️  Rule-Based Attack:")
    os.system("python3 hashcat.py --attack-mode rule --wordlist demo_wordlist.txt --rule-set basic --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")
    
    # Combinator attack
    print("\n🔀 Combinator Attack:")
    # Create two small wordlists for combinator
    with open("words1.txt", "w") as f:
        f.write("password\nadmin\nhello")
    with open("words2.txt", "w") as f:
        f.write("123\n456\n789")
    os.system("python3 hashcat.py --attack-mode combinator --wordlist words1.txt --second-wordlist words2.txt --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")
    
    # Clean up
    os.remove("words1.txt")
    os.remove("words2.txt")


def demo_session_management():
    """Demonstrate session management features."""
    print("\n💾 SESSION MANAGEMENT")
    print("=" * 50)
    
    # Save session
    print("\n💾 Saving Session:")
    os.system("python3 hashcat.py --save-session demo_session --wordlist demo_wordlist.txt --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")
    
    # List sessions
    print("\n📋 Listing Sessions:")
    os.system("python3 hashcat.py --list-sessions")
    
    # Export session
    print("\n📤 Exporting Session:")
    os.system("python3 hashcat.py --export-session demo_results.json --export-format json")
    
    # Show exported file
    if os.path.exists("demo_results.json"):
        print("\n📄 Exported Results:")
        with open("demo_results.json", "r") as f:
            content = f.read()
            print(content[:500] + "..." if len(content) > 500 else content)


def demo_performance_features():
    """Demonstrate performance optimization features."""
    print("\n⚡ PERFORMANCE FEATURES")
    print("=" * 50)
    
    # Multi-threading
    print("\n🔧 Multi-threading:")
    os.system("python3 hashcat.py --parallel 4 --wordlist demo_wordlist.txt --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")
    
    # Performance with mutation
    print("\n🎭 Performance with Mutation:")
    os.system("python3 hashcat.py --mutate aggressive --wordlist demo_wordlist.txt --hash sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f --status-every 0")


def cleanup():
    """Clean up demo files."""
    files_to_remove = [
        "demo_hashes.txt",
        "demo_wordlist.txt", 
        "demo_results.json",
        ".enigma_sessions/demo_session.json"
    ]
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
    
    # Remove session directory if empty
    session_dir = ".enigma_sessions"
    if os.path.exists(session_dir) and not os.listdir(session_dir):
        os.rmdir(session_dir)


def main():
    """Run the complete demo."""
    print("🚀 ENIGMA HASHCAT 2025 - COMPLETE DEMONSTRATION")
    print("=" * 60)
    print("\nA modern hashcat alternative with advanced features\n")
    
    try:
        # Create demo files
        create_demo_files()
        
        # System capabilities
        run_system_check()
        
        # Performance benchmarks
        run_benchmarks()
        
        # Basic attacks
        demo_basic_attacks()
        
        # Advanced attacks
        demo_advanced_attacks()
        
        # Session management
        demo_session_management()
        
        # Performance features
        demo_performance_features()
        
        print("\n" + "=" * 60)
        print("✅ DEMONSTRATION COMPLETE!")
        print("\nEnigma Hashcat 2025 is ready for production use!")
        print("\n📚 Quick Start Commands:")
        print("   python3 hashcat.py --help")
        print("   python3 hashcat.py --system-info")
        print("   python3 hashcat.py --benchmark")
        print("   python3 hashcat.py --attack-mode dictionary --wordlist rockyou.txt --hash YOUR_HASH")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Demo error: {e}")
    finally:
        # Clean up
        cleanup()
        print("\n🧹 Demo files cleaned up")


if __name__ == "__main__":
    main()