"""
투자실적_dashboard.html → GitHub churee20/finance main 브랜치 Push 스크립트
실행: python github_push.py
"""
import base64, json, urllib.request, urllib.error, urllib.parse
from pathlib import Path
from datetime import datetime
import sys
# Windows 출력 인코딩 설정
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN  = "YOUR_GITHUB_TOKEN_HERE"  # 환경변수 또는 직접 입력
OWNER  = "churee20"
REPO   = "finance"
BRANCH = "main"
REMOTE_PATH = "투자실적_dashboard.html"
LOCAL_FILE  = Path(__file__).parent / "투자실적_dashboard.html"

# 한글 경로 URL 인코딩
_encoded_path = urllib.parse.quote(REMOTE_PATH, safe='')
API_BASE = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{_encoded_path}"
HEADERS  = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json",
    "User-Agent": "investment-dashboard-pusher"
}

def api_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

def api_put(url, data):
    body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=HEADERS, method="PUT")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def push():
    print(f"[1] 로컬 파일 읽기: {LOCAL_FILE}")
    content = LOCAL_FILE.read_bytes()
    encoded = base64.b64encode(content).decode()

    print(f"[2] GitHub 기존 파일 SHA 확인...")
    existing = api_get(API_BASE)
    sha = existing["sha"] if existing else None
    print(f"    → {'업데이트' if sha else '신규 생성'} (SHA: {sha or 'N/A'})")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    payload = {
        "message": f"투자실적 대시보드 업데이트 ({now})",
        "content": encoded,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    print(f"[3] GitHub Push 중...")
    result = api_put(API_BASE, payload)
    url = result["content"]["html_url"]
    print(f"[✅ 완료] {url}")
    return url

if __name__ == "__main__":
    try:
        push()
    except Exception as e:
        print(f"[❌ 오류] {e}")
