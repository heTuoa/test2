import time

import requests

class TestProjecList(object):
    def test_project_list(self):
        host = "http://xfcc-boe.bytedance.net"
        path = "/f100/api/nova_crm/project_list"
        params = {"page_no": 1,
                  "page_size": 15,
                  "timestamp": 1621495086298
                  }
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                   "Cookie": "MONITOR_WEB_ID=6ea52aff-9e09-441e-a4fb-ae0f534e6c1d; _ga=GA1.2.613940271.1611455300; byteio_version=new; n_mh=unQRywF5kC1OJB-dfADhYqPD58vyw3bm8vWM29WII6c; sid_guard=dd596a092a36b21385263632b22863ca%7C1614599205%7C5183999%7CFri%2C+30-Apr-2021+11%3A46%3A44+GMT; gftoken=ZGQ1OTZhMDkyYXwxNjE0NTk5MzQ2Mzl8fDAGBgYGBgY; local=zh-CN; timezone=%28GMT%2B8%3A00%29%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4%26-%26%E4%B8%8A%E6%B5%B7%7C%28GMT%2B8%3A00%29China%26Standard%26Time%26-%26Shanghai%7C%28GMT%2B8%3A00%29%E4%B8%AD%E5%9B%BD%E6%A8%99%E6%BA%96%E6%99%82%26-%26%E4%B8%8A%E6%B5%B7%7C480%7CAsia%2FShanghai; googtrans=/zh-CN/zh-CN; gfsitesid=ZGQ1OTZhMDkyYXwxNjE0NTk5MzQ2Mzl8fDE1MzA5Mzk3Mzg5NTU4NjkHBwcHBwcH; admin-csrf-token=Q4KZ0pbhsWp5+0MRfIORjuwhglH81EA7ZZ3muf9yT/oqUhU2SMkmb3PYjnNWO5DK0cebV7sIdvqLRxx1KCYzGaEDxZf7W4rSnfDiS/RDxhzlvvhNqb1+YG8hcc8lWuVYNhsl0w==; f100=MTYyMDkwMDEyNXxEdi1CQkFFQ180SUFBUkFCRUFBQV80dl9nZ0FDQm5OMGNtbHVad3dHQUFSMWMyVnlEU3B6YzI4dVZYTmxja2x1Wm1fX2d3TUJBUWhWYzJWeVNXNW1id0hfaEFBQkJ3RUZSVzFoYVd3QkRBQUJCa1Z0WVdsc2N3SF9oZ0FCRFVWdGNHeHZlV1ZsU1dSVGRISUJEQUFCQWtsRUFRUUFBUVJPWVcxbEFRd0FBUWhWYzJWeWJtRnRaUUVNQUFFS1JXMXdiRzk1WldWSlpBRUVBQUFBRnYtRkFnRUJDRnRkYzNSeWFXNW5BZi1HQUFFTUFBRF96Xy1FWUFFWmQyRnVaMkpoYjJOdmJtZEFZbmwwWldSaGJtTmxMbU52YlFFQkdYZGhibWRpWVc5amIyNW5RR0o1ZEdWa1lXNWpaUzVqYjIwQkJ6WTVNakE1TURVQl9RRnNEQUVMZDJGdVoySmhiMk52Ym1jQkMzZGhibWRpWVc5amIyNW5BQVp6ZEhKcGJtY01Cd0FGZEc5clpXNE5LbTloZFhSb01pNVViMnRsYnYtSEF3RUJCVlJ2YTJWdUFmLUlBQUVFQVF0QlkyTmxjM05VYjJ0bGJnRU1BQUVKVkc5clpXNVVlWEJsQVF3QUFReFNaV1p5WlhOb1ZHOXJaVzRCREFBQkJrVjRjR2x5ZVFIX2lnQUFBQkRfaVFVQkFRUlVhVzFsQWYtS0FBQUFjZi1JYmdFb05qYzJaREk0WVRFMU5UQTBOMlk0WkdKbE9HWTFNalU0Tm1aa1ptWmxNRFkzWW1RNU1qVXdOd0VHUW1WaGNtVnlBU2czWXpjNE56TXdORFJoWm1ZMk9UTmlOR1F5T1RZeFl6SmtabUZpTXpnek9XUm1OMk01TURrekFROEJBQUFBRHRoV2ZSd0lvT1dzQWVBQXxsSVRCX0Q_BR5-zWGbPaEvgF-CEBwg_HQdsPW9BdikhQ==; tt_webid=6962063442959123999; MONITOR_WEB_ID=04285969-e1a3-47c0-9c3f-9fac2b832d52; _gid=GA1.2.1723361100.1621494621"
        }
        r = requests.request("GET", url=host+path, params=params, headers=headers)
        response = r.json()
        assert response["message"] == "success"