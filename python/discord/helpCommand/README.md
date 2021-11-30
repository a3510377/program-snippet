# discord py

###### tags: `discord`, `discord bot`, `discord py`, `python`

### 初始化

`python >= 3.8`

### 添加方式

```python
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.load_extension("help")

bot.run("your token")
```

### 備註

由於為較久以前寫的可能有 Bug 請至 dc 群報告( DC 群連結請到[這](/README.md) )
