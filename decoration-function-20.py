import webbrowser

def validator(func): # декоратор
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Посилання не вірне")
    return wrapper # повернення функції без звернення до неї

@validator # підключення декоратора
def open_url(url):
    webbrowser.open(url)

open_url('https://www.youtube.com/') # посилання на сайт