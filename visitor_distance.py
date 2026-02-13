#휴양림 예약자 거주지와 휴양림 위치 사이 거리를 확인

import pandas as pd
from geopy.distance import geodesic

def calculate_distance(row, huyang_csv):
    if pd.isna(row["Latitude"]) or pd.isna(row["Longitude"]):
        return None
    
    huyang_row = huyang_csv[huyang_csv["name"] == row["휴양림명"]]
    if huyang_row.empty:
        return None
    
    huyang_coords = (huyang_row.iloc[0]["lat"], huyang_row.iloc[0]["lon"])
    row_coords = (row["Latitude"], row["Longitude"])
    
    distance = geodesic(huyang_coords, row_coords).kilometers
    return distance

# 휴양림.csv 파일 읽기 (encoding='euc-kr' 추가)
csv_huyang = pd.read_csv("D:/minseon/hu/데이터_휴양림_통합/all.csv", encoding='euc-kr')

# 파일 이름들의 리스트 생성
file_names = ["2019-1", "2019-2", "2019-3", "2019-4", "2020-1", "2020-2", "2020-3", "2020-4"]

# 반복문을 통해 데이터 파일들을 처리하고 결과를 저장
for file_name in file_names:
    # 데이터 파일 읽기
    csv_2019 = pd.read_csv(f"D:/minseon/hu/데이터_휴양림_통합/{file_name}.csv")
    
    # 새로운 열로 '거리(km)' 추가
    csv_2019["거리(km)"] = csv_2019.apply(calculate_distance, huyang_csv=csv_huyang, axis=1)
    
    # 결과를 새로운 CSV 파일로 저장
    csv_2019.to_csv(f"D:/minseon/hu/데이터_휴양림_통합/result_{file_name}.csv", index=False)
