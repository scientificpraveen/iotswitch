const http = require('http');
const url = require('url');

// Define the initial state of the pins (D4 - D7)
let pinsState = {
  D4: false,
  D5: false,
  D6: false,
  D7: false
};

// Create an HTTP server
const server = http.createServer((req, res) => {
  const { method, pathname, query } = req;

  if (pathname === '/pins' && method === 'GET') {
    // Return the current state of all pins as JSON
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(pinsState));

  } else if (pathname.startsWith('/pins/') && method === 'PUT') {
    // Extract pin from URL
    const pin = pathname.split('/')[2];
    
    if (pinsState.hasOwnProperty(pin)) {
      let body = '';
      req.on('data', chunk => {
        body += chunk;
      });

      req.on('end', () => {
        const state = JSON.parse(body).state;
        if (state === 'on' || state === 'off') {
          // Update the pin state
          pinsState[pin] = state === 'on';
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ message: `Pin ${pin} is now ${state}` }));
        } else {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ message: 'Invalid state. Use "on" or "off".' }));
        }
      });
    } else {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ message: 'Invalid pin.' }));
    }

  } else {
    // Return 404 for any other routes
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ message: 'Not Found' }));
  }
});

// Start the server
server.listen(5000, () => {
  console.log('Server running at http://167.71.237.12:5000');
});
