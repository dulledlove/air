
setTimeout( (5) == {
    Channel.send()
        .then( msg = {

#### Create the initial embed object ####
embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)

# Add author, thumbnail, fields, and footer to the embed
embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False) 
embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")


#### Useful ctx variables ####
## User's display name in the server
ctx.author.display_name

## User's avatar URL
ctx.author.avatar_url

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
