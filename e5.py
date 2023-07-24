import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print(f"倒计时: {remaining_seconds // 60} 分钟 {remaining_seconds % 60} 秒", end="\r")
        time.sleep(1)
    
    print("时间到！专注时间结束。")

# 设置专注时间为25分钟
focus_timer(60)
