from .celery import app
import celery
import time
from django.core.mail import send_mail, BadHeaderError
from .utils import beams_client
from project_celery.settings import EMAIL_HOST_USER


class CallbackSendEmail(celery.Task):
    def on_success(self, retval, task_id, args, kwargs):
        print(task_id + ' Send email seccess')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('false')
        pass
    pass


@app.task()
def run_in_10s():
    response = beams_client.publish_to_interests(
        interests=['hello'],
        publish_body={
            'apns': {
                'aps': {
                    'alert': {
                        'title': 'Hello',
                        'body': 'Hello, world!',
                    },
                },
            },
            'fcm': {
                'notification': {
                    'title': 'Hello',
                    'body': 'Hello, world!',
                },
            },
            'web': {
                'notification': {
                    'title': 'Hello',
                    'body': 'Hello, world!',
                },
            },
        },
    )

    print(response['publishId'])

    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

    print("hello world")


@app.task(bind=True, name='send_email_tasks', base=CallbackSendEmail, track_started=True)
def send_email(self, subject, data, receiver):
    try:
        self.update_state(state="PROGRESS", meta={'progress': 50})
        # holding time 1s
        time.sleep(1)
        a = send_mail(subject, data, EMAIL_HOST_USER, [receiver],)
        self.update_state(state="PROGRESS", meta={'progress': 90})
        if a < 1:
            return "User can not receive email"
        return 'Email send success'
    except BadHeaderError:
        return 'bad header'


@app.task()
def show_log(data):
    response = beams_client.publish_to_interests(
        interests=['hello'],
        publish_body={
            'apns': {
                'aps': {
                    'alert': {
                        'title': 'Hello',
                        'body': data,
                    },
                },
            },
            'fcm': {
                'notification': {
                    'title': 'Hello',
                    'body': data,
                },
            },
            'web': {
                'notification': {
                    'title': 'Hello',
                    'body': data,
                },
            },
        },
    )

    print(response['publishId'])

    print("Status " + data)
