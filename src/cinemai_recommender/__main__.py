"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """CinemAIRecommender."""


if __name__ == "__main__":
    main(prog_name="CinemAIRecommender")  # pragma: no cover
