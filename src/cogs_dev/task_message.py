from discord.ext import tasks, commands
import datetime


class TaskMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.checker.start()
        self.schedule_list.start()
        self.schedule = []

    @tasks.loop(seconds=1.0)
    async def checker(self):
        for i in self.schedule:
            if datetime.datetime.strptime(i, '%Y-%m-%d-%H:%M:%S') < datetime.datetime.now():
                print(self.schedule)
                self.schedule.remove(i)

    @tasks.loop(seconds=10.0)
    async def schedule_list(self):
        print(self.schedule)

    @commands.command()
    async def add_schedule (self, ctx, *args):
        tstr = args[0]
        tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d-%H:%M:%S')
        print(tdatetime)
        print(datetime.datetime.now())
        if tdatetime > datetime.datetime.now():
            self.schedule.append(args[0])
            await ctx.channel.send(f'{ctx.author.mention} {args[0]}に設定しました')

        else:
            await ctx.channel.send(f'{ctx.author.mention} "時刻指定がおかしいです(%Y-%m-%d-%H:%M:%S)')

    @commands.command()
    async def print_schedule (self, ctx):
        await ctx.channel.send(f'{ctx.author.mention} {self.schedule}')

def setup(bot):
    bot.add_cog(TaskMessage(bot))