import discord
from discord.ext import tasks, commands
from datetime import datetime
import sqlite3
import settings
import time

DB_NAME = settings.DB_NAME

class TaskMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.checker.start()
        self.schedule = []
        # DBセットアップ
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()

    # タスクのチェック
    @tasks.loop(seconds=1.0)
    async def checker(self):
        try:
            self.cur.execute('SELECT * FROM task_schedule')
        except AttributeError:
            time.sleep(20)
        schedule = self.cur.fetchall()
        now = datetime.now()
        for i in schedule:
            if datetime.strptime(i[1], '%Y-%m-%d-%H:%M:%S') < now:
                print(i)
                channel = self.bot.get_channel(int(i[3]))
                await channel.send(int(i[2]))
                self.cur.executemany('DELETE FROM task_schedule WHERE id = (?)', str(i[0]))
        self.conn.commit()

    #タスクの追加
    @commands.command()
    async def add_schedule (self, ctx, *args):
        # 引数のチェック
        if len(args) == 1:
            await ctx.channel.send(f'{ctx.author.mention} 引数がおかしいようです 例: add_schedule 2020-12-31-24:59:59 755450475880644678')

        tstr = args[0]

        # Datetime型に変換
        try:
            tdatetime = datetime.strptime(tstr, '%Y-%m-%d-%H:%M:%S')
        except ValueError:
            await ctx.channel.send(f'{ctx.author.mention} 時刻フォーマットがおかしいです 例:2020-12-31-24:59:59')
            return

        # 指定した日付が過去か確認
        if tdatetime > datetime.now():
            self.schedule.append(args[0])
            db_value = [args[0], args[1], ctx.message.channel.id]
            self.cur.executemany('INSERT INTO task_schedule values(null, ?, ?, ?)', (db_value,))
            await ctx.channel.send(f'{ctx.author.mention} {args[0]}に{args[1]}をチャンネル"{ctx.message.channel.name}"にリマインドします')
        else:
            await ctx.channel.send(f'{ctx.author.mention} 時刻が過去になっています')
            return


    #タスク一覧表示
    @commands.command()
    async def print_schedule(self, ctx):
        self.cur.execute('SELECT * FROM task_schedule')
        all_schedule = self.cur.fetchall()
        print_schedule = []
        for i in all_schedule:
            print_schedule.append(f'{i[1]} {i[2]}')
        await ctx.channel.send(f'{ctx.author.mention} {print_schedule}')

def setup(bot):
    bot.add_cog(TaskMessage(bot))