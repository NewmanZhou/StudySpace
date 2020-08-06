# -*- coding: utf-8 -*-
# @Time   : 2019/12/16 11:12 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: curl2python.py
# @Software: PyCharm
import time

import requests, json, time


def wukonguser():
    cookies = {
        'odin_tt': '572c7c7c8f5ba77d0090e9ade78165ef45ead6783f45fdf237c806b3b1f48764421842dcf7ad0de6dcb6a02a84db7a33',
        'qh[360]': '1',
        'install_id': '92974975793',
        'ttreq': '1$182ca0a9824dbfcd00b1b9af8e63526eb22b10f9',
    }

    headers = {
        'X-SS-REQ-TICKET': '1576466025930',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8207 Build/KTU84P) WendaArticle/7.6.4 okhttp/3.10.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'lf.snssdk.com',
    }

    params = (
        ('iid', '92974975793'),
        ('device_id', '7898061635'),
        ('ac', 'wifi'),
        ('channel', 'baidu'),
        ('aid', '1165'),
        ('app_name', 'wenda'),
        ('version_code', '764'),
        ('version_name', '7.6.4'),
        ('device_platform', 'android'),
        ('ssmix', 'a'),
        ('device_type', 'R8207'),
        ('device_brand', 'OPPO'),
        ('language', 'zh'),
        ('os_api', '19'),
        ('os_version', '4.4.4'),
        ('uuid', '865685026456493'),
        ('openudid', 'aa864676b309bf74'),
        ('manifest_version_code', '264'),
        ('resolution', '720*1280'),
        ('dpi', '320'),
        ('update_version_code', '7640'),
        ('_rticket', '1576466025926'),
        ('rom_version', 'coloros_v2.0.1_r8207_11_141122'),
        ('fp', 'a_fake_fp'),
        ('wenda_app_version', '15'),
        ('ts', '1576466026'),
        ('as', 'l26225759f9ffae6adf626'),
        ('mas', '00168ca7f7117c34d16ca5d9610f876a6c5373535919b95399b959'),
    )

    data = 'min_behot_time=1576465611&api_param=%7B%22feed_load_more_new%22%3A%221%22%7D&category=answer_feed&refresh_method='

    response = requests.post('https://lf.snssdk.com/wendaapp/v1/recommend/feed/', headers=headers, params=params,
                             cookies=cookies, data=data)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.post('https://lf.snssdk.com/wendaapp/v1/recommend/feed/?iid=92974975793&device_id=7898061635&ac=wifi&channel=baidu&aid=1165&app_name=wenda&version_code=764&version_name=7.6.4&device_platform=android&ssmix=a&device_type=R8207&device_brand=OPPO&language=zh&os_api=19&os_version=4.4.4&uuid=865685026456493&openudid=aa864676b309bf74&manifest_version_code=264&resolution=720*1280&dpi=320&update_version_code=7640&_rticket=1576466025926&rom_version=coloros_v2.0.1_r8207_11_141122&fp=a_fake_fp&wenda_app_version=15&ts=1576466026&as=l26225759f9ffae6adf626&mas=00168ca7f7117c34d16ca5d9610f876a6c5373535919b95399b959', headers=headers, cookies=cookies, data=data)
    dict_data = json.loads(response.text)
    data = dict_data["data"]["data"]
    print(len(data))
    for i in data:
        uname = i["answer_layer_struct"]["user"]["uname"]
        user_id = i["answer_layer_struct"]["user"]["user_id"]
        print(uname)
        print(user_id)
        # url = "https://lf.snssdk.com/wendaapp/v3/user/brow/?other_uid=%s" % user_id
        # res = requests.get(url,headers=headers)
        # print(json.loads(res.text))


