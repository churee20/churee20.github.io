# 🖥️ 회사 PC 은퇴준비 자동화 설치 가이드

> 이 문서는 Cowork + Claude in Chrome을 회사 PC에 설치하고, 매일 오전 9시/오후 4시 자동 투자 실적 집계가 실행되도록 설정하는 방법을 안내합니다.

---

## 📋 사전 준비

| 항목 | 내용 |
|------|------|
| OS | Windows 10 / 11 |
| 브라우저 | Google Chrome (필수) |
| 계정 | Anthropic 계정 (`churee20@gmail.com`) |
| 구글 계정 | 구글 시트 접근 가능한 계정 |
| 공유 폴더 | 집 PC의 `D:\클로드\은퇴준비\은퇴준비` 폴더를 네트워크 드라이브 또는 클라우드(OneDrive/Google Drive)로 공유 |

---

## STEP 1. Cowork 설치

1. [https://claude.ai/download](https://claude.ai/download) 접속
2. **"Download for Windows"** 클릭 → 설치 파일 실행
3. 설치 완료 후 실행 → `churee20@gmail.com`으로 로그인
4. 좌측 패널에서 **"Cowork"** 모드 선택

---

## STEP 2. Claude in Chrome 확장 프로그램 설치

1. Chrome 브라우저 열기
2. [크롬 웹스토어](https://chromewebstore.google.com) 접속
3. **"Claude for Chrome"** 또는 **"Claude in Chrome"** 검색
4. **"Chrome에 추가"** 클릭 → 설치
5. 설치 완료 후 확장 프로그램 아이콘 클릭 → `churee20@gmail.com`으로 로그인

> ⚠️ **중요**: 자동 실행 시 Chrome이 열려 있어야 구글 시트 실시간 데이터를 읽을 수 있습니다.

---

## STEP 3. 작업 폴더 연결

집 PC의 은퇴준비 폴더를 회사 PC에서도 접근할 수 있도록 설정합니다.

### 방법 A: OneDrive 동기화 (권장)
1. `D:\클로드\은퇴준비\은퇴준비` 폴더를 OneDrive에 업로드 (또는 OneDrive 폴더 내로 이동)
2. 회사 PC에서 OneDrive 로그인 → 동기화 확인
3. Cowork에서 해당 폴더 선택

### 방법 B: USB/네트워크 드라이브
1. 해당 폴더를 USB 또는 네트워크 드라이브에 복사
2. 회사 PC에서 폴더 접근 후 Cowork 연결

### Cowork에서 폴더 연결 방법
1. Cowork 실행 → 좌측 **"폴더 선택"** 버튼 클릭
2. 은퇴준비 폴더 선택 → **"확인"**

---

## STEP 4. 구글 계정 연결 (구글 드라이브 MCP)

구글 시트 실시간 데이터를 읽으려면 Google Drive 연결이 필요합니다.

1. Cowork 실행 → **"플러그인"** 또는 **"연결"** 메뉴
2. **"Google Drive"** 커넥터 찾기 → **"연결"** 클릭
3. 구글 계정 로그인 화면에서 `churee20@gmail.com` 선택 → 권한 허용

---

## STEP 5. 스케쥴 자동 실행 확인

집 PC에서 이미 설정된 스케쥴이 동기화됩니다.

- 자동 실행 시간: **매일 오전 9시 / 오후 4시**
- 실행 내용:
  - 구글 시트에서 실시간 투자 금액 수집
  - `투자실적_일별추적.json` 업데이트
  - `투자실적_집계보고서.xlsx` 업데이트

### 수동 실행 방법
Cowork 채팅창에 아래 메시지 입력:
```
지금 투자 실적 집계 실행해줘
```

---

## STEP 6. 정상 동작 확인

설치 완료 후 아래 사항을 확인하세요:

- [ ] Cowork 로그인 완료
- [ ] Claude in Chrome 확장 설치 및 로그인 완료
- [ ] 은퇴준비 폴더 연결 완료
- [ ] Google Drive 커넥터 연결 완료
- [ ] Chrome이 열린 상태로 Cowork 실행 시 구글 시트 접근 가능

---

## ❓ 자주 묻는 문제

| 증상 | 해결 방법 |
|------|----------|
| "Chrome 연결 안됨" 오류 | Chrome이 열려 있는지 확인, Claude in Chrome 확장 로그인 확인 |
| 구글 시트 데이터 못 읽음 | Google Drive MCP 연결 상태 확인 |
| 폴더 파일이 안 보임 | Cowork에서 폴더 재연결 |
| 스케쥴이 실행 안 됨 | PC가 켜져 있어야 하며 Cowork 앱이 실행 중이어야 함 |

---

## 📁 주요 파일 위치

```
은퇴준비/
├── 1.자산 투자 실적(신규).xlsx     ← 투자 현황 원본
├── 투자실적_집계보고서.xlsx         ← 자동 집계 보고서
├── 투자실적_일별추적.json           ← 일별 데이터 (자동 업데이트)
└── 회사PC_설치가이드.md             ← 이 파일
```

---

*문서 작성: Claude Cowork | 최종 업데이트: 2026-06-04*
