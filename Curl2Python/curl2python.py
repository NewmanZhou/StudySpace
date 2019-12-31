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
        chlid = i.get("chlid","")
        chlname = i["chlname"]
        print(chlid)
        print(chlname)
        if chlid :
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
        ('action', 'down'),
        ('pullNum', '3'),
        ('dailyOpenNum', '1'),
        ('gv', '6.7.51'),
        ('av', '6.7.51'),
        ('uid', '865685026456494'),
        ('deviceid', '865685026456494'),
        ('proid', 'ifengnews'),
        ('os', 'android_19'),
        ('df', 'androidphone'),
        ('vt', '5'),
        ('screen', '720x1280'),
        ('publishid', '2607'),
        ('nw', 'wifi'),
        ('loginid', ''),
        ('adAid', ''),
        ('st', str(int(time.time()*10000))),
        ('sn', 'c96f710ca387362468cb9c3f4321e253'),
    )


    response = requests.post('https://api.iclient.ifeng.com/followFeeds', headers=headers, params=params, )

    dict_datas = json.loads(response.text)
    if dict_datas:
        items = dict_datas[0].get("item")
        for item in items:
            try:
                followid = (item["subscribe"]["followid"])
                fenghuang_user(followid)
            except Exception:
                print(item)

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
    print("\n\n")
    print(response.url)

if __name__ == '__main__':
    # while True:
    fenghuang()
    # fenghuang_user("source_封面新闻")

