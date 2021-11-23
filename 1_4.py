import requests
import json


def save_image(image_url, file_name):
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(image_response.content)


url = "https://dapi.kakao.com/v2/search/image"
headers = {"Authorization": "KakaoAK 86b88f9cdcb3985d9405bf346204a80d"}
data = {"query": "아이언맨"}

response = requests.post(url, headers=headers, data=data)

if response.status_code != 200:
    print("error beacuse ", response.json())
else:
    count = 0
    for image_info in response.json()["documents"]:
        print(
            f"[{count}th] image_url = , siteName = ",
            image_info["image_url"],
            image_info["display_sitename"],
        )
        count = count + 1
        file_name = "./Image_collection/test_%d.jpg" % (count)
        save_image(image_info["image_url"], file_name)

# Docs : https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-image