def qeh():
    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'Referer': 'http://cnews.qq.com/cnews/android/',
        # 'User-Agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56130(android)',
        # 'svqn': '1_4',
        # 'qn-rid': '7ec0b258-c31e-4376-9391-1f5d75984260',
        # 'snqn': 'J8NAd4GLIB1VK/3Yav7BmDkSBl7W2HgSqyO8H8N7B0IBY/WBwj2JF3Id20cIpytJNOoB5XtzWNolvxgJJ5Tlqi47A4sNwNt52pIwnf5iCCYphrAngDl0bcMxqhtSfgCOtuu1Jrq1nxJmVd03/LIA3A==',
        # 'qn-sig': '5c13ba4db411d31ab9bd65b3754c4edf',
    }

    params = (
        ('devid', '865685026456493'),
    )

    data = {
        'cityList': '\u5317\u4EAC',
        'id_cid': '',
        'page': '8',
        'last_id': '20191209A03EOM00',
        'lastRefreshTime': '1576547290',
        'refresh_from': 'refresh_footer',
        'method': '1',
        'isUpdatingLocation': '1',
        'last_time': '1576547290',
        'cachedCount': '18',
        'kankaninfo': '{"realTimeVideoData":{"lastestRefreshExposeData":[{"aid":"20190308V0CGVF00","algid":"","article_type":"4","channelId":"daily_timeline","exposureTime":"1576547291493","idStr":"a0846lrqvcx","policy":""}]}}',
        'picSizeMode': '0',
        'omgbizid': '',
        'Cookie': '&lskey=&luin=&skey=&uin=&logintype=0',
        'viewsub_time': '0',
        'direction': '1',
        'qn-sig': '5c13ba4db411d31ab9bd65b3754c4edf',
        'activefrom': 'icon',
        'qaid': '01401F0E7ABA4E05D0631F94D17F8E71',
        'logfrom': '0',
        'chlid': 'daily_timeline',
        'manualRefresh': '1',
        'REQExecTime': '1576548009053',
        'qqnetwork': 'wifi',
        'chRefreshTimes': '8',
        'commonIsFirstLaunch': '1',
        'unixtimesign': '1576548009058',
        'imsi_history': '460110010192032',
        'forward': '1',
        'commonGray': '1_3|2_0|12_0|49_1|14_1|17_1|30_1|99_0',
        'ssid': 'peopletech-dev',
        'REQBuildTime': '1576548009053',
        'adCookie': '{"responsed_ad_data":"TnWsPQpWrxuxKTH_pI5qj!niCjLqTouhSBgdAywbvu5RNph47er3btDRuqAfyFdQc9f2RgVh91kN6JuhnaT__bjCV9JNBg2VU!WkkaTPwyp2mt9VkdWHmP8LNUXrPENmXgSswAdSox1PBh3Oi_Lk6bGfbnvEu!JbzHaPDS1T_bOPLafn!2Yi9ZXwHTE5vdPOfrlPOQ8ZM3nOkeLhZH4pCab4fTukoW4PwdAu9hCmKDj20oul4Diaoh_7jFLLMpzpIhvzCqDRLy8ByQ9InQn9LDp3H_5sCbr1BgCtZOuOmmO97N0g8IVkhOnsuWjiPmebvji8HuzeOgOriSDV2txZCLEagzjv6Ok70!msaPlbptJkxZE6z!fvOCn!O2AlDFq9PHtVSn!SueqN4PRZpSUOs36Bh3Z69jrhp_T2mXmVth91L5lIFA!A8mmmqb!!iq7DDzvg4RPJRexMIHYQbyN1EFSf5Y!vSQGdiFWX2McReVSxXD_REfUiZy2nprUFr60tz8_cswluMMgHUl5kiQ0bTe0sO60bBy4YwNDOXAspWtllKuKCJuCrPjea0T4RCgxRLLPJc3Zf5pvNALC12dHYsaq7BUFfsQxCylJqGKPFcsaFR5nG!xFW_1iG9aUsU3Xba7lwkRIXJmAcNcg92f2rmhk5f6rYQ3r0Z_zUEKXOUXv!sHusmx0hNmervMIt!b6D0a!sMJpo7jOm7MX52HUYe19sgOKUxIGzBtpIOctAAShbwCbM0ORpJGBbXQZczUojQ4Im3wz_yiRE4xML__4pFgROb9lXvQg3qe8xlCjm4dg"}',
        'lastCheckCardType': '0',
        'oldadcode': '',
        'qn-rid': '7ec0b258-c31e-4376-9391-1f5d75984260',
        'currentTab': 'kuaibao',
        'firstStart': '0',
        'proxy_addr': '172.30.6.19:8889',
        'kingCardType': '0',
        'qimei': '865685026456493',
        'commonsid': 'b25dd995fa9041fcb128c9b043f31777',
        'sessionid': '',
        'refreshType': 'normal',
        'bssid': '16:74:9c:d9:ce:0e',
        'taid': '0101869F7F7CE858774F5EF1BA4C626006BA2A812BDE458B8993075A451FAF208D79898C8A324A2A8F67D33D',
        'preload': '1',
        'is_wap': '0',
        'imsi': '460110010192032',
        'omgid': '',
        'uid': 'aa864676b309bf74',
        'store': '9002512',
        'hw': 'OPPO_R8207',
        'devid': '865685026456493',
        'appversion': '6.1.30',
        'screen_width': '720',
        'hw_fp': 'OPPO/R8207/R1C:4.4.4/KTU84P/1390465867:user/release-keys',
        'mac': 'a8:1b:5a:2d:98:d5',
        'appver': '19_areading_6.1.30',
        'codeclevel': '0.0',
        'android_id': 'aa864676b309bf74',
        'origin_imei': '865685026456493',
        'rover': '1',
        'sceneid': '',
        'mid': 'da6e388edf43849d4714a89271e67d6093085c31',
        'apptype': 'android',
        'gpu': 'Qualcomm Adreno (TM) 405',
        'screen_height': '1280'
    }

    response = requests.post('https://r.cnews.qq.com/getSubNewsInterest', headers=headers)

    dict_data = json.loads(response.text)
    newslist = dict_data["newslist"]
    print(len(newslist))
    for i in newslist:
        chlid = i.get("chlid", "")
        chlname = i["chlname"]
        print(chlid)
        print(chlname)
        if chlid:
            print(i)


def qeh_user():
    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'Referer': 'http://cnews.qq.com/cnews/android/',
        # 'User-Agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56130(android)',
        # 'svqn': '1_4',
        # 'qn-rid': '3603149b-75c6-46bd-adb4-cddd7cbeacf9',
        # 'snqn': 'FWfNf1wLKvzEPXIafxFJPqb+onpQgoeZxzAflBvv/pcvV6KlwLff5/FOlDv9AHnzrqQ4X1rNrddxtEipMmx9tSrVUfb4XBg3CEBVTlCxATG4JUCg2YeIxofoWQXeLzh004clYXLBpEnIshivnBg1kg==',
        # 'qn-sig': '13ccbf874adb08c43d14ac8ae1952c40',
    }

    params = (
        ('devid', '865685026456493'),
    )

    data = {
        'picSizeMode': '0',
        'omgbizid': '',
        'Cookie': '&lskey=&luin=&skey=&uin=&logintype=0',
        'qn-sig': '13ccbf874adb08c43d14ac8ae1952c40',
        'media_openid': '',
        'activefrom': 'icon',
        'from': 'related_medias',
        'chlid': '5215397',
        'REQExecTime': '1576548836162',
        'qqnetwork': 'wifi',
        'commonIsFirstLaunch': '1',
        'unixtimesign': '1576548836171',
        'imsi_history': '460110010192032',
        'commonGray': '1_3|2_0|12_0|49_1|14_1|17_1|30_1|99_0',
        'ssid': 'peopletech-dev',
        'REQBuildTime': '1576548836161',
        'lastCheckCardType': '0',
        'qn-rid': '3603149b-75c6-46bd-adb4-cddd7cbeacf9',
        'currentTab': 'kuaibao',
        'proxy_addr': '172.30.6.19:8889',
        'kingCardType': '0',
        'qimei': '865685026456493',
        'commonsid': 'b25dd995fa9041fcb128c9b043f31777',
        'format': 'json',
        'bssid': '16:74:9c:d9:ce:0e',
        'taid': '0101869F7F7CE858774F5EF1BA4C626006BA2A812BDE458B8993075A451FAF208D79898C8A324A2A8F67D33D',
        'is_wap': '0',
        'imsi': '460110010192032',
        'needCluster': 'yes',
        'omgid': '',
        'uid': 'aa864676b309bf74',
        'store': '9002512',
        'hw': 'OPPO_R8207',
        'devid': '865685026456493',
        'appversion': '6.1.30',
        'screen_width': '720',
        'hw_fp': 'OPPO/R8207/R1C:4.4.4/KTU84P/1390465867:user/release-keys',
        'mac': 'a8:1b:5a:2d:98:d5',
        'appver': '19_areading_6.1.30',
        'codeclevel': '0.0',
        'android_id': 'aa864676b309bf74',
        'origin_imei': '865685026456493',
        'rover': '1',
        'sceneid': '',
        'mid': 'da6e388edf43849d4714a89271e67d6093085c31',
        'apptype': 'android',
        'gpu': 'Qualcomm Adreno (TM) 405',
        'screen_height': '1280'
    }

    response = requests.post('https://r.cnews.qq.com/getSubItem', headers=headers,
                             data=data)

    print(response.text)


