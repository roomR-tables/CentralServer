# CentralServer

## Requirements
- Python > 3.6
- virtualenv

## Installation

```bash
# Create an isolated environment
virtualenv --no-site-packages -p $(which python3) venv

# Activate isolated environment
source venv/bin/activate

# Install packages
pip3 install setuptools

# Install dependencies
python setup.py develop

# Start server
venv/bin/pserve serve development.ini
```