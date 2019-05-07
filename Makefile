# META ]--------------------------------------------------------------------------------------------
.PHONY: help.stub help
help.stub: help

RED="\033[91m"
END="\033[0m"

help:
	@echo "help         Display this message."
	@echo "run          Generate a sample spiral"
	@echo "test         Run testing suite."
	@echo "clean        Standardize repository."
	@echo "deps         Install dependencies."

# EXAMPLES ]----------------------------------------------------------------------------------------
.PHONY: run
run:
	python main.py 36 --modulus 6

# CORE ]--------------------------------------------------------------------------------------------
.PHONY: test clean deps

test:
	black --check .
	pylint *.py src

clean:
	black .

deps:
	pip install -r requirements.txt
