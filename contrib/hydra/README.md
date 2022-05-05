# ORY Kratos as Login Provider for ORY Hydra

**Warning: ** this is a preliminary example and will properly be implemented in ORY Kratos directly.

For now, to run this example execute:

```shell script
$ docker-compose up --build
```

Next, create an OAuth2 Client

```shell script
$ docker-compose exec hydra \
    hydra clients create \
    --endpoint http://127.0.0.1:4445 \
    --id auth-code-client \
    --secret secret \
    --grant-types authorization_code,refresh_token \
    --response-types code,id_token \
    --scope openid,offline \
    --callbacks http://127.0.0.1:5555/callback
```

and perform an OAuth2 Authorize Code Flow

```shell script
$ docker-compose exec hydra \
    hydra token user \
    --client-id auth-code-client \
    --client-secret secret \
    --endpoint http://127.0.0.1:4444/ \
    --port 5555 \
    --scope openid,offline
```

Next, create an OAuth2 Client for Client Credentials Flow
```shell script
$ docker-compose exec hydra \
    hydra clients create \
    --endpoint http://127.0.0.1:4445 \
    --id oathkeeper \
    --secret dummy-oathkeeper-secret \
    --grant-types client_credentials \
    --scope \
    --response-types token 
    
```
# client credentials authenticator
```shell script
curl -X GET --user oathkeeper:dummy-oathkeeper-secret http://localhost:4455/anything/oauth-cred-example
```
# jwt authenticator
```shell script
curl -X GET -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNjMzA0MGUwLTNmN2ItNDRmYS04OWZiLTRmODNiMDg0MTU2ZCIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiaHR0cHM6Ly9teS1iYWNrZW5kLXNlcnZpY2Uvc29tZS9lbmRwb2ludCJdLCJleHAiOjE2NTE3MDA3NzIsImlhdCI6MTY1MTcwMDcxMiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo0NDU1IiwianRpIjoiZWUwMzNiZDUtMjE2MC00OWQ0LWFlYzItOGEwZGY3YTQyM2Q2IiwibmJmIjoxNjUxNzAwNzEyLCJzZXEtYWNjb3VudC1pZCI6ImJhciIsInN1YiI6Im9hdGhrZWVwZXIifQ.FVUUr8bPEC93gABRDMbOMXrOlXHKpVe6Tw__H0yd1BBTwye04ZUkCIqa_7x7LvGNnqvAQzS5Aa2XtyorHY-X57RJnvg6vQg9EIm83nc3WQ3kIr3Xrzkcq_NOCn8dSx2x9lArbqo_ktpnaSfZuMQ6AcM5CQcTLflgGBXgIKK4gzwmMGluGLZmFSneGtd9o3JnltFqGR1c5MPznD0oSTmLUcHNqDZ7b8SKHot9k80RVHj-7hn4_YBigz2eqQ8CTmr2fbgtQBrP-0mJ4eCJBg8g-i0tSZ55o9E2VLWLZbDAh2jj7vUtajNXVcHmkCZW6yuZu6nQpQORnpwc373mkouH-A' http://localhost:4455/anything/oauth-cred-example
```

# Oauth introspection
```shell script

curl -X GET -H 'Authorization: Bearer r3zZsaPoP-c0SyBXMZGicot7Ts634FHcxak1_kPCD9U.xFeMn7ZBDHsv-jYskj95O6WUJsFX1uywB_Fxr9JnFZo' http://localhost:4455/anything/oauth-cred-example
```

# Inspect the session hydrator endpoint data and add Extra fields used by id_token mutator.