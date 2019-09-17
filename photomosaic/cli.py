import sys
import subprocess
import click
from photomosaic.api import mosaicfy, is_animated


def _get_default_open():
    platform = 'linux' if 'linux' in sys.platform.lower() else sys.platform.lower()
    return {
        'linux': 'eog',
        'darwin': 'open -a safari'
    }.get(platform, 'open')


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--tile_size', default=8)
@click.option('--scale', default=1)
@click.option('--output_file')
@click.option('--show/--no-show', default=False)
@click.option('--open_with', default=_get_default_open())
def cli(filename, **kwargs):
    show = kwargs.pop('show', False)
    result = mosaicfy(filename, **kwargs)
    if show:
        if is_animated(filename):
            cmd = f'{kwargs.get("default_open", _get_default_open())} {result.gif_path}'
            subprocess.run(cmd.split())
        else:
            result.image.show()


if __name__ == '__main__':
    cli()
