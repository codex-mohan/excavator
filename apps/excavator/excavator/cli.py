#!/usr/bin/env python

import logging
from rich import print
from rich.logging import RichHandler

# Configure the root logger
logging.basicConfig(
    level="INFO",  # Set the minimum logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(message)s", # RichHandler handles formatting, so we use a simple format here
    datefmt="[%X]", # Format for the time part of the log message
    handlers=[RichHandler()] # Use RichHandler for console output
)

# Get a logger for this module
log = logging.getLogger(__name__)
from typer import Typer

app = Typer()

@app.command()
def hello():
    print("Hello, world!")

@app.command()
def get_env():
    log.info("Getting environment variables")
    import os
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def run():
    """Runs the CLI"""
    log.info("Running CLI")
    app()
    log.info("CLI started")

if __name__ == "__main__":
    run()
