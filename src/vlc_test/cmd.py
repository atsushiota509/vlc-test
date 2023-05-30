import subprocess
import click


@click.option('-d', '--dst', type=click.STRING, default="239.255.1.5")
@click.option('-p', '--port', type=click.INT, default=1234)
@click.option('-t', '--ttl', type=click.INT, default=64)
@click.argument('input_file')
@click.command()
def cmd(dst: str, port: int, ttl: int, input_file: str):
    sout = f"'#rtp{{ dst={dst},port={port},mux=ts,ttl={ttl} }}'"
    subprocess.run(["vlc", "-I", "dummy", input_file, "--sout", sout])
