import click
from setenv import setenv
from setup import setup
from clean import clean


@click.group()
def main():
    pass


commands = [setenv, setup, clean]

for c in commands:
    main.add_command(c)

if __name__ == "__main__":
    main()
