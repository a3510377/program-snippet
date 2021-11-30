
import asyncio

import discord
from discord.ext import commands
import re


class Help_Cog(commands.Cog, name="幫助類"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(brief="幫助", usage="<指令>")
    async def help(self, ctx, command=None):
        """幫助命令"""
        embed = discord.Embed(title="幫助", colour=ctx.author.colour)
        embeds = []
        for cog_name in list(self.bot.cogs):
            cmd_text = ""
            _embed = discord.Embed(
                title=f"{cog_name}", colour=ctx.author.colour)
            for cmd in self.bot.cogs[str(cog_name)].get_commands():
                _embed.add_field(name=f"**`{aliases if cmd.aliases else cmd}`** **:**",
                                 value=f"{(cmd.brief if cmd.brief else cmd.help) if (cmd.brief if cmd.brief else cmd.help) else '無'}")
                aliases = f"{cmd}"
                for i in cmd.aliases:
                    aliases += f"/{i}"
                cmd_text += f"**`{aliases if cmd.aliases else cmd}`** **:** {(cmd.brief if cmd.brief else cmd.help) if (cmd.brief if cmd.brief else cmd.help) else '無'}\n"
            if cmd_text:
                embed.add_field(name=f"{cog_name}",
                                value=f"{cmd_text}", inline=False)
                embeds.append(_embed)

        # 拜託別刪
        _embed = discord.Embed(title="Help 指令製作 猴子")
        _embed.add_field(name="猴子的 github", value="https://github.com/a3510377/")
        _embed.add_field(name="help command github", value="https://github.com/a3510377/program-snippet")
        embed.append(_embed)

        if command == "*":
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        elif not command:
            await self.check_emoji(ctx, embeds)
        else:
            cmd = self.bot.get_command(command)
            if cmd:
                try:
                    aliases = f"[{cmd}/"
                    for i in cmd.aliases:
                        aliases += f"{i}"
                    aliases += "]"
                    brief = ""
                    if cmd.brief:
                        brief += f"{cmd.brief}\n"
                    embed = discord.Embed(
                        title=f"{aliases if cmd.aliases else cmd}", description=f"{brief}", colour=ctx.author.colour)
                    embed.add_field(
                        name="用法", value=f"{self.bot.prefix}{aliases if cmd.aliases else cmd} {cmd.usage if cmd.usage else ''}", inline=False)
                    try:
                        cmd_help = re.findall(
                            r"https://[A-Za-z0-9/.]*.png", cmd.help)[-1:][0]
                    except:
                        cmd_help = ""
                    else:
                        embed.set_image(
                            url=cmd_help)
                    embed.add_field(
                        name="說明", value=f"{(cmd.help).replace(cmd_help, '')}", inline=False)
                    embed.set_thumbnail(url=self.bot.user.avatar_url)
                    await ctx.send(embed=embed)
                except Exception as err:
                    await ctx.send(err)
            else:
                await ctx.send("無該指令")

    async def check_emoji(self, ctx, embeds):
        max_page = len(embeds) - 1
        message = await ctx.send(embed=embeds[0])
        emojis = ["⏪", "◀️", "▶️", "⏩", "🛑"]
        for emoji in emojis:
            await message.add_reaction(emoji)
        page = 0

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in emojis
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=30, check=check)
                if str(reaction.emoji) == "▶️" and page < max_page:
                    page += 1
                    await message.edit(embed=embeds[page])
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        pass
                elif str(reaction.emoji) == "⏩" and page < max_page:
                    page += 2
                    await message.edit(embed=embeds[page])
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        pass
                elif str(reaction.emoji) == "◀️" and page >= 1:
                    page -= 1
                    await message.edit(embed=embeds[page])
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        pass
                elif str(reaction.emoji) == "⏪" and page >= 1:
                    page -= 2
                    await message.edit(embed=embeds[page])
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        pass
                elif str(message.emoji) == "🛑":
                    await message.clear_reactions()
                    return
            except asyncio.TimeoutError:
                await message.clear_reactions()
                return


def setup(bot: commands.Bot):
    bot.add_cog(Help_Cog(bot))
