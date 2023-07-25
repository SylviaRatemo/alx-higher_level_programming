#!/usr/bin/node
// star wars
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
        if (err) {
                return console.log(err);
        }
        const data = JSON.parse(body);
        console.log(data.title);
});
