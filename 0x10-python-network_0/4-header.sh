#!/bin/bash
# send a GET request with a specific header and display the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
