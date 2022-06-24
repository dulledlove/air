
time.sleep(3)== {
    Channel.send()
        .then( msg = {
print('rain embed configuring...')
embed=discord.Embed(title="a rain has come", url="https://www.rblxwild.com", description="join now or ur gay.")
embed.set_author(name="notifier says...")
embed.add_field(name=" ", value=" ", inline=True)
await ctx.send(embed=embed)

        }
},1000);

//rich presence code

static void UpdatePresence()
{
    DiscordRichPresence discordPresence;
    memset(&discordPresence, 0, sizeof(discordPresence));
    discordPresence.state = "searching the web for rains...";
    discordPresence.startTimestamp = 1507665886;
    discordPresence.endTimestamp = 1507665886;
    discordPresence.largeImageText = "Numbani";
    discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657";
    discordPresence.partyMax = 1;
    discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= ";
    Discord_UpdatePresence(&discordPresence);
}
