#!/usr/bin/env python3
"""
Migration Engine - Main Entry Point

Command-line tool for migrating CSV data to PostgreSQL with ETL pipeline.
"""

from src.cli import cli

if __name__ == '__main__':
    cli()