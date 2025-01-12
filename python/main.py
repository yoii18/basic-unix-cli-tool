import os
import click

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option(
    '--filename',
    is_flag=True
)
def file_size(files, filename):
    print(files)
    for file in files:
        filesize = os.path.getsize(file)
        res = f"{filesize} {file}"
        click.echo(res)
    #print(os.path.abspath(file))

if __name__ == '__main__':
    file_size()