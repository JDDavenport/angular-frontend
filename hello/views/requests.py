from django.conf import settings
from django_mako_plus import view_function, jscontext
import requests

@view_function
def azureml(request):
    url = "https://ussouthcentral.services.azureml.net/workspaces/6b0729d249cb4a49b95e3c1378e05fbf/services/612011b83e7943e89b2f420b23bde931/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n\r\n        \"Inputs\": {\r\n\r\n                \"input1\":\r\n                {\r\n                    \"ColumnNames\": [\"Gender\", \"State\", \"Credentials\", \"Specialty\"],\r\n                    \"Values\": [ [ \"M\", \"UT\", \"Pediatric Medicine\", \"M.D.\" ],]\r\n                },        },\r\n            \"GlobalParameters\": {\r\n}\r\n    }"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer P8Dbkr8tHN2QO5vKmu8DHLnejmtCJZSvqgb27QYLhlv+zaPvdn84hXGXkgQ7jWvfO7BXFqdmeTdkxJn2XGxkYA==",
        'cache-control': "no-cache",
        'Postman-Token': "00e5837e-738b-419c-9023-c6130559f9e6"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    response = response.json()
    context = {
        'response' : response,
    }
    return request.dmp.render('azureml.html', context)