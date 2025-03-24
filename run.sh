#!/bin/bash

OS=$(uname)

case "$OS" in
    "Linux")
        python3 main.py
        ;;
    "Darwin")
        python3 main.py
        ;;
    "CYGWIN"* | "MINGW"* | "MSYS"*)
        python main.py
        ;;
    *)
        echo "Unknown OS"
        exit 1
        ;;
esac
