# 투자 실적 집계 Agent 지침서

> 이 파일은 Claude(Cowork)가 투자 실적 집계 작업을 자동으로 수행할 때 따라야 할 전체 워크플로우를 정의합니다.
> 집 PC / 회사 PC 어디서든 동일하게 실행됩니다.

---

## 📋 Agent 역할

Google Sheets에서 실시간 투자 데이터를 수집하여 `투자실적_집계보고서.xlsx`를 업데이트하고, Investment Dashboard를 생성한다.

---

## ⏰ 실행 스케줄

| 시간 | 실행 내용 |
|------|----------|
| 오후 4:00 | 장 마감 후 최종 집계 |

> 스케줄 등록: Cowork 채팅창에서 "매일 오전 10시, 오후 1시, 오후 3시, 오후 4시에 투자 실적 집계 실행해줘" 입력

---

## 📊 데이터 소스

**Google Sheets 파일명:** `1. 자산 투자 실적(종목별)`

- Claude in Chrome 확장 프로그램을 통해 접근
- Chrome에 해당 시트가 열려 있거나, Google Drive MCP로 접근 가능해야 함
- 시트 구성: 계좌별 투자원금 / 현재금액 / 수익금액 / 수익률 데이터 포함

**수집 대상 계좌:**
- 퇴직연금 (220-91)
- 개인연금 (기존)
- 개인연금 (신)
- 개인투자 계좌

---

## 📁 출력 파일

모두 `D:\00.은퇴계획\01.투자실적\` 폴더 기준:

| 파일 | 설명 |
|------|------|
| `투자실적_집계보고서.xlsx` | 메인 집계 보고서 (4개 시트) |
| `투자실적_일별추적.json` | 일별 원시 데이터 이력 |

---

## 🔄 실행 워크플로우

### STEP 1. Google Sheets 데이터 수집

Claude in Chrome을 사용하여 Google Sheets에서 데이터를 읽는다.

```
수집 항목:
- 각 계좌별: 투자원금, 현재금액, 수익금액, 수익률(배), 수익률(%)
- 총합계: 전체 투자원금, 현재금액, 수익금액, 수익률
- 기준 시각: 수집 시점의 날짜/시간 (YYYY-MM-DD HH:MM 형식)
```

### STEP 2. 투자실적_일별추적.json 업데이트

`D:\00.은퇴계획\01.투자실적\투자실적_일별추적.json` 파일에 오늘 데이터를 추가/갱신한다.

```json
{
  "date": "YYYY-MM-DD",
  "time": "YYYY-MM-DD HH:MM",
  "source": "google_sheets_live",
  "total_inv": 총투자원금,
  "total_cur": 총현재금액,
  "total_profit": 총수익금액,
  "total_rate": 총수익률(배),
  "pension_inv": 연금투자원금,
  "pension_cur": 연금현재금액,
  "pension_rate": 연금수익률,
  "personal_inv": 개인투자원금,
  "personal_cur": 개인현재금액,
  "personal_rate": 개인수익률,
  "day_profit": 일일수익금액,
  "day_rate_pct": 일일수익률(%),
  "pension_day_profit": 연금일일수익,
  "personal_day_profit": 개인일일수익
}
```

- 같은 날짜 데이터가 있으면 가장 최신 집계로 **덮어쓰기**
- 다른 날짜면 배열에 **추가**

### STEP 3. 투자실적_집계보고서.xlsx 업데이트

4개 시트를 모두 업데이트한다.

#### 시트 1: 현재 실적

| 열 | 내용 |
|----|------|
| A | 계좌명 |
| B | 투자원금 |
| C | 현재금액 |
| D | 수익금액 |
| E | 수익률(배) |
| F | 수익률(%) |

- 헤더 행 1: `📊 투자 실적 현황  |  기준일: YYYY-MM-DD HH:MM  [Google Sheets 실시간]`
- 계좌별 개별 행 + 합계 행 포함
- 오늘 데이터로 **전체 갱신**

#### 시트 2: 일별 추적

| 열 | 내용 |
|----|------|
| A | 날짜 |
| B | 구분 (연금 / 개인투자) |
| C | 투자원금 |
| D | 현재금액 |
| E | 수익금액 |
| F | 수익률(%) |

- 헤더: `📅 일별 투자 실적 추적`
- 오늘 날짜가 이미 있으면 **덮어쓰기**, 없으면 **추가**
- `투자실적_일별추적.json` 데이터 기반으로 채움

#### 시트 3: 주별 추적

- 일별 데이터를 주 단위로 집계 (월요일 기준)
- 해당 주의 최신 데이터를 대표값으로 사용
- 헤더: `📅 주별 투자 실적 추적`
- 열 구성: 일별 추적과 동일

#### 시트 4: 월별 실적

| 열 | 내용 |
|----|------|
| A | 월 (YYYY-MM) |
| B | 계좌명 |
| C | 투자원금 |
| D | 현재금액 |
| E | 수익금액 |
| F | 수익률(%) |

- 헤더: `📆 월별 투자 실적`
- 이번 달 데이터 추가/갱신, 과거 데이터 유지
- 계좌별 상세 행 + 합계 행 포함

### STEP 4. Investment Dashboard 생성/업데이트

`D:\00.은퇴계획\01.투자실적\투자실적_dashboard.html` 파일을 생성하거나 Cowork artifact로 업데이트한다.

**Dashboard 구성 요소:**
- 헤더: 기준 시각, 전체 수익률
- 카드: 총 투자원금 / 총 현재금액 / 총 수익금액 / 전일대비
- 차트 1: 계좌별 현재금액 비중 (파이차트)
- 차트 2: 일별 수익률 추이 (라인차트, 최근 30일)
- 차트 3: 월별 수익금액 (바차트)
- 테이블: 계좌별 상세 실적

**⚠️ 억 단위 표시 규칙 (반드시 준수):**
- 1억 = 100,000,000 (1e8)
- 올바른 계산: `값 / 100,000,000` → 예) 943,254,114 / 1e8 = **9.4억** ✅
- 잘못된 계산: `값 / 100,000` → 예) 943,254,114 / 1e5 = 9,433억 ❌
- 카드, stat chip, 카카오톡 메시지 등 모든 억 단위 표시에 적용

### STEP 5. 카카오톡 알림 전송 (오후 4시 실행 시에만)

실행 시각이 15:30~16:30 사이일 경우에만 카카오톡으로 투자 실적 요약을 전송한다.

```
MCP 도구: mcp__2f6af25d-505d-4e7a-8bee-84e1989ad903__KakaotalkChat-MemoChat
최대 200자 제한 — 반드시 200자 이내로 작성
```

**메시지 형식 (200자 이내, 공백 최소화):**
```
📊 투자 실적 (YYYY-MM-DD 16:00)
💰 연금
현재:₩X.X억|수익:+X.X억|+X%
전일대비:▲/▼X.X억(X%)
📈 개인투자
현재:₩X.X억|수익:+X.X억|+X%
전일대비:▲/▼X.X억(X%)
🏦 전체
현재:₩X.X억|수익:+X.X억|+X%
전일대비:▲/▼X.X억(X%)
```

- 시간 표기는 항상 **16:00** 고정 (실행 시각이 아닌 장 마감 기준)
- 숫자는 억 단위 소수점 1자리 (÷1억, 예: 526,750,590 → ₩5.3억)

> ⚠️ 200자 초과 시 숫자를 억 단위로 줄여서 전송 (예: ₩5.2억)

### STEP 6. GitHub Push (오후 4시 실행 시에만)

실행 시각이 15:30~16:30 사이인 경우, `투자실적_dashboard.html`을 GitHub에 Push한다.

```
방법: Python 스크립트 실행
스크립트 위치: D:\00.은퇴계획\01.투자실적\github_push.py
대상 레포: https://github.com/churee20/finance (main 브랜치)
```

**실행 방법 (Desktop Commander 사용 시):**
```
start_process로 python 실행:
  python D:\00.은퇴계획\01.투자실적\github_push.py
