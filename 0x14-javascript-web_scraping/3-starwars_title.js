#!/usr/bin/node
//star wars
const request = require('request');

const Id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${Id}`;


request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const Data = JSON.parse(body);
      console.log(Data.title);
  }
});
