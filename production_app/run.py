import click

@click.command()
@click.option('-p', '--port', type=int, default=5000)
def main(port):
    print(port)
    #initialize_app(app)


main()
