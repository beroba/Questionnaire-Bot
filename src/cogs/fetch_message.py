from discord.ext import commands

class FetchMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fetch (self, ctx, *args):
        """ /{COMMAND_PREFIX} fetch {MESSAGE_ID} でメッセージ内容をPrintf

        - 正常
        /{COMMAND_PREFIX} fetch {MESSAGE_ID}
            >>> Message: {Message} EMOJI_Count: {Number_of_Emojis} Channel: {Guild_Name}.{Channel_Name} Time: {Time}

        - メッセージが見つからない場合
            >>> I'm sorry I couldn't find the message

        - 引数が多い場合
        /{COMMAND_PREFIX} fetch ID AAAA AAAA
            >>> Error: There are many arguments
                Sample: /{COMMAND_PREFIX} fetch {MESSAGE_ID}

        - 引数が足りない場合
        /{COMMAND_PREFIX} fetch
            >>> Error: Not enough arguments
                Sample: /{COMMAND_PREFIX} fetch {MESSAGE_ID}
        """


        return



def setup(bot):
    bot.add_cog(FetchMessage(bot))