# Generator-CLI

`generator-cli` is a simple command-line interface (CLI) tool for generating valid Brazilian CPF, CNPJ, and UUID (versions 4 and 6) identifiers. It supports copying generated values directly to your clipboard or printing them to the terminal, with options for formatted or unformatted output.

## Features

- Generate valid **CPF** (Cadastro de Pessoas Físicas)
- Generate valid **CNPJ** (Cadastro Nacional da Pessoa Jurídica)
- Generate **UUID v4** (Universally Unique Identifier version 4)
- Generate **UUID v6** (Universally Unique Identifier version 6)
- Option to copy results to clipboard or print them in the terminal
- Option to generate CPF and CNPJ with or without formatting (punctuation)
- Easy installation and uninstallation

## Installation

### Requirements

Before installing the CLI, ensure you have the following installed:

- **Python 3.x** (check using `python3 --version`)
- **pip3** (Python package manager)

### Installing

1. **Clone the repository** or download the project files:
   ```bash
   git clone https://github.com/thomasalmeida/generator-cli.git
   cd generator-cli
   ```

2. **Run the installation** using the provided `Makefile`:
   ```bash
   make install
   ```

   This will:
   - Install necessary Python dependencies
   - Move the Python script to `/usr/local/bin` so you can use the `generator` command globally

## Usage

Once installed, you can use the `generator` command as follows:

### Generate CPF

- Copy a formatted CPF to the clipboard:
  ```bash
  generator cpf
  ```

- Print a formatted CPF to the terminal:
  ```bash
  generator cpf -p
  ```

- Copy an unformatted CPF to the clipboard:
  ```bash
  generator cpf -n
  ```

- Print an unformatted CPF to the terminal:
  ```bash
  generator cpf -p -n
  ```

### Generate CNPJ

- Copy a formatted CNPJ to the clipboard:
  ```bash
  generator cnpj
  ```

- Print a formatted CNPJ to the terminal:
  ```bash
  generator cnpj -p
  ```

- Copy an unformatted CNPJ to the clipboard:
  ```bash
  generator cnpj -n
  ```

- Print an unformatted CNPJ to the terminal:
  ```bash
  generator cnpj -p -n
  ```

### Generate UUID v4

- Copy the generated UUID v4 to the clipboard:
  ```bash
  generator uuid4
  ```

- Print the UUID v4 to the terminal:
  ```bash
  generator uuid4 -p
  ```

### Generate UUID v6

- Copy the generated UUID v6 to the clipboard:
  ```bash
  generator uuid6
  ```

- Print the UUID v6 to the terminal:
  ```bash
  generator uuid6 -p
  ```

## Command Options

- `-p, --print-only`: Prints the generated identifier to the terminal instead of copying it to the clipboard.
- `-n, --no-format`: (For CPF and CNPJ only) Generates the identifier without punctuation (dots, slashes, and dashes).

These options can be used separately or together.

## Uninstalling

To uninstall the `generator-cli`, run the following command:

```bash
sudo generator uninstall
```

This will remove the binary from `/usr/local/bin`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

