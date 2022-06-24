

time.sleep(3)== {
    Channel.send()
        .then( msg = {
print('rain embed configuring...')

def lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

await lib.discord.channels['@0.3.0'].messages.create({
  "channel_id": `${context.params.event.channel_id}`,
  "content": "",
  "tts": false,
  "allowed_mentions": {
    "replied_user": false,
    "parse": [
      "everyone"
    ],
    "roles": [
      "@everyone"
    ],
    "users": [
      "@everyone"
    ]
  },
  "embeds": [
    {
      "type": "rich",
      "title": `a rain has started.`,
      "description": `join now or ur gay`,
      "color": 0x00FFFF,
      "author": {
        "name": `notifier says... `
      },
      "url": `https://www.rblxwild.com`
    }
  ]
});
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
