#평면 직각 좌표계(Projected Coordinate System) X_Coor / Y_Coor값을 위도/경도 (Lat/Lon)로 변환
#pip install pyproj

import pandas as pd
from pyproj import Proj, transform

# CSV 파일 경로
csv_file = "D:/minseon/hu/데이터_휴양림_통합/2020_1분기_사용.csv"

# UTM 좌표계 (EPSG:5178)와 경도, 위도 좌표계 (EPSG:4326) 정의
utm_proj = Proj(init="EPSG:5178")
wgs84_proj = Proj(init="EPSG:4326")

# CSV 파일 불러오기
data = pd.read_csv(csv_file, encoding='euc-kr')

# X_Coor와 Y_Coor 값을 경도와 위도로 변환하는 함수
def convert_to_longitude_latitude(x, y):
    longitude, latitude = transform(utm_proj, wgs84_proj, x, y)
    return longitude, latitude

# 변환된 값을 저장할 리스트
longitude_list = []
latitude_list = []

# CSV 파일의 각 행에 대해 변환 수행
for index, row in data.iterrows():
    x_coor = row["X_Coor"]
    y_coor = row["Y_Coor"]
    
    # X_Coor와 Y_Coor를 경도와 위도로 변환
    longitude, latitude = convert_to_longitude_latitude(x_coor, y_coor)
    
    # 변환된 값 리스트에 추가
    longitude_list.append(longitude)
    latitude_list.append(latitude)

# 변환된 결과를 데이터프레임에 추가
data["Longitude"] = longitude_list
data["Latitude"] = latitude_list

# 변환된 데이터프레임을 새로운 CSV 파일로 저장
data.to_csv("D:/minseon/hu/데이터_휴양림_통합/2020-1.csv", index=False)
