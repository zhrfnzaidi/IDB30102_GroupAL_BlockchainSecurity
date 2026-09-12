"""
Data Preprocessing Module
Smart Contract Vulnerability Detection
Author: Ahmad Zaim Zharfan bin Mohd Zaidi
Date: September 2026
"""

import os
import re
import json
import numpy as np

def tokenize_source_code(source_code):
    """Tokenize Solidity source code into tokens."""
    tokens = re.findall(r'\w+|[^\w\s]', source_code)
    return tokens

def extract_opcode(bytecode):
    """Extract opcode sequences from EVM bytecode."""
    opcodes = bytecode.split()
    return opcodes

def load_cfg(cfg_file):
    """Load control-flow graph from JSON file."""
    with open(cfg_file, 'r') as f:
        cfg = json.load(f)
    return cfg

def pad_sequence(seq, max_length):
    """Pad sequences to uniform length."""
    if len(seq) < max_length:
        seq = seq + [0] * (max_length - len(seq))
    else:
        seq = seq[:max_length]
    return seq

if __name__ == "__main__":
    print("Data Preprocessing Module - Ready")
