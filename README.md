# Recreation-Forest-Simulation
* 전국 휴양림 데이터의 지오코딩을 진행해 분포를 시각화
* 방문자 데이터를 전처리해 방문차 통계를 확인  

<br>

### Directory Structure

 ```text 
  Recreation-Forest-Simulation/
├── 📂 R/                     # 핵심 시뮬레이션 코드 (Core Simulation)
│   ├── run.R                 # [메인] 실행 파일
│   ├── createAgents.R        # 에이전트 생성
│   ├── getDist.R             # 거리 행렬 계산
│   └── (agent.*.R / lodge.*.R) # 의사결정 로직
│
├── # 데이터 전처리 도구 (Tools)
├── Coordinate Transformation.py  # 좌표계 변환 (TM -> WGS84)
├── visitor_distance.py           # 거리 계산 (OD Analysis)
├── Geocoding.R                   # 주소 -> 좌표 변환
└── README.md                 # 프로젝트 설명서
```

<br>

**[전국 휴양림 지도 시각화]**

<img width="370" height="543" alt="image" src="https://github.com/user-attachments/assets/92d4c28a-3293-4f47-8ae2-f3a1a1756fae" />

<br>
<br>

**[실제 휴양림 방문자 통계]**

<img width="1161" height="552" alt="image" src="https://github.com/user-attachments/assets/ae3cd1d2-ff62-448b-a9ac-260f7c5753a7" />

<br>
<br>

**[행위자 기반 모형(Agent-Based Model, ABM)]**
<br>

### Simulation Flowchart


```text
[START: run.R]
      │
      ├── 1. Setup Phase
      │     ├── createAgents.R  (가상 이용객 500명 생성)
      │     └── getDist.R       (거주지-휴양림 거리 계산)
      │
      ▼
[LOOP: 1 to 52 Weeks] ──────────────────────────────┐
      │                                             │
      ├── 2. Agent Decision Process (개인)          │
      │     ├── agent.consider.R (갈까 말까? 확률 계산)
      │     ├── agent.search.R   (어디 갈까? 점수 평가)
      │     └── agent.decide.R   (신청 완료)
      │                                             │
      ├── 3. System Process (시설)                  │
      │     └── lodge.decide.R   (추첨 및 배정)      │
      │                                             │
      └─────────────────────────────────────────────┘
      │
      ▼
[END: Visualization]
      └── run.R (결과 그래프 출력)
```


<img width="566" height="410" alt="Rplot02" src="https://github.com/user-attachments/assets/925f04d3-0290-4422-b9be-0cb5975ad1ff" />
