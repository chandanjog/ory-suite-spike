# run using python hydrator-api.py
# Use ngrok to expose and use ngrok url in the Oathkeeper config

from flask import Flask, json, request

# canned response
# https://mockbin.org/bin/61620bab-25ee-4a58-a873-b6e53286e1ce


api = Flask(__name__)

@api.route('/hydrator', methods=['POST'])
def hydrator():
    # example request data with User ID as subject::
    # b'{"subject":"75942b04-bd16-4d61-b779-9a7fa595c0c2","extra":{"client_id":"auth-code-client","scope":"openid offline","user_id":"bar","username":""},"header":null,"match_context":{"regexp_capture_groups":["localhost"],"url":{"Scheme":"http","Opaque":"","User":null,"Host":"localhost:4455","Path":"/anything/oauth-cred-example","RawPath":"","ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":""},"method":"GET","header":{"Accept":["*/*"],"Authorization":["Bearer 1MKuHJ8g3lYPxYAVP2aw1DQaIapWNU5mpXWMOs0YNaY.ikeeiumQ1Hj40WKeuOIBvHfjFEMRNz1jIVqE5JkI0Bk"],"User-Agent":["curl/7.58.0"]}}}\n'
    # example request data with OAuth 2 Client ID as subject::
    # b'{"subject":"oathkeeper","extra":null,"header":null,"match_context":{"regexp_capture_groups":["localhost"],"url":{"Scheme":"http","Opaque":"","User":null,"Host":"localhost:4455","Path":"/anything/oauth-cred-example","RawPath":"","ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":""},"method":"GET","header":{"Accept":["*/*"],"Authorization":["Basic b2F0aGtlZXBlcjpkdW1teS1vYXRoa2VlcGVyLXNlY3JldA=="],"User-Agent":["curl/7.58.0"]}}}\n'
    print("request data::")
    print(request.get_data())

    print("request data::")
    print(request.headers)

    print("----------------------------")
    print(request.get_json(force=True))
    copy = request.get_json(force=True)

    print("------------------")
    print(copy["subject"])
    # Can modify add extra parameters to the session data before returning back
    # use the "subject" to decide if it's a User logging in via Authorize code flow or OAuth 2 Client via Client Credentials flow

    dummy_account_ids = ["account-id-1", "accound-id-2"]
    dummy_organisation_id = "organisation-id-1"

    # add "extra" fields for "allowed_account_ids" and "organisation_id" as claims that can be used for Authorization decision.
    if(copy["extra"] == None): # when client_credentials flow is triggered
        copy["extra"] = {}
    copy["extra"]["allowedAccountIds"] = dummy_account_ids
    copy["extra"]["organisationId"] = dummy_organisation_id
    return json.dumps(copy)
    # return request.get_data()

if __name__ == '__main__':
    api.run()


# curl -H 'Content-Type: application/json' -X POST http://localhost:5000/hydrator -d '{"subject":"75942b04-bd16-4d61-b779-9a7fa595c0c2","extra":{"client_id":"auth-code-client","scope":"openid offline","user_id":"bar","username":""},"header":null,"match_context":{"regexp_capture_groups":["localhost"],"url":{"Scheme":"http","Opaque":"","User":null,"Host":"localhost:4455","Path":"/anything/oauth-cred-example","RawPath":"","ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":""},"method":"GET","header":{"Accept":["*/*"],"Authorization":["Bearer 1MKuHJ8g3lYPxYAVP2aw1DQaIapWNU5mpXWMOs0YNaY.ikeeiumQ1Hj40WKeuOIBvHfjFEMRNz1jIVqE5JkI0Bk"],"User-Agent":["curl/7.58.0"]}}}'