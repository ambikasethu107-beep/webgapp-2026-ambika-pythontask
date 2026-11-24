from plyer import notification

print("Program Started")

try:
    notification.notify(
        title="Python Notification",
        message="Hello! Notification Working",
        app_name="My Python App",
        timeout=20  
    )
    print("Notification command executed")

except Exception as e:
    print("Error:", e)

input("Press Enter to Exit")