import inspect
from datetime import datetime
BOLD = '\033[1m'
CYAN = '\033[36m'
RESET = '\033[0m'
BLINK = '\033[5m'  # Always blinking effect
UNDERLINE = '\033[4m'  # Underline for extra emphasis
RED = '\033[31m'  # Red color for warnings/errors
def dj_print(*args, **kwargs):
    frame = inspect.currentframe().f_back
    filename = frame.f_globals["__file__"]
    lineno = frame.f_lineno
    timestamp = datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p")

    message = ' '.join(str(arg) for arg in args)
    print(
        f"\n📌 [{timestamp}]\n"
        f"📁 {CYAN}{BOLD}{filename}:{lineno}{RESET}"
        f"🔸 {RED}{BOLD}{UNDERLINE} {message} {RESET}",  # Bold, Underlined, Red emphasis
        **kwargs
    )