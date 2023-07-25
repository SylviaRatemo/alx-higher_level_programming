#!/usr/bin/node
const request = require('request');

function fetchMovieTitle(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  
  request(url, (err, res, body) => {
    if (err) {
      console.error('Error:', err);
    } else if (res.statusCode !== 200) {
      console.error('Error: Unexpected status code:', res.statusCode);
    } else {
      try {
        const data = JSON.parse(body);
        console.log(data.title);
      } catch (error) {
        console.error('Error parsing JSON:', error.message);
      }
    }
  });
}

// Check if a movie ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide the movie ID as a command-line argument.');
} else {
  const movieId = process.argv[2];
  fetchMovieTitle(movieId);
}

