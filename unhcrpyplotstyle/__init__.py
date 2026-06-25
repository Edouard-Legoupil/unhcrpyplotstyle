"""
UNHCR Python Plot Style Package

Provides Matplotlib styles following the UNHCR Data Visualization Guidelines.
"""

# Import font utilities
from .font_utils import setup_font_fallback, get_current_font, check_lato_available, install_lato_instructions

# Set up font fallback when package is imported
font_used = setup_font_fallback()

# Package information
__version__ = "0.2.0"
__author__ = "UNHCR Data Visualization Team"
__license__ = "MIT"
__description__ = "Matplotlib styles following UNHCR Data Visualization Guidelines"

# Print font info on import
print(f"UNHCR Plot Style v{__version__} loaded")
print(f"Using font: {font_used}")
if font_used != "lato":
    print("Note: Lato font not found. Using fallback font.")
    print("Install Lato for best results: https://www.latofonts.com/")
