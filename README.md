# Crypto Bud

A mood based crypto tracking application. The main repository is private.
I am creating the API before I connect everything to the main repository.

Intending on keeping the API public so that anyone can use. 
For now I use a third part API to get the price - and it might look redundant, but I'll replace it with my code soon. Once I get the framework down.

## How to run

Prepping

Create a creds.py file in the root directory, and specify the API key in apikey variable 
(This will change soon enough once I add my own code instead of the third party API)

Running

- docker build -t <tagname> .
- docker run -p 8000:8000 <tagname>
  
Use postman or directly browse to the URL
https://127.0.0.1:8000
