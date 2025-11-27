# Enigma Hashcat 2025 - Quick Start Guide

## 🚀 Installation

### Option 1: From Source
```bash
# Clone the repository
git clone https://github.com/dragonghidra/enigma.git
cd enigma

# Install dependencies
pip install -r requirements.txt

# Optional: Install for development
pip install -e .
```

### Option 2: Using pip (when published)
```bash
pip install enigma-hashcat
```

## 🎯 Basic Usage

### Check System Capabilities
```bash
python3 hashcat.py --system-info
python3 hashcat.py --benchmark
```

### Dictionary Attack
```bash
python3 hashcat.py --attack-mode dictionary --wordlist rockyou.txt --hash sha256:YOUR_HASH
```

### Mask Attack (Brute Force)
```bash
# 4-digit PIN
python3 hashcat.py --attack-mode mask --mask ?d?d?d?d --hash-file hashes.txt

# 8-character password with uppercase, lowercase, digits
python3 hashcat.py --attack-mode mask --mask ?u?l?l?l?l?d?d?d --hash YOUR_HASH
```

### Hybrid Attack
```bash
# Dictionary words with 2-digit suffix
python3 hashcat.py --attack-mode hybrid --wordlist words.txt --append-mask ?d?d --hash YOUR_HASH
```

## 🚀 Advanced Features

### Rule-Based Attacks
```bash
# Basic rules (case changes, appending digits)
python3 hashcat.py --attack-mode rule --wordlist words.txt --rule-set basic --hash YOUR_HASH

# Advanced rules (leetspeak, character substitution)
python3 hashcat.py --attack-mode rule --wordlist words.txt --rule-set advanced --hash YOUR_HASH

# Leetspeak rules
python3 hashcat.py --attack-mode rule --wordlist words.txt --rule-set leetspeak --hash YOUR_HASH
```

### Combinator Attack
```bash
# Combine words from two different wordlists
python3 hashcat.py --attack-mode combinator --wordlist words1.txt --second-wordlist words2.txt --hash YOUR_HASH
```

### PRINCE Attack
```bash
# Generate password combinations
python3 hashcat.py --attack-mode prince --wordlist words.txt --max-length 8 --hash YOUR_HASH
```

### Markov Chain Attack
```bash
# Generate passwords using statistical model
python3 hashcat.py --attack-mode markov --wordlist words.txt --markov-order 2 --markov-count 1000 --hash YOUR_HASH
```

## 💾 Session Management

### Save and Restore Sessions
```bash
# Save current cracking session
python3 hashcat.py --save-session my_session --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH

# Restore and continue
python3 hashcat.py --restore my_session

# List all sessions
python3 hashcat.py --list-sessions

# Delete a session
python3 hashcat.py --delete-session my_session
```

### Export Results
```bash
# Export to JSON
python3 hashcat.py --export-session results.json --export-format json

# Export to CSV
python3 hashcat.py --export-session results.csv --export-format csv

# Export in hashcat potfile format
python3 hashcat.py --export-session potfile.txt --export-format hashcat
```

## ⚡ Performance Optimization

### Multi-threading
```bash
# Use all available CPU cores
python3 hashcat.py --parallel auto --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH

# Specify number of threads
python3 hashcat.py --parallel 8 --attack-mode mask --mask ?d?d?d?d --hash YOUR_HASH
```

### Memory Management
```bash
# Limit candidate generation
python3 hashcat.py --max-candidates 1000000 --attack-mode hybrid --wordlist words.txt --append-mask ?d?d?d

# Disable status updates for maximum speed
python3 hashcat.py --status-every 0 --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH
```

### Mutation Levels
```bash
# No mutation (fastest)
python3 hashcat.py --mutate none --wordlist curated_words.txt --hash YOUR_HASH

# Simple mutation (case changes, common suffixes)
python3 hashcat.py --mutate simple --wordlist words.txt --hash YOUR_HASH

# Aggressive mutation (leetspeak, extensive modifications)
python3 hashcat.py --mutate aggressive --wordlist words.txt --hash YOUR_HASH
```

## 🎭 Mask Patterns

### Built-in Character Sets
- `?l` = abcdefghijklmnopqrstuvwxyz
- `?u` = ABCDEFGHIJKLMNOPQRSTUVWXYZ  
- `?d` = 0123456789
- `?s` = !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
- `?a` = ?l?u?d?s

