import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please Drink water Now!!!!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = r"C:\Users\Bhagyashree\Desktop\v_python\icon.ico",
            timeout = 12
        )
        time.sleep(60*60)#It will show the notification every 1 hr