# REST API for electronic wallets
Чтобы запустить приложение необходимо скачать репозиторий на 
компьютер и запустить команду 
```python
python manage.py runserver
```
## Authorization
### Request
`/api/auth/login`

## Get list of Wallets
### Request 
` GET api/wallet/ `
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

## Get a Wallet
### Request 
` GET api/wallet/<int:id>/ `
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

## Get list of Operations
### Request 
` GET api/operation/ `
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

## Get list of Users
### Request 
` GET api/user/ `
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

## Create a new Wallet
### Request 
` POST api/Wallet/ `
```
{
      "balance_RUB": float,
      "balance_USD": float,
      "id_person": int
}
```
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

## Create a new Operation
### Request 
` POST api/Wallet/ `
```
{
    "type": "",
    "money": float,
    "unit": "",
    "id_wallet_1": int,
    "id_wallet_2": int
}
```
### Response
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[]
```

______________________________________
## Admin-panel
` /admin/ `

## Main page
` / `

## Login page
` /accounts/login/ `

## List of Wallets and create a Wallet page
` accounts/profile/add/ `

## Transfer money page
`/accounts/profile/transfer/ `

## User Card page
` /users/<int:id> `

## Wallet Card page
` /wallets/<int:id> `
