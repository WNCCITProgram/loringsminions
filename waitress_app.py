print("=== WAITRESS_APP.PY STARTUP MARKER ===", flush=True)
import sys
sys.stdout.flush()
"""
Filename: waitress_app.py
Description: This script sets up and runs a Waitress WSGI server
to serve a Flask web application.
"""

from main_app import app
import os
from sys import stdout, path
import logging
import logging.handlers

# Add current directory to path to ensure imports work
path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Get the absolute path to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, "logs")
# Use waitress_app.log as the base so rotated files are waitress_app.log, waitress_app.log.2025-08-19, etc.
LOG_FILE = os.path.join(LOG_DIR, "waitress_app.log")

# Create logs directory
os.makedirs(LOG_DIR, exist_ok=True)

THREADS = 64

# Initialize logger as None - will be set up below
logger = None

# NOW set up logging AFTER main_app import to override its configuration
try:
    # Get or create the waitress logger
    logger = logging.getLogger('waitress_app')
    logger.setLevel(logging.INFO)
    
    # Clear any existing handlers from this logger
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Use TimedRotatingFileHandler so rotated files are waitress_app.log, waitress_app.log.2025-08-19, etc.
    handler = logging.handlers.TimedRotatingFileHandler(
        LOG_FILE, when="midnight", interval=1, backupCount=7, encoding="utf-8"
    )
    
    # Rotated name format: waitress_app.log.2025-08-19
    handler.suffix = "%Y-%m-%d"
    import re
    handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Prevent this logger from propagating to root logger (which main_app might control)
    logger.propagate = False
    
    # Test logging immediately
    logger.info("=== Waitress app logging reconfigured with rotation ===")
    logger.info(f"Script directory: {SCRIPT_DIR}")
    logger.info(f"Current working directory: {os.getcwd()}")
    logger.info(f"Log base file (current): {LOG_FILE}")
    logger.info("Flask app imported successfully")
    
    # Force flush
    handler.flush()
    
except Exception as e:
    print(f"Logging setup failed: {e}")
    # Fallback: create basic console logger
    logger = logging.getLogger('waitress_app_fallback')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(console_handler)
    logger.info("Using fallback console logging due to file logging failure")


def main():
    port = int(os.environ.get("HTTP_PLATFORM_PORT", 8080))
    host = "127.0.0.1"  # Changed from 0.0.0.0 - try localhost only

    try:
        if logger:
            logger.info(f"Starting Waitress server on {host}:{port}")
            logger.info(f"HTTP_PLATFORM_PORT raw: {os.environ.get('HTTP_PLATFORM_PORT', 'NOT SET')}")
            logger.info(f"Host binding: {host}")
        print(f"Starting Waitress server on {host}:{port}", flush=True)
        print(f"HTTP_PLATFORM_PORT: {os.environ.get('HTTP_PLATFORM_PORT', 'NOT SET')}", flush=True)
        print(f"Host: {host}", flush=True)
        print(f"Python PID: {os.getpid()}", flush=True)
    except Exception as e:
        print(f"Logging error: {e}", flush=True)

    try:
        from waitress import serve
        print(f"About to call serve() with app={app}, host={host}, port={port}", flush=True)
        print(f"Calling serve with threads={THREADS}, connection_limit=1000", flush=True)
        stdout.flush()
        
        # Call serve - this blocks until server stops
        serve(
            app,
            host=host,
            port=port,
            threads=THREADS,
            connection_limit=1000,
            channel_timeout=120,
            _start=True  # Ensure server starts immediately
        )
        print("serve() returned (this shouldn't happen)", flush=True)
    except Exception as e:
        import traceback
        error_msg = f"Failed to start Waitress: {e}\n{traceback.format_exc()}"
        try:
            if logger:
                logger.error(error_msg)
        except:
            pass
        print(error_msg, flush=True)
        exit(1)


if __name__ == "__main__":
    try:
        if logger:
            logger.info("Running as main script")
        print("waitress_app.py: Running as main script", flush=True)
    except Exception as e:
        print(f"Startup logging error: {e}", flush=True)
    main()
else:
    try:
        if logger:
            logger.info("Module imported by IIS")
        print("waitress_app.py: Module imported by IIS", flush=True)
    except Exception as e:
        print(f"Import logging error: {e}", flush=True)
