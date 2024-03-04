import click
import sys
import os


def file_stat(file):
    lines_cnt, words_cnt, bytes_cnt = 0, 0, 0
    for line in file.readlines():
        lines_cnt += 1
        words_cnt += len(line.split())
        bytes_cnt += len(line.encode())
    return lines_cnt, words_cnt, bytes_cnt


@click.command()
@click.argument("filenames", type=click.Path(exists=True), nargs=-1, required=False)
def wc(filenames):
    lines_total, words_total, bytes_total = 0, 0, 0

    if not filenames:
        lines_total, words_total, bytes_total = file_stat(sys.stdin)
        click.echo(f"{lines_total} {words_total} {bytes_total}")
    else:
        for filename in filenames:
            with open(filename, "r") as file:
                file_lines_cnt, file_words_cnt, file_bytes_cnt = file_stat(file)
            click.echo(
                f"{file_lines_cnt : <5} {file_words_cnt : <5} {file_bytes_cnt : <5} {filename}"
            )
            lines_total += file_lines_cnt
            words_total += file_words_cnt
            bytes_total += file_bytes_cnt

        if len(filenames) > 1:
            click.echo(
                f"{lines_total : <5} {words_total : <5} {bytes_total : <5} total"
            )


if __name__ == "__main__":
    wc()
