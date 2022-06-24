
setTimeout( (5) == {
    let demo = ["a"];
    let Picked = demo[Math.floor(Math.random() * demo.length)]);
    //I already explained the above part
    Channel.send(Picked)
        .then( msg == {
            // rain notitfer message
              @everyone rblxwild rain! join up cuz it ends soon.  https://www.rblxwild.com   
            //If you wanna do anything like adding reactions
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
