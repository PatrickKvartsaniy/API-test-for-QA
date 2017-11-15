# API-test-for-QA

Steps:

1. Download or clone repository.
2. pip3 install -r requirements.txt
3. Run app (python3 api.py). ==> Of course you need python3
4. QA!

!!!Example!!! usage

$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader

GET the list

$ curl http://localhost:5000/weather
>>(weather list here)

GET a single city weather

$ curl http://localhost:5000/weather/Kyiv
>> (Kyiv weather here)

DELETE a city

$ curl http://localhost:5000/weather/<city_name> -X DELETE -v

> DELETE /weather/city_name HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.8.3 Python/3.5.5
< Date: Mon, 01 Oct 2012 22:10:32 GMT

Add a new city weather

$ curl http://localhost:5000/weather -d "<city_name>=(new city weather)" -X POST -v

> POST /weather HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 25
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:12:58 GMT
<
* Closing connection #0
{<city_name>: "New city weather"}

Update a task

$ curl http://localhost:5000/weather/<city_name> -d "<city_name>=something new" -X PUT -v

> PUT /weather/<city_name> HTTP/1.1
> Host: localhost:5000
> Accept: */*
> Content-Length: 20
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.8.3 Python/2.7.3
< Date: Mon, 01 Oct 2012 22:13:00 GMT
<
* Closing connection #0
{"<city_name>=something new"}