def zhihu():
    cookies = {
        'q_c1': '39898967861240c794c757bf8e6e8e11|1577166064000|1577166064000',
        '_xsrf': 'CVx0eWhua7FxcJV0mMWLTtpch40FjSwP',
        'tgw_l7_route': '302fb19f026f5b11b5e883a5cbbb5031',
        'z_c0': '2|1:0|10:1577166061|4:z_c0|92:Z3QyLjBBQUFBQUJaZmZoc1FqYTZ4RWVHQUFBQUFBQXhOVlFKZ0FnQVhLUFptS3VKaEJWajZ2Y2xXNk9hb2Q3RFIxZz09|edc5a473e87f08564d41089a939b3fbd0dbda9e81768f0b392097b6773d62780',
    }

    headers = {
        'x-api-version': '3.0.86',
        'X-Ab-Param': 'se_college=default;top_ebook=0;li_vip_no_ad_mon=0;zr_expslotpaid=1;ug_goodcomment_0=1;se_zu_onebox=0;soc_bignew=1;tsp_vote=2;se_preset_label=0;se_zu_recommend=0;se_multi_task_new=2;se_cate=1;zr_km_prerank=new;se_likebutton=0;se_waterfall=0;zr_km_slot_style=event_card;se_ad_index=10;zr_prerank_heatscore=true;tp_header_style=1;sem_up_growth=in_app;ls_fmp4=0;se_wannasearch=a;li_cln_vl=no;li_query_match=0;se_cardrank_3=0;tp_qa_metacard=1;ug_fw_answ_aut_1=0;li_tjys_ec_ab=0;li_ebook_audio=1;se_dnn_unbias=1;ug_follow_answerer_0=0;top_ydyq=X;se_expired_ob=0;soc_zcfw_broadcast=0;tp_m_intro_re_topic=1;se_pek_test2=0;se_perf=0;zr_new_commodity=1;top_root=0;li_answer_card=0;zw_payc_qaedit=0;zr_slotpaidexp=3;soc_brdcst3=0;li_qc_pt=0;zr_video_recall=current_recall;soc_authormore=0;pf_noti_entry_num=0;zr_km_feed_nlp=old;zr_rewrite_query=1;se_new_merger=1;zr_art_rec=base;li_qa_ad_card=0;se_webrs=1;li_vip_lr=1;zr_km_topic_zann=new;li_album_liutongab=0;qap_payc_invite=0;tp_meta_card=0;soc_yxzl_zcfw=0;se_webtimebox=1;se_senet=0;li_se_heat=1;tp_club_pk=1;soc_leave_recommend=2;se_mobileweb=1;se_subtext=1;tp_club_header=1;se_entity_model=1;se_ltr_dnn_cp=0;se_topiclabel=1;pf_creator_card=1;se_payconsult=5;se_auto_syn=0;se_ctx=0;ls_zvideo_trans=0;se_spb309=0;tp_score_1=a;top_v_album=1;zw_sameq_sorce=999;se_college_cm=1;tp_qa_metacard_top=top;top_hotcommerce=1;zr_des_detail=0;se_cardrank_2=1;tp_sft=a;zr_paid_answer_merge=50;se_webmajorob=0;se_websearch=3;soc_update=1;zr_rec_answer_cp=close;se_cardrank_1=0;li_purchase_test=0;se_famous=1;zr_rel_search=base;top_test_4_liguangyi=1;tp_topic_entry=0;se_pek_test=0;tp_topic_head=0;li_qa_btn_text=0;zr_se_new_xgb=0;se_multianswer=1;li_qa_new_cover=1;se_pek_test3=0;top_native_answer=1;li_se_section=1;li_sku_bottom_bar_re=0;se_club_post=5;zr_article_new=close;tp_club_qa=1;se_amovietab=1;tp_sticky_android=2;li_android_vip=0;li_se_media_icon=1;zr_km_item_prerank=old;se_p_slideshow=1;qap_ques_invite=0;zr_recall_heatscore=4_6;se_col_boost=1;se_sug_entrance=0;se_hotmore=2;soc_stickypush=0;zr_paid_answer_exp=0;se_use_zitem=0;tp_sft_v2=d;se_rel_search=1;tp_topic_rec=1;pf_foltopic_usernum=50;li_hot_score_ab=0;zr_esmm_model=old;ls_zvideo_rec=2;li_paid_answer_exp=0;se_agency= 0;zr_answer_rec_cp=open;zr_intervene=1;zr_km_feed_prerank=new;se_aa_base=0;soc_zuichangfangwen=0;ug_zero_follow=0;se_ab=0;se_movietab=1;ug_zero_follow_0=0;soc_zcfw_shipinshiti=1;top_quality=0;zr_km_answer=open_cvr;se_time_threshold=0;soc_special=0;se_entity_model_14=0;se_cardrank_4=1;zr_km_sku_mix=sku_55;zr_test_aa1=1;tp_club_qa_pic=1;se_ltr_cp_new=0;top_new_feed=5;se_whitelist=1;soc_cardheight=0;se_ctr=0;se_hot_timebox=1;soc_notification=1;se_site_onebox=0;se_preset_tech=0;soc_ri_merge=0;ls_zvideo_license=1;zr_ans_rec=gbrank;zr_km_style=base;li_salt_hot=1;zr_book_chap=1;se_related_index=0;soc_zcfw_broadcast2=1;zr_km_recall=default;tp_topic_tab=0;zr_km_feed_rerank=0;li_qa_cover=old;qap_thanks=1;se_ios_spb309=1;se_sug=1;ug_newtag=1;zr_esmm_model_mix=model_17;soc_bigone=1;ls_zvideo_like=2;tsp_hotlist_ui=4;li_de=no;se_colorfultab=1;se_lottery=0;top_universalebook=1;zr_video_rank_nn=new_rank;se_new_topic=0;soc_zcfw_badcase=0;tp_qa_toast=1;ug_follow_topic_1=2;se_timebox_up=0;se_billboardsearch=0;se_featured=1;se_search_feed=N;zr_slot_cold_start=aver;zr_paid_answer_mix=mixed_13;tp_topic_style=0;soc_wonderuser_recom=0;qap_question_visitor= 0;se_adxtest=1;se_member_rescore=0;tsp_redirecthotlist=4;pf_fuceng=1;qap_question_author=0;zr_video_rank=new_rank;ug_follow_answerer=0;li_pay_banner_type=6;se_topicfeed=0;pf_newguide_vertical=0;se_hotsearch=0;se_backsearch=0;li_video_section=1;li_se_across=1;ls_videoad=2',
        'User-Agent': 'com.zhihu.android/Futureve/5.15.1 Mozilla/5.0 (Linux; Android 4.4.4; R8207 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36',
        'x-app-version': '5.15.1',
        'x-app-za': 'OS=Android&Release=4.4.4&Model=R8207&VersionName=5.15.1&VersionCode=658&Width=720&Height=1280&Installer=%E5%BA%94%E7%94%A8%E5%AE%9D&DeviceType=AndroidPhone&Brand=OPPO&OperatorType=46011',
        'x-app-flavor': 'myapp',
        'x-app-build': 'release',
        'x-network-type': 'WiFi',
        'X-SUGER': 'SU1FST04NjU2ODUwMjY0NTY0OTM7QU5EUk9JRF9JRD1hYTg2NDY3NmIzMDliZjc0O01BQz1BODoxQjo1QToyRDo5ODpENTtDT09SRF9MQVQ9MzkuOTIwMTk1O0NPT1JEX0xORz0xMTYuNDY3NjUyO0NPT1JEX1RJTUVTVEFNUD0xNTc3MTY2MDU1',
        'X-ZST-82': '1.0ALCh0-mujRAMAAAASwUAADEuMB2lAV4AAAAAjhOUX6TZ41hh3OPv1Rc7kZodna0=',
        'x-udid': 'AIDhEbGujRBLBYbEj9KXDRmGgwXGryNEAT0=',
        'Authorization': 'Bearer gt2.0AAAAABZffhsQja6xEeGAAAAAAAxNVQJgAgAXKPZmKuJhBVj6vclW6Oaod7DR1g==',
        'Host': 'api.zhihu.com',
    }

    params = (
        # ('session_token', 'a2de17617e48c22435e89b8c1dae63bd'),
        ('page_number', '5'),
        ('limit', '6'),
        ('action', 'pull'),
        ('before_id', '23'),
        ('scroll', 'up'),
        ('start_type', 'warm'),
    )

    response = requests.get('https://api.zhihu.com/topstory/recommend', headers=headers)

    print(response.text)


