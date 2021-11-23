import requests

url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

img_response = requests.get(url)

if img_response.status_code == 200:
    print(img_response.content)

    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)