```

**Desktop Commander 미사용 시 — Claude in Chrome JavaScript로 실행:**
1. `mcp__Claude_in_Chrome__tabs_context_mcp` 로 탭 확인
2. GitHub.com 탭에서 `javascript_tool`로 GitHub API 직접 호출
   - Token: github_push.py 내 TOKEN 변수 참조
   - 파일 내용: `투자실적_dashboard.html`을 base64 인코딩하여 PUT

### STEP 7. Live Artifact 갱신 (모든 실행 시)

Cowork sidebar의 **"Investment Dashboard"** artifact를 최신 데이터로 업데이트한다.

```
방법:
1. mcp__cowork__list_artifacts 로 artifact ID 확인 (id: "investment-dashboard")
2. STEP 4와 동일한 데이터로 artifact HTML 작성 (light mode, :root{color-scheme:light})
3. mcp__cowork__update_artifact 호출
   - id: "investment-dashboard"
   - html_path: 작성한 HTML 파일 경로
   - update_summary: "YYYY-MM-DD HH:MM 기준 데이터 갱신 — 현재금액 ₩X억, 수익률 X%"
```

**주의사항:**
- Artifact는 light mode 전용 (배경 밝은색, 텍스트 어두운색)
- 허용 CDN만 사용: Chart.js 4.5.0 (위 URL 그대로)
- localStorage 사용 금지

---

## 🖥️ 회사 PC 실행 전 체크리스트

```
□ Cowork 앱 실행 중 (churee20@gmail.com 로그인)
□ Chrome 열려 있음 + Claude in Chrome 확장 로그인됨
□ 은퇴준비 폴더 Cowork에 연결됨
□ Google Drive MCP 커넥터 연결됨 (또는 Chrome에 Google Sheets 탭 열려 있음)
```

---

## 💬 수동 실행 명령어

Cowork 채팅창에 아래 메시지 중 하나를 입력하면 즉시 실행된다:

```
지금 투자 실적 집계 실행해줘
```
```
투자 실적 업데이트해줘
```
```
Google Sheets에서 투자 실적 가져와서 보고서 업데이트해줘
```

---

## ⚠️ 에러 대응

| 상황 | 조치 |
|------|------|
| Chrome 연결 안 됨 | Chrome 재시작 → Claude in Chrome 확장 재로그인 |
| Google Sheets 접근 불가 | Google Drive MCP 재연결 또는 Chrome에서 시트 직접 열기 |
| 파일 쓰기 오류 | 엑셀 파일이 열려 있으면 닫고 재실행 |
| 데이터 없음 | 장 시간 외(오전 9시 이전, 오후 4시 이후) 시트 미업데이트 상태일 수 있음 |

---

## 📂 폴더 구조

```
D:\00.은퇴계획\01.투자실적\
├── agent.md                          ← 이 파일 (Agent 지침)
├── 투자실적_집계보고서.xlsx            ← 메인 집계 보고서
├── 투자실적_일별추적.json              ← 일별 원시 데이터
├── 투자실적_dashboard.html            ← Investment Dashboard
└── 백업/
    ├── 회사PC_설치가이드.md
    └── 투자실적_일별추적.json (백업)
```

---

*최종 업데이트: 2026-06-08 | Claude Cowork 자동 생성*