def fenghuang():
    headers = {
        'User-Agent': 'ifengnews/6.7.51(Android;android_4.4.4;OPPO/R8207)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'api.iclient.ifeng.com',
    }

    params = (
        # ('action', 'down'),
        # ('pullNum', '3'),
        # ('dailyOpenNum', '1'),
        # ('gv', '6.7.51'),
        # ('av', '6.7.51'),
        ('uid', str(int(time.time() * 100000))),
        # ('deviceid', '865685026456494'),
        # ('proid', 'ifengnews'),
        # ('os', 'android_19'),
        # ('df', 'androidphone'),
        # ('vt', '5'),
        # ('screen', '720x1280'),
        # ('publishid', '2607'),
        # ('nw', 'wifi'),
        # ('loginid', ''),
        # ('adAid', ''),
        ('st', str(int(time.time() * 10000))),
        # ('sn', 'c96f710ca387362468cb9c3f4321e253'),
    )

    # https://api.iclient.ifeng.com/followFeeds?uid=157794974813075&st=15779497481307
    response = requests.post('https://api.iclient.ifeng.com/followFeeds', headers=headers, params=params, )

    dict_datas = json.loads(response.text)
    print(response.url)
    if dict_datas:
        items = dict_datas[0].get("item")
        for item in items:
            try:
                followid = (item["subscribe"]["followid"])
                fenghuang_user(followid)
            except KeyError:
                pass


def fenghuang_user(followid):
    headers = {
        'User-Agent': 'ifengnews/6.7.51(Android;android_4.4.4;OPPO/R8207)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'api.3g.ifeng.com',
    }

    params = (
        ('proid', 'ifengnews'),
        ('followid', followid),
    )

    response = requests.post('https://api.3g.ifeng.com/api_wemedia_index_info', headers=headers, params=params,
                             )

    print(response.text)
    print("\n")
    print(response.url)
    print("\n")


def sina():
    import requests

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'rand': '756',
        'urlSign': '38aa974835',
        'signVer': '2.0',
        'gsid': '',
        'X-User-Agent': 'OPPO-R8207__sinanews__7.29.5__android__4.4.4__485',
        'User-Agent': 'OPPO-R8207__sinanews__7.29.5__android__4.4.4__485',
        'SN-REQID': '1578536653183cda081738346',
        'Host': 'newsapi.sina.cn',
    }

    params = (
        ('resource', 'feed'),
        ('behavior', 'manual'),
        ('lDid', '46ff19af-fe44-454f-8734-2e7a4ec6495c'),
        ('oldChwm', ''),
        ('weiboUid', ''),
        ('listCount', '17'),
        ('ua', 'OPPO-R8207__sinanews__7.29.5__android__4.4.4__485'),
        ('oaid', ''),
        ('localSign', 'a_c0f13903-f4f7-4ddc-bbc4-f0a92c2902e9'),
        ('seId', '12266f1928'),
        ('deviceModel', 'OPPO__OPPO__R8207'),
        ('andId', ''),
        ('osVersion', '4.4.4'),
        ('deviceId', 'c05aae5dffb89bcf'),
        ('ssoVer', '3'),
        ('imei', ''),
        ('chwm', '12606_0020'),
        ('mpName', '\u63A8\u8350'),
        ('upTimes', '0'),
        ('sn', ''),
        ('connectionType', '2'),
        ('lastTimestamp', '1578536631'),
        ('topStyle', 'z'),
        ('open_adtype', '0'),
        ('loadingAdTimestamp', '0'),
        ('loginType', '0'),
        ('userType', 'install'),
        ('pullTimes', '5'),
        ('appVersion', '7.29.5'),
        ('resolution', '720x1280'),
        ('replacedFlag', '1'),
        ('osSdk', '19'),
        ('authGuid', ''),
        ('sand', 'aXlldvB/MUQmU+yIl0CKSMSo0mkRYsKvBj/ssybPjcQ='),
        ('from', '6000095012'),
        ('downTimes', '4'),
        ('pullDirection', 'down'),
        ('authUid', ''),
        ('link', ''),
        ('location', '39.921582,116.473809'),
        ('deviceIdV1', 'c05aae5dffb89bcf'),
        ('authToken', ''),
        ('channel', 'news_toutiao'),
        ('accessToken', ''),
        ('aId', '01AxJCGp7n44qzdcgl6mfBgqMsr91ZQxRYApk12g4Ivt8i3WI.'),
        ('mac', ''),
        ('city', 'CN11010500000000'),
        ('weiboSuid', ''),
    )

    response = requests.get('https://newsapi.sina.cn/', headers=headers, params=params)

    print(response.text)


