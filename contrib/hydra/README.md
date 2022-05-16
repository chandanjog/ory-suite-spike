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
curl -X GET -H 'Sequence-Authorization-Header: eyJhbGciOiJSUzI1NiIsImtpZCI6IjNjMzA0MGUwLTNmN2ItNDRmYS04OWZiLTRmODNiMDg0MTU2ZCIsInR5cCI6IkpXVCJ9.eyJhbGxvd2VkLWFjY291bnQtaWRzIjoiW2FjY291bnQtaWQtMSBhY2NvdW5kLWlkLTJdIiwiYXVkIjpbImh0dHBzOi8vbXktYmFja2VuZC1zZXJ2aWNlL3NvbWUvZW5kcG9pbnQiXSwiZXhwIjoxNjUxNzUwNjExLCJpYXQiOjE2NTE3NDcwMTEsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NDQ1NSIsImp0aSI6IjY1ZjM5N2RiLTZiYmEtNDkyNC04MTIxLTFlZTU0MmNlYTZkNyIsIm5iZiI6MTY1MTc0NzAxMSwib3JnYW5pc2F0aW9uLWlkIjoib3JnYW5pc2F0aW9uLWlkLTEiLCJzdWIiOiJvYXRoa2VlcGVyIn0.elMZZvGeZyzF3LP9diPmIbVQdhW9qah-6KgCuPVSRlvUxAe3jnSmyL5cqhp_JPo5Bm7YK86sVVgaDQfdZ0FrRpqwcC5fBysZ1qIRrsTo1Gw7WUPZ-1Wo_DBT2FUmvl5CJPKeFO7qEZ80h5hf646fvczNBfX25qQjjc4d5PQbOEZRewIhD4Yl0xks2P7GMWC9XXxpxhwKURzeQLoMX_HFiTwe2OBM8Xc4ikKb0k0ydTCycCo99T-kX4EnyFWbgv38LX_CS3n2bg9FaWP_Vx60FrQF2FYUjIqluZwpxorp1wDH1S4vtbYnvfqmK-CnPZtajfI67th1kXfos-DwZfjieA' http://localhost:4455/anything/oauth-cred-example
```

# Oauth introspection
```shell script

curl -X GET -H 'Authorization: Bearer r3zZsaPoP-c0SyBXMZGicot7Ts634FHcxak1_kPCD9U.xFeMn7ZBDHsv-jYskj95O6WUJsFX1uywB_Fxr9JnFZo' http://localhost:4455/anything/oauth-cred-example
```

# Inspect the session hydrator endpoint data and add Extra fields used by id_token mutator.