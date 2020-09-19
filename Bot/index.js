// require the discord.js module
const Discord = require('discord.js');
// create a new Discord client
const client = new Discord.Client();


client.login('');
// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
	console.log('Ready!');
});


client.on('message', async message => {
    console.log(message.content);

    if (message.content === '!ping') {
        // send back "Pong." to the channel the message was sent in
        message.channel.send('Pong.');
    }

    if (msg.content === `!test`) {      
        msg.channel.type === (`"dm"`) + msg.author.sendMessage(`hello World`) 
      }
/*
    if (message.member.voice.channel) {
		const connection = await message.member.voice.channel.join();
	}
*/
});