def qqkandian():
    import requests

    cookies = {
        'uin': '380994877',
        'skey': 'mXDhQW3neg',  # @oLkpjKGgK
    }

    headers = {
        'User-Agent': 'QQ/8.2.6 Android/0.17 Android/4.4.4',
        'Host': 'kandian.qq.com',
    }

    params = (
        ('srcID', '1'),
        ('reportInfo', 'eyJuZXR3b3JrVHlwZSI6MX0='),
        ('pageCookies', ''),
        ('bkn', '1066362718'),
        ('channelID', '40531'),
    )

    response = requests.get('https://kandian.qq.com/cgi-bin/kandianChannelFeeds/getChannelFeeds', headers=headers,
                            params=params, cookies=cookies)

    print(response.text)
    '''
    accountID
    '''


def yidian():
    import requests

    cookies = {
        'JSESSIONID': 'koBIksB-VpWY31jb9de-EA',
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'a1.go2yd.com',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8207 Build/KTU84P)',
    }

    params = (
        ('platform', '1'),
        ('appid', 'yidian'),
        ('distribution', 'app.qq.com'),
        ('version', '024400'),
        ('docid', 'V_060rMNcJ'),
        ('net', 'wifi'),
    )

    data = '{"clientInfo":{"userInfo":{"businessarea":[{"location":"39.916114,116.480024","name":"\u7EA2\u5E99"},{"location":"39.920246,116.462411","name":"\u547C\u5BB6\u697C"},{"location":"39.926917,116.472791","name":"\u6C34\u7893\u5B50"}],"region":"%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E6%9C%9D%E9%98%B3%E5%8C%BA%2C%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E9%87%91%E5%8F%B0%E5%8C%97%E8%A1%97%E9%9D%A0%E8%BF%91%E5%91%BC%E5%AE%B6%E6%A5%BC%E4%B8%AD%E5%BF%83%E5%B0%8F%E5%AD%A6%28%E4%B8%9C%E6%A0%A1%E5%8C%BA%29","vaId":"","aaId":"","imei":"fb3c75d093528f0b8a630611cda08173","cityCode":"010","androidId":"aa864676b309bf74","mac":"a8:1b:5a:2d:98:d5","adCode":"110105","country":"CN","AOI":[{"id":"B000A84J19","location":"39.92089,116.47411","area":23472.455,"name":"\u4EBA\u6C11\u65E5\u62A5\u793E\u5BBF\u820D\u5317\u533A"}],"udId":"","appVersion":"5.2.1.1","oaId":"","GPS":"39.9215693,116.4738677","language":"zh","serviceProvider":""},"requestInfo":{"is_video":false},"deviceInfo":{"screenHeight":1230,"UA":"Dalvik\\/1.6.0 (Linux; U; Android 4.4.4; R8207 Build\\/KTU84P)","ppi":320,"androidVersion":"4.4.4","model":"R8207","screenWidth":720,"manufacturer":"OPPO","device":"R1C","brand":"OPPO"}}}'

    response = requests.post('http://a1.go2yd.com/Website/contents/related-news2', headers=headers, params=params,
                             cookies=cookies)

    print(response.text)


def yidian_01():
    import requests

    cookies = {
        'JSESSIONID': 'koBIksB-VpWY31jb9de-EA',
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'a1.go2yd.com',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8207 Build/KTU84P)',
    }

    params = (
        ('platform', '1'),
        ('os', '19'),
        ('cstart', '0'),
        ('profile_id', '559026144'),
        ('androidId', '6c4360a0e0670f17979ba1d3399f2368'),
        ('appid', 'yidian'),
        ('tab', 'all'),
        ('cv', '5.2.1.1'),
        ('personalRec', '1'),
        ('distribution', 'app.qq.com'),
        ('reqid', 'fm3thb92_1579262084987_366'),
        ('version', '024400'),
        ('cend', '30'),
        ('brand', 'OPPO'),
        ('apk_meta_channel', 'app.qq.com'),
        ('signature',
         'jOJ7rPdESWAouxe-0XhXBVtyCKHebIPL4awgDjSh9Qhe3X2Znzz92Dk7cL6eUBj072YcBDfGjBEYyfey7kHT1ypt79RJ-YjZxMRDC_PRPJ7UJwLHhRqY3iTI-OXESRbtxNt5soEJdDl9bAdXdyZDVMuMXra9kJyl5pOjcV99IAc'),
        ('fields',
         ['docid', 'date', 'image', 'image_urls', 'like', 'source', 'title', 'url', 'comment_count', 'up', 'down']),
        ('net', 'wifi'),
    )

    data = '{"clientInfo":{"userInfo":{"businessarea":[{"location":"39.916114,116.480024","name":"\u7EA2\u5E99"},{"location":"39.920246,116.462411","name":"\u547C\u5BB6\u697C"},{"location":"39.926917,116.472791","name":"\u6C34\u7893\u5B50"}],"region":"%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E6%9C%9D%E9%98%B3%E5%8C%BA%2C%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E9%87%91%E5%8F%B0%E5%8C%97%E8%A1%97%E9%9D%A0%E8%BF%91%E5%91%BC%E5%AE%B6%E6%A5%BC%E4%B8%AD%E5%BF%83%E5%B0%8F%E5%AD%A6%28%E4%B8%9C%E6%A0%A1%E5%8C%BA%29","vaId":"","aaId":"","imei":"fb3c75d093528f0b8a630611cda08173","cityCode":"010","androidId":"aa864676b309bf74","mac":"a8:1b:5a:2d:98:d5","adCode":"110105","country":"CN","AOI":[{"id":"B000A84J19","location":"39.92089,116.47411","area":23472.455,"name":"\u4EBA\u6C11\u65E5\u62A5\u793E\u5BBF\u820D\u5317\u533A"}],"udId":"","appVersion":"5.2.1.1","oaId":"","GPS":"39.9215693,116.4738677","language":"zh","serviceProvider":""},"deviceInfo":{"screenHeight":1230,"UA":"Dalvik\\/1.6.0 (Linux; U; Android 4.4.4; R8207 Build\\/KTU84P)","ppi":320,"androidVersion":"4.4.4","model":"R8207","screenWidth":720,"manufacturer":"OPPO","device":"R1C","brand":"OPPO"}}}'

    response = requests.post('http://a1.go2yd.com/Website/channel/news-list-for-profile', headers=headers,
                             params=params, cookies=cookies)

    print(response.text)


