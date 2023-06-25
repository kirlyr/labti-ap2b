## request dr latihan labti

# import json
# from urllib import request

# url = "https://api.github.com/users/kirlyr"

# response = request.urlopen(url)

# data = json.loads(response.read())

# print("== BACA PROFILE GITHUB ==")
# print(f"Nama \t\t: {data['name']}")
# print(f"Lokasi \t\t: {data['location']}")
# print(f"Institusi \t: {data['company']}")
# print(f"Follower\t: {data['followers']}")
# print(f"Dibuat pada\t: {data['created_at']}")


## reqeust latihan dr inet
## contoh 1
# import requests

# url = "https://instagram.com/irfunbasiru"

# response = requests.get(url)

# print(response.text)


## contoh 2 menambahkan input untuk mencari data lebih spesifik
# import requests

# print("search by username or else")
# user = input("> ")
# queryURL = url + f"?username={user}" #jika mencari yg lain ganti usernamenya
# response = requests.get(queryURL)

# print(response.text)