### Custom Character Sets
```bash
# Custom lowercase (only a,b,c)
python3 hashcat.py --charset-lower "abc" --mask ?l?l?l?l --hash YOUR_HASH

# Custom digits (only 1,2,3)
python3 hashcat.py --charset-digit "123" --mask ?d?d?d --hash YOUR_HASH

# Custom symbols
python3 hashcat.py --charset-symbol "!@#$" --mask ?s?s?s --hash YOUR_HASH
```

### Common Mask Patterns
```bash
# 8-character password: 1 uppercase, 6 lowercase, 1 digit
python3 hashcat.py --mask ?u?l?l?l?l?l?l?d --hash YOUR_HASH

# 10-character password: mixed case and digits
python3 hashcat.py --mask ?u?l?l?l?d?u?l?l?l?d --hash YOUR_HASH

# Phone number format
python3 hashcat.py --mask ?d?d?d-?d?d?d-?d?d?d?d --hash YOUR_HASH
```

## 🔧 Hash Formats

### Supported Formats

**Simple Hashes:**
```bash
# Algorithm:Digest
sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
md5:5d41402abc4b2a76b9719d911017c592

# Algorithm:Salt:Digest  
sha256:salt:5b3d2c5e5a5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e5a5e
```

**PBKDF2:**
```bash
# Colon format
pbkdf2-sha256:120000:salt:48a99ed11c2f6ce4928ec2ad39db81f8f4d48039c8eed253e9a02f067d7a347c

# Modular format
$pbkdf2-sha256$120000$salt$SKme0RwvbOSSjsKtOduB-PTUgDnI7tJT6aAvBn16NHw
```

**Scrypt:**
```bash
# Colon format
scrypt:16384:8:1:salt:3d47b5c77dee05a144663062b47de0b804e2b3cf15cd10ddb0f97a00776b6196

# Modular format
$scrypt$14$8$1$salt$PUe1x33uBaFEZjBitH3guATis88VzRDdsPl6AHdrYZY
```

**Bcrypt:**
```bash
$2b$12$3DqZavjWLJPe2GvtIL/UiunWx/HqbgSTuRWHKXHs6sp949/G/F7aa
```

**Argon2:**
```bash
$argon2id$v=19$m=65536,t=3,p=2$kXw8azYV6p0LvLb7rSVMyQ$xU4kpGtT7IeyT1g8PK9hZjiIbXUr3ZLez7ayc8Qy3NI
```

## 🎮 GPU Acceleration

### Automatic Detection
```bash
# GPU support is automatically detected and used
python3 hashcat.py --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH
```

### Manual Configuration
```bash
# Force CPU-only mode (if GPU causes issues)
export ENIGMA_FORCE_CPU=1
python3 hashcat.py --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH
```

## 📊 Monitoring and Analysis

### Real-time Status
```bash
# Status updates every 1000 candidates (default)
python3 hashcat.py --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH

# More frequent updates
python3 hashcat.py --status-every 100 --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH

# No status updates (maximum performance)
python3 hashcat.py --status-every 0 --attack-mode dictionary --wordlist words.txt --hash YOUR_HASH
```

### Keep Going Mode
```bash
# Continue after finding first match
python3 hashcat.py --keep-going --attack-mode dictionary --wordlist words.txt --hash-file multiple_hashes.txt
```

## 🛠️ Troubleshooting

### Common Issues

**Missing Dependencies:**
```bash
pip install bcrypt argon2-cffi psutil
```

**GPU Detection Issues:**
```bash
# Check GPU availability
python3 -c "from python.hashcat_like.gpu_acceleration import detect_gpu; print(detect_gpu())"
```

**Memory Issues:**
```bash
# Use smaller batches
python3 hashcat.py --max-candidates 100000 --attack-mode mask --mask ?d?d?d?d?d?d
```

## 🎪 Demo Mode

Run the complete demonstration:
```bash
python3 demo.py
```

## 📚 Additional Resources

- Full documentation: `python3 hashcat.py --help`
- Example files: `python/hashcat_like/example_hashes.txt`
- Source code: GitHub repository
- Issue tracking: GitHub Issues

---

**Enigma Hashcat 2025** - Modern password recovery toolkit for security professionals and researchers.