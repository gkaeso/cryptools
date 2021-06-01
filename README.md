CRYPTOOLS
---------

A python program encrypting and decrypting messages with basic crypto-algorithms.

_______________

## Objective

The idea behind this app was to:

- create a **REST** API
- create an **asynchronous** app
- use **containerisation**

_______________

## Installation

Requires Python 3.9 and Docker.

Clone this Git repository, then move to the directory and run the following command:
  
    docker-compose up

The Docker service is shut down using the following command:

    docker-compose down

_______________

## Usage

All ciphers expect POST calls.
Request must have a JSON-formatted body. 
Output is a JSON-formatted.

Default port is 5000.

Typical encryption input parameters (inside request body):

    {
        "text": "message to encrypt",
        "encrypt" true,
        "key": 1,             // optional
        "keys": [2,3]         // optional
    }

_N.B._ Optional parameters depend on the cipher to use.

Typical decryption input parameters (inside request body):

    {
        "text": "message to decrypt",
        "encrypt" false,
        "key": 1,             // optional
        "keys": [2,3]         // optional
    }

_N.B._ Optional parameters depend on the cipher to use.

Typical output parameters:

    {
        "text": "ENCRYPTED OR DECRYPTED MESSAGE"
    }

_N.B._ Output text is always in capital letters.

##### Atbash Cipher

Below are examples of use made with Postman.

To call the request handler:
  
    http://localhost:5000/cipher/atbash/

_e.g._

    Input:
    {
        "text": "abc",
        "encrypt": true
    }

    Output: 
    {
        "text": "ZYX"
    }

##### Caesar Cipher

Below are examples of use made with Postman.

To call the request handler:
  
    http://localhost:5000/cipher/caesar/

_e.g._

    Input:
    {
        "text": "abc",
        "key": 3,
        "encrypt": true
    }

    Output: 
    {
        "text": "DEF"
    }

##### Affine Cipher

Below are examples of use made with Postman.

To call the request handler:
  
    http://localhost:5000/cipher/affine/

_e.g._

    Input:
    {
        "text": "message",
        "keys": [3,2],
        "encrypt": true
    }

    Output: 
    {
        "text": "MOEECUO"
    }
_______________

## Technical

Containerisation is made possible with **Docker**.

Asynchronous paradigm implemented using **tornado**.

Unit testing made with **unittest**
Tests made with **Postman**.

_N.B._ All ciphers in the app use JSON as input / output.
