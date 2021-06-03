import click


@click.group("plotnft", short_help="Manage your plot NFTs")
def plotnft_cmd() -> None:
    pass


@plotnft_cmd.command("show", short_help="Show plotnft information")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=None, show_default=True, required=False)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def show_cmd(wallet_rpc_port: int, fingerprint: int, id: int) -> None:
    import asyncio
    from .wallet_funcs import execute_with_wallet
    from .plotnft_funcs import show

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, {"id": id}, show))


@plotnft_cmd.command("create", short_help="Create a plot NFT")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-u", "--pool_url", help="HTTPS host:port of the pool to join", type=str, required=True)
def create_cmd(wallet_rpc_port: int, fingerprint: int, pool_url: str) -> None:
    import asyncio
    from .wallet_funcs import execute_with_wallet
    from .plotnft_funcs import create

    extra_params = {"pool_url": pool_url}
    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, create))