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

### Receiving Data 
The microservice will respond with JSON-formatted data representing the requested pets.
Below is an example of what this looks like.

```
{
  "animals": [
    {
      "_links": {
        "organization": {
          "href": "/v2/organizations/ga38"
        },
        "self": {
          "href": "/v2/animals/70825338"
        },
        "type": {
          "href": "/v2/types/dog"
        }
      },
      "age": "Adult",
      "attributes": {
        "declawed": null,
        "house_trained": false,
        "shots_current": true,
        "spayed_neutered": true,
        "special_needs": false
      },
      "breeds": {
        "mixed": true,
        "primary": "Pit Bull Terrier",
        "secondary": null,
        "unknown": false
      },
      "coat": null,
      "colors": {
        "primary": null,
        "secondary": null,
        "tertiary": null
      },
      "contact": {
        "address": {
          "address1": "251 Automation Drive",
          "address2": null,
          "city": "Carrollton",
          "country": "US",
          "postcode": "30117",
          "state": "GA"
        },
        "email": null,
        "phone": "770-214-3590 "
      },
      "description": "Toga is a 7.5 year old Pit mix who is extremely sweet, playful, and loving. Toga loves to smile all...",
      "distance": null,
      "environment": {
        "cats": null,
        "children": null,
        "dogs": null
      },
      "gender": "Male",
      "id": 70825338,
      "name": "Toga",
      "organization_animal_id": "20255945",
      "organization_id": "GA38",
      "photos": [],
      "primary_photo_cropped": null,
      "published_at": "2024-02-23T09:55:46+0000",
      "size": "Medium",
      "species": "Dog",
      "status": "adoptable",
      "status_changed_at": "2024-02-23T09:55:47+0000",
      "tags": [],
      "type": "Dog",
      "url": "https://www.petfinder.com/dog/toga-70825338/ga/carrollton/carroll-county-animal-shelter-ga38/?referrer_id=fd8b497a-af59-458a-b6d9-383b5e2f8682&utm_source=api&utm_medium=partnership&utm_content=fd8b497a-af59-458a-b6d9-383b5e2f8682",
      "videos": []
    }


# UML Diagram

![image](https://github.com/johnmel3/CS361_petfinder_MS/assets/122661573/f8a139af-39e4-485a-9cf1-4ef71f7397ff)

```

