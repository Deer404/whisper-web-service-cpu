import requests
import time


def login():
    # 执行登录逻辑，获取token
    response = requests.post('/login',
                             json={
                                 'username': 'your_username',
                                 'password': 'your_password'
                             })
    if response.status_code == 200:
        return response.json().get('token')
    else:
        return None


def get_jobs(token):
    # 调用接口获取任务，传递token
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('/jobs', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def transcribe(job):
    print("transcribing job")
    # 执行任务的代码
    # ...


def send_result(result, token):
    # 将结果传递给接口，传递token
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post('/xxx', json=result, headers=headers)
    if response.status_code == 200:
        print('结果传递成功')
    else:
        print('结果传递失败')


def main():
    token = login()
    if not token:
        print('登录失败')
        return

    while True:
        jobs = get_jobs(token)
        if len(jobs) == 0:
            # 如果没有任务，则等待一段时间后继续轮询
            time.sleep(5)
            continue

        for job in jobs:
            transcribe(job)
            send_result(job['result'], token)


if __name__ == '__main__':
    main()
