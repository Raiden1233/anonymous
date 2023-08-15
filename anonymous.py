@Raiden.tree.command(name='anonymous', description='Send message anonymously') # replace name Raiden with the name of your own  bot. 
async def anonymous(interaction: discord.Interaction, message: str):  # Feel free to change the name anonymous to confess.
   em = discord.Embed(title = f'⌦ 𓊈𒆜 ANONYMOUS MESSAGE 𒆜𓊉࿐☠️ ',description = f'** ♡˗ˏ✎ ➔  {message} **\n\n ╰┈➤Volume: ■■■■■□□□' )
   await interaction.channel.send(embed= em)
   await interaction.response.send_message(f'✅ **Your message has been sent anonymously :>**', ephemeral=True)
# Have fun lol.
