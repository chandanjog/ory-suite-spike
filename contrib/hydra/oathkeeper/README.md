# Generate JWKS key
```docker run oryd/oathkeeper:v0.38.23-beta.1 credentials generate --alg RS256 > jwks.json```

# Test setup

```
curl http://127.0.0.1:4456/health/alive`
{"status":"ok"}
```

```
curl http://127.0.0.1:4456/health/ready
{"status":"ok"}
```

```
curl http://127.0.0.1:4456/rules
```

# Authorizing requests

curl -X GET http://127.0.0.1:4455/anything/header
{
"args": {},
"data": "",
"files": {},
"form": {},
"headers": {
"Accept": "*/*",
"Accept-Encoding": "gzip",
"Host": "httpbin.org",
"User-Agent": "curl/7.54.0",
"X-User": "guest"
},
"json": null,
"method": "GET",
"origin": "172.17.0.1, 82.135.11.242, 172.17.0.1",
"url": "https://httpbin.org/anything/header/anything/header"
}

# Make request and accept JSON (we get an error response)
curl -H "Accept: application/json" -X GET http://127.0.0.1:4455/anything/deny
{
"error":{
"code":403,
"status":"Forbidden",
"message":"Access credentials aren't sufficient to access this resource"
}
}

# Make request and accept text/* (we get a redirect response).
curl -H "Accept: text/html" -X GET http://127.0.0.1:4455/anything/deny
<a href="https://www.ory.sh/docs">Found</a>.

curl -X GET http://127.0.0.1:4455/anything/id_token
{
"args": {},
"data": "",
"files": {},
"form": {},
"headers": {
"Accept": "*/*",
"Accept-Encoding": "gzip",
"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3N2E2NWE0LTUzM2YtNDFhYi1hODI2LTgxNDliMDM2NDQ0MyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgwMTg1MTcsImlhdCI6MTU1ODAxODQ1NywiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo0NDU1LyIsImp0aSI6IjExNmRiNzhmLTQyMjEtNDU2ZC05OWIzLTY4NGJkMWVjYThjZSIsIm5iZiI6MTU1ODAxODQ1Nywic3ViIjoiZ3Vlc3QifQ.2VKW-oYtzkFGRPgK3sb4iRlObDSzW8PyHzgNiQubppFSlp0bzJLl4Rnt56orJndPqIa7hwsm8YIskf-Wp-FA1piv-aG_XljkUjgilKr3cncMXDP15yDRwZj8g0iVKEhnugQsw_zWf5gMU2YBev2Eyv4xciJxbhrKCat-X8xNT9SvAbwpY-VxQdu_rnpu1GKCA54DyIX6r-Qh5bQPrrT7NvIupA7jJQ23qq83m4C1cQfBgzlhm7dcCuPqKunYKRsc7NZuER3lT6TjkhsF1qhf7o7BZmCnhz6VuH8L8TwMZS8IJWKSjJd8dEKKwxwPkNXOcZO8A3hIO8SZx4Yd7jrONA",
"Host": "httpbin.org",
"User-Agent": "curl/7.54.0"
},
"json": null,
"method": "GET",
"origin": "172.17.0.1, 82.135.11.242, 172.17.0.1",
"url": "https://httpbin.org/anything/id_token/anything/id_token"
}



# Oauth credentials rule 

## Without header
```
curl -X GET http://localhost:4455/oauth-cred-example
{"error":{"code":401,"status":"Unauthorized","message":"Access credentials are invalid"}}
```

## With header values passing client creds 
```
curl -X GET --user oathkeeper:dummy-oathkeeper-secret http://localhost:4455/oauth-cred-example
{"error":{"code":401,"status":"Unauthorized","message":"Access credentials are invalid"}}
```
