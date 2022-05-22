@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("9、发起一级代理立即上架")
@pytest.mark.run(order=83)
@pytest.mark.parametrize("test_data", ["first_agent_project_launch_release"], indirect=True)
def test_first_agent_project_launch_release(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_launch_release test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_launch_release resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))
        time.sleep(0.5)


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("10、审核-确认一级代理上架审核")
@pytest.mark.run(order=84)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_launch_release_pass"], indirect=True)
def test_smart_process_first_agent_project_launch_release_pass(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info("test_smart_process_first_agent_project_launch_release_pass test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交上架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_smart_process_first_agent_project_launch_release_pass resp:{}".format(response))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("11、发起一级代理下架")
@pytest.mark.run(order=85)
@pytest.mark.parametrize("test_data", ["first_agent_project_launch_withdrawal"], indirect=True)
def test_first_agent_project_launch_withdrawal(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_launch_withdrawal test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_launch_withdrawal resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("12、审核-确认一级代理下架审核")
@pytest.mark.run(order=86)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_launch_withdrawal_pass"], indirect=True)
def test_smart_process_first_agent_project_launch_withdrawal_pass(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info("test_smart_process_first_agent_project_launch_withdrawal_pass test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交下架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_smart_process_first_agent_project_launch_withdrawal_pass resp:{}".format(response))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("13、发起一级代理预上架")
@pytest.mark.run(order=87)
@pytest.mark.parametrize("test_data", ["first_agent_project_preparatory_launch_release"], indirect=True)
def test_first_agent_project_preparatory_launch_release(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_preparatory_launch_release test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 3))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_preparatory_launch_release resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("14、审核-确认一级代理预上架审核")
@pytest.mark.run(order=88)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_preparatory_launch_release_pass"],
                         indirect=True)
def test_smart_process_first_agent_project_preparatory_launch_release_pass(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info(
        "test_smart_process_first_agent_project_preparatory_launch_release_pass test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交上架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_smart_process_first_agent_project_preparatory_launch_release_pass resp:{}".format(response))
        time.sleep(3)


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("15、发起一级代理预下架")
@pytest.mark.run(order=89)
@pytest.mark.parametrize("test_data", ["first_agent_project_preparatory_launch_withdrawal"], indirect=True)
def test_first_agent_project_preparatory_launch_withdrawal(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_preparatory_launch_withdrawal test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 3))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_preparatory_launch_withdrawal resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("16、审核-确认一级代理预下架审核")
@pytest.mark.run(order=90)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_preparatory_launch_withdrawal_pass"],
                         indirect=True)
def test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info("test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass test_data={}".format(
        list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交下架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info(
            "test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass resp:{}".format(response))
        time.sleep(3)


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("17、发起一级代理预上架")
@pytest.mark.run(order=91)
@pytest.mark.parametrize("test_data", ["first_agent_project_preparatory_launch_release_cancel_release"], indirect=True)
def test_first_agent_project_preparatory_launch_release_cancel_release(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info(
        "test_first_agent_project_preparatory_launch_release_cancel_release test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 10))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_preparatory_launch_release_cancel_release resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("18、审核-确认一级代理预上架审核")
@pytest.mark.run(order=92)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_launch_release_pass_cancel_release"],
                         indirect=True)
def test_smart_process_first_agent_project_launch_release_pass_cancel_release(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info("test_smart_process_first_agent_project_launch_release_pass_cancel_release test_data={}".format(
        list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交上架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info(
            "test_smart_process_first_agent_project_launch_release_pass_cancel_release resp:{}".format(response))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("19、取消一级代理预上架")
@pytest.mark.run(order=93)
@pytest.mark.parametrize("test_data", ["first_agent_project_cancel_timed_release"], indirect=True)
def test_first_agent_project_cancel_timed_release(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_cancel_timed_release test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 10))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_cancel_timed_release resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("20、发起一级代理立即上架")
@pytest.mark.run(order=94)
@pytest.mark.parametrize("test_data", ["first_agent_project_launch_release_cancel_withdrawal"], indirect=True)
def test_first_agent_project_launch_release_cancel_withdrawal(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_launch_release_cancel_withdrawal test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_launch_release_cancel_withdrawal resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("21、审核-确认一级代理上架审核")
@pytest.mark.run(order=95)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data", ["smart_process_first_agent_project_launch_release_pass_cancel_withdrawal"],
                         indirect=True)
def test_smart_process_first_agent_project_launch_release_pass_cancel_withdrawal(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info("test_smart_process_first_agent_project_launch_release_pass_cancel_withdrawal test_data={}".format(
        list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交上架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info(
            "test_smart_process_first_agent_project_launch_release_pass_cancel_withdrawal resp:{}".format(response))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("22、发起一级代理预下架")
@pytest.mark.run(order=96)
@pytest.mark.parametrize("test_data", ["first_agent_project_preparatory_launch_withdrawal_cancel_withdrawal"],
                         indirect=True)
def test_first_agent_project_preparatory_launch_withdrawal_cancel_withdrawal(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info(
        "test_first_agent_project_preparatory_launch_withdrawal_cancel_withdrawal test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 10))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info(
            "test_first_agent_project_preparatory_launch_withdrawal_cancel_withdrawal resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("23、审核-确认一级代理预下架审核")
@pytest.mark.run(order=97)
# @pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("test_data",
                         ["smart_process_first_agent_project_preparatory_launch_withdrawal_pass_cancel_withdrawal"],
                         indirect=True)
def test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass_cancel_withdrawal(self, env, test_data):
    info, data, expect = list(test_data)
    logging.info(
        "test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass_cancel_withdrawal test_data={}".format(
            list(test_data)))
    with allure.step(info["desc"]):
        # 查询
        exe_cmd = "select * from dist_project_entry_suborder where project_id = '{project_id}' and action_type = {action_type} and project_type = 1 ORDER BY submit_time DESC". \
            format(project_id=env["project_id"], action_type=actions_dict["提交下架审核"]["action_type"])
        logging.info("check_sql_execute_command:{}".format(exe_cmd))
        sql_res = Rows(f_cc_boe.get_conn().cursor(), exe_cmd).execute()
        logging.info("check_sql_res:{}".format(sql_res))
        review_id = 0
        if sql_res:
            review_id = sql_res[0][6]

        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["extra_data"]["review_id"] = str(review_id)
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info(
            "test_smart_process_first_agent_project_preparatory_launch_withdrawal_pass_cancel_withdrawal resp:{}".format(
                response))
        time.sleep(3)


@asserts.upload(owner='houyuhan', biz_type='客开CRM')
@allure.story("24、取消一级代理预下架")
@pytest.mark.run(order=98)
@pytest.mark.parametrize("test_data", ["first_agent_project_cancel_timed_withdrawal"], indirect=True)
def test_first_agent_project_cancel_timed_withdrawal(self, env, test_data, db_config):
    info, data, expect = list(test_data)
    logging.info("test_first_agent_project_cancel_timed_withdrawal test_data={}".format(list(test_data)))
    with allure.step(info["desc"]):
        data["headers"]["x-tt-env"] = os.environ.get("ENV_LABEL", "prod")
        data["headers"]["Cookie"] = env["Cookie-xfcc"]
        data["body"]["project_id"] = env["project_id"]
        data["body"]["sales_time"] = str(int(time.time() + 10))
        response = post(url=env["hosts"]["xfcc"] + data["path"], headers=data["headers"],
                        data=json.dumps(data["body"]))
        assert_http_response(response, expect)
        logging.info("test_first_agent_project_cancel_timed_withdrawal resp:{}".format(response))
        logging.info("env1 {}".format(env["project_id"]))