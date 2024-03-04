import click
import sys


@click.command()
@click.argument("filenames", type=click.Path(exists=True), nargs=-1, required=False)
def nl(filenames):
    if not filenames:
        for i, line in enumerate(sys.stdin, start=1):
            click.echo(f"{i : <5}{line}", nl=False)
    else:
        start = 1
        for filename in filenames:
            with open(filename, "r") as file:
                for i, line in enumerate(file.readlines(), start=start):
                    click.echo(f"{i : <5}{line}", nl=False)
            start = i + 1


if __name__ == "__main__":
    nl()
