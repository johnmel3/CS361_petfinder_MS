# CS361_PetfinderAPI_MS

This microservice makes a call to the Petfinder API and returns pet information in the form of JSON.

## Prerequisites

- Python 3.x
- Flask

## Using the Microservice

### Requesting Data

Information can be fetched from the microservice through several methods, including using a web browser (for simple GET requests) or a command-line tool like `curl`.

#### Web Browser

1. Open a web browser.
2. Enter the full URL into your browser's address bar.
3. The default Flask port is 5000, so in this example, enter [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
4. A GET request to the `/pets` endpoint to retrieve a JSON response with 5 cats: [http://127.0.0.1:5000/pets?type=cat&limit=5](http://127.0.0.1:5000/pets?type=cat&limit=5).

#### Using curl

`curl` is a command-line tool to make web requests. To make the same request as above
using `curl`, you would open a terminal or command prompt and enter the following command:

`curl "http://127.0.0.1:5000/pets?type=cat&limit=5"`

This command performs a GET request to the microservice's `/pets` endpoint with the query
parameters (`type=cat&limit=5`). The microservice processes this request
and returns a JSON response with data on 5 cats, which is displayed in the terminal.