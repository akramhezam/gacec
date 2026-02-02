#!/bin/bash

# GACECCon Website Startup Script
# This script starts the backend server and opens the website

echo "╔════════════════════════════════════════════════════════╗"
echo "║                                                        ║"
echo "║       Starting GACECCon Website...                     ║"
echo "║                                                        ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 is not installed"
    echo "Please install Python3 to run this application"
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Flask not found. Installing dependencies..."
    pip3 install -r requirements.txt --user
fi

echo "🚀 Starting server..."
echo ""

# Start the Flask server
python3 app.py

# Note: The server will continue running until you press Ctrl+C
