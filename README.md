# Recreation-Forest-Simulation
* 전국 휴양림 데이터의 지오코딩을 진행해 분포를 시각화
* 방문자 데이터를 전처리해 방문차 통계를 확인

**[전국 휴양림 지도 시각화]**

<img width="370" height="543" alt="image" src="https://github.com/user-attachments/assets/92d4c28a-3293-4f47-8ae2-f3a1a1756fae" />

**[실제 휴양림 방문자 통계]**

<img width="1161" height="552" alt="image" src="https://github.com/user-attachments/assets/ae3cd1d2-ff62-448b-a9ac-260f7c5753a7" />


**[행위자 기반 모형(Agent-Based Model, ABM)]**

### Simulation Flowchart

```mermaid
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
