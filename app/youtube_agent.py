from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import os

def watch_youtube(video_url):
    # 브라우저 옵션 설정
    watch_time = random.randint(30, 120)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    # options.add_argument("--mute-audio")  # 음소거

    # Headless로 실행하려면 이 줄 추가
    options.add_argument("--headless")

    # 드라이버 실행
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print(f"🎬 Opening video: {video_url}")
        driver.get(video_url)

        # 광고 Skip (있을 경우)
        time.sleep(5)
        try:
            skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
            skip_button.click()
            print("⏩ 광고 스킵")
        except:
            print("📺 광고 없음 또는 자동 재생 중")

        # ▶️ Play 버튼 강제 클릭 (필요한 경우)
        try:
            play_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-large-play-button')
            play_button.click()
            print("▶️ Play 버튼 클릭")
        except Exception:
            print("✅ 영상 자동 재생 중이거나 Play 버튼 없음")

        # 재생 확인: video 태그를 찾아 상태 확인
        try:
            video = driver.find_element(By.TAG_NAME, "video")
            is_playing = driver.execute_script("return !arguments[0].paused;", video)
            print("🎵 영상 재생 상태:", "재생 중" if is_playing else "일시정지 상태")
        except:
            print("⚠️ 영상 요소(video tag) 확인 실패")

        # 지정된 시간 동안 시청
        print(f"⏳ Watching for {watch_time} seconds...")
        time.sleep(watch_time)

    finally:
        driver.quit()
        print("🛑 브라우저 종료")

# 예제 실행
if __name__ == "__main__":
    video_url = os.environ.get("YOUTUBE_URL", "https://www.youtube.com/watch?v=EiHx5oEIvG4")
    watch_youtube(video_url)

