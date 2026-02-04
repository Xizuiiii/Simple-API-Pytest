import requests
import pytest

def create_api(test_title,test_body):
    url ="https://jsonplaceholder.typicode.com/posts"
    data ={
        "title": test_title,
        "body": test_body,
        "userId":1
    }
    response = requests.post(url,json=data)
    return response

@pytest.mark.parametrize('title,body',[('normal'
    ,'nomal_title'), ('','empty'), ('a'*10, 'long_title')]
)


def test_success_api(title,body):
    result=create_api(title,body)
    print(f'\n服务器返回: {result.json()}')
    assert result.status_code ==201
