const Discord = require('discord.js'); // Подключаем библиотеку discord.js
const robot = new Discord.Client({ intents: ['GUILDS', 'GUILD_MESSAGES']}); // Объявляем, что robot - бот
const comms = require("./comms.js"); // Подключаем файл с командами для бота
const fs = require('fs'); // Подключаем родной модуль файловой системы node.js  
let config = require('./config.json'); // Подключаем файл с параметрами и информацией
let token = config.token; // «Вытаскиваем» из него токен
let prefix = config.prefix; // «Вытаскиваем» из него префикс

robot.on("ready", function() {
  /* При успешном запуске, в консоли появится сообщение «[Имя бота] запустился!» */
  console.log(robot.user.username + " запустился!");
  robot.generateInvite(['ADMINISTRATOR','KICK_MEMBERS', 'BAN_MEMBERS', 'SEND_MESSAGES']).then((link) => { // < //
  console.log("https://discord.com/api/oauth2/authorize?client_id=893621358137856091&permissions=8&scope=bot")  // << //
})});


robot.on('message', (msg) => {
	if(msg.author.username != robot.user.username && msg.author.discriminator != robot.user.discriminator){
    	var comm = msg.content.trim()+" ";
	    var ok = false;
	    var comm_name = comm.slice(0, comm.indexOf(" "));
	    var messArr = comm.split(" ");
	    for(comm_count in comms.comms){
	    	var comm2 = prefix + comms.comms[comm_count].name;
	    	if(comm2 == comm_name){
	    		comms.comms[comm_count].out(robot, msg, messArr);
	    	}
	    }
    } 
});


robot.login(token); // Авторизация бота