# 一点资讯视频数据采集
def yidian_02():
    import requests

    cookies = {
        'JSESSIONID': 'sxYGFtM0o5FwCTBGej-BWg',
    }

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; f100 Build/LMY48Z)',
        'Content-Type': 'application/json',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Host': 'a1.go2yd.com',
    }
    params = (
        ('platform', '1'),
        ('interest_id',
         'd4XLO2ArglN7pnWr0OD5BoppFZoaTgWJVAa12BMsyLzBo9ko-f3zmRycJ3mvs5ZmLQVROR6leXjBV5RD7PtvEmcc5k8HJss_PAWize5SqwTZPs24Di4F71zKmTIc1jRtBySVQQMKJNdz1N72XQ7V5E22-SVh7CxwhsfFOyW3pax_qpBEY1987t8UYW_9Z9qJssSEcFIX8LwWNPMWXJVaPA'),
        ('appid', 'yidian'),
        # ('searchentry', 'search_video_media'),
        ('cv', '5.2.1.1'),
        ('distribution', 'app.qq.com'),
        ('reqid', 'fm3thb92_1579338720115_367'),
        ('version', '024400'),
        ('signature',
         'Ekyu6QOerg_9akX9TrP8m5xqupjdIqzDkGBk4mXobmmzxINrs09I1iP1RlvZZHqTz2_KgjAPrxopLVSCKtmaK8JLBfhdRQPPWcC3m6ZDIi8fpGn2I2pGEDgnglYPFO2eyf4LzIbjt_SMngLZPZlTGx28_GpfSRDIA6c3-T-GHj4'),
        ('fields',
         ['docid', 'date', 'image', 'image_urls', 'like', 'source', 'title', 'url', 'comment_count', 'up', 'down']),
    )

    data = '{"clientInfo": {"deviceInfo": {"model": "f100", "device": "x86", "androidVersion": "5.1.1", "screenWidth": 720, "screenHeight": 1242, "ppi": 240, "brand": "gionee", "manufacturer": "gionee", "UA": "Dalvik\\\\/2.1.0 (Linux; U; Android 5.1.1; f100 Build\\\\/LMY48Z)"}, "userInfo": {"imei": "418480a4accdedf941c5c6014e91e5fd", "mac": "00:81:2d:6b:af:12", "language": "zh", "country": "CN", "serviceProvider": "CHINA MOBILE", "appVersion": "5.0.7.2", "androidId": "1735d985f0fd1b97", "region": "", "cityCode": "010", "adCode": "110101", "GPS": "", "businessarea": [], "AOI": []}}}'

    response = requests.post('http://a1.go2yd.com/Website/channel/news-list-for-vertical', headers=headers,
                             params=params, cookies=cookies, data=data)

    print(response.text)


def yidian_03():
    import requests

    cookies = {
        'JSESSIONID': 'koBIksB-VpWY31jb9de-EA',
    }

    headers = {
        'Host': 'a1.go2yd.com',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8207 Build/KTU84P)',
    }
    params = (
        ('platform', '1'),
        ('cstart', '30'),
        ('interest_id',
         'd4XLO2ArglN7pnWr0OD5BoppFZoaTgWJVAa12BMsyLzBo9ko-f3zmRycJ3mvs5ZmLQVROR6leXjBV5RD7PtvEmcc5k8HJss_PAWize5SqwTZPs24Di4F71zKmTIc1jRtBySVQQMKJNdz1N72XQ7V5E22-SVh7CxwhsfFOyW3pax_qpBEY1987t8UYW_9Z9qJssSEcFIX8LwWNPMWXJVaPA'),
        ('appid', 'yidian'),
        ('cv', '5.2.1.1'),
        ('distribution', 'app.qq.com'),
        ('reqid', 'fm3thb92_1579339985663_360'),
        ('version', '024400'),
        ('signature',
         'uyhJIT9SIEXsjEaNfRgfmpZsNmZJGiSRRItMcX0du75WU6mmArMnzHxcuWZfzJSC-aJukwhkCJh2pjD5Rt-Vxlyw9OftdqvJibQVBevuWQbwI-0oqwYRultkAirhqzfW4hXTYZseViJIN0p017pgzwcdI8EB_AWrwQMwg0GlT54'),
        ('fields',
         ['docid', 'date', 'image', 'image_urls', 'like', 'source', 'title', 'url', 'comment_count', 'up', 'down']),
    )

    response = requests.get('http://a1.go2yd.com/Website/channel/news-list-for-vertical', headers=headers,
                            params=params, cookies=cookies)

    print(response.text)

