# -*- coding: utf-8 -*-

import argparse
import subprocess
import sys
from os.path import isdir
from subprocess import CalledProcessError

try:
    from bot import Von
except (ImportError, SyntaxError):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--run", help="run bot", action="store_true")
parser.add_argument("-u", "--upgrade", help="upgrade dependencies", action="store_true")
args = parser.parse_args()


def is_venv():
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def install_dependencies():
    arguments = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]

    if args.upgrade:
        arguments.insert(4, "--upgrade")

    if not is_venv():
        arguments.insert(4, "--user")

    try:
        command = " ".join(arguments)
        subprocess.check_call(command, shell=True)
    except CalledProcessError:
        print("Dependency installation failed.")


def main():
    if not sys.version_info >= (3, 6):
        print("Python 3.6 or above is required to run Von.")
        sys.exit(1)

    print("Installing dependencies...")
    install_dependencies()

    print("Setup complete.")
    if args.run:
        print("Starting bot...")
        Von().run()
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
