import logging
import time

import requests

import urllib3


class TestProjecList(object):
    def test_project_list(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        host = "https://xfcc-boe.bytedance.net"
        path = "/f100/api/nova_crm/project_list"
        params = {"page_no": 1,
                  "page_size": 15,
                  "timestamp": 1621495086298
                  }
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                   "Cookie": "sid_guard=4c6fbbb81d98a464da6d7a17044e544a%7C1667793917%7C5183999%7CFri%2C+06-Jan-2023+04%3A05%3A16+GMT; n_mh_xfl_xfcc_boe=paF0HsdwvRjKYOyAykD2gPmGv4Be_51wk5spW7PGqaM; sid_guard_xfl_xfcc_boe=3f928ad0f391c530960f0127a301ee07%7C1679643289%7C5184000%7CTue%2C+23-May-2023+07%3A34%3A49+GMT; uid_tt_xfl_xfcc_boe=a0ba64be6c6d05483f2866e5ded93f26; uid_tt_ss_xfl_xfcc_boe=a0ba64be6c6d05483f2866e5ded93f26; sid_tt_xfl_xfcc_boe=3f928ad0f391c530960f0127a301ee07; sessionid_xfl_xfcc_boe=3f928ad0f391c530960f0127a301ee07; sessionid_ss_xfl_xfcc_boe=3f928ad0f391c530960f0127a301ee07; sid_ucp_v1_xfl_xfcc_boe=1.0.0-KGIwYTU0ZWI2ZDVlYTJjMWMyOGM5NTdmOWVmZTg5MjM2ZjIwODY5ZWQKFwjOpuGTvo2MAxCZpfWgBhiTOzgCQPEHEH8aA2JvZSIgM2Y5MjhhZDBmMzkxYzUzMDk2MGYwMTI3YTMwMWVlMDc; ssid_ucp_v1_xfl_xfcc_boe=1.0.0-KGIwYTU0ZWI2ZDVlYTJjMWMyOGM5NTdmOWVmZTg5MjM2ZjIwODY5ZWQKFwjOpuGTvo2MAxCZpfWgBhiTOzgCQPEHEH8aA2JvZSIgM2Y5MjhhZDBmMzkxYzUzMDk2MGYwMTI3YTMwMWVlMDc; local=zh-CN; timezone=%28GMT%2B8%3A00%29%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4%26-%26%E4%B8%8A%E6%B5%B7%7C%28GMT%2B8%3A00%29China%26Standard%26Time%26-%26Shanghai%7C%28GMT%2B8%3A00%29%E4%B8%AD%E5%9B%BD%E6%A8%99%E6%BA%96%E6%99%82%26-%26%E4%B8%8A%E6%B5%B7%7C480%7CAsia%2FShanghai; s_v_web_id=verify_lgknfs34_CNRRy72M_Q57Z_4iPT_BUFT_07CUiHcGwMhH; X-Risk-Browser-Id=1e6ee1672fd0d489360c3fff707fafee939b4d17711cf03c67a90e1137a7ff79; _tea_utm_cache_7571=undefined; gfsitesid=MTk2NjEwMjQyN3wxNjgzMTg1NzA1NTl8fDAGBgYGBgY; gftoken=MTk2NjEwMjQyN3wxNjgzMTg1NzA1NTl8fDAGBgYGBgY"
        }
        r = requests.request("GET", url=host+path, params=params, headers=headers, verify=False)
        response = r.json()
        logging.info('11111')
        print(response)
        assert response["message"] == "success"