#!/usr/bin/node
// character check
const request = require('request');

const url = `${process.argv[2]}`;
const id = '/18/';
request(url, (err, res, body) => {
        if (err) {
                return console.log(err);
        }
	let count = 0;
        const data = JSON.parse(body);
	for (const film of data.results) {
		for (const character of film.characters) {
			count += (character.includes(id) ? 1 :0);
		}
	}
        console.log(count);
});
