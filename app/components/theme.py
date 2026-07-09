"""Theme manager for Systemic Tau Platform."""

from __future__ import annotations

import streamlit as st
from pathlib import Path
import re

CONFIG_PATH = Path(".streamlit/config.toml")

LIGHT_COLORS = {
    "--stp-navy": "#0D4F6B",
    "--stp-deep": "#1A2332",
    "--stp-teal": "#1A8A8A",
    "--stp-teal-soft": "#E6F5F5",
    "--stp-purple": "#5B4B8A",
    "--stp-purple-soft": "#F0ECF7",
    "--stp-sand": "#F4F1EA",
    "--stp-sand-2": "#EBE6DC",
    "--stp-alert": "#C45C26",
    "--stp-bg": "#F7F8FA",
    "--stp-surface": "#FFFFFF",
    "--stp-border": "#E4E9EF",
    "--stp-border-strong": "#D0D7DE",
    "--stp-muted": "#5B6775",
    "--stp-muted-2": "#8B95A1",
    "--stp-success": "#1B7A4E",
    "--stp-radius": "14px",
    "--stp-radius-sm": "10px",
    "--stp-radius-lg": "20px",
    "--stp-shadow": "0 4px 20px rgba(26, 35, 50, 0.06)",
    "--stp-shadow-md": "0 10px 36px rgba(13, 79, 107, 0.12)",
    "--stp-shadow-lg": "0 18px 48px rgba(13, 79, 107, 0.16)",
}

DARK_COLORS = {
    "--stp-navy": "#0F172A", 
    "--stp-deep": "#F8FAFC", 
    "--stp-teal": "#06B6D4", 
    "--stp-teal-soft": "rgba(6, 182, 212, 0.15)",
    "--stp-purple": "#A855F7", 
    "--stp-purple-soft": "rgba(168, 85, 247, 0.15)",
    "--stp-sand": "#1E293B", 
    "--stp-sand-2": "#334155", 
    "--stp-alert": "#F43F5E", 
    "--stp-bg": "#0B1120", 
    "--stp-surface": "rgba(30, 41, 59, 0.6)", 
    "--stp-border": "rgba(255, 255, 255, 0.1)",
    "--stp-border-strong": "rgba(255, 255, 255, 0.2)",
    "--stp-muted": "#CBD5E1",  # Fixed contrast issue: Bright Slate for text
    "--stp-muted-2": "#94A3B8",
    "--stp-success": "#10B981", 
    "--stp-radius": "14px",
    "--stp-radius-sm": "10px",
    "--stp-radius-lg": "20px",
    "--stp-shadow": "0 4px 20px rgba(0, 0, 0, 0.3)",
    "--stp-shadow-md": "0 8px 32px rgba(6, 182, 212, 0.15)",
    "--stp-shadow-lg": "0 12px 48px rgba(168, 85, 247, 0.15)",
}

def get_current_theme_base() -> str:
    """Returns 'dark' or 'light'."""
    if not CONFIG_PATH.exists():
        return "light"
    content = CONFIG_PATH.read_text()
    match = re.search(r'base\s*=\s*"(.*?)"', content)
    if match:
        return match.group(1)
    return "light"

def toggle_theme(is_dark: bool) -> None:
    if not CONFIG_PATH.exists():
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        content = '[theme]\nbase = "light"\nprimaryColor = "#1A8A8A"\nbackgroundColor = "#F7F8FA"\nsecondaryBackgroundColor = "#F4F1EA"\ntextColor = "#1A2332"\nfont = "sans serif"\n'
    else:
        content = CONFIG_PATH.read_text()
        
    if is_dark:
        content = re.sub(r'base\s*=\s*".*"', 'base = "dark"', content)
        content = re.sub(r'primaryColor\s*=\s*".*"', 'primaryColor = "#06B6D4"', content)
        content = re.sub(r'backgroundColor\s*=\s*".*"', 'backgroundColor = "#0B1120"', content)
        content = re.sub(r'secondaryBackgroundColor\s*=\s*".*"', 'secondaryBackgroundColor = "#111827"', content)
        content = re.sub(r'textColor\s*=\s*".*"', 'textColor = "#F8FAFC"', content)
    else:
        content = re.sub(r'base\s*=\s*".*"', 'base = "light"', content)
        content = re.sub(r'primaryColor\s*=\s*".*"', 'primaryColor = "#1A8A8A"', content)
        content = re.sub(r'backgroundColor\s*=\s*".*"', 'backgroundColor = "#F7F8FA"', content)
        content = re.sub(r'secondaryBackgroundColor\s*=\s*".*"', 'secondaryBackgroundColor = "#F4F1EA"', content)
        content = re.sub(r'textColor\s*=\s*".*"', 'textColor = "#1A2332"', content)
        
    CONFIG_PATH.write_text(content)
    st.rerun()

def inject_theme_css() -> None:
    """Injects the dynamic CSS variables based on the active theme."""
    is_dark = get_current_theme_base() == "dark"
    colors = DARK_COLORS if is_dark else LIGHT_COLORS
    
    vars_css = "\n".join([f"  {k}: {v};" for k, v in colors.items()])
    
    # We also inject font family here to ensure it applies globally
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    :root {{
{vars_css}
    }}
    * {{
        font-family: var(--stp-font);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
