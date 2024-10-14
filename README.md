# Web Crawler API

## Overview

This project implements a web crawler that is triggered by an API call to a web service. It takes two parameters: a root webpage to crawl and the depth to which to crawl. The API returns a JSON object with the crawled links up to the specified depth. 

## Features

- Trigger a web crawl through an API endpoint.
- Specify the root webpage and depth as parameters.
- Receive crawled links in a structured JSON format.

## API Contract

### Endpoint
POST /api/crawl


### Request Parameters

| Parameter | Type   | Description                        |
|-----------|--------|------------------------------------|
| `url`     | string | The root webpage to crawl.         |
| `depth`   | int    | The depth of crawling (0 for root only). |

### Example Request

```bash
curl -X POST "http://your-api-url/api/crawl" \
-H "Content-Type: application/json" \
-d '{"url": "https://stackoverflow.com", "depth": 2}'
```
### Example Response
{"items":[{"tags":["python"],"owner":{"account_id":25871006,"reputation":35,"user_id":19601890,"user_type":"registered","profile_image":"https://lh3.googleusercontent.com/a-/AFdZucqa63vWkl7_sK2Iuq720Na-Gk5oe3ufAgOzVlx6=k-s256","display_name":"SUMIT SINGH","link":"https://stackoverflow.com/users/19601890/sumit-singh"},"is_answered":false,"view_count":23,"closed_date":1728918869,"answer_count":0,"score":-3,"last_activity_date":1728925962,"creation_date":1728918306,"last_edit_date"...

