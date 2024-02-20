#!/usr/bin/node

const request = require('request');
const num = process.argv[2];
request('http://swapi.co/api/films/' + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
