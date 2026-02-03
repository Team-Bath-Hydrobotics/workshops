# Workshop Setup Guide

Welcome! This guide will help you get set up to run the workshop materials.

## Quick Start Options

### Option 1: Binder (No Installation Needed)
Run the notebooks directly in your browser without installing anything:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/YOUR-USERNAME/Hydrobotics-Workshops/main)

Click the badge above to launch the notebooks in Binder. This is the easiest option if you're unfamiliar with Git or Python.

---

### Option 2: Local Setup (Recommended for Development)

#### Prerequisites
- **Python 3.11 LTS** 
- Git (optional, but recommended)

#### Steps

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/Team-Bath-Hydrobotics/workshops.git
   cd Hydrobotics-Workshops
   ```

2. **Create a virtual environment** (recommended)
   
   **On macOS/Linux:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Note:** The requirements file includes compatible versions of OpenCV and NumPy to prevent version conflicts.

4. **Launch Jupyter**
   ```bash
   jupyter notebook
   ```
   
   This will open Jupyter in your browser. Navigate to `workshops/2026/Febuary BCSS Workshop/Tracks/` to find the notebooks.

---

## What's Included

### AI Track
- **Machine Learning**: Object detection introduction with YOLOv8

### Vision Track
- **Depth Estimation**: Stereo vision depth calculation
- **Vision Fundamentals**: Core computer vision concepts
- **Checkerboard**: Camera calibration
- example.txt a file containing example solutions to cells required for the depth estimation task

### System Design Track
- **Architecture**: System design patterns

---

## Troubleshooting

### "pip not found" or "command not found: pip"
Use `python3 -m pip` instead:
```bash
python3 -m pip install -r requirements.txt
```

### Python 3.11 not installed
If you don't have Python 3.11:

**Option A: Using Homebrew (macOS)**
```bash
brew install python@3.11
# Then create venv with:
/usr/local/opt/python@3.11/bin/python3.11 -m venv venv
```

**Option B: Using pyenv**
```bash
pyenv install 3.11.9
pyenv local 3.11.9
python3 -m venv venv
```

**Option C: Download from python.org**
Visit [python.org/downloads](https://www.python.org/downloads/) and install Python 3.11 LTS.

### Segmentation fault / Kernel crash with OpenCV
If you get a crash when running `cv2.findChessboardCornersSB()` or similar:
1. **This is a known OpenCV incompatibility with Python 3.13 on Apple Silicon**
2. Ensure you're using Python 3.11 (not 3.13):
   ```bash
   python3 --version  # Must show 3.11.x
   which python3      # Should show python3.11 path
   ```
3. If you have Python 3.13 installed, uninstall it or create the venv specifically with Python 3.11:
   ```bash
   rm -rf venv
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### NumPy/OpenCV compatibility error
The `requirements.txt` is pre-configured with compatible versions. If you still see errors:
```bash
pip install --upgrade opencv-python
```

### Jupyter won't start
Make sure you've activated the virtual environment and installed all dependencies:
```bash
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
jupyter notebook
```

### Verify Python 3.11 is being used
To confirm you're using the correct Python version:
```bash
python3 --version        # Should show Python 3.11.x
which python3            # Should point to Python 3.11
pip --version            # Should show pip X.X.X from /path/to/python3.11
```

---

## For Instructors

To enable Binder support:
1. Push this repository to GitHub
2. Update the Binder link in this file with your GitHub username and repository name
3. Share the Binder link with participants

Binder automatically builds the environment using `requirements.txt` and `runtime.txt`.

---

## Need Help?

If you encounter issues:
1. **Verify Python 3.11 is installed and active:** `python3 --version`
2. Ensure you've created and activated a virtual environment with Python 3.11
3. Reinstall dependencies: `pip install --upgrade -r requirements.txt`
4. Check that no Python 3.13 is interfering (it will cause OpenCV crashes)
