import subprocess

def get_wifi_info():
    ssid = "Not Connected"
    password = "N/A"

    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], timeout=3).decode("utf-8")
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
                break

        if ssid != "Not Connected":
            try:
                profile = subprocess.check_output(["netsh", "wlan", "show", "profile", ssid, "key=clear"], timeout=3).decode("utf-8")
                for line in profile.splitlines():
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        break
            except subprocess.CalledProcessError:
                password = "No password set or profile not found"

    except subprocess.TimeoutExpired:
        ssid = "Timeout"
        password = "Command took too long"
    except Exception as e:
        ssid = "Error"
        password = str(e)

    return ssid, password

ssid, password = get_wifi_info()
print(f"📶 SSID: {ssid}")
print(f"🔑 Password: {password}")