def tonghuashun_yidin():
    import requests

    cookies = {
        'JSESSIONID': 'koBIksB-VpWY31jb9de-EA',
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'a1.go2yd.com',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8207 Build/KTU84P)',
    }

    params = (
        ('platform', '1'),
        ('os', '19'),
        ('cstart', '30'),
        ('profile_id', '227259132'),
        ('androidId', '6c4360a0e0670f17979ba1d3399f2368'),
        ('appid', 'yidian'),
        ('tab', 'all'),
        ('cv', '5.2.1.1'),
        ('personalRec', '1'),
        ('distribution', 'app.qq.com'),
        ('reqid', 'fm3thb92_1579587076743_437'),
        ('version', '024400'),
        ('cend', '30'),
        ('brand', 'OPPO'),
        ('apk_meta_channel', 'app.qq.com'),
        ('signature',
         'q67QuyJ2b8EOhjLFRKwvNc2yX8hyALGWNWaIaTTyAY9KREZvZp1Or0Sdgd1I7rmu-wUXN7-T7DwKlrwT8E2RDxZCt6LldoHrnUrPoZnMvz6diQy91Or5BAqp4mgCvFx1F0Aag3DDorqk1kvg-SmjdRrE-POc3R4Tn9lSGSynPsw'),
        ('fields',
         ['docid', 'date', 'image', 'image_urls', 'like', 'source', 'title', 'url', '\ncomment_count', 'up', 'down']),
        ('net', 'wifi'),
    )


    response = requests.post('http://a1.go2yd.com/Website/channel/news-list-for-profile', headers=headers,
                             params=params, cookies=cookies)

    data_res = json.loads(response.text)
    data_list = data_res["result"]
    for data in data_list:
        title = data["title"]
        print(title)

def fenhuang_user_list_pager():
    import requests

    headers = {
        'User-Agent': 'ifengnews/6.7.61(Android;android_4.4.4;OPPO/R8207)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'api.3g.ifeng.com',
    }

    params = (
        ('followid', ['weMedia_310999', 'weMedia_310999']),
        # ('tag', 'article'), # 文章
        ('tag', 'video'), # 视频
        ('page', '1'),
        # ('gv', '6.7.61'),
        # ('av', '6.7.61'),
        ('uid', str(int(time.time() * 100000))),
        # ('deviceid', '865685026456493'),
        # ('proid', 'ifengnews'),
        # ('os', 'android_19'),
        # ('df', 'androidphone'),
        # ('vt', '5'),
        # ('screen', '720x1280'),
        # ('publishid', '2011'),
        # ('nw', 'wifi'),
        # ('loginid', ''),
        # ('adAid', ''),
        ('st', str(int(time.time() * 10000))),
        # ('sn', '3ce24674047b4a866fe69e960c8f3d3d'),
    )


    response = requests.get('https://api.3g.ifeng.com/api_wemedia_index', headers=headers, params=params)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.post('https://api.3g.ifeng.com/api_wemedia_index?followid=weMedia_767468&tag=article&followid=weMedia_767468&page=2&gv=6.7.61&av=6.7.61&uid=865685026456493&deviceid=865685026456493&proid=ifengnews&os=android_19&df=androidphone&vt=5&screen=720x1280&publishid=2011&nw=wifi&loginid=&adAid=&st=15794157981677&sn=3ce24674047b4a866fe69e960c8f3d3d', headers=headers, data=data)

    print(response.text)

def yizhuan_zhihu(pagenum):
    import requests

    cookies = {
        'ckt': '1579573138',
        'SERVERID': 'b2423565d5dad72693e41bc165a503d1|1579573137|1579573129',
        'Identification': '18801169146',
        'Token': 'YzVlNjJhNjctNzg4Ni00N2NlLWE3ZTEtMDFlODQ2M2MzMjYxLDEwMDA4',
        'ct': 'YzVlNjJhNjctNzg4Ni00N2NlLWE3ZTEtMDFlODQ2M2MzMjYxLDEwMDA4_1579573130628',
        'Hm_lpvt_ced0fdd76ec7917e53cc84fc7c4d4777': '1579573131',
        'Hm_lvt_ced0fdd76ec7917e53cc84fc7c4d4777': '1579261744,1579513944,1579513966,1579573131',
        'sid': 'YzVlNjJhNjctNzg4Ni00N2NlLWE3ZTEtMDFlODQ2M2MzMjYxLDEwMDA4',
    }

    headers = {
        'Host': 'tool.people.cn',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'zh-cn',
        'origin': 'https://tool.people.cn',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'referer': 'https://tool.people.cn/work.html',
        'ajax': 'true',
    }

    data = 'PageIndex={}&PageSize=15&OrderBy%5B0%5D%5BName%5D=HMCTDate&OrderBy%5B0%5D%5BOrderByType%5D=2&Where%5B0%5D%5BName%5D=APID&Where%5B0%5D%5BSymbol%5D=1&Where%5B0%5D%5BValue%5D=1&Where%5B1%5D%5BName%5D=HMCTDate&Where%5B1%5D%5BSymbol%5D=5&Where%5B1%5D%5BValue%5D=2020-01-15%2000%3A00&Where%5B2%5D%5BName%5D=HMCTDate&Where%5B2%5D%5BSymbol%5D=6&Where%5B2%5D%5BValue%5D=2020-01-22%2000%3A00&cp=sw8tm81zjnq&sp=2sx142k614q2m1ok19'.format(pagenum)

    response = requests.post('https://tool.people.cn/Mediabrary/Topic/MContent', headers=headers, cookies=cookies,
                             data=data)


    print(response.text)

def douchachalist():
    import requests

    headers = {
        'Host': 'api.douchacha.com',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://www.douchacha.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Referer': 'https://www.douchacha.com/',
        'Accept-Language': 'zh-cn',
    }

    params = (
        ('\nts', '1581561604664'),
        ('he', 'www.douchacha.com'),
        ('sign', 'fbf7d86113c93ad3'),
    )

    data = '{"page_no":1,"page_size":10,"params_data":{"label_name":"","period":"WEEK","period_value":"20200209"}}'

    response = requests.post('https://api.douchacha.com/api/tiktok/ranking/user_list_gain', headers=headers,
                             params=params, data=data)

    print(response.text)

def douchachauser():
    import requests

    headers = {
        'Host': 'api.douchacha.com',
        'Origin': 'https://www.douchacha.com',
        'd-f': 'MTU4MTU2MzA3NDY1NDpuMDVzQkJBdW5yb0ZuZU5YSjNXRUVERGRtRkE1RGM0ZHhqYjAzTE5RTHNzJTNEOjYxY2Q1NGY5ZTBjZDljMTc=',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODIxNjY3NDEsInVzZXJJZCI6MTIyNzc4NTg4ODkwMTA0MjE3OCwiY3JlYXRlRGF0ZSI6IjIwMjAtMDItMTMgMTA6NDU6NDEifQ.vdzCC0TCYlppNE9_4JIQli1jxBa_85m3CbnQNuvNJsM',
        'Referer': 'https://www.douchacha.com/',
        'Accept-Language': 'zh-cn',
    }

    params = (
        ('userId', '93189025747'),
    )

    response = requests.get('https://api.douchacha.com/api/tiktok/user/profile', headers=headers, params=params)

    print(response.text)

