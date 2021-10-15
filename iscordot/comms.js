const config = require('./config.json');
const Discord = require('discord.js');
const prefix = config.prefix;
const versions = config.versions;


// Команды //

function test(robot, mess, args) {
  mess.channel.send("Тест!")
}

function hello(robot, mess, args) {
  mess.reply("Привет!")
}


// Список комманд //

var comms_list = [{
    name: "test",
    out: test,
    about: "Тестовая команда"
  },
  {
    name: "hello",
    out: hello,
    about: "Команда для приветствия!"
  }];

module.exports.comms = comms_list;