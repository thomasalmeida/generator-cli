#!/usr/bin/env python3

import click
import os
import shutil
import sys
import random
import pyperclip
import time

INSTALL_DIR = "/usr/local/bin/generator"

def generate_cpf(formatted=True):
    base_numbers = [random.randint(0, 9) for _ in range(9)]

    total_sum = sum((10 - i) * base_numbers[i] for i in range(9))
    first_digit = (total_sum * 10 % 11) % 10
    base_numbers.append(first_digit)

    total_sum = sum((11 - i) * base_numbers[i] for i in range(10))
    second_digit = (total_sum * 10 % 11) % 10
    base_numbers.append(second_digit)

    cpf = ''.join(map(str, base_numbers))

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if formatted else cpf

def generate_cnpj(formatted=True):
    base_numbers = [random.randint(0, 9) for _ in range(12)]

    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total_sum = sum(base_numbers[i] * weights[i] for i in range(12))
    first_digit = 11 - (total_sum % 11)
    first_digit = 0 if first_digit > 9 else first_digit
    base_numbers.append(first_digit)

    weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total_sum = sum(base_numbers[i] * weights[i] for i in range(13))
    second_digit = 11 - (total_sum % 11)
    second_digit = 0 if second_digit > 9 else second_digit
    base_numbers.append(second_digit)

    cnpj = ''.join(map(str, base_numbers))

    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}" if formatted else cnpj

def generate_uuid4():
    hex_chars = '0123456789abcdef'
    uuid = ''.join(random.choice(hex_chars) for _ in range(32))
    return f"{uuid[:8]}-{uuid[8:12]}-4{uuid[13:16]}-{uuid[16:20]}-{uuid[20:]}"

def generate_uuid6():
    timestamp = int(time.time() * 1000000)  # Microseconds since epoch
    timestamp_hex = format(timestamp, '012x')
    clock_seq = random.randint(0, 0x3fff)  # 14-bit clock sequence
    node = random.randint(0, 0xffffffffffff)  # 48-bit node ID
    uuid = f"{timestamp_hex[:8]}-{timestamp_hex[8:12]}-6{timestamp_hex[12:15]}-{format(clock_seq | 0x8000, '04x')}-{format(node, '012x')}"
    return uuid

@click.group()
def generator():
    """CLI tool to generate valid CPF, CNPJ, UUID v4, and UUID v6."""
    pass

@generator.command()
@click.option('-p', '--print-only', is_flag=True, help='Prints the CPF to the terminal instead of copying it.')
@click.option('-n', '--no-format', is_flag=True, help='Generates the CPF without punctuation.')
def cpf(print_only, no_format):
    """Generates a valid CPF."""
    cpf_number = generate_cpf(formatted=not no_format)
    if print_only:
        click.echo(cpf_number)
    else:
        pyperclip.copy(cpf_number)
        click.echo("CPF copied to clipboard!")

@generator.command()
@click.option('-p', '--print-only', is_flag=True, help='Prints the CNPJ to the terminal instead of copying it.')
@click.option('-n', '--no-format', is_flag=True, help='Generates the CNPJ without punctuation.')
def cnpj(print_only, no_format):
    """Generates a valid CNPJ."""
    cnpj_number = generate_cnpj(formatted=not no_format)
    if print_only:
        click.echo(cnpj_number)
    else:
        pyperclip.copy(cnpj_number)
        click.echo("CNPJ copied to clipboard!")

@generator.command()
@click.option('-p', '--print-only', is_flag=True, help='Prints the UUID v4 to the terminal instead of copying it.')
def uuid4(print_only):
    """Generates a UUID version 4."""
    uuid_v4 = generate_uuid4()
    if print_only:
        click.echo(uuid_v4)
    else:
        pyperclip.copy(uuid_v4)
        click.echo("UUID v4 copied to clipboard!")

@generator.command()
@click.option('-p', '--print-only', is_flag=True, help='Prints the UUID v6 to the terminal instead of copying it.')
def uuid6(print_only):
    """Generates a UUID version 6."""
    uuid_v6 = generate_uuid6()
    if print_only:
        click.echo(uuid_v6)
    else:
        pyperclip.copy(uuid_v6)
        click.echo("UUID v6 copied to clipboard!")

@generator.command()
def uninstall():
    """Uninstalls the generator CLI."""
    if os.geteuid() != 0:
        click.echo("Please run this command as root (use sudo).")
        sys.exit(1)

    click.confirm("Are you sure you want to uninstall the generator CLI?", abort=True)

    # Remove the script directory
    if os.path.exists(INSTALL_DIR):
        shutil.rmtree(INSTALL_DIR)
        click.echo(f"Removed binary: {INSTALL_DIR}")

    click.echo("Uninstallation complete.")

if __name__ == '__main__':
    generator()
