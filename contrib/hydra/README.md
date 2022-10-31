
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

```shell script
$ docker-compose exec hydra \
    hydra clients create \
    --endpoint http://127.0.0.1:4445 \
    --id client-flow-12333 \
    --secret secret \
    --grant-types client_credentials \
    --response-types token \
    --scope scope-a,scope-b
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

docker-compose exec hydra hydra clients create --endpoint http://127.0.0.1:4445 --token-endpoint-auth-method none --callbacks http://localhost:3001/dashboard/ --allowed-cors-origins=http://localhost:3001 --scope openid,offline,product --name seqhq-1234

curl --request POST -sL \
--header "Content-Type: application/json" \
--data '{
"schema_id": "default",
"state": "active",
"traits": {
"email": "email@test.com"
},
"credentials": {
"password": {
"config": {
"password": "mysecurepassword"
}
}
}
}' http://127.0.0.1:4434/admin/identities

--------------------------------
Dashboard web ENV

REACT_APP_CLIENT_ID=eb7ca558-79c8-4cea-8c61-e231da6850f9
REACT_APP_REDIRECT_URI=http://localhost:3001/dashboard/
REACT_APP_AUTHORIZATION_ENDPOINT=http://127.0.0.1:4444/oauth2/auth
REACT_APP_TOKEN_ENDPOINT=http://127.0.0.1:4444/oauth2/token
REACT_APP_REQUESTED_SCOPES=openid product
REACT_APP_BFF_SERVER_URL=http://localhost:4000/graphql
REACT_APP_SENTRY_DSN=https://62feed8e2df046afb5c10efd77b57827@o1307904.ingest.sentry.io/6553019
REACT_APP_SENTRY_ENVIRONMENT=local
REACT_APP_TOKEN_REVOKE_ENDPOINT=http://127.0.0.1:4444/oauth2/revoke
REACT_APP_AUTH_URL=https://dev.seqhq.io/auth/logout
REACT_APP_API_ORIGIN=https://dev.seqhq.io
 
--------------------------------





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
curl -X GET -H 'Sequence-Authorization-Header: eyJhbGciOiJSUzI1NiIsImtpZCI6IjNjMzA0MGUwLTNmN2ItNDRmYS04OWZiLTRmODNiMDg0MTU2ZCIsInR5cCI6IkpXVCJ9.eyJhbGxvd2VkLWFjY291bnQtaWRzIjoiW2FjY291bnQtaWQtMSBhY2NvdW5kLWlkLTJdIiwiYXVkIjpbImh0dHBzOi8vbXktYmFja2VuZC1zZXJ2aWNlL3NvbWUvZW5kcG9pbnQiXSwiZXhwIjoxNjUxNzUwNjExLCJpYXQiOjE2NTE3NDcwMTEsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NDQ1NSIsImp0aSI6IjY1ZjM5N2RiLTZiYmEtNDkyNC04MTIxLTFlZTU0MmNlYTZkNyIsIm5iZiI6MTY1MTc0NzAxMSwib3JnYW5pc2F0aW9uLWlkIjoib3JnYW5pc2F0aW9uLWlkLTEiLCJzdWIiOiJvYXRoa2VlcGVyIn0.elMZZvGeZyzF3LP9diPmIbVQdhW9qah-6KgCuPVSRlvUxAe3jnSmyL5cqhp_JPo5Bm7YK86sVVgaDQfdZ0FrRpqwcC5fBysZ1qIRrsTo1Gw7WUPZ-1Wo_DBT2FUmvl5CJPKeFO7qEZ80h5hf646fvczNBfX25qQjjc4d5PQbOEZRewIhD4Yl0xks2P7GMWC9XXxpxhwKURzeQLoMX_HFiTwe2OBM8Xc4ikKb0k0ydTCycCo99T-kX4EnyFWbgv38LX_CS3n2bg9FaWP_Vx60FrQF2FYUjIqluZwpxorp1wDH1S4vtbYnvfqmK-CnPZtajfI67th1kXfos-DwZfjieA' http://localhost:4455/anything/oauth-cred-example
```

# Oauth introspection
```shell script

curl -X GET -H 'Authorization: Bearer rh_SLS1BaZHz4bMA1TEu74epPGoiMkT4n_Bff6woYO8.NNvvuLvg2tiSBTOnmIIqW1OrI5vto0LhBfI-cm7DLn0' http://localhost:4455/anything/oauth-cred-example
```

# Inspect the session hydrator endpoint data and add Extra fields used by id_token mutator.