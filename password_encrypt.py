from passlib.hash import sha256_crypt
# https://pypi.python.org/pypi/passlib
password = sha256_crypt.encrypt("password")
password2 = sha256_crypt.encrypt("password")

print(password)
print(password2)

print(sha256_crypt.verify("password", password))
print(sha256_crypt.verify("password", '$5$rounds=535000$.hpCTkoIDSjdyQZb$zXiBR5tNBAgB0Yokqh3fuXrZP3nsCHtg88zOph4EqD6'))
print(sha256_crypt.verify("password1", '$5$rounds=535000$.hpCTkoIDSjdyQZb$zXiBR5tNBAgB0Yokqh3fuXrZP3nsCHtg88zOph4EqD6'))
