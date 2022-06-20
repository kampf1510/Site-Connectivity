"""This module provides the CLI for Checker."""

import argparse


def read_user_cli_args():
    """Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(
        prog="checker", description="check the availability of websites"
    )
    # Adds ability to pass a URL to the CLI.
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    # Adds functionality to read URLs from a file to the CLI.
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    # Adds asynchronous site-connectivity functionality to the CLI.
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" ')
    else:
        print(f'"Offline?"  \n  Error: "{error}"')
