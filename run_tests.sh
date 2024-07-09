#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the test suite
pytest tests/test_app.py

# Capture the exit code of the pytest command
EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

# Return the exit code
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
