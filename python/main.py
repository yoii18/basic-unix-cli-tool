import os
import click

def line_count(files):
    for file in files:
        with open(file, 'r') as fp:
            lines = len(fp.readlines())
        res = f"{lines} {file}"
        click.echo(res)

def file_size(files, size):
    for file in files:
        filesize = os.path.getsize(file)
        res = f"{filesize} {file}"
        click.echo(res)

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option(
    '--size',
    '-s',
    'get_bytes',
    is_flag=True
)
@click.option(
    '--line-count',
    '-l',
    'get_lines',
    is_flag=True
)
def final(files, get_bytes, get_lines):
    if get_bytes:
        file_size(files, size)
    if get_lines:
        line_count(files)


if __name__ == '__main__':
    final()