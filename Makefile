.PHONY: run export_package install

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  run: Run the program"
	@echo "  export_package: Export the package to requirements.txt"
	@echo "  install: Install the package from requirements.txt"

run:
	@echo "Running the program..."
	@python src/main.py

export_package:
	@echo "Exporting the package to requirements.txt..."
	@pip freeze > requirements.txt

install:
	@echo "Installing the package from requirements.txt..."
	@pip install -r requirements.txt
