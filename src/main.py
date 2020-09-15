from discord.ext import commands
import settings
import traceback

DISCORD_TOKEN = settings.DISCORD_TOKEN
COMMAND_PREFIX = settings.COMMAND_PREFIX

INITIAL_EXETENDIONS = [
    'cogs.fetch_message' ,
]


class MyBot(commands.Bot):
    def __init__(self, command_prefix) -> None:
        super().__init__(command_prefix)

        for cog in INITIAL_EXETENDIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()


if __name__ == "__main__":
    bot = MyBot(command_prefix=COMMAND_PREFIX)
    bot.run(settings.TOKEN)