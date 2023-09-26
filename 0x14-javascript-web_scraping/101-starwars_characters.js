#!/usr/bin/node
// print Star Wars movie character names for a given episode
const request = require('request');
const idTitle = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + idTitle;

request(url, function (error, response, body) {
  if (error) return console.error('error:', error);

  const list = JSON.parse(body).characters;
  for (const uri of list) {
    request(uri, function (error1, response1, body1) {
      if (error1) return console.error('error:', error1);
      console.log(JSON.parse(body1).name);
    });
  }
});
