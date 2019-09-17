# DjangoRestFrameworkWithJWT
DRF and JWT Implementation
Get A token
 curl --request POST \
  --url http://localhost:8000/api/jwt-auth/ \
  --header 'content-type: application/json' \
  --data '{"username": "desired_username", "password": "desired_password"}'
  //HINT: u have to create user and pwd with python manage.py createsuperuser

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6IiIsInVzZXJuYW1lIjoidGVzdF91c2VyIiwiZXhwIjoxNDk1OTkyOTg2fQ.sWSzdiBNNcXDqhcdcjWKjwpPsVV7tCIie-uit_Yz7W0"}

Access Subscribers
curl -H "Content-Type: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6IiIsInVzZXJuYW1lIjoidGVzdF91c2VyIiwiZXhwIjoxNDk1OTkyOTg2fQ.sWSzdiBNNcXDqhcdcjWKjwpPsVV7tCIie-uit_Yz7W0" -X GET  http://localhost:8000/api/subscribers/

Tutorial from:
http://polyglot.ninja/django-rest-framework-json-web-tokens-jwt/
