Place your development TLS certificates here.

Expected filenames:

- `dev.fullchain.pem`
- `dev.key.pem`

For local development you can generate self-signed certificates with:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout dev.key.pem \
  -out dev.fullchain.pem \
  -subj "/CN=localhost"
```
