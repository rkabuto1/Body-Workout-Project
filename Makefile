run:
	@echo "Running Rick Kabuto's Body Workout Generator..."
	@python3 main.py

clean:
	@echo "Cleaning up Python cache and compiled files..."
	@find . -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -name "*.pyo" -exec rm -f {} +

.PHONY: run clean
