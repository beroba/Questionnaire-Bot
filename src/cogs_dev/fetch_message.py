import discord
from discord.ext import commands

class FetchMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fetch (self, ctx, *args):
        """ /{COMMAND_PREFIX} fetch {MESSAGE_ID} でメッセージ内容を出力

        - 正常
        /{COMMAND_PREFIX} fetch {MESSAGE_ID}
            >>> Name: {送信者の名前} Message: {メッセージ内容} EMOJI_Count: {絵文字の数} Channel: {送信されたチャンネル名} Time: {送信時刻}

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

        # 引数の受け渡し
        message_id = args[0]

        # 引数が多い
        if 2 <= len(args):
            message = """```Error: There are many arguments
Sample: /{COMMAND_PREFIX} fetch {MESSAGE_ID}```
            """
            await ctx.channel.send(f'{ctx.author.mention} {message}')

        # 引数が足りない
        if 0 == len(args):
            message = """```Error: Not enough arguments
Sample: /{COMMAND_PREFIX} fetch {MESSAGE_ID}```
            """
            await ctx.channel.send(f'{ctx.author.mention} {message}')

        # メッセージの取得
        for i in ctx.guild.text_channels:
            try:
                request_message = await i.fetch_message(message_id)
            except discord.errors.NotFound:
                pass

        # request_messageにメッセージがなければエラー
        try:
            request_message
        except NameError:
            await ctx.channel.send(f'{ctx.author.mention} I\'m sorry I couldn\'t find the message')
            return

        # それぞれの変数に渡す
        request_message_name = request_message.author.display_name
        request_message_content = request_message.content
        request_message_channel = request_message.channel.name
        request_message_time = request_message.created_at

        # 絵文字集計
        reactions = request_message.reactions



        # Emojiが0以上なら集計
        if 0 < len(reactions):
            request_message_reactions = ""
            for i in reactions:
                if i.custom_emoji:
                    request_message_reactions += (i.emoji.name)
                else:
                    request_message_reactions += (i.emoji)
                request_message_reactions += (f' Count:{i.count} ')
            request_message_reactions += f' AllCount:{len(reactions)} '
        else:
            request_message_reactions = 0
        print(f'Name: {request_message_name} Message: {request_message_content} < EMOJI: {request_message_reactions} > Channel: {request_message_channel} Time: {request_message_time}')
        await ctx.channel.send(f'Name: {request_message_name} Message: `{request_message_content}` < EMOJI: {request_message_reactions} > Channel: {request_message_channel} Time: {request_message_time}')

        return



def setup(bot):
    bot.add_cog(FetchMessage(bot))