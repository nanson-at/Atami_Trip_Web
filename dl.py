import urllib.request
import urllib.parse
import os
import time

dest_dir = "img"
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Flat list of all stops in order of itineraryData in index.html
names = [
    "品川プリンスホテル",
    "熱海駅 / 品川駅",
    "Orix Rent-a-car 熱海駅前店",
    "塔之澤 一之湯本館",
    "蘆之湖海盜船",
    "大涌谷",
    "箱根神社",
    "駒ヶ岳ロープウェー",
    "Fashion Center Shimamura",
    "伊豆シャボテンヴィレッジ",
    "門脇吊橋",
    "大室山",
    "伊豆シャボテン動物公園",
    "城崎海岸 & 一碧湖",
    "伊豆ぐらんぱる公園",
    "伊豆高原グランイルミ",
    "CAINZ Izu Kōgen",
    "The Lighthouse Seaside Inn",
    "白浜海岸",
    "ペリーロード",
    "龍宮窟",
    "Shimamura 服飾店",
    "熱海銀座商店街",
    "Shimamura 購物",
    "來宮神社",
    "熱海サンビーチ"
]

for i, name in enumerate(names):
    filename = f"image_{i}.jpg"
    filepath = os.path.join(dest_dir, filename)
    if os.path.exists(filepath):
        continue
        
    query = urllib.parse.quote(name + ' Japan scenic travel photography beautiful outdoors')
    url = f"https://image.pollinations.ai/prompt/{query}?width=800&height=1000&nologo=true&seed=42"
    print(f"Downloading [{i}/{len(names)}] {name} -> {filename} ...")
    
    attempts = 0
    while attempts < 3:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Saved {filename}")
            break
        except Exception as e:
            attempts += 1
            print(f"Attempt {attempts} failed for {name}: {e}")
            time.sleep(2)

print("All downloads complete!")
