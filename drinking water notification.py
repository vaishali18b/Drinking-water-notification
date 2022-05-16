#import time
from plyer import notification

#if __name__=="___main__":
notification.notify(
        title="**Please Drink Water Now !!",
        message="The National Academics of Sciences,Engineering and Medicine determined that an adequate daliy fluid intake is : About 3.7 liters for men and 2.7 liters for women a day.",
        app_icon=r"C:\Users\LENOVO\Desktop\projects\icon.ico",
        timeout=10,
        toast=False
    )