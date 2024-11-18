# EPAiV5-Session19
EPAiV5 Session 19 assignment - Classes Part 1

# Smart Device Management System

![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session19/actions/workflows/python-app-1.yml/badge.svg)


## Overview
This project implements a Smart Device Management System in Python, providing a flexible and extensible framework for handling IoT devices. The system includes features for device status tracking, online/offline management, and custom device information handling.

## Features

- Device status management and monitoring
- Online/offline device state tracking
- Custom device information handling through properties
- Type-safe implementation with proper error handling
- Class-level device counting mechanism
- Flexible status parameter updates

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
### Basic Example

```python
# Create a new smart device
device = SmartDevice("Camera", "C-3000")
# Update device status
device.update_status("battery", 80)
# Get device status
battery_level = device.get_status("battery")
# Toggle device online status
device.toggle_online()
# Get device information
print(device.device_info())
```

### Custom Device Info
```python
device = SmartDevice("Lock", "L-1000")
# Define custom device info function
def custom_info():
    return f"Security Device: {device.device_name}"
# Set custom device info
device.device_info = custom_info
```

## Key Classes

### SmartDevice
The main class handling device operations with the following key methods:

- `__init__(part_name, part_model, part_online=False)`: Initialize device
- `update_status(param, value)`: Update device parameters
- `get_status(param)`: Retrieve device parameters
- `toggle_online()`: Toggle device online status
- `reset()`: Reset device status
- `device_info`: Property for custom device information

## Testing

Run tests using pytest:

```bash
pytest test_smart_device.py
```
