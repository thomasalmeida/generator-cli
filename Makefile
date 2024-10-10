# Name of the Python script and installation directories
SCRIPT_NAME=generator.py
TARGET_NAME=generator
INSTALL_PATH=/usr/local/bin/

.PHONY: install

# Check if Python 3 and pip are installed
check-python:
	@which python3 > /dev/null || (echo "Python 3 is not installed. Aborting." && exit 1)
	@which pip3 > /dev/null || (echo "pip3 is not installed. Aborting." && exit 1)

# Install dependencies via pip
install-deps:
	@pip3 install -r requirements.txt

install: check-python install-deps
	@echo "Installing $(TARGET_NAME)..."
	@sudo mv $(SCRIPT_NAME) $(INSTALL_PATH)/$(TARGET_NAME)
	@sudo chmod +x $(INSTALL_PATH)/$(TARGET_NAME)
	@rm -rf Makefile README.md requirements.txt .git
	@echo "$(TARGET_NAME) has been installed. You can now use the '$(TARGET_NAME)' command."

