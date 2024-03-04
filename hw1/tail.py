import click
import sys


@click.command()
@click.argument("filenames", type=click.Path(exists=True), nargs=-1, required=False)
def tail(filenames):
    if not filenames:
        lines = sys.stdin.readlines()
        for line in lines[-10:]:
            click.echo(line, nl=False)
    else:
        for filename in filenames:
            if len(filenames) > 1:
                click.echo(f"==> {filename} <==")
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines[-10:]:
                    click.echo(line, nl=False)
            click.echo()


if __name__ == "__main__":
    tail()
