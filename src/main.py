from discord.ext import commands
import settings
import traceback

DISCORD_TOKEN = settings.DISCORD_TOKEN
COMMAND_PREFIX = settings.COMMAND_PREFIX
RUN_MODE = settings.RUN_MODE

# cogsフォルダのみ追加
INITIAL_EXETENDIONS = [
    'cogs.fetch_message' ,
]

# cogs_devフォルダのみ追加
DEV_COGS = [

]

# RUN_MODEがDEVならcogs_devの中身も読む
if RUN_MODE == "DEV":
    INITIAL_EXETENDIONS.append(DEV_COGS)



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
    bot.run(settings.DISCORD_TOKEN)