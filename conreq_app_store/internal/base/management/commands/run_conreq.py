from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs all commands needed to safely start Conreq."

    def handle(self, *args, **options):
        port = options["port"]
        verbosity = "-v " + str(options["verbosity"])

        call_command("migrate", "--noinput", verbosity)
        call_command("runserver", f"0.0.0.0:{port}", verbosity)

    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--port",
            help="Select the port number for Conreq to run on.",
            default=8000,
            type=int,
        )
