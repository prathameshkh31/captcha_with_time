import random
import threading
import string
def generate_captcha(length=5):
    chars=string.ascii_letters+string.digits
    captcha=''.join(random.choice(chars) for _ in range(length))
    return captcha
def input_with_timeout(prompt,timeout=120):
    result=[None]
    def get_input():
        result[0]=input(prompt)
    thread=threading.Thread(target=get_input,daemon=True)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print('You ran out of time')
        return None
    else:
        return result[0]
def verify_captcha():
    captcha=generate_captcha(6)
    print(f' \n {captcha} ')
    user_input=input_with_timeout('Enter the above captcha code')
    if user_input is None:
        print('You ran out of time')
        return False
    elif user_input=='':
        print("You didn't enter anything")
        return False
    else:
        if user_input==captcha:
            print('Verified User ,and also enter the login credentials within  time')
            return True
        elif user_input!=captcha:
            print('Unverified User,you are not human')
            return False
while True:
    if verify_captcha():
        print('Access: Granted')
    else:
        print('Access: Denied')
    should_continue=input('Again captcha code for verification ? (y/n) \n').lower()
    if should_continue!='y':
        print('Jay shree krishna')
        break
            