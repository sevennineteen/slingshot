slingshot
=========

Slingshot is a simple wrapper to expose [Pyslinger](https://github.com/sevennineteen/pyslinger) as a service.

This provides a simple HTTP bridge to the CQ loading service, allowing the rest of the migration project to be developed using whatever you like. 

The only requirement is that you write your payloads to files in the Pyslinger-specified JSON format.

## Usage

Send a payload to Slingshot with an HTTP POST like so:

    curl -F payload=@page_example.json http://localhost:5000/

Use `-F` to set additional configurations:


* `cq_server` (defaults to **http://localhost:4502**)
* `username` (defaults to **admin**)
* `password` (defaults to **admin**)
* `static_root` (defaults to **.**)

For example:

    curl -F payload=@asset_example.json -F username=me -F password=P@55w0rd -F static_root=/my/assets http://localhost:5000/