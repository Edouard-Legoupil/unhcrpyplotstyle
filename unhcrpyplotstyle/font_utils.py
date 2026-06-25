"""
Font utility functions for UNHCR plot styles.

Handles font fallback when Lato is not available.
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Font fallback mechanism
FONT_FAMILY = None

def setup_font_fallback():
    """Set up font fallback mechanism for Lato font."""
    global FONT_FAMILY
    
    # Try to use Lato first
    try:
        # Check if Lato is available
        plt.rcParams['font.family'] = 'lato'
        plt.rcParams['font.sans-serif'] = ['Lato', 'DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif']
        FONT_FAMILY = 'lato'
        return 'lato'
    except Exception:
        pass
    
    # Fallback to Arial (more widely available)
    try:
        plt.rcParams['font.family'] = 'arial'
        plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica', 'sans-serif']
        FONT_FAMILY = 'arial'
        return 'arial'
    except Exception:
        pass
    
    # Final fallback to sans-serif
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Helvetica', 'Arial', 'sans-serif']
    FONT_FAMILY = 'sans-serif'
    return 'sans-serif'

def get_current_font():
    """Return the current font family being used."""
    return FONT_FAMILY

def check_lato_available():
    """Check if Lato font is available on the system."""
    try:
        # Try to actually use the font to verify it's available
        test_fig, test_ax = plt.subplots()
        test_ax.set_title('Test', fontname='Lato')
        plt.close(test_fig)
        return True
    except Exception:
        return 'Lato' in [f.name for f in fm.fontManager.ttflist]

def install_lato_instructions():
    """Return instructions for installing Lato font."""
    instructions = """
    Lato Font Installation Instructions:
    
    Linux (Debian/Ubuntu):
        sudo apt-get install fonts-lato
    
    Linux (Fedora/RHEL):
        sudo dnf install lato-fonts
    
    macOS (Homebrew):
        brew install --cask font-lato
    
    Windows:
        1. Download Lato font from https://www.latofonts.com/
        2. Right-click the .ttf files and select "Install"
    
    After installing, restart your Python kernel or session.
    """
    return instructions

# Set up font fallback when module is imported
setup_font_fallback()