# 第二页请求
def douchachaListNextPage():
    import requests

    headers = {
        'Host': 'api.douchacha.com',
        'Origin': 'https://www.douchacha.com',
        'Content-Type': 'application/json;charset=utf-8',
        'Accept-Language': 'zh-cn',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODIxNjY3NDEsInVzZXJJZCI6MTIyNzc4NTg4ODkwMTA0MjE3OCwiY3JlYXRlRGF0ZSI6IjIwMjAtMDItMTMgMTA6NDU6NDEifQ.vdzCC0TCYlppNE9_4JIQli1jxBa_85m3CbnQNuvNJsM',
        'Referer': 'https://www.douchacha.com/',
    }

    params = (
        ('ts', '1581570838996'),
        ('he', 'n05sBBAunroFneNXJ3WEEDDdmFA5Dc4dxjb03LNQLss='),
        ('sign', 'b4c91df9621bb001'),
    )

    data = '{"page_no":1,"page_size":10,"params_data":{"label_name":"","period":"WEEK","period_value":"20200209"}}'

    response = requests.post('https://api.douchacha.com/api/tiktok/ranking/user_list_gain', headers=headers,
                             params=params, data=data)

    print(response.text)

def sohuUser():
    import requests

    headers = {
        'Host': 'api.k.sohu.com',
        # 'x-tingyun-id': '9lCBGZzA0AQ;c=2;r=1402102220;',
        'user-agent': 'okhttp/3.9.1',
    }

    params = (
        ('p1', 'NjY1MTc2MDA4NjE2MTQ2OTUzMQ%3D%3D'),
        # ('u', '1'),
        # ('pid', '6651760620662599724'),
        # ('token',
        #  'SN_GbM4E/Eaxexa0kDUuoyN39aOkX8BH1w0lVV1.7TWnk1ulieW2AHnpfHU4mKsF856AXRsqSC5xfdQH/4Bg6GBGuhNn51MRuW6IjGI6J6TMvXbLJcRT1Ork3biVSk9I4Nn0nkBmVa69WV5.SJQVhqlVTt0KoZiAZiydNm4LuPdugA='),
        # ('gid', '02ffff11061101fe371ecc6cdf2d19603fbcdde24899b6'),
        # ('ppAppId', '110608'),
        # ('ppAppVs', '6.3.8'),
        ('queryPid', '5992226693438681195'),
    )

    response = requests.get('https://api.k.sohu.com/api/v2/usercenter/query.go',  params=params)

    print(response.text)

def sohuUserNum():
    import requests

    headers = {
        'Host': 'api.k.sohu.com',
        # 'SCOOKIE': '256f1ed86c0ee9ff332d2bf8a7bf721c7379dac52353dc2b3759ee0785e3fb3264e8e44fae390b12674e50891c12f8917898bf63dd27f95bc45f1d427e3ecef844f776997f0b05999a6ba1672ed0c2baa0facc11eedde4273683bdcb9cbe2eada24e8d2d49fdb72fdfce506d0f51c0ec420e85db253981db3c274d6ea73b9d61d37299cdd1f51e408597add8d8a668f634fade8588658c997e368022bc997837c8c8c243652021a06bf194d8474d2b781618b11140a01609968f505f7b7e295f992aa17c641d848c7102c1047f0b089f0b85ad741e31aedbad2d092fe7ce2e2bb41266f438c52bf55d072015f4d46aac9af815adf40a1d780cf6f79b0ff78179384c36528554ecf7a8d551307465ba239484f804563c0b848502458e4efef5fc0864d549556db3e91f60e962cdf04e7c04b023a9af5b648fc341227ca079a2929f906e21c98a78c5187a2c05c8fc96d366f74fce56dd4c05e9d0a53ee4f02610342186971897b1532b64cc13727f63d51b6be98a7f80db1100bf0c69c6865007bd2df2fe7f95709d439f8256cabbfe0d7cf89f269d9a3717cd6d0bc15d1fce4a5cccc6f2fb35a170aebc0863a0e68eac9dde831eb1c157dffc501057c980cb5c9b9d63fc7aa828cbb5d6586b65c9aa908370f352bd63fd7ccc668aa6abe5d1b5f8f32000611682ea0e4f70c9a35dce6dbd3ffa3389deaf054453027962c419e0be36e33a0c3ebe5efcd96c2e42ac7ca205c64a915a955b993469ef57cb9612a26e1b5a4243ba80f555527d6a4e8123ea',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.116 Mobile Safari/537.36 JsKit/1.0 (Android);',
        'Referer': 'https://api.k.sohu.com/h5apps/newssdk.sohu.com/modules/newSearch/newSearch.html?type=morepop&keyfrom=input&refertype=1&keyword=7500km',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
    }

    params = (
        # ('rt', 'json'),
        # ('pageNo', '1'),
        ('words', '每日经济新闻'),
        # ('keyword', '7500km'),
        ('p1', 'NjY1MTc2MDA4NjE2MTQ2OTUzMQ=='),
        # ('pageSize', '10'),
        # ('type', '0'),
        # ('pid', '6651760620662599724'),
        # ('token',
        #  'SN_GbM4E/Eaxexa0kDUuoyN39aOkX8BH1w0lVV1.7TWnk1ulieW2AHnpfHU4mKsF856AXRsqSC5xfdQH/4Bg6GBGuhNn51MRuW6IjGI6J6TMvXbLJcRT1Ork3biVSk9I4Nn0nkBmVa69WV5.SJQVhqlVTt0KoZiAZiydNm4LuPdugA='),
        # ('gid', '02ffff11061101fe371ecc6cdf2d19603fbcdde24899b6'),
        # ('apiVersion', '42'),
        # ('sid', '10'),
        # ('u', '1'),
        # ('bid', ''),
        # ('keyfrom', 'input'),
        # ('autoCorrection', ''),
        # ('refertype', '1'),
        # ('versionName', '6.3.8'),
        # ('os', 'android'),
        # ('picScale', '16'),
        # ('h', '1812'),
        # ('_', '1587544433763'),
    )

    response = requests.get('https://api.k.sohu.com/api/search/v6/search.go', headers=headers, params=params)


    print(response.text)

if __name__ == '__main__':
    # douchachalist()
    # douchachauser()
    sohuUserNum()