# -*- coding: utf-8 -*-
# @Time   : 2021/4/8 11:34 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: raid_forums.py
# @Software: PyCharm
from scrapy.http import HtmlResponse


def getList():
    import requests

    headers = {
        'authority': 'raidforums.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://raidforums.com/Forum-Leaks-Market',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '__cfduid=d9a71ee157baa0921dd7b7ae50cda9f601617278345; PHPSESSID=kq7qlk2ab95e2s9fpppohioftp; _ga=GA1.2.1976683420.1617785940; _gid=GA1.2.917586713.1617785940; RFLovesYou_category-tab-preference=tab87%2Ctab93; RFLovesYou_mybb[announcements]=0; RFLovesYou_mybb[threadread]=a%3A2%3A%7Bi%3A130954%3Bi%3A1617786381%3Bi%3A131327%3Bi%3A1617786469%3B%7D; cf_chl_prog=a23; cf_clearance=39edb051c6f5099962ce1a393061f8f820eb88e2-1617850447-0-250; RFLovesYou_mybb[lastvisit]=1617786469; RFLovesYou_sid=d4365804f931c92a4ff973512da5c288; RFLovesYou_mybb[lastactive]=1617851348',
    }

    params = (
        ('page', '2'),
    )

    url = 'https://raidforums.com/Forum-Leaks-Market'
    response = requests.get(url, headers=headers, params=params)

    print(url, response.text)






def create_response(url, html):
    response = HtmlResponse(url=url, encoding='utf-8', body=html)
    return response.xpath

def parse_list():
    url = 'https://raidforums.com/Forum-Leaks-Market'
    str_html = '''
    <!DOCTYPE html>
    <html xml:lang="en" lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>Leaks Market | RaidForums</title>
    <meta property="og:title" content="Leaks Market | RaidForums" />
    <meta property="og:image" content="https://cdn.raidforums.com/i/RF_sSL0.png" />
    <meta name="twitter:title" content="Leaks Market | RaidForums" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@1dot3dot3dot7" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@1dot3dot3dot7" />
    <meta name="keywords" content="RaidForums, Free Databases, Database Forums, Leak Forums, Database Dumps, Database Breaches, Databases, Marketplace, Leaks, Breaches, Combolists, Cracking, free premium accounts, Wordlists" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <script src="/cdn-cgi/apps/head/cTLepM-aow2UFHXBvxRTmiQXyls.js"></script><link rel="icon" type="image/x-icon" href="https://cdn.raidforums.com/s/favicon.ico" />
    <link rel="shortcut icon" type="image/x-icon" href="https://cdn.raidforums.com/s/favicon.ico" />
    <link type="application/rss+xml" rel="alternate" title="Latest Threads (RSS 2.0)" href="https://raidforums.com/syndication.php" />
    <link type="application/atom+xml" rel="alternate" title="Latest Threads (Atom 1.0)" href="https://raidforums.com/syndication.php?type=atom1.0" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/all.min.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/roboto.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/normalize.min.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/lib.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/global.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/custom.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/ficons.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/star_ratings.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/thread_status.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/css3.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/alerts.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/plugins.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/mobile.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/hovercards.min.css?v=6.9" />
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/jquery.js?ver=3.5.1"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/jquery.plugins.min.js"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/general.js"></script><script type="text/javascript">
    <!--
    	lang.unknown_error = "An unknown error has occurred.";
    	lang.select2_match = "One result is available, press enter to select it.";
    	lang.select2_matches = "{1} results are available, use up and down arrow keys to navigate.";
    	lang.select2_nomatches = "No matches found";
    	lang.select2_inputtooshort_single = "Please enter one or more character";
    	lang.select2_inputtooshort_plural = "Please enter {1} or more characters";
    	lang.select2_inputtoolong_single = "Please delete one character";
    	lang.select2_inputtoolong_plural = "Please delete {1} characters";
    	lang.select2_selectiontoobig_single = "You can only select one item";
    	lang.select2_selectiontoobig_plural = "You can only select {1} items";
    	lang.select2_loadmore = "Loading more results&hellip;";
    	lang.select2_searching = "Searching&hellip;";

    	var templates = {
    		modal: "<div class=\"modal\">\
    	<div style=\"overflow-y: auto; max-height: 400px;\">\
    		<table border=\"0\" cellspacing=\"0\" cellpadding=\"5\" class=\"tborder\">\
    			<tr>\
    				<td class=\"thead\" colspan=\"2\"><strong>__message__</strong></td>\
    			</tr>\
    			<tr>\
    				<td colspan=\"2\" class=\"trow1\">\
    				<div style=\"text-align: center\" class=\"modal_buttons\">__buttons__</div></td>\
    			</tr>\
    		</table>\
    	</div>\
    </div>",
    		modal_button: "<input type=\"submit\" class=\"button\" value=\"__title__\"/>&nbsp;"
    	};

    	var cookieDomain = ".raidforums.com";
    	var cookiePath = "/";
    	var cookiePrefix = "RFLovesYou_";
    	var cookieSecureFlag = "1";
    	var deleteevent_confirm = "Are you sure you want to delete this event?";
    	var removeattach_confirm = "Are you sure you want to remove the selected attachment from this post?";
    	var loading_text = 'Loading. <br />Please Wait&hellip;';
    	var saving_changes = 'Saving changes&hellip;';
    	var use_xmlhttprequest = "1";
    	var my_post_key = "b912526a0a0e2e398808b8fd7ddbfac7";
    	var rootpath = "https://raidforums.com";
    	var imagepath = "https://cdn.raidforums.com/images/raid";
      	var yes_confirm = "Yes";
    	var no_confirm = "No";
    	var MyBBEditor = null;
    	var spinner_image = "https://cdn.raidforums.com/images/raid/spinner.gif";
    	var spinner = "<i class='fas fa-spinner fa-spin'></i>";
    	var modal_zindex = 9999;
    // -->
    </script>
    <link rel="alternate" type="application/rss+xml" title="Latest Threads in Leaks Market (RSS 2.0)" href="https://raidforums.com/syndication.php?fid=216" />
    <link rel="alternate" type="application/atom+xml" title="Latest Threads in Leaks Market (Atom 1.0)" href="https://raidforums.com/syndication.php?type=atom1.0&amp;fid=216" />
    <script type="text/javascript">
    <!--
    	lang.no_new_posts = "Forum Contains No New Posts";
    	lang.click_mark_read = "Click to mark this forum as read";
    	lang.inline_edit_description = "(Click and hold to edit)";
    	lang.post_fetch_error = "There was an error fetching the posts.";
    // -->
    </script>

    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/jeditable/jeditable.min.js"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/inline_edit.js?v=1821"></script>
    <meta name="description" content="A place to buy/sell/trade databases and leaks...." />
    <meta name="twitter:description" content="A place to buy/sell/trade databases and leaks...." />
    <meta name="og:description" content="A place to buy/sell/trade databases and leaks...." />
    <link rel="canonical" href="https://raidforums.com/Forum-Leaks-Market" />
    </head>
    <body>
    <script src="https://cdn.raidforums.com/jscripts/raid_colors.js"></script>
    <div id="container">
    <a name="top" id="top"></a>
    <header>
    <nav id="panel">
    <div class="wrapper" style="">
    <div id="sidenav">
    <div class="sidenav__bars"><i class="fas fa-bars"></i></div>
    <ul class="sidenav__menu nav">
    <li class="sidenav__home hidden-sm"><a href="https://raidforums.com"><i class="fas fa-home"></i></a></li>
    <li><a href="https://rf.ws/databases"><i class="fas fa-database"></i>Databases</a></li>
    <li><a href="https://raidforums.com/upgrades.php"><i class="fas fa-star"></i>Upgrades</a></li>
    <li class="sidenav__extras dropdown">
    <a href="https://raidforums.com/extras.php" class="dropdown-button">
    <i class="fas fa-plus"></i>Extras
    </a>
    <ul class="sidenav__sub-menu dropdown-content nav-columns rounded" data-position="-7">
    <li>
    <a href="https://raidforums.com/newpoints.php">
    <i class="fas fa-coins"></i>Credits
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/awards.php">
    <i class="fas fa-medal"></i>Awards
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/bans.php">
    <i class="fas fa-user-slash"></i>Ban List
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/misc.php?action=help">
    <i class="fas fa-briefcase"></i>Rules & Policies
    </a>
    </li>
    </ul>
    </li>
    </ul>
    </div>
    <ul class="panel__user nav">
    <li>
    <a href="https://raidforums.com/member.php?action=login" class="panel__module panel__module--login rounded"><i class="fas fa-sign-in-alt"></i>Login</a>
    </li>
    <li class="talign-mright">
    <a href="https://raidforums.com/member.php?action=register" class="panel__module panel__module--register rounded"><i class="fas fa-user-plus"></i>Register</a>
    </li>
    </ul>
    </div>
    </nav>
    <div class="logo noselect">
    <div class="wrapper" style="">
    <div class="logo__image" style="display: block;">
    <a href="https://raidforums.com"><img src="https://cdn.raidforums.com/s/logo/Logo_default.png" alt="RaidForums" title="RaidForums" /></a>
    </div>
    <div class="logo__text" style="display: none;">
    <a href="https://raidforums.com"><span>RAID</span>FORUMS</a>
    </div>
    </div>
    </div>
    </header>
    <nav id="breadcrumb" class="wrapper rounded-top" style="">
    <ul class="breadcrumb__main nav talign-mleft">
    <li class="breadcrumb__bit"><a href="https://raidforums.com/index.php">RaidForums</a>
    <span class="breadcrumb__sep"><i class="fas fa-angle-right hidden-md"></i></span>
    </li>
    <li class="breadcrumb__bit"><a href="Forum-Leaks">Leaks</a></li>
    <span class="breadcrumb__sep"><i class="fas fa-angle-right hidden-md"></i></span>
    <li class="breadcrumb__active">Leaks Market</li>
    </ul>
    <ul class="breadcrumb__fast-links nav talign-mright">
    <li class="hidden-lg">
    <a href="https://raidforums.com/misc.php?action=markread&my_post_key=b912526a0a0e2e398808b8fd7ddbfac7" class="rounded">
    Mark all as read
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/search.php?action=getdaily" class="rounded">
    Today's posts
    </a>
    </li>
    </ul>
    </nav>
    <main id="content" class="wrapper rounded-bottom" style="">
    <fieldset class="advert"><legend>Temporary Advertisements:</legend><div><a href="https://xsmtp.to/" rel="nofollow" target="_blank"><img loading="lazy" src="https://cdn.raidforums.com/i/RF_AnaO.gif" width="600px" height="70px" alt="XSMTP Advertisement" title="XSMTP Advertisement"></a></div></fieldset><br>

    <section id="forum-info" class="talign-mleft talign-mright rounded">
    <div class="forum-info__forum">
    <div class="forum-info__icon-row ficon_216 d-table-cell align-middle">
    <i class="fas fa-circle-notch"></i>
    </div>
    <div class="d-table-cell">
    <span class="forum-info__name rounded">Leaks Market</span>
    <div class="forum-info__description">
    A place to buy/sell/trade databases and leaks.
    <a href="misc.php?action=markread&amp;fid=216">Mark this forum read</a>
    </div>
    </div>
    </div>
    <div class="forum-info__new-thread">
    </div>
    </section>
    <section id="forum-display">
    <table border="0" cellspacing="0" cellpadding="5" class="tborder tfixed">
    <tr>
    <td class="thead thead--dark"><strong>Rules</strong></td>
    </tr>
    <tr>
    <td class="trow1 scaleimages">Do not post multiple threads for the same shop or sale, this is strictly forbidden and will result in an instant ban (if you need to edit your thread contact a mod).<br />
    Do not bump your thread more than once a day or you will also be banned.<br />
    Use the following format or your thread will be deleted; <a href="misc.php?action=safelinks&url=https%3A%2F%2Fraidforums.com%2FThread-STAFF-Leaks-Market-Format" target="_blank" rel="noopener" class="mycode_url">https://raidforums.com/Thread-STAFF-Leaks-Market-Format</a></td>
    </tr>
    </table>
    <br />
    <div class="forum-display__pagination-top">
    <div class="pagination talign-mleft">
    <span class="pages">Pages (147):</span>
    <span class="pagination_current">1</span>
    <a href="Forum-Leaks-Market?page=2" class="pagination_page">2</a>
    <a href="Forum-Leaks-Market?page=3" class="pagination_page">3</a>
    <a href="Forum-Leaks-Market?page=4" class="pagination_page">4</a>
    <a href="Forum-Leaks-Market?page=5" class="pagination_page">5</a>
    &hellip; <a href="Forum-Leaks-Market?page=147" class="pagination_last">147</a>
    <a href="Forum-Leaks-Market?page=2" class="pagination_next">Next &raquo;</a>
    <div class="popup_menu drop_go_page" style="display: none;">
    <form action="Forum-Leaks-Market?page=1" method="post">
    <label for="page">Jump to page:</label> <input type="number" class="textbox" name="page" value="1" size="4" min="1" max="147" />
    <input type="submit" class="button" value="Go" />
    </form>
    </div>
    <a href="javascript:void(0)" class="go_page" title="Jump to page"><i class="fas fa-caret-down fa-fw" title="Jump to page"></i></a>&nbsp;
    <script type="text/javascript">
    	var go_page = 'go_page_' + $(".go_page").length;
    	$(".go_page").last().attr('id', go_page);
    	$(".drop_go_page").last().attr('id', go_page + '_popup');
    	$('#' + go_page).popupMenu(false).on('click', function() {
    		var drop_go_page = $(this).prev('.drop_go_page');
    		if (drop_go_page.is(':visible')) {
    			drop_go_page.find('.textbox').trigger('focus');
    		}
    	});
    </script>
    </div>
    </div>
    <table border="0" cellspacing="0" cellpadding="5" class="forum-display__thread-list tborder clear">
    <tr>
    <td class="thead forum-display__thread-tcat" colspan="2" width="66%"><span class="smalltext"><strong><a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=subject&amp;order=asc">Thread</a> / <a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=starter&amp;order=asc">Author</a> </strong></span></td>
    <td class="thead hidden-sm" align="center" width="7%"><span class="smalltext"><strong><a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=replies&amp;order=desc">Replies</a> </strong></span></td>
    <td class="thead hidden-sm" align="center" width="7%"><span class="smalltext"><strong><a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=views&amp;order=desc">Views</a> </strong></span></td>
    <td class="thead hidden-sm" align="right" width="20%"><span class="smalltext"><strong><a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=lastpost&amp;order=desc">Last Post</a>
    <span class="smalltext">[<a href="Forum-Leaks-Market?datecut=9999&amp;prefix=0&amp;sortby=lastpost&amp;order=asc">asc</a>]</span>
    </strong></span></td>
    </tr>
    <tr>
    <td class="tcat" colspan="6">Forum Announcements</td>
    </tr>
    <tr>
    <td align="center" class="trow1 forumdisplay_announcement" width="2%"><span class="thread_status folder" title=""><i class="fas fa-folder"></i></span></td>

    <td class="trow1 forumdisplay_announcement forum-display__thread-name">
    <a href="Announcement-RaidForums-Mirrors" class="subject_old">RaidForums Mirrors</a>
    <div class="author smalltext"><a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></div>
    </td>
    <td align="center" class="trow1 forumdisplay_announcement hidden-sm">-</td>
    <td align="center" class="trow1 forumdisplay_announcement hidden-sm">-</td>
    <td class="trow1 forumdisplay_announcement hidden-sm" style="white-space: nowrap; text-align: right"><span class="smalltext">April 25, 2020 at 07:35 PM</span></td>
    </tr>
    <tr>
    <td align="center" class="trow2 forumdisplay_announcement" width="2%"><span class="thread_status folder" title=""><i class="fas fa-folder"></i></span></td>

    <td class="trow2 forumdisplay_announcement forum-display__thread-name">
    <a href="Announcement-Official-Middleman-Service" class="subject_old">Official Middleman Service</a>
    <div class="author smalltext"><a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></div>
    </td>
    <td align="center" class="trow2 forumdisplay_announcement hidden-sm">-</td>
    <td align="center" class="trow2 forumdisplay_announcement hidden-sm">-</td>
    <td class="trow2 forumdisplay_announcement hidden-sm" style="white-space: nowrap; text-align: right"><span class="smalltext">July 24, 2018 at 05:03 PM</span></td>
    </tr>
    <tr>
    <td align="center" class="trow1 forumdisplay_announcement" width="2%"><span class="thread_status folder" title=""><i class="fas fa-folder"></i></span></td>

    <td class="trow1 forumdisplay_announcement forum-display__thread-name">
    <a href="Announcement-How-to-get-Credits" class="subject_old">How to get Credits?</a>
    <div class="author smalltext"><a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></div>
    </td>
    <td align="center" class="trow1 forumdisplay_announcement hidden-sm">-</td>
    <td align="center" class="trow1 forumdisplay_announcement hidden-sm">-</td>
    <td class="trow1 forumdisplay_announcement hidden-sm" style="white-space: nowrap; text-align: right"><span class="smalltext">January 01, 1970 at 01:59 PM</span></td>
    </tr>
    <tr>
    <td class="tcat" colspan="6">Important Threads</td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--hotfolder inline_row paid-sticky-row">
    <td align="center" class="trow1 forumdisplay_sticky" width="2%">
    <span class="thread_status hotfolder" title="No new posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_sticky">
    <div>
    <div> <span class="rf_tprefix rf_stickyp">PAID-STICKY</span>&nbsp;<span class=" subject_old" id="tid_129470"><a href="Thread-PAID-STICKY-SELLING-COMBOS-BRIKK-ME-HIGHEST-QUALITY-COMBOS" class="forum-display__thread-name"><span class="forum-display__thread-subject">SELLING COMBOS - BRIKK.ME HIGHEST QUALITY COMBOS</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-BriKK"><span class="rf_i rf_mvp">BriKK</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 19, 2021 at 06:53 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-PAID-STICKY-SELLING-COMBOS-BRIKK-ME-HIGHEST-QUALITY-COMBOS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-BriKK"><span class="rf_i rf_mvp">BriKK</span></a> (<span title="April 08, 2021 at 02:18 AM">6 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=129470" onclick="MyBB.whoPosted(129470); return false;">10</a></td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm">5,939</td>
    <td class="trow1 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 02:18 AM">6 hours ago</span><br />
    <a href="Thread-PAID-STICKY-SELLING-COMBOS-BRIKK-ME-HIGHEST-QUALITY-COMBOS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-BriKK"><span class="rf_i rf_mvp">BriKK</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row paid-sticky-row">
    <td align="center" class="trow2 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix rf_stickyp">PAID-STICKY</span>&nbsp;<span class=" subject_new" id="tid_113649"><a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91" class="forum-display__thread-name"><span class="forum-display__thread-subject">BUYING Private databases【Indonesia】</span></a></span>
    <span class="smalltext">(Pages:
    <a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91">1</a>
    <a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91?page=2">2</a>
    )</span>
    </div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-spookjun"><span class="rf_i rf_god">spookjun</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> November 01, 2020 at 11:10 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-80R3XU5"><span class="rf_noob">80R3XU5</span></a> (March 31, 2021 at 07:25 PM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=113649" onclick="MyBB.whoPosted(113649); return false;">22</a></td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm">37,379</td>
    <td class="trow2 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">March 31, 2021 at 07:25 PM<br />
    <a href="Thread-PAID-STICKY-BUYING-Private-databases%E3%80%90Indonesia%E3%80%91?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-80R3XU5"><span class="rf_noob">80R3XU5</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row paid-sticky-row">
    <td align="center" class="trow1 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix rf_stickyp">PAID-STICKY</span>&nbsp;<span class=" subject_new" id="tid_115636"><a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn" class="forum-display__thread-name"><span class="forum-display__thread-subject">BUYING decrypted private databases and us ssn</span></a></span>
    <span class="smalltext">(Pages:
    <a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn">1</a>
    <a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn?page=2">2</a>
    )</span>
    </div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-actor"><span class="rf_i rf_god">actor</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> November 20, 2020 at 01:30 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Limeimei"><span class="rf_noob">Limeimei</span></a> (March 24, 2021 at 01:18 PM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=115636" onclick="MyBB.whoPosted(115636); return false;">18</a></td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm">24,019</td>
    <td class="trow1 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">March 24, 2021 at 01:18 PM<br />
    <a href="Thread-PAID-STICKY-BUYING-decrypted-private-databases-and-us-ssn?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Limeimei"><span class="rf_noob">Limeimei</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotclosefolder inline_row">
    <td align="center" class="trow2 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotclosefolder" title="New posts. Hot thread. Closed thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-STAFF-Jaw-s-Middleman-Service?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_staffp">IMPORTANT-READ</span>&nbsp;<span class=" subject_new" id="tid_118402"><a href="Thread-STAFF-Jaw-s-Middleman-Service" class="forum-display__thread-name"><span class="forum-display__thread-subject">Jaw's Middleman Service</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Jaw"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>Jaw</b></span> </a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> December 16, 2020 at 05:18 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-STAFF-Jaw-s-Middleman-Service?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Jaw"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>Jaw</b></span> </a> (February 09, 2021 at 09:12 PM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=118402" onclick="MyBB.whoPosted(118402); return false;">1</a></td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm">17,090</td>
    <td class="trow2 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">February 09, 2021 at 09:12 PM<br />
    <a href="Thread-STAFF-Jaw-s-Middleman-Service?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Jaw"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>Jaw</b></span> </a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotclosefolder inline_row">
    <td align="center" class="trow1 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotclosefolder" title="New posts. Hot thread. Closed thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-STAFF-Tips-For-Safe-Trades--96794?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_staffp">IMPORTANT-READ</span>&nbsp;<span class=" subject_new" id="tid_96794"><a href="Thread-STAFF-Tips-For-Safe-Trades--96794" class="forum-display__thread-name"><span class="forum-display__thread-subject">Tips For Safe Trades</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-moot"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>moot</b></span> </a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> May 30, 2020 at 09:19 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-STAFF-Tips-For-Safe-Trades--96794?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-moot"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>moot</b></span> </a> (May 30, 2020 at 09:19 AM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=96794" onclick="MyBB.whoPosted(96794); return false;">0</a></td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm">27,280</td>
    <td class="trow1 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">May 30, 2020 at 09:19 AM<br />
    <a href="Thread-STAFF-Tips-For-Safe-Trades--96794?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-moot"><i class="rf_a"></i><span class="rf_owner" style="color: #ecf0f1; text-shadow: 2px 2px 6px #b30000;" <b>moot</b></span> </a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotclosefolder inline_row">
    <td align="center" class="trow2 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotclosefolder" title="New posts. Hot thread. Closed thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-STAFF-Leaks-Market-Format?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_staffp">IMPORTANT-READ</span>&nbsp;<span class=" subject_new" id="tid_85193"><a href="Thread-STAFF-Leaks-Market-Format" class="forum-display__thread-name"><span class="forum-display__thread-subject">Leaks Market Format</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> February 20, 2020 at 02:13 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-STAFF-Leaks-Market-Format?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a> (February 20, 2020 at 02:13 AM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=85193" onclick="MyBB.whoPosted(85193); return false;">0</a></td>
    <td align="center" class="trow2 forumdisplay_sticky hidden-sm">29,635</td>
    <td class="trow2 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">February 20, 2020 at 02:13 AM<br />
    <a href="Thread-STAFF-Leaks-Market-Format?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotclosefolder inline_row">
    <td align="center" class="trow1 forumdisplay_sticky" width="2%">
    <span class="thread_status newhotclosefolder" title="New posts. Hot thread. Closed thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_sticky">
    <div>
    <div>
    <a href="Thread-Database-Trading-Buying-Selling?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class=" subject_new" id="tid_26051"><a href="Thread-Database-Trading-Buying-Selling" class="forum-display__thread-name"><span class="forum-display__thread-subject">Database Trading/Buying/Selling</span></a></span>
    <span class="smalltext">(Pages:
    <a href="Thread-Database-Trading-Buying-Selling">1</a>
    <a href="Thread-Database-Trading-Buying-Selling?page=2">2</a>
    <a href="Thread-Database-Trading-Buying-Selling?page=3">3</a>
    <a href="Thread-Database-Trading-Buying-Selling?page=4">4</a>
    ... <a href="Thread-Database-Trading-Buying-Selling?page=233">233</a>
    )</span>
    </div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Omnichorus"><span class="rf_i rf_god">Omnichorus</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> September 07, 2017 at 03:17 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-Database-Trading-Buying-Selling?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a> (February 20, 2020 at 01:59 AM)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=26051" onclick="MyBB.whoPosted(26051); return false;">2,791</a></td>
    <td align="center" class="trow1 forumdisplay_sticky hidden-sm">1,281,648</td>
    <td class="trow1 forumdisplay_sticky hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext">February 20, 2020 at 01:59 AM<br />
    <a href="Thread-Database-Trading-Buying-Selling?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Omnipotent"><i class="rf_o"></i><span class="rf_owner">Omnipotent</span></a></span>
    </td>
    </tr>
    <tr>
    <td class="tcat" colspan="6">Normal Threads</td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-Games-User-Pass-9kk-Mailpass-1-7kk-HQ-Volorant-League-of-Legends-Twitch?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_128231"><a href="Thread-SELLING-Games-User-Pass-9kk-Mailpass-1-7kk-HQ-Volorant-League-of-Legends-Twitch" class="forum-display__thread-name"><span class="forum-display__thread-subject">Games User:Pass 9kk||Mailpass 1.7kk HQ Volorant/League of Legends/Twitch</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 08, 2021 at 09:09 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-Games-User-Pass-9kk-Mailpass-1-7kk-HQ-Volorant-League-of-Legends-Twitch?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a> (<span title="April 08, 2021 at 08:18 AM">17 minutes ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=128231" onclick="MyBB.whoPosted(128231); return false;">1</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">2,022</td>
     <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 08:18 AM">17 minutes ago</span><br />
    <a href="Thread-SELLING-Games-User-Pass-9kk-Mailpass-1-7kk-HQ-Volorant-League-of-Legends-Twitch?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-Crypto-dump-25-file-MailPass?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_128428"><a href="Thread-SELLING-Crypto-dump-25-file-MailPass" class="forum-display__thread-name"><span class="forum-display__thread-subject">Crypto dump |25-file| MailPass</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 09, 2021 at 08:37 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-Crypto-dump-25-file-MailPass?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a> (<span title="April 08, 2021 at 08:16 AM">18 minutes ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=128428" onclick="MyBB.whoPosted(128428); return false;">2</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">3,287</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 08:16 AM">18 minutes ago</span><br />
    <a href="Thread-SELLING-Crypto-dump-25-file-MailPass?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Djinne"><span class="rf_i rf_vip">Djinne</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_131302"><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record" class="forum-display__thread-name"><span class="forum-display__thread-subject">LinkedIn 1Billion(1000Million) Record</span></a></span>
    <span class="smalltext">(Pages:
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record">1</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=2">2</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=3">3</a>
    )</span>
    </div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-TomLiner"><span class="rf_i rf_god">TomLiner</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 03, 2021 at 01:41 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-test112299"><span class="rf_i rf_vip">test112299</span></a> (<span title="April 08, 2021 at 08:16 AM">18 minutes ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131302" onclick="MyBB.whoPosted(131302); return false;">32</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">6,208</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 08:16 AM">18 minutes ago</span><br />
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-test112299"><span class="rf_i rf_vip">test112299</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-Alexa-Rank-59k-Online-Marketing-Majority-USA-Webshell?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_129104"><a href="Thread-SELLING-Alexa-Rank-59k-Online-Marketing-Majority-USA-Webshell" class="forum-display__thread-name"><span class="forum-display__thread-subject">Alexa Rank 59k - Online Marketing - Majority USA - Webshell</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-kehanet00"><span class="rf_elite">kehanet00</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 16, 2021 at 11:53 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-Alexa-Rank-59k-Online-Marketing-Majority-USA-Webshell?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-0x123"><span class="rf_noob">0x123</span></a> (<span title="April 08, 2021 at 08:07 AM">27 minutes ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=129104" onclick="MyBB.whoPosted(129104); return false;">4</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">702</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 08:07 AM">27 minutes ago</span><br />
    <a href="Thread-SELLING-Alexa-Rank-59k-Online-Marketing-Majority-USA-Webshell?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-0x123"><span class="rf_noob">0x123</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-China-BIGDATA-QQ-QQ-INFO-WEIBO-PHONE-1-5-BILLION-RECORDS?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_127889"><a href="Thread-SELLING-China-BIGDATA-QQ-QQ-INFO-WEIBO-PHONE-1-5-BILLION-RECORDS" class="forum-display__thread-name"><span class="forum-display__thread-subject">China: BIGDATA (QQ+QQ INFO+WEIBO+PHONE) (1,5 BILLION RECORDS)</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-PieWithNothing"><span class="rf_i rf_god">PieWithNothing</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 05, 2021 at 12:38 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-China-BIGDATA-QQ-QQ-INFO-WEIBO-PHONE-1-5-BILLION-RECORDS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-dataenth"><span class="rf_noob">dataenth</span></a> (<span title="April 08, 2021 at 07:36 AM">58 minutes ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=127889" onclick="MyBB.whoPosted(127889); return false;">4</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">1,718</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 07:36 AM">58 minutes ago</span><br />
    <a href="Thread-SELLING-China-BIGDATA-QQ-QQ-INFO-WEIBO-PHONE-1-5-BILLION-RECORDS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-dataenth"><span class="rf_noob">dataenth</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-phone-name-credit-limit-of-Vietnam?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_130851"><a href="Thread-SELLING-phone-name-credit-limit-of-Vietnam" class="forum-display__thread-name"><span class="forum-display__thread-subject">phone, name, credit limit of Vietnam</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-nmnn"><span class="rf_noob">nmnn</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 30, 2021 at 05:38 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-phone-name-credit-limit-of-Vietnam?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-nmnn"><span class="rf_noob">nmnn</span></a> (<span title="April 08, 2021 at 07:29 AM">1 hour ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=130851" onclick="MyBB.whoPosted(130851); return false;">5</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">639</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 07:29 AM">1 hour ago</span><br />
    <a href="Thread-SELLING-phone-name-credit-limit-of-Vietnam?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-nmnn"><span class="rf_noob">nmnn</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div> 
    <a href="Thread-SELLING-btcmarkets-net-accounts-leak?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_132105"><a href="Thread-SELLING-btcmarkets-net-accounts-leak" class="forum-display__thread-name"><span class="forum-display__thread-subject">btcmarkets.net accounts leak</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-dribbledata"><span class="rf_i rf_vip">dribbledata</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> <span title="April 08, 2021 at 07:21 AM">1 hour ago</span></span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-btcmarkets-net-accounts-leak?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-dribbledata"><span class="rf_i rf_vip">dribbledata</span></a> (<span title="April 08, 2021 at 07:21 AM">1 hour ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=132105" onclick="MyBB.whoPosted(132105); return false;">0</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">24</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 07:21 AM">1 hour ago</span><br />
    <a href="Thread-SELLING-btcmarkets-net-accounts-leak?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-dribbledata"><span class="rf_i rf_vip">dribbledata</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_132073"><a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook" class="forum-display__thread-name"><span class="forum-display__thread-subject">Companies DB from linkedin or facebook</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-jcanale13"><span class="rf_noob">jcanale13</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> <span title="April 07, 2021 at 09:11 PM">11 hours ago</span></span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-billion025"><span class="rf_noob">billion025</span></a> (<span title="April 08, 2021 at 07:10 AM">1 hour ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=132073" onclick="MyBB.whoPosted(132073); return false;">1</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">161</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 07:10 AM">1 hour ago</span><br />
    <a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-billion025"><span class="rf_noob">billion025</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-daryn-online-3-mill-bcrypt-Kazakhstan-with-phone-numbers?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_131293"><a href="Thread-SELLING-daryn-online-3-mill-bcrypt-Kazakhstan-with-phone-numbers" class="forum-display__thread-name"><span class="forum-display__thread-subject">daryn.online 3 mill bcrypt Kazakhstan with phone numbers</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-kyogre"><span class="rf_noob">kyogre</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 03, 2021 at 12:24 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-daryn-online-3-mill-bcrypt-Kazakhstan-with-phone-numbers?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-kyogre"><span class="rf_noob">kyogre</span></a> (<span title="April 08, 2021 at 06:16 AM">2 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131293" onclick="MyBB.whoPosted(131293); return false;">2</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">155</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 06:16 AM">2 hours ago</span><br />
    <a href="Thread-SELLING-daryn-online-3-mill-bcrypt-Kazakhstan-with-phone-numbers?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-kyogre"><span class="rf_noob">kyogre</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Crypto-exchanges-databases-Ledger-or-others?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131677"><a href="Thread-BUYING-Crypto-exchanges-databases-Ledger-or-others" class="forum-display__thread-name"><span class="forum-display__thread-subject">Crypto exchanges databases | Ledger or others</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Globaks"><span class="rf_noob">Globaks</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 05, 2021 at 03:05 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Crypto-exchanges-databases-Ledger-or-others?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-mizaru1337"><span class="rf_noob">mizaru1337</span></a> (<span title="April 08, 2021 at 05:35 AM">2 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131677" onclick="MyBB.whoPosted(131677); return false;">2</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">146</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 05:35 AM">2 hours ago</span><br />
    <a href="Thread-BUYING-Crypto-exchanges-databases-Ledger-or-others?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-mizaru1337"><span class="rf_noob">mizaru1337</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-Free-11k-India-student-database-Free-with-email-and-phone-numbers?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_131298"><a href="Thread-SELLING-Free-11k-India-student-database-Free-with-email-and-phone-numbers" class="forum-display__thread-name"><span class="forum-display__thread-subject">Free 11k India student database Free with email and phone numbers</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-thunder-buddie"><span class="rf_noob">thunder_buddie</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 03, 2021 at 12:56 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-Free-11k-India-student-database-Free-with-email-and-phone-numbers?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-azadforever"><span class="rf_noob">azadforever</span></a> (<span title="April 08, 2021 at 05:23 AM">3 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131298" onclick="MyBB.whoPosted(131298); return false;">5</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">430</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 05:23 AM">3 hours ago</span><br />
    <a href="Thread-SELLING-Free-11k-India-student-database-Free-with-email-and-phone-numbers?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-azadforever"><span class="rf_noob">azadforever</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Seeking-Online-casino-and-casino-affiliates-databases?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131969"><a href="Thread-BUYING-Seeking-Online-casino-and-casino-affiliates-databases" class="forum-display__thread-name"><span class="forum-display__thread-subject">Seeking Online casino and casino affiliates databases</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-pusimiga"><span class="rf_noob">pusimiga</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> <span title="April 07, 2021">Yesterday</span> at 03:18 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
     <a href="Thread-BUYING-Seeking-Online-casino-and-casino-affiliates-databases?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Soco"><span class="rf_noob">Soco</span></a> (<span title="April 08, 2021 at 05:19 AM">3 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131969" onclick="MyBB.whoPosted(131969); return false;">1</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">120</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 05:19 AM">3 hours ago</span><br />
    <a href="Thread-BUYING-Seeking-Online-casino-and-casino-affiliates-databases?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Soco"><span class="rf_noob">Soco</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-BUYING-GERMAN-DATABASES-2020?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131517"><a href="Thread-BUYING-BUYING-GERMAN-DATABASES-2020" class="forum-display__thread-name"><span class="forum-display__thread-subject">BUYING GERMAN DATABASES 2020</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-dyson01"><span class="rf_i rf_vip">dyson01</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 04, 2021 at 10:47 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-BUYING-GERMAN-DATABASES-2020?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 04:28 AM">4 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131517" onclick="MyBB.whoPosted(131517); return false;">2</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">245</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 04:28 AM">4 hours ago</span><br />
    <a href="Thread-BUYING-BUYING-GERMAN-DATABASES-2020?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-BE-Private-Email-base-w-additional-info?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131623"><a href="Thread-BUYING-BE-Private-Email-base-w-additional-info" class="forum-display__thread-name"><span class="forum-display__thread-subject">[BE] Private Email base w/additional info</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-cartercartier"><span class="rf_i rf_god">cartercartier</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 05, 2021 at 10:07 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-BE-Private-Email-base-w-additional-info?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 04:26 AM">4 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131623" onclick="MyBB.whoPosted(131623); return false;">1</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">178</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 04:26 AM">4 hours ago</span><br />
    <a href="Thread-BUYING-BE-Private-Email-base-w-additional-info?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Looking-for-worldwide-crypto-leads-db?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131735"><a href="Thread-BUYING-Looking-for-worldwide-crypto-leads-db" class="forum-display__thread-name"><span class="forum-display__thread-subject">Looking for worldwide crypto leads/db</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-wilki123"><span class="rf_noob">wilki123</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 05, 2021 at 07:36 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Looking-for-worldwide-crypto-leads-db?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 04:16 AM">4 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131735" onclick="MyBB.whoPosted(131735); return false;">3</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">184</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 04:16 AM">4 hours ago</span><br />
    <a href="Thread-BUYING-Looking-for-worldwide-crypto-leads-db?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Private-dumps-or-crypto-related-data?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_130919"><a href="Thread-BUYING-Private-dumps-or-crypto-related-data" class="forum-display__thread-name"><span class="forum-display__thread-subject">Private dumps or crypto related data</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Mileena"><span class="rf_noob">Mileena</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 30, 2021 at 08:09 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Private-dumps-or-crypto-related-data?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 04:09 AM">4 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=130919" onclick="MyBB.whoPosted(130919); return false;">3</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">522</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 04:09 AM">4 hours ago</span><br />
    <a href="Thread-BUYING-Private-dumps-or-crypto-related-data?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Buying-US-verified-leads?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131216"><a href="Thread-BUYING-Buying-US-verified-leads" class="forum-display__thread-name"><span class="forum-display__thread-subject">Buying US verified leads</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-michealferhuson"><span class="rf_noob">michealferhuson</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 02, 2021 at 05:00 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Buying-US-verified-leads?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 03:20 AM">5 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131216" onclick="MyBB.whoPosted(131216); return false;">1</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">169</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 03:20 AM">5 hours ago</span><br />
    <a href="Thread-BUYING-Buying-US-verified-leads?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Crypto-Combo-Leads?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_131304"><a href="Thread-BUYING-Crypto-Combo-Leads" class="forum-display__thread-name"><span class="forum-display__thread-subject">Crypto Combo/Leads</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-alisonbucker"><span class="rf_noob">alisonbucker</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 03, 2021 at 01:58 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Crypto-Combo-Leads?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 03:17 AM">5 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131304" onclick="MyBB.whoPosted(131304); return false;">1</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">165</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 03:17 AM">5 hours ago</span><br />
    <a href="Thread-BUYING-Crypto-Combo-Leads?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-USA-PRIVATE-DEHASHED-DB-S?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_130953"><a href="Thread-BUYING-USA-PRIVATE-DEHASHED-DB-S" class="forum-display__thread-name"><span class="forum-display__thread-subject">USA PRIVATE DEHASHED DB'S</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-omarr0"><span class="rf_elite">omarr0</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 31, 2021 at 01:58 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-USA-PRIVATE-DEHASHED-DB-S?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a> (<span title="April 08, 2021 at 03:13 AM">5 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=130953" onclick="MyBB.whoPosted(130953); return false;">4</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">528</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 03:13 AM">5 hours ago</span><br />
    <a href="Thread-BUYING-USA-PRIVATE-DEHASHED-DB-S?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Rollins"><i class="rf_i rf_god"></i><span style="color: #800080; text-shadow: 2px 2px 3px #00000;"><b>Rollins</b></span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Brazilian-APIS?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_132063"><a href="Thread-BUYING-Brazilian-APIS" class="forum-display__thread-name"><span class="forum-display__thread-subject">Brazilian APIS</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-henry-11"><span class="rf_noob">henry_11</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> <span title="April 07, 2021">Yesterday</span> at 07:37 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Brazilian-APIS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Kissie"><span class="rf_noob">Kissie</span></a> (<span title="April 08, 2021 at 02:55 AM">5 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=132063" onclick="MyBB.whoPosted(132063); return false;">1</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">225</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 02:55 AM">5 hours ago</span><br />
    <a href="Thread-BUYING-Brazilian-APIS?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Kissie"><span class="rf_noob">Kissie</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newfolder" title="New posts."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-BUYING-Virustotal-VT-API-keys?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<span class=" subject_new" id="tid_132059"><a href="Thread-BUYING-Virustotal-VT-API-keys" class="forum-display__thread-name"><span class="forum-display__thread-subject">Virustotal (VT) API keys</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-baluji"><span class="rf_noob">baluji</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> <span title="April 07, 2021">Yesterday</span> at 06:40 PM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-BUYING-Virustotal-VT-API-keys?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Kissie"><span class="rf_noob">Kissie</span></a> (<span title="April 08, 2021 at 02:54 AM">5 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=132059" onclick="MyBB.whoPosted(132059); return false;">1</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">156</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 02:54 AM">5 hours ago</span><br />
    <a href="Thread-BUYING-Virustotal-VT-API-keys?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Kissie"><span class="rf_noob">Kissie</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow1 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow1 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-3M-Cashalo-com?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_131540"><a href="Thread-SELLING-3M-Cashalo-com" class="forum-display__thread-name"><span class="forum-display__thread-subject">[3M] Cashalo.com</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-Drekavac"><span class="rf_i rf_god">Drekavac</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> April 05, 2021 at 12:07 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-3M-Cashalo-com?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-papertowel"><span class="rf_noob">papertowel</span></a> (<span title="April 08, 2021 at 01:57 AM">6 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131540" onclick="MyBB.whoPosted(131540); return false;">3</a></td>
    <td align="center" class="trow1 forumdisplay_regular hidden-sm">631</td>
    <td class="trow1 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 01:57 AM">6 hours ago</span><br />
    <a href="Thread-SELLING-3M-Cashalo-com?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-papertowel"><span class="rf_noob">papertowel</span></a></span>
    </td>
    </tr>
    <tr class="forum-display__thread forum-display__thread--newhotfolder inline_row">
    <td align="center" class="trow2 forumdisplay_regular" width="2%">
    <span class="thread_status newhotfolder" title="New posts. Hot thread."><i class="fas fa-folder"></i></span>
    </td>
    <td class="trow2 forumdisplay_regular">
    <div>
    <div>
    <a href="Thread-SELLING-France-Eu-Licensed-Anime-Product-Database?action=newpost" class="forum-display__thread-prefix forum-display__thread-prefix--new-thread rounded" title="Go to first unread post">New</a>
    <span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<span class=" subject_new" id="tid_129872"><a href="Thread-SELLING-France-Eu-Licensed-Anime-Product-Database" class="forum-display__thread-name"><span class="forum-display__thread-subject">France + Eu - Licensed Anime Product - Database</span></a></span></div>
    <span class="author smalltext">by <a href="https://raidforums.com/User-kehanet00"><span class="rf_elite">kehanet00</span></a></span>
    <span class="forum-display__thread-date"><i class="far fa-clock"></i> March 23, 2021 at 12:59 AM</span>
    <div class="smalltext visible-sm">
    <div class="lastpost">
    <a href="Thread-SELLING-France-Eu-Licensed-Anime-Product-Database?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-kehanet00"><span class="rf_elite">kehanet00</span></a> (<span title="April 08, 2021 at 12:50 AM">7 hours ago</span>)
    </div>
    </div>
    </div>
    </td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm"><a href="https://raidforums.com/misc.php?action=whoposted&tid=129872" onclick="MyBB.whoPosted(129872); return false;">2</a></td>
    <td align="center" class="trow2 forumdisplay_regular hidden-sm">591</td>
    <td class="trow2 forumdisplay_regular hidden-sm" style="white-space: nowrap; text-align: right;">
    <span class="lastpost smalltext"><span title="April 08, 2021 at 12:50 AM">7 hours ago</span><br />
    <a href="Thread-SELLING-France-Eu-Licensed-Anime-Product-Database?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-kehanet00"><span class="rf_elite">kehanet00</span></a></span>
    </td>
    </tr>
    <tr>
    <td class="tfoot" align="right" colspan="6">
    <form action="forumdisplay.php" method="get">
    <input type="hidden" name="fid" value="216" />
    <select name="sortby">
    <option value="subject">Sort by: Subject</option>
    <option value="lastpost" selected="selected">Sort by: Last Post</option>
    <option value="starter">Sort by: Author</option>
    <option value="started">Sort by: Creation Time</option>
    <option value="replies">Sort by: Replies</option>
    <option value="views">Sort by: Views</option>
    </select>
    <select name="order">
    <option value="asc">Order: Ascending</option>
    <option value="desc" selected="selected">Order: Descending</option>
    </select>
    <select name="datecut">
    <option value="1">From: Today</option>
    <option value="5">From: 5 Days Ago</option>
    <option value="10">From: 10 Days Ago</option>
    <option value="20">From: 20 Days Ago</option>
    <option value="50">From: 50 Days Ago</option>
    <option value="75">From: 75 Days Ago</option>
    <option value="100">From: 100 Days Ago</option>
    <option value="365">From: The Last Year</option>
    <option value="9999" selected="selected">From: The Beginning</option>
    </select>
    <select name="prefix">
    <option value="-2">Prefix: Any Prefix</option>
    <option value="-1">Prefix: No Prefix</option>
    <option value="0" selected="selected">Prefix: Any/No Prefix</option>
    <option value="29">Prefix: BUYING</option>
    <option value="33">Prefix: PAID-STICKY</option>
    <option value="34">Prefix: READ-ME</option>
    <option value="27">Prefix: SELLING</option>
    <option value="32">Prefix: STAFF</option>
    <option value="28">Prefix: TRADING</option>
    </select>
    <input type="submit" class="button" value="Go" />
    </form>
    </td>
    </tr>
    </table>
    <div class="float_left">
    <div class="pagination talign-mleft">
    <span class="pages">Pages (147):</span>
    <span class="pagination_current">1</span>
    <a href="Forum-Leaks-Market?page=2" class="pagination_page">2</a>
    <a href="Forum-Leaks-Market?page=3" class="pagination_page">3</a>
    <a href="Forum-Leaks-Market?page=4" class="pagination_page">4</a>
    <a href="Forum-Leaks-Market?page=5" class="pagination_page">5</a>
    &hellip; <a href="Forum-Leaks-Market?page=147" class="pagination_last">147</a>
    <a href="Forum-Leaks-Market?page=2" class="pagination_next">Next &raquo;</a>
    <div class="popup_menu drop_go_page" style="display: none;">
    <form action="Forum-Leaks-Market?page=1" method="post">
    <label for="page">Jump to page:</label> <input type="number" class="textbox" name="page" value="1" size="4" min="1" max="147" />
    <input type="submit" class="button" value="Go" />
    </form>
    </div>
    <a href="javascript:void(0)" class="go_page" title="Jump to page"><i class="fas fa-caret-down fa-fw" title="Jump to page"></i></a>&nbsp;
    <script type="text/javascript">
    	var go_page = 'go_page_' + $(".go_page").length;
    	$(".go_page").last().attr('id', go_page);
    	$(".drop_go_page").last().attr('id', go_page + '_popup');
    	$('#' + go_page).popupMenu(false).on('click', function() {
    		var drop_go_page = $(this).prev('.drop_go_page');
    		if (drop_go_page.is(':visible')) {
    			drop_go_page.find('.textbox').trigger('focus');
    		}
    	});
    </script>
    </div>
    </div>
    <div class="float_right" style="margin-top: 4px;">
    </div>
    <br class="clear" />
    <br />
    <section id="forum-tools" class="group talign-pleft talign-pright">
    <div class="forum-tools__legend float-left rounded">
    <ul class="forum-tools__nav-legend nav-columns rounded">
    <li><span class="thread_status newfolder" title="New Posts"><i class="fas fa-folder fa-fw"></i></span> New Posts</li>
    <li><span class="thread_status folder" title="No New Posts"><i class="fas fa-folder fa-fw"></i></span> No New Posts</li>
    <li><span class="thread_status newhotfolder" title="Hot Thread (New)"><i class="fas fa-folder fa-fw"></i></span> Hot Thread (New)</li>
    <li><span class="thread_status hotfolder" title="Hot Thread (No New)"><i class="fas fa-folder fa-fw"></i></span> Hot Thread (No New)</li>
    </ul>
    </div>
    <div class="float-right" style="text-align: right;">
    </div>
    </section>
    </section>
    <br />
    <section id="users-browsing" class="smalltext"><i class="fas fa-street-view"></i> &nbsp;Users browsing this forum: <a href="https://raidforums.com/User-0x123"><span class="rf_noob">0x123</span></a>, <a href="https://raidforums.com/User-4wayswing"><span class="rf_await">4wayswing</span></a>, <a href="https://raidforums.com/User-aaQSteRbFPcEqFV"><span class="rf_noob">aaQSteRbFPcEqFV</span></a>, <a href="https://raidforums.com/User-barthomer"><span class="rf_noob">barthomer</span></a>, <a href="https://raidforums.com/User-biomushroom"><span class="rf_noob">biomushroom</span></a>, <a href="https://raidforums.com/User-challenggee"><span class="rf_noob">challenggee</span></a>, <a href="https://raidforums.com/User-codymulliniks"><span class="rf_noob">codymulliniks</span></a>, <a href="https://raidforums.com/User-DragonDwarf"><span class="rf_noob">DragonDwarf</span></a>, <a href="https://raidforums.com/User-dribbledata"><span class="rf_i rf_vip">dribbledata</span></a>, <a href="https://raidforums.com/User-fr33kl0w"><span class="rf_noob">fr33kl0w</span></a>, <a href="https://raidforums.com/User-gammorah"><span class="rf_noob">gammorah</span></a>, <a href="https://raidforums.com/User-jp022"><span class="rf_noob">jp022</span></a>, <a href="https://raidforums.com/User-kurobutah"><span class="rf_noob">kurobutah</span></a>, <a href="https://raidforums.com/User-m2ma"><span class="rf_noob">m2ma</span></a>, <a href="https://raidforums.com/User-meowpower"><span class="rf_noob">meowpower</span></a>, <a href="https://raidforums.com/User-mresh987"><span class="rf_i rf_vip">mresh987</span></a>, <a href="https://raidforums.com/User-Mr-APT"><span class="rf_member">Mr_APT</span></a>, <a href="https://raidforums.com/User-n110"><span class="rf_noob">n110</span></a>, <a href="https://raidforums.com/User-naginagi-nomi"><span class="rf_noob">naginagi-nomi</span></a>, <a href="https://raidforums.com/User-Nono24"><span class="rf_noob">Nono24</span></a>, <a href="https://raidforums.com/User-nullable"><span class="rf_i rf_vip">nullable</span></a>, <a href="https://raidforums.com/User-PyroTank"><span class="rf_noob">PyroTank</span></a>, <a href="https://raidforums.com/User-s0muchraid"><span class="rf_noob">s0muchraid</span></a>, <a href="https://raidforums.com/User-siberkuvvet"><span class="rf_noob">siberkuvvet</span></a>, <a href="https://raidforums.com/User-Silent-Plug"><span class="rf_i rf_mvp">Silent-Plug</span></a>, <a href="https://raidforums.com/User-tawjarvis"><span class="rf_i rf_vip">tawjarvis</span></a>, <a href="https://raidforums.com/User-testwahaha"><span class="rf_noob">testwahaha</span></a>, <a href="https://raidforums.com/User-topor3z"><span class="rf_noob">topor3z</span></a>, <a href="https://raidforums.com/User-vikvikvik"><span class="rf_noob">vikvikvik</span></a>, <a href="https://raidforums.com/User-warri0r23"><span class="rf_member">warri0r23</span></a>, <a href="https://raidforums.com/User-wixedteam"><span class="rf_i rf_vip">wixedteam</span></a>, <a href="https://raidforums.com/User-Z3r0471"><span class="rf_i rf_mvp">Z3r0471</span></a>, <a href="https://raidforums.com/User-zachariahburt"><span class="rf_noob">zachariahburt</span></a>, 5 Invisible User(s), 38 Guest(s)</section>
    </main> 
    <footer id="footer">
    <div class="footer__upper">
    <div class="wrapper talign-pright talign-pleft" style="">
    <ul class="footer__general-links nav">
    <li><a href="https://raidforums.com"><i class="fa fa-home footicon"></i>Raid Forums</a></li>
    <li><a href="./misc.php?action=help&hid=24"><i class="fa fa-envelope footicon"></i>Contact Us</a></li>

    <li><a href="misc.php?action=help"><i class="fa fa-briefcase footicon"></i>Legal Policies</a></li>

    <li><a href="https://raidforums.com/misc.php?action=syndication"><i class="fa fa-rss footicon"></i>RSS Syndication</a></li>
    </ul>
    <ul class="footer__social-links nav">
    <li><a href="https://rf.ws/keybase" target="_blank" class="footer__keybase"><i class="fab fa-keybase"></i></a></li>
    <li><a href="https://rf.ws/telegram" target="_blank" class="footer__telegram"><i class="fab fa-telegram-plane"></i></a></li>
    <li><a href="https://rf.ws/facebook" target="_blank" class="footer__facebook"><i class="fab fa-facebook-f"></i></a></li>
    <li><a href="https://rf.ws/youtube" target="_blank" class="footer__youtube"><i class="fab fa-youtube"></i></a></li>
    <li><a href="https://rf.ws/twitter" target="_blank" class="footer__twitter"><i class="fab fa-twitter"></i></a></li>
    </ul>
    </div>
    </div>
    <div class="footer__lower">
    <div class="wrapper talign-pright talign-pleft" style="">
    <div class="footer__datetime"><strong>Current time:</strong> April 08, 2021, 08:35 AM</div>
    <div class="footer__copyright">
    Powered By <a href="https://raidforums.com/User-Omnipotent" target="_blank">Omnipotent</a>, &copy; <a href="//www.dmca.com/Protection/Status.aspx?ID=c9c968fb-e6df-4653-ac37-89cc29dea488&refurl=https://raidforums.com/" target="_blank">2015-2021</a>
    </div>
    </div>
    </div>
    </footer>
    </div> 
    <div id="guest-alert" class="guest-alert rounded hidden-md" style="display:none">
    <div class="guest-alert__head">Guest Alert!</div>
    <a href="member.php?action=register" class="smalltext">Join today to experience everything we have to offer such as Leaks, Database Breaches, Adult Content and much more.</a>
    <a nohref title="Close Welcome Message" class="guest-alert__close hide-parent-onclick">x</a>
    </div>
    <script src="https://cdn.raidforums.com/jscripts/raid.js?v=1.3" defer></script>
    <div id="scrolltop" title="Jump Up" style="display:none"></div>
    <script src="https://cdn.raidforums.com/jscripts/raid_scrolltop.js" async defer></script>
    </body>
    </html>
    '''
    base_url = 'https://raidforums.com/'
    xp = create_response(url, str_html)
    list_datas = xp('//tr[contains(@class,"forum-display__thread")]')
    print(len(list_datas))
    for data in list_datas:
        title = data.xpath('td[2]/div/div[1]//span[@class="forum-display__thread-subject"]/text()').extract_first()
        url = base_url + data.xpath(
            'td[2]/div/div[1]//span[@class="forum-display__thread-subject"]/../@href').extract_first()

        user_id = data.xpath('td[2]//span[@class="author smalltext"]/a/span/text()').extract_first()
        publish_time = data.xpath('td[2]//span[@class="forum-display__thread-date"]/text()').extract_first().strip()
        if not publish_time:
            publish_time = data.xpath('td[2]//span[@class="forum-display__thread-date"]/span/@title') \
                .extract_first()
        print(title)
        print(user_id)
        print(publish_time)
        print(url)
        print('\n')


def parse_content():
    content_html = '''
    <!DOCTYPE html>
    <html xml:lang="en" lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>LinkedIn 1Billion(1000Million) Record | RaidForums</title>
    <meta property="og:type" content="article" />
    <meta property="og:title" content="LinkedIn 1Billion(1000Million) Record | RaidForums" />
    <meta name="twitter:title" content="LinkedIn 1Billion(1000Million) Record | RaidForums" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@1dot3dot3dot7" />
    <meta name="keywords" content="RaidForums, Free Databases, Database Forums, Leak Forums, Database Dumps, Database Breaches, Databases, Marketplace, Leaks, Breaches, Combolists, Cracking, free premium accounts, Wordlists" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <script src="/cdn-cgi/apps/head/cTLepM-aow2UFHXBvxRTmiQXyls.js"></script><link rel="icon" type="image/x-icon" href="https://cdn.raidforums.com/s/favicon.ico" />
    <link rel="shortcut icon" type="image/x-icon" href="https://cdn.raidforums.com/s/favicon.ico" />
    <link type="application/rss+xml" rel="alternate" title="Latest Threads (RSS 2.0)" href="https://raidforums.com/syndication.php" />
    <link type="application/atom+xml" rel="alternate" title="Latest Threads (Atom 1.0)" href="https://raidforums.com/syndication.php?type=atom1.0" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/all.min.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/roboto.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/s/css/normalize.min.css" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/lib.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/global.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/custom.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/showthread.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/star_ratings.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/css3.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/alerts.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/plugins.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/mobile.min.css?v=6.9" />
    <link type="text/css" rel="stylesheet" href="https://cdn.raidforums.com/cache/themes/theme29/hovercards.min.css?v=6.9" />
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/jquery.js?ver=3.5.1"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/jquery.plugins.min.js"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/general.js"></script><script type="text/javascript">
    <!--
    	lang.unknown_error = "An unknown error has occurred.";
    	lang.select2_match = "One result is available, press enter to select it.";
    	lang.select2_matches = "{1} results are available, use up and down arrow keys to navigate.";
    	lang.select2_nomatches = "No matches found";
    	lang.select2_inputtooshort_single = "Please enter one or more character";
    	lang.select2_inputtooshort_plural = "Please enter {1} or more characters";
    	lang.select2_inputtoolong_single = "Please delete one character";
    	lang.select2_inputtoolong_plural = "Please delete {1} characters";
    	lang.select2_selectiontoobig_single = "You can only select one item";
    	lang.select2_selectiontoobig_plural = "You can only select {1} items";
    	lang.select2_loadmore = "Loading more results&hellip;";
    	lang.select2_searching = "Searching&hellip;";

    	var templates = {
    		modal: "<div class=\"modal\">\
    	<div style=\"overflow-y: auto; max-height: 400px;\">\
    		<table border=\"0\" cellspacing=\"0\" cellpadding=\"5\" class=\"tborder\">\
    			<tr>\
    				<td class=\"thead\" colspan=\"2\"><strong>__message__</strong></td>\
    			</tr>\
    			<tr>\
    				<td colspan=\"2\" class=\"trow1\">\
    				<div style=\"text-align: center\" class=\"modal_buttons\">__buttons__</div></td>\
    			</tr>\
    		</table>\
    	</div>\
    </div>",
    		modal_button: "<input type=\"submit\" class=\"button\" value=\"__title__\"/>&nbsp;"
    	};

    	var cookieDomain = ".raidforums.com";
    	var cookiePath = "/";
    	var cookiePrefix = "RFLovesYou_";
    	var cookieSecureFlag = "1";
    	var deleteevent_confirm = "Are you sure you want to delete this event?";
    	var removeattach_confirm = "Are you sure you want to remove the selected attachment from this post?";
    	var loading_text = 'Loading. <br />Please Wait&hellip;';
    	var saving_changes = 'Saving changes&hellip;';
    	var use_xmlhttprequest = "1";
    	var my_post_key = "b912526a0a0e2e398808b8fd7ddbfac7";
    	var rootpath = "https://raidforums.com";
    	var imagepath = "https://cdn.raidforums.com/images/raid";
      	var yes_confirm = "Yes";
    	var no_confirm = "No";
    	var MyBBEditor = null;
    	var spinner_image = "https://cdn.raidforums.com/images/raid/spinner.gif";
    	var spinner = "<i class='fas fa-spinner fa-spin'></i>";
    	var modal_zindex = 9999;
    // -->
    </script>
    <script type="text/javascript">
    <!--
    	var quickdelete_confirm = "Are you sure you want to delete this post?";
    	var quickrestore_confirm = "Are you sure you want to restore this post?";
    	var allowEditReason = "1";
    	lang.save_changes = "Save Changes";
    	lang.cancel_edit = "Cancel Edit";
    	lang.quick_edit_update_error = "There was an error editing your reply:";
    	lang.quick_reply_post_error = "There was an error posting your reply:";
    	lang.quick_delete_error = "There was an error deleting your reply:";
    	lang.quick_delete_success = "The post was deleted successfully.";
    	lang.quick_delete_thread_success = "The thread was deleted successfully.";
    	lang.quick_restore_error = "There was an error restoring your reply:";
    	lang.quick_restore_success = "The post was restored successfully.";
    	lang.editreason = "Edit Reason";
    	lang.post_deleted_error = "You can not perform this action to a deleted post.";
    	lang.softdelete_thread = "Soft Delete Thread";
    	lang.restore_thread = "Restore Thread";
    // -->
    </script>

    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/report.js?ver=1820"></script>
    <script src="https://cdn.raidforums.com/jscripts/jeditable/jeditable.min.js"></script>
    <script type="text/javascript" src="https://cdn.raidforums.com/jscripts/thread.js?ver=1822"></script>
    <script>
    var securitycaptcha = {
    	newreply: 1,
    	editpost: 1
    }
    $(function() {
    	if (securitycaptcha.newreply)
    		$('#quick_reply_submit').off('click');

    	if (securitycaptcha.editpost)
    		$('[id^=edit_post_]').off('click');
    })
    </script>
    <meta property="og:image" content="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" />
    <meta name="twitter:image" content="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" />
    <meta name="description" content="I have 520Million +500Million Other Data My Telegram: 1- 520Million data: 50 records as sample: {&quot;Key&quot;:&quot;IDaec32d2de20b3b87&quot;,&quot;FirstName&quot;:&quot;Nur&quot;,&quot;LastName&quot;:&quot;S..." />
    <meta name="twitter:description" content="I have 520Million +500Million Other Data My Telegram: 1- 520Million data: 50 records as sample: {&quot;Key&quot;:&quot;IDaec32d2de20b3b87&quot;,&quot;FirstName&quot;:&quot;Nur&quot;,&quot;LastName&quot;:&quot;S..." />
    <meta name="og:description" content="I have 520Million +500Million Other Data My Telegram: 1- 520Million data: 50 records as sample: {&quot;Key&quot;:&quot;IDaec32d2de20b3b87&quot;,&quot;FirstName&quot;:&quot;Nur&quot;,&quot;LastName&quot;:&quot;S..." />
    <link rel="canonical" href="https://raidforums.com/Thread-SELLING-LinkedIn-1Billion-1000Million-Record" />
    </head>
    <body>
    <script src="https://cdn.raidforums.com/jscripts/raid_colors.js"></script>
    <div id="container">
    <a name="top" id="top"></a>
    <header>
    <nav id="panel">
    <div class="wrapper" style="">
    <div id="sidenav">
    <div class="sidenav__bars"><i class="fas fa-bars"></i></div>
    <ul class="sidenav__menu nav">
    <li class="sidenav__home hidden-sm"><a href="https://raidforums.com"><i class="fas fa-home"></i></a></li>
    <li><a href="https://rf.ws/databases"><i class="fas fa-database"></i>Databases</a></li>
    <li><a href="https://raidforums.com/upgrades.php"><i class="fas fa-star"></i>Upgrades</a></li>
    <li class="sidenav__extras dropdown">
    <a href="https://raidforums.com/extras.php" class="dropdown-button">
    <i class="fas fa-plus"></i>Extras
    </a>
    <ul class="sidenav__sub-menu dropdown-content nav-columns rounded" data-position="-7">
    <li>
    <a href="https://raidforums.com/newpoints.php">
    <i class="fas fa-coins"></i>Credits
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/awards.php">
    <i class="fas fa-medal"></i>Awards
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/bans.php">
    <i class="fas fa-user-slash"></i>Ban List
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/misc.php?action=help">
    <i class="fas fa-briefcase"></i>Rules & Policies
    </a>
    </li>
    </ul>
    </li>
    </ul>
    </div>
    <ul class="panel__user nav">
    <li>
    <a href="https://raidforums.com/member.php?action=login" class="panel__module panel__module--login rounded"><i class="fas fa-sign-in-alt"></i>Login</a>
    </li>
    <li class="talign-mright">
    <a href="https://raidforums.com/member.php?action=register" class="panel__module panel__module--register rounded"><i class="fas fa-user-plus"></i>Register</a>
    </li>
    </ul>
    </div>
    </nav>
    <div class="logo noselect">
    <div class="wrapper" style="">
    <div class="logo__image" style="display: block;">
    <a href="https://raidforums.com"><img src="https://cdn.raidforums.com/s/logo/Logo_default.png" alt="RaidForums" title="RaidForums" /></a>
    </div>
    <div class="logo__text" style="display: none;">
    <a href="https://raidforums.com"><span>RAID</span>FORUMS</a>
    </div>
    </div>
    </div>
    </header>
    <nav id="breadcrumb" class="wrapper rounded-top" style="">
    <ul class="breadcrumb__main nav talign-mleft">
    <li class="breadcrumb__bit"><a href="https://raidforums.com/index.php">RaidForums</a>
    <span class="breadcrumb__sep"><i class="fas fa-angle-right hidden-md"></i></span>
    </li>
    <li class="breadcrumb__bit"><a href="Forum-Leaks">Leaks</a>
    <span class="breadcrumb__sep"><i class="fas fa-angle-right hidden-md"></i></span>
    </li>
    <li class="breadcrumb__bit"><a href="Forum-Leaks-Market">Leaks Market</a>
    <i class="fas fa-caret-down fa-fw pagination_breadcrumb_link" id="breadcrumb_multipage"></i>
    <div id="breadcrumb_multipage_popup" class="pagination pagination_breadcrumb" style="display: none;">
    <a href="forum-216.html" class="pagination_current">1</a>
    <a href="forum-216-page-2.html" class="pagination_page">2</a>
    <a href="forum-216-page-3.html" class="pagination_page">3</a>
    <a href="forum-216-page-4.html" class="pagination_page">4</a>
    <a href="forum-216-page-5.html" class="pagination_page">5</a>
    &hellip; <a href="forum-216-page-147.html" class="pagination_last">147</a>
    <a href="forum-216-page-2.html" class="pagination_next">Next &raquo;</a>
    </div>
    <script type="text/javascript">
    // <!--
    	if(use_xmlhttprequest == "1")
    	{
    		$("#breadcrumb_multipage").popupMenu();
    	}
    // -->
    </script>
    </li>
    <span class="breadcrumb__sep"><i class="fas fa-angle-right hidden-md"></i></span>
    <li class="breadcrumb__active"><span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;LinkedIn 1Billion(1000Million) Record</li>
    </ul>
    <ul class="breadcrumb__fast-links nav talign-mright">
    <li class="hidden-lg">
    <a href="https://raidforums.com/misc.php?action=markread&my_post_key=b912526a0a0e2e398808b8fd7ddbfac7" class="rounded">
    Mark all as read
    </a>
    </li>
    <li>
    <a href="https://raidforums.com/search.php?action=getdaily" class="rounded">
    Today's posts
    </a>
    </li>
    </ul>
    </nav>
    <main id="content" class="wrapper rounded-bottom" style="">
    <fieldset class="advert"><legend>Temporary Advertisements:</legend><div><a href="https://raidforums.com/Thread-BUYING-Freshest-leak-need-to-include-Email-password" rel="nofollow" target="_blank"><img loading="lazy" src="https://cdn.raidforums.com/i/RF_gVeA.gif" width="600px" height="70px" alt="Buying Databases Advertisement" title="Buying Databases Advertisement"></a></div></fieldset><br>

    <section id="thread-info" class="rounded talign-mleft talign-mright">

    <div class="thread-info__thread-wrap">
    <div class="thread-info__thread">
    <span class="thread-info__name rounded"><span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;LinkedIn 1Billion(1000Million) Record</span>
    <div class="thread-info__datetime">by TomLiner - April 03, 2021 at 01:41 PM</div>
    </div>
    <div class="thread-info__new-reply">
    </div>
    </div>
    </section>
    <section id="thread-navigation" class="group">
    <div class="float-left">
    <div class="pagination talign-mleft">
    <span class="pages">Pages (3):</span>
    <span class="pagination_current">1</span>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=2" class="pagination_page">2</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=3" class="pagination_page">3</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=2" class="pagination_next">Next &raquo;</a>
    </div>
    </div>
    </section>
    <section id="show-thread">
    <table border="0" cellspacing="0" cellpadding="5" class="tborder tfixed clear">
    <tr>
    <td id="posts_container">
    <div id="posts">
    <a name="pid3649114" id="pid3649114"></a>
    <div class="post " style="" id="post_3649114">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-TomLiner"><span class="rf_i rf_god">TomLiner</span></a></div>
    <a href="User-TomLiner" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">GOD User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/s/ranks/god.png" alt="GOD Upgraded Member" title="GOD Upgraded Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">16</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">6</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Feb 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121989907"><strong class="reputation_positive">254</strong></a>
    </span>
    </div>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=1" title="GOD"><span class="rf_i rf_god rf_awardsi huge fitted link icon"></span></a><a href="https://raidforums.com/awards.php?view=20" title="Refer 100 people to RF."><img src="https://cdn.raidforums.com/s/shop/cancerino.png" alt="Refer 100 people to RF." /></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3649114#pid3649114" title="LinkedIn 1Billion(1000Million) Record">#1</a></strong>
    </div>
    <span class="post_date">April 03, 2021 at 01:41 PM <span class="post_edit" id="edited_by_3649114">
    <span class="edited_post">This post was last modified: <span title="April 07, 2021 at 09:53 PM">11 hours ago</span> by <a href="https://raidforums.com/User-TomLiner">TomLiner</a>. Edited 2 times in total.
    <em>Edit Reason: edit and add my ID</em>
    </span>
    </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3649114">
    I have 520Million +500Million Other Data<br />
    <br />
    My Telegram: @<a href="https://raidforums.com/User-TomLiner" class="mycode_mention" target="_blank"><span class="rf_i rf_god">TomLiner</span></a><br />
    <br />
    <br />
    1- 520Million data:<br />
    50 records as sample:<br />
    <div class="codeblock"><div class="body" dir="ltr"><code>{"Key":"IDaec32d2de20b3b87","FirstName":"Nur","LastName":"Slamet","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2015-12-15T13:03:43","HQCompanyName":"pt. dasaplast nusantara","Position":"tax","Level":"General","Department1":"Finance","DepartmentFunction":"Tax","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"tax","Level":"General","Department1":"Finance","FunctionalArea":"Tax","DecisionMaker":false,"End":"Present","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nur+Slamet+pt.+dasaplast+nusantara","SourceList":[]}<br />
    {"Key":"IDaec31c1df35c7515","FirstName":"Raden","LastName":"Prima","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:18","HQCompanyName":"PT Adaro Energy, Tbk","Position":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d9abb8bdbcb7f7a9abb0b4b899b8bdb8abb6f7bab6b4">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"XXdb5ff904529c27f8","Experience":[{"HQCompanyId":"XXdb5ff904529c27f8","Title":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"XXdb5ff904529c27f8","Updated":"2016-09-15T14:20:47.879374Z"},{"Title":"People Development Officer","DecisionMaker":false,"Start":"January 2013","End":"January 2014","Duration":"1 Year","Updated":"2016-09-15T14:20:49.269986Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Raden+Prima+PT+Adaro+Energy,+Tbk","SourceList":[]}<br />
    {"Key":"IDaec31367e617538f","FirstName":"Jimmi","LastName":"Huang","City":"Medang","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.357780","Longitude":"106.654720","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-19T19:57:39","HQCompanyName":"PT Aplaus Duta Kreasi","Position":"Web Development","Level":"General","Department1":"Technology","DepartmentFunction":"Web Development","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Web Development","Level":"General","Department1":"Technology","FunctionalArea":"Web Development","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","Updated":"2016-10-27T23:26:48.308924Z"},{"Title":"Brand Analyst","DecisionMaker":false,"Start":"January 2011","End":"December 2012","Duration":"1 Year 11 months","Updated":"2016-10-27T23:26:48.726943Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Jimmi+Huang+PT+Aplaus+Duta+Kreasi","SourceList":[]}<br />
    {"Key":"IDaec30d78223c1126","FirstName":"Yohanes","LastName":"Agung","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T19:57:59","HQCompanyName":"HANS PRODUCTION PHOTOGRAPHY","Position":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"End":"Present","Updated":"2016-10-27T18:38:36.599078Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yohanes+Agung+HANS+PRODUCTION+PHOTOGRAPHY","SourceList":[]}<br />
    {"Key":"IDaec30b62244d0e4d","FirstName":"Rindu","LastName":"Tarigan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"Indosat Ooredoo","Position":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="dba9b2b5bfaef5afbaa9b2bcbab59bb2b5bfb4a8baaff5b8b4b6">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.1957124+00:00","HQCompanyId":"ID962bc091e8a0f07c","Experience":[{"HQCompanyId":"ID962bc091e8a0f07c","Title":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"2003","End":"2015","SecondaryCompanyId":"ID962bc091e8a0f07c","Updated":"2016-09-16T16:57:26.30909Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Rindu+Tarigan+Indosat+Ooredoo","SourceList":[]}<br />
    {"Key":"IDaec2f04742efc165","FirstName":"Djie","LastName":"Merie","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"FM Group Indonesia","Position":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-17T01:26:14.95928Z"},{"Title":"Consultant","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-09-17T01:26:17.428004Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Djie+Merie+FM+Group+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec2d5768cae15c7","FirstName":"Sani","LastName":"Kurniawan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-18T21:58:49","HQCompanyName":"PT Pangansari Utama","Position":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"HQCompanyId":"XXc43ca4f532d93106","Experience":[{"HQCompanyId":"XXc43ca4f532d93106","Title":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","SecondaryCompanyId":"XXc43ca4f532d93106","Updated":"2016-10-27T15:30:30.332807Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sani+Kurniawan+PT+Pangansari+Utama","SourceList":[]}<br />
    {"Key":"IDaec2ad4ade70d967","FirstName":"Albert","LastName":"Prabowo","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:39","HQCompanyName":"Fashion Photographer","Position":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Experience":[{"Title":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","EmailAddress":"","Updated":null},{"HQCompanyId":"CN14282ad89ed4b365","Title":"Technical Team Leader VAS Engineer","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"November 2009","End":"January 2018","Duration":"8 Years 2 months","SecondaryCompanyId":"CN14282ad89ed4b365","Updated":"2016-10-27T12:54:51.181502Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Albert+Prabowo+Fashion+Photographer","SourceList":[]}<br />
    {"Key":"IDaec27ee0121967d7","FirstName":"Zami","LastName":"Zen","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"potrait","Position":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"Start":"October 2015","End":"Present","Duration":"11 months","Updated":"2016-12-07T04:10:48.705501Z"},{"Title":"Student","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T04:11:03.346252Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Zami+Zen+potrait","SourceList":[]}<br />
    {"Key":"IDaec278ea5aebe9a3","FirstName":"Agustinus","LastName":"Edo","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"PT. Sigma Metrasys Solution","Position":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"HQCompanyId":"ID3bc190ebfc539b69","Experience":[{"HQCompanyId":"ID3bc190ebfc539b69","Title":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"Start":"July 2013","End":"Present","Duration":"3 Years 2 months","SecondaryCompanyId":"ID3bc190ebfc539b69","Updated":"2016-12-07T09:22:25.825471Z"},{"HQCompanyId":"ID3bc190ebfc539b69","Title":"Internship Program","DecisionMaker":false,"Start":"June 2012","End":"November 2012","Duration":"5 months","Updated":"2016-12-07T09:22:30.387929Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Agustinus+Edo+PT.+Sigma+Metrasys+Solution","SourceList":[]}<br />
    {"Key":"IDaec1c2006dd22bfa","FirstName":"Anggie","LastName":"Buntoro","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-20T18:43:46","HQCompanyName":"PT.APL Logistics","Position":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 11 months","Updated":"2016-10-28T13:20:37.602039Z"},{"HQCompanyId":"SG781880de3052a221","Title":"warehouse analyst","DecisionMaker":false,"Start":"December 2009","End":"Present","Duration":"6 Years 6 months","Updated":"2016-10-28T13:20:38.081021Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggie+Buntoro+PT.APL+Logistics","SourceList":[]}<br />
    {"Key":"IDaec1b6fc0d739f26","FirstName":"Bambang","LastName":"Wahyu","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:58","HQCompanyName":"The Trans Luxury Hotel","Position":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Experience":[{"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Title":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"December 2011","End":"Present","Duration":"4 Years 9 months","SecondaryCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Updated":"2016-12-07T15:24:25.677779Z"},{"HQCompanyId":"154a343b-88ce-421e-b444-574474e9b3ea","Title":"Engineering Technician","DecisionMaker":false,"Start":"2003","End":"2010","Updated":"2016-12-07T15:24:25.912165Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Bambang+Wahyu+The+Trans+Luxury+Hotel","SourceList":[]}<br />
    {"Key":"IDaec18daced53216e","FirstName":"Gebreine Jessyca","LastName":"SE MM","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:46","HQCompanyName":"PT Kreasi Cemerlang Lestari, Gajah Tunggal Group (Fashion Retail Company)","Position":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"Start":"July 2014","End":"Present","Duration":"1 Year 10 months","Updated":"2016-09-14T06:01:28.168302Z"},{"HQCompanyId":"DE3b7431aab5afd0e9","Title":"Business, Brand, and Marketing Freelance Consultant","DecisionMaker":false,"Start":"July 2011","End":"May 2014","Duration":"2 Years 10 months","Updated":"2016-09-14T06:01:31.855765Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Gebreine+Jessyca+SE+MM+PT+Kreasi+Cemerlang+Lestari,+Gajah+Tunggal+Group+(Fashion+Retail+Company)","SourceList":[]}<br />
    {"Key":"IDaec1793cac70cd03","FirstName":"Yuliati","LastName":"Noeriman","City":"Jawa","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.914720","Longitude":"107.630830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:27:33","HQCompanyName":"Paxel","Position":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDf572612d5ca2b9f6","Title":"GM of Sales Training and Development","Level":"Director","Department1":"HR","Department2":"Sales","FunctionalArea":"training","DecisionMaker":true,"Start":"December 2011","End":"September 2017","Duration":"5 Years 9 months","SecondaryCompanyId":"IDf572612d5ca2b9f6","Updated":"2016-11-24T15:41:06.250065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yuliati+Noeriman+Paxel","SourceList":[]}<br />
    {"Key":"IDaec165e886db96a3","FirstName":"Leila","LastName":"Ruwaidah","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Phone":"","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2018-02-06T17:42:29","HQCompanyName":"PT. Sigma Cipta Caraka (Telkomsigma)","Position":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"IDdff5ea184ffc7c9f","Experience":[{"HQCompanyId":"IDdff5ea184ffc7c9f","Title":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"IDdff5ea184ffc7c9f","Updated":"2016-10-27T19:09:11.66686Z"},{"HQCompanyId":"ID9ad9575f43590343","Title":"Assessment Center Staff","DecisionMaker":false,"Start":"2002","End":"2007","Updated":"2016-10-27T19:09:12.510604Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Leila+Ruwaidah+PT.+Sigma+Cipta+Caraka+(Telkomsigma)","SourceList":[]}<br />
    {"Key":"IDaec15555d8f6d001","FirstName":"Dedy","LastName":"Prasetyono","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T09:46:34","HQCompanyName":"selular","Position":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"Start":"April 2005","End":"Present","Duration":"11 Years 1 month","Updated":"2016-09-15T15:21:43.891635Z"},{"Title":"pic sales telkom flexi","DecisionMaker":false,"Start":"March 2003","End":"June 2006","Duration":"3 Years 3 months","Updated":"2016-09-15T15:21:45.172879Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dedy+Prasetyono+selular","SourceList":[]}<br />
    {"Key":"IDaec134a6a5ed1dc2","FirstName":"Lenny","LastName":"Iod","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-25T18:21:18","HQCompanyName":"Pt. Indofood CBP Sukses Makmur Tbk.","Position":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"End":"Present","Updated":"2016-11-24T13:37:21.841804Z"},{"Title":"Regional Manager (Pacific and South America Region)","DecisionMaker":false,"Start":"January 2008","End":"Present","Duration":"8 Years 7 months","Updated":"2016-11-24T13:37:22.654297Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Lenny+Iod+Pt.+Indofood+CBP+Sukses+Makmur+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec11de108d114a9","FirstName":"Anis","LastName":"Soyyati","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:37","HQCompanyName":"detikcom","Position":"Social Media","Level":"General","Department1":"Marketing","DepartmentFunction":"Social","DecisionMaker":false,"HQCompanyId":"ID53f2a78f4a31b2b9","Experience":[{"HQCompanyId":"ID53f2a78f4a31b2b9","Title":"Social Media","Level":"General","Department1":"Marketing","FunctionalArea":"Social","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"ID53f2a78f4a31b2b9","Updated":"2016-09-16T13:32:38.638812Z"},{"HQCompanyId":"XX872fb88b1920a258","Title":"HRD GA","DecisionMaker":false,"Start":"October 2011","End":"April 2012","Duration":"6 months","Updated":"2016-09-16T13:32:39.357547Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anis+Soyyati+detikcom","SourceList":[]}<br />
    {"Key":"IDaec112db7df1e5a4","FirstName":"Mariesa","LastName":"Handayani","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:25:51","HQCompanyName":"PT.Pertamina (Persero)","Position":"-","Level":"General","Department1":"general","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ea878b98838f998bc4828b848e8b938b8483aa9a8f989e8b8783848bc4898587">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-03-03T06:23:11","HQCompanyId":"ID080fe301945f4f70","Experience":[{"HQCompanyId":"ID080fe301945f4f70","Title":"-","Level":"General","Department1":"general","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"ID080fe301945f4f70","Updated":"2016-09-13T23:50:33.161596Z"},{"HQCompanyId":"ID080fe301945f4f70","Title":"Assistant Economy &amp; Policy - Corporate Strategic Planning","DecisionMaker":false,"Start":"January 2011","End":"January 2012","Duration":"1 Year","Updated":"2016-09-13T23:50:35.72405Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Mariesa+Handayani+PT.Pertamina+(Persero)","SourceList":[]}<br />
    {"Key":"IDaec0e16edee655ef","FirstName":"Sanda","LastName":"Redman","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:48","HQCompanyName":"International Organization for Migration (IOM)","Position":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"CH0605c865fa324d07","Experience":[{"HQCompanyId":"CH0605c865fa324d07","Title":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"Start":"June 2006","End":"June 2011","Duration":"5 Years","SecondaryCompanyId":"CH0605c865fa324d07","Updated":"2016-10-27T18:56:50.117866Z"},{"Title":"Graphic Designer","DecisionMaker":false,"Start":"November 2004","End":"May 2006","Duration":"1 Year 6 months","Updated":"2016-10-27T18:56:50.289713Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sanda+Redman+International+Organization+for+Migration+(IOM)","SourceList":[]}<br />
    {"Key":"IDaec0b6a25116fccb","FirstName":"Falah","LastName":"Azmi","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T09:46:36","HQCompanyName":"PT Kencana Trans Wisata","Position":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":null},{"Title":"Manager","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":"2016-09-15T13:59:28.021962Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Falah+Azmi+PT+Kencana+Trans+Wisata","SourceList":[]}<br />
    {"Key":"IDaec0aa2b82ab5ed6","FirstName":"Ritter","LastName":"Dante","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-05-31T03:24:36","HQCompanyName":"Teleplan International","Position":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2d5f445959485f03494c4359486d594841485d414c43034e4240">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-02-16T15:06:00","HQCompanyId":"NL002000c570268aec","Experience":[{"HQCompanyId":"NL002000c570268aec","Title":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"March 2014","End":"Present","Duration":"2 Years 2 months","SecondaryCompanyId":"NL002000c570268aec","Updated":"2016-09-14T23:38:46.545336Z"},{"HQCompanyId":"MY0fd181d432ffe31f","Title":"ICT Administrator - Network","DecisionMaker":false,"Start":"April 2012","End":"February 2014","Duration":"1 Year 10 months","Updated":"2016-09-14T23:38:47.717177Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ritter+Dante+Teleplan+International","SourceList":[]}<br />
    {"Key":"IDaec0a2cf3196ac38","FirstName":"Faheem","LastName":"Khan","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:46","HQCompanyName":"PT Ascenta Group","Position":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T10:23:17.136269Z"},{"Title":"Business Development","DecisionMaker":false,"Start":"January 2015","End":"September 2017","Duration":"2 Years 8 months","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Faheem+Khan+PT+Ascenta+Group","SourceList":[]}<br />
    {"Key":"IDaec09acfd6feb5c8","FirstName":"Prasasti","LastName":"Dinar","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T02:32:05","HQCompanyName":"PT HM Sampoerna Tbk.","Position":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"IDe55fa88903bd39c6","Experience":[{"HQCompanyId":"IDe55fa88903bd39c6","Title":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"Start":"August 2008","End":"Present","Duration":"8 Years","SecondaryCompanyId":"IDe55fa88903bd39c6","Updated":"2016-11-24T20:49:25.674919Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Prasasti+Dinar+PT+HM+Sampoerna+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec09a0e25208c10","FirstName":"Merryntan","LastName":"Delima","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-20T14:30:13","HQCompanyName":"PT Forisa Nusapersada","Position":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"XXa1b6a80cecb3cb5e","Experience":[{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"XXa1b6a80cecb3cb5e","Updated":null},{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","DecisionMaker":false,"Start":"November 2007","End":"November 2012","Duration":"5 Years","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Merryntan+Delima+PT+Forisa+Nusapersada","SourceList":[]}<br />
    {"Key":"IDaec080f3c1a06167","FirstName":"Made","LastName":"Ari Puspita Sari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:16","HQCompanyName":"Sale Stock","Position":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"XX62ed1a82872fc897","Experience":[{"HQCompanyId":"XX62ed1a82872fc897","Title":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"July 2015","End":"Present","Duration":"11 months","SecondaryCompanyId":"XX62ed1a82872fc897","Updated":"2016-09-16T19:39:59.253217Z"},{"HQCompanyId":"AU779e74ff0dbd83c8","Title":"Test Lead","DecisionMaker":false,"Start":"January 2015","End":"June 2015","Duration":"5 months","Updated":"2016-09-16T19:40:00.206327Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Made+Ari+Puspita+Sari+Sale+Stock","SourceList":[]}<br />
    {"Key":"IDaec069c3d4427717","FirstName":"Isidorus","LastName":"Ariyanto","City":"Yogyakarta","RegionCode":"10","RegionName":"Yogyakarta","Country":"Indonesia","Latitude":"-7.782780","Longitude":"110.360830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-01T16:27:07","HQCompanyName":"Maesindo Indonesia, Ltd","Position":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"End":"Present","Updated":"2016-06-26T18:22:59.667065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Isidorus+Ariyanto+Maesindo+Indonesia,+Ltd","SourceList":[]}<br />
    {"Key":"IDaec0671dd16ec00f","FirstName":"Dewi","LastName":"Sugiharti","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"PT.A.J.Manulife Indonesia","Position":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"Start":"2005","End":"Present","Updated":"2016-09-16T12:28:20.269948Z"},{"Title":"accounting","DecisionMaker":false,"Start":"2000","End":"2000","Updated":"2016-09-16T12:28:20.535554Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dewi+Sugiharti+PT.A.J.Manulife+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec04504c00835bf","FirstName":"Ampu","LastName":"Resmanto","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:26:59","HQCompanyName":"PT Reckitt Benckiser Indonesia","Position":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDe6499abd1663cb98","Title":"TPM Manager at TA-Brewery","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2014","End":"September 2017","Duration":"3 Years","SecondaryCompanyId":"IDe6499abd1663cb98","Updated":"2016-10-28T06:59:00.924465Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ampu+Resmanto+PT+Reckitt+Benckiser+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec03a0815453494","FirstName":"Nadya","LastName":"Lupita","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT Antam Tbk","Position":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="610f000518004f0d141108150021000f15000c4f020e0c">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2017-04-05T13:55:56","HQCompanyId":"ID321b32dec7d18c8b","Experience":[{"HQCompanyId":"ID321b32dec7d18c8b","Title":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"January 2015","End":"Present","Duration":"1 Year 4 months","SecondaryCompanyId":"ID321b32dec7d18c8b","Updated":"2016-09-13T23:48:42.319372Z"},{"HQCompanyId":"ID9a11f8867bff4c72","Title":"Secretary of CEO","DecisionMaker":false,"Start":"August 2014","End":"December 2014","Duration":"4 months","Updated":"2016-09-13T23:48:43.053732Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nadya+Lupita+PT+Antam+Tbk","SourceList":[]}<br />
    {"Key":"IDaec0343c7485dba1","FirstName":"Surya","LastName":"Febianto","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-21T16:40:57","HQCompanyName":"PT. Agung Sedayu Group","Position":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID08710b895fe19eb7","Experience":[{"HQCompanyId":"ID08710b895fe19eb7","Title":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"2010","End":"Present","SecondaryCompanyId":"ID08710b895fe19eb7","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Surya+Febianto+PT.+Agung+Sedayu+Group","SourceList":[]}<br />
    {"Key":"IDaec02d845f729852","FirstName":"Arianto Teddy","LastName":"Wibowo","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T00:22:41","HQCompanyName":"Mango Terrace Restaurant","Position":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"Start":"September 2014","End":"Present","Duration":"1 Year 11 months","Updated":"2016-11-24T13:34:59.693143Z"},{"Title":"tidak bekerja","DecisionMaker":false,"Start":"January 2014","End":"September 2014","Duration":"8 months","Updated":"2016-11-24T13:35:00.230168Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Arianto+Teddy+Wibowo+Mango+Terrace+Restaurant","SourceList":[]}<br />
    {"Key":"IDaec0234a72a88b32","FirstName":"Iin Azairin","LastName":"Aziz","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-09-14T11:37:43","HQCompanyName":"PT Bakrie Metal Industries","Position":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T00:53:30.894808Z"},{"Title":"Assisstant to CEO - Business Process Development","DecisionMaker":false,"Start":"August 2014","End":"Present","Duration":"2 Years 1 month","Updated":"2016-12-07T00:53:38.848008Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Iin+Azairin+Aziz+PT+Bakrie+Metal+Industries","SourceList":[]}<br />
    {"Key":"IDaec00c9d182a1877","FirstName":"Kiagus","LastName":"Firmansyah","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-25T17:15:48","HQCompanyName":"PT. Trans Retail Indonesia","Position":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","DepartmentFunction":"creative","DecisionMaker":false,"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Experience":[{"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Title":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","FunctionalArea":"creative","DecisionMaker":false,"Start":"February 2010","End":"Present","Duration":"6 Years 6 months","SecondaryCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Updated":"2016-11-24T09:46:10.797726Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Kiagus+Firmansyah+PT.+Trans+Retail+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec0034a7587853d","FirstName":"Houtman","LastName":"Simanjuntak","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-19T03:39:55","HQCompanyName":"Virtus and Varda as newly established company offering environmental solutions to the industries.","Position":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Experience":[{"Title":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T15:11:54.946605Z"},{"HQCompanyId":"ID325cb8f3d7bd7ef8","Title":"President Director &amp; CEO","DecisionMaker":false,"Start":"January 1997","End":"March 2015","Duration":"18 Years 2 months","Updated":"2016-09-15T15:12:00.243412Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Houtman+Simanjuntak+Virtus+and+Varda+as+newly+established+company+offering+environmental+solutions+to+the+industries.","SourceList":[]}<br />
    {"Key":"IDaec003092517f6af","FirstName":"Nena","LastName":"Ermila","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT. Asuransi Jasa Indonesia","Position":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID8ec56f05a752fc4b","Experience":[{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2016","End":"Present","Duration":"4 months","SecondaryCompanyId":"ID8ec56f05a752fc4b","Updated":"2016-09-15T04:07:01.514989Z"},{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Sub Division Head","DecisionMaker":false,"Start":"October 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-09-15T04:07:02.811851Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nena+Ermila+PT.+Asuransi+Jasa+Indonesia","SourceList":[]}<br />
    {"Key":"IDaebff7f35e83819d","FirstName":"Didik","LastName":"Wibawanto","City":"Bandar Lampung","RegionCode":"15","RegionName":"Lampung","Country":"Indonesia","Latitude":"-5.425440","Longitude":"105.258030","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-26T20:10:55","HQCompanyName":"Private Corporation","Position":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Experience":[{"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Title":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"5 months","SecondaryCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Updated":"2016-11-24T17:01:02Z"},{"Title":"Chief Information Officer","DecisionMaker":false,"Start":"September 2015","End":"Present","Duration":"11 months","Updated":"2016-11-24T17:01:02.814897Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Didik+Wibawanto+Private+Corporation","SourceList":[]}<br />
    {"Key":"IDaebff37ce8ef65d7","FirstName":"Elin-Psg","LastName":"Herliana","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T03:24:35","HQCompanyName":"Olympus Property","Position":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3a5f565354174a495d14525f4856535b545b7a555643574a4f494a48554a5f484e4314595557">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3833261+00:00","HQCompanyId":"US21d063d73525fb16","Experience":[{"HQCompanyId":"US21d063d73525fb16","Title":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 10 months","SecondaryCompanyId":"abc284e2-5a4a-43d4-8468-1cee07fe4fb5","Updated":"2016-09-15T03:14:55.432942Z"},{"HQCompanyId":"ID47b7a4355d2abb19","Title":"Koodinator Kantor Kas","DecisionMaker":false,"Start":"1999","End":"2007","Updated":"2016-09-15T03:14:56.636055Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Elin-Psg+Herliana+Olympus+Property","SourceList":[]}<br />
    {"Key":"IDaebfef534eac0d49","FirstName":"Yulnia","LastName":"Azriani","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T21:10:41","HQCompanyName":"PT Putra Taro Paloma (subsidiary of PT Tiga Pilar Sejahtera)","Position":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"Start":"November 2012","End":"April 2015","Duration":"2 Years 5 months","Updated":"2016-09-15T18:39:52.681431Z"},{"Title":"Marketing Supervisor for RoC","DecisionMaker":false,"Start":"February 2010","End":"August 2011","Duration":"1 Year 6 months","Updated":"2016-09-15T18:39:54.71263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yulnia+Azriani+PT+Putra+Taro+Paloma+(subsidiary+of+PT+Tiga+Pilar+Sejahtera)","SourceList":[]}<br />
    {"Key":"IDaebfd4becc131607","FirstName":"MizanStore","LastName":".Com","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-16T21:08:41","HQCompanyName":"PT Mizan Digital Publishing","Position":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"June 2013","End":"Present","Duration":"3 Years","Updated":"2016-10-27T05:59:56.131533Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=MizanStore+.Com+PT+Mizan+Digital+Publishing","SourceList":[]}<br />
    {"Key":"IDaebfb9cd79b65f90","FirstName":"Riadi","LastName":"Wirawan","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T21:10:34","HQCompanyName":"MMC Hospital","Position":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"End":"Present","Updated":"2016-09-15T23:51:32.140538Z"},{"Title":"Dr","DecisionMaker":false,"Start":"January 1990","End":"Present","Duration":"26 Years 4 months","Updated":"2016-09-15T23:51:32.140538Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Riadi+Wirawan+MMC+Hospital","SourceList":[]}<br />
    {"Key":"IDaebf803066abb18a","FirstName":"Anna","LastName":"Myr","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:30","HQCompanyName":"Smart Advert","Position":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-10-27T19:07:16.619651Z"},{"Title":"Administration Staff","DecisionMaker":false,"Start":"November 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-10-27T19:07:25.260324Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anna+Myr+Smart+Advert","SourceList":[]}<br />
    {"Key":"IDaebf7fa59c3f2c61","FirstName":"Herman","LastName":"Tea","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-08-26T20:11:14","HQCompanyName":"smpn 1 gununghalu","Position":"staf","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"staf","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2004","End":"Present","Duration":"12 Years 7 months","Updated":"2016-11-25T02:05:46.310689Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Herman+Tea+smpn+1+gununghalu","SourceList":[]}<br />
    {"Key":"IDaebf6eeabefb13b1","FirstName":"Anggun","LastName":"Triadi","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T03:24:38","HQCompanyName":"Dwisapta Advertising","Position":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"February 2011","End":"Present","Duration":"5 Years 3 months","Updated":"2016-09-15T02:10:36.579721Z"},{"HQCompanyId":"IDda4ac54b00ab8257","Title":"Account Director","DecisionMaker":false,"Start":"January 2009","End":"January 2011","Duration":"2 Years","Updated":"2016-09-15T02:10:39.970247Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggun+Triadi+Dwisapta+Advertising","SourceList":[]}<br />
    {"Key":"IDaebf4c097ed370c9","FirstName":"Hans","LastName":"Ferdinan","City":"Makassar","RegionCode":"38","RegionName":"South Sulawesi","Country":"Indonesia","Latitude":"-5.140000","Longitude":"119.422100","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-19T19:57:40","HQCompanyName":"PT Bank Nationalnobu Tbk","Position":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"April 2014","End":"Present","Duration":"2 Years 2 months","Updated":"2016-10-27T18:52:30.413971Z"},{"HQCompanyId":"ID67b4599c6320e3f7","Title":"Marketing Manager","DecisionMaker":false,"Start":"April 2012","End":"April 2014","Duration":"2 Years","Updated":"2016-10-27T18:52:30.913991Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Hans+Ferdinan+PT+Bank+Nationalnobu+Tbk","SourceList":[]}<br />
    {"Key":"IDaebf415f88033514","FirstName":"Yessie Afriana","LastName":"Wulandari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"PT PEMBANGUNAN PERUMAHAN (PERSERO)","Position":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-16T10:38:42.422819Z"},{"Title":"Civil Engineer","DecisionMaker":false,"Start":"May 2013","End":"January 2014","Duration":"8 months","Updated":"2016-09-16T10:38:46.110263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yessie+Afriana+Wulandari+PT+PEMBANGUNAN+PERUMAHAN+(PERSERO)","SourceList":[]}<br />
    {"Key":"IDaebf1453d77ae08c","FirstName":"Debby Niken","LastName":"Kartika W","City":"Surabaya","RegionCode":"08","RegionName":"East Java","Country":"Indonesia","Latitude":"-7.249170","Longitude":"112.750830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-02T14:44:18","HQCompanyName":"Cv. BM Surabaya","Position":"IA","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"IA","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"3 months","Updated":"2016-09-16T13:11:39.999845Z"},{"Title":"Senior Staf","DecisionMaker":false,"Start":"September 2015","End":"January 2016","Duration":"4 months","Updated":"2016-09-16T13:11:43.99979Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Debby+Niken+Kartika+W+Cv.+BM+Surabaya","SourceList":[]}<br />
    {"Key":"IDaebf000ee0827443","FirstName":"Vebi","LastName":"Nadhira","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:29","HQCompanyName":"Institut Teknologi Bandung","Position":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"HQCompanyId":"IDc5a1b238422cffa9","Experience":[{"HQCompanyId":"IDc5a1b238422cffa9","Title":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"IDc5a1b238422cffa9","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Vebi+Nadhira+Institut+Teknologi+Bandung","SourceList":[]}<br />
    {"Key":"IDaebed0315a11669b","FirstName":"Ratu","LastName":"Wijaksana","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:26","HQCompanyName":"Smilebuilderz LLC","Position":"dentist, health team","Level":"General","Department1":"Medical","DepartmentFunction":"Dentist","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c1b3a0b5b4b681b2aca8ada4a3b4a8ada5a4b3bbefa2aeac">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"US08bccec1e3cec938","Experience":[{"HQCompanyId":"US08bccec1e3cec938","Title":"dentist, health team","Level":"General","Department1":"Medical","FunctionalArea":"Dentist","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"US08bccec1e3cec938","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ratu+Wijaksana+Smilebuilderz+LLC","SourceList":[]}<br />
    {"Key":"IDaebeca27f944b5ff","FirstName":"Budi","LastName":"Telly","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-01T21:27:04","HQCompanyName":"PT. Tirtakencana Tatawarna","Position":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"ID5d4a1a67c8710963","Experience":[{"HQCompanyId":"ID5d4a1a67c8710963","Title":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"ID5d4a1a67c8710963","Updated":"2016-09-16T21:17:15.12617Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Budi+Telly+PT.+Tirtakencana+Tatawarna","SourceList":[]}</code></div></div><br />
    1 Million records<br />
    <div class="hidden-content rounded">
    <div class="hidden-content__title">
    <span class="hidden-content__custom-title">1Million records</span>
    <span class="hidden-content__default-title">Hidden Content</span>
    </div>
    <div class="hidden-content__main">You must <a href="member.php?action=register">register</a> or <a href="member.php?action=login">login</a> to view this content. </div>
    </div>
    <br />
    <br />
    <br />
    2- Other 500Million Data<br />
    <br />
    <div class="codeblock"><div class="body" dir="ltr"><code>100M-LINKEDIN.zip<br />
    35M LINKEDIN CONTACT (WITH COMPANY) B2B.zip<br />
    2.5M US B2B Linkedin.zip<br />
    25M-Linkedin.zip<br />
    Australia Linkedin 194K.zip<br />
    Linkedin - 250 758 057.zip<br />
    Linkedin 34 Million Linkedin Emails.zip<br />
    linkedin 37 million db-16M.zip<br />
    Linkedin 45k With Full Details.zip<br />
    linkedin db 35M.zip<br />
    Linkedin DB with Profile URLS 21M.zip<br />
    Linkedin Dehased 1GB.zip<br />
    Linkedin Pakistan.zip<br />
    Linkedin sorted by Titles.zip<br />
    Linkedin-Company-Education_FR.zip<br />
    LinkedIn.rar<br />
    Linkedin2.zip<br />
    LinkedInMain 16M.zip</code></div></div><img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" alt="[Image: dqJxEFX.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" data-image-modal-original="https://i.imgur.com/dqJxEFX.png" data-image-modal-safe="1" /><br />
    <br />
    <br />
    <br />
    for more detail PM me on telegram: @<a href="https://raidforums.com/User-TomLiner" class="mycode_mention" target="_blank"><span class="rf_i rf_god">TomLiner</span></a>
    </div>
    <div class="post_meta" id="post_meta_3649114">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3649114" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3649352" id="pid3649352"></a>
    <div class="post " style="" id="post_3649352">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-yahya934"><span class="rf_i rf_vip">yahya934</span></a></div>
    <a href="User-yahya934" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">V.I.P User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_795A9.png" alt="VIP Upgraded Member" title="VIP Upgraded Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">26</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Dec 2020</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121950077"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=3" title="VIP"><span class="rf_i rf_vip rf_awardsi huge fitted link icon"></span></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3649352#pid3649352" title="RE: LinkedIn 1Billion(1000Million) Record">#2</a></strong>
    </div>
    <span class="post_date">April 03, 2021 at 02:51 PM <span class="post_edit" id="edited_by_3649352"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3649352">
    good gooooooooooooood
    </div>
    <div class="post_meta" id="post_meta_3649352">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3649352" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3649749" id="pid3649749"></a>
    <div class="post " style="" id="post_3649749">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-warri0r23"><span class="rf_member">warri0r23</span></a></div>
    <a href="User-warri0r23" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/uploads/avatars/avatar_121802418.png?dateline=1609229371" alt="" width="130" height="130" /></a>
    </div>
    <div class="post__user-title">Advanced User
    <span class="post__buddy-status"><a href="online.php" title="Online" class="post__status post__status--online"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge"></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">64</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Mar 2020</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121802418"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <span class="user_service" data-years="1">1 Year of service</span>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3649749#pid3649749" title="RE: LinkedIn 1Billion(1000Million) Record">#3</a></strong>
    </div>
    <span class="post_date">April 03, 2021 at 04:57 PM <span class="post_edit" id="edited_by_3649749"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3649749">
    Thank you for sharing it... how is this data is????<br />
    As LinkedIn got data breach in 2016...
    </div>
    <div class="post_meta" id="post_meta_3649749">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3649749" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3651199" id="pid3651199"></a>
    <div class="post " style="" id="post_3651199">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-zorar"><span class="rf_i rf_vip">zorar</span></a></div>
    <a href="User-zorar" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar1-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">V.I.P User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_795A9.png" alt="VIP Upgraded Member" title="VIP Upgraded Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">1</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=122032777"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=3" title="VIP"><span class="rf_i rf_vip rf_awardsi huge fitted link icon"></span></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3651199#pid3651199" title="RE: LinkedIn 1Billion(1000Million) Record">#4</a></strong>
    </div>
    <span class="post_date">April 03, 2021 at 09:14 PM <span class="post_edit" id="edited_by_3651199"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3651199">
    left you a rep, may share the fb and LinkedIn link?
    </div>
    <div class="post_meta" id="post_meta_3651199">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3651199" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3652198" id="pid3652198"></a>
    <div class="post " style="" id="post_3652198">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-KRYBT0N"><span class="rf_noob">KRYBT0N</span></a></div>
    <a href="User-KRYBT0N" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">New User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_yfVa.png" alt="Member" title="Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">4</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=122034360"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3652198#pid3652198" title="RE: LinkedIn 1Billion(1000Million) Record">#5</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 12:51 AM <span class="post_edit" id="edited_by_3652198"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3652198">
    <blockquote class="mycode_quote"><cite><span> (April 03, 2021 at 01:41 PM)</span>TomLiner Wrote: <a rel="nofollow" href="misc.php?action=safelinks&url=https%3A%2F%2Fraidforums.com%2FThread-SELLING-LinkedIn-1Billion-1000Million-Record%3Fpid%3D3649114%23pid3649114" class="quick_jump"><i class="fas fa-long-arrow-alt-right"></i></a></cite>I have 520Million +500Million Other Data<br />
    <br />
    <br />
    1- 520Million data:<br />
    50 records as sample:<br />
    <div class="codeblock"><div class="body" dir="ltr"><code>{"Key":"IDaec32d2de20b3b87","FirstName":"Nur","LastName":"Slamet","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2015-12-15T13:03:43","HQCompanyName":"pt. dasaplast nusantara","Position":"tax","Level":"General","Department1":"Finance","DepartmentFunction":"Tax","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"tax","Level":"General","Department1":"Finance","FunctionalArea":"Tax","DecisionMaker":false,"End":"Present","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nur+Slamet+pt.+dasaplast+nusantara","SourceList":[]}<br />
    {"Key":"IDaec31c1df35c7515","FirstName":"Raden","LastName":"Prima","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:18","HQCompanyName":"PT Adaro Energy, Tbk","Position":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a4d6c5c0c1ca8ad4d6cdc9c5e4c5c0c5d6cb8ac7cbc9">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"XXdb5ff904529c27f8","Experience":[{"HQCompanyId":"XXdb5ff904529c27f8","Title":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"XXdb5ff904529c27f8","Updated":"2016-09-15T14:20:47.879374Z"},{"Title":"People Development Officer","DecisionMaker":false,"Start":"January 2013","End":"January 2014","Duration":"1 Year","Updated":"2016-09-15T14:20:49.269986Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Raden+Prima+PT+Adaro+Energy,+Tbk","SourceList":[]}<br />
    {"Key":"IDaec31367e617538f","FirstName":"Jimmi","LastName":"Huang","City":"Medang","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.357780","Longitude":"106.654720","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-19T19:57:39","HQCompanyName":"PT Aplaus Duta Kreasi","Position":"Web Development","Level":"General","Department1":"Technology","DepartmentFunction":"Web Development","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Web Development","Level":"General","Department1":"Technology","FunctionalArea":"Web Development","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","Updated":"2016-10-27T23:26:48.308924Z"},{"Title":"Brand Analyst","DecisionMaker":false,"Start":"January 2011","End":"December 2012","Duration":"1 Year 11 months","Updated":"2016-10-27T23:26:48.726943Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Jimmi+Huang+PT+Aplaus+Duta+Kreasi","SourceList":[]}<br />
    {"Key":"IDaec30d78223c1126","FirstName":"Yohanes","LastName":"Agung","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T19:57:59","HQCompanyName":"HANS PRODUCTION PHOTOGRAPHY","Position":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"End":"Present","Updated":"2016-10-27T18:38:36.599078Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yohanes+Agung+HANS+PRODUCTION+PHOTOGRAPHY","SourceList":[]}<br />
    {"Key":"IDaec30b62244d0e4d","FirstName":"Rindu","LastName":"Tarigan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"Indosat Ooredoo","Position":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2b5942454f5e055f4a59424c4a456b42454f44584a5f05484446">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.1957124+00:00","HQCompanyId":"ID962bc091e8a0f07c","Experience":[{"HQCompanyId":"ID962bc091e8a0f07c","Title":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"2003","End":"2015","SecondaryCompanyId":"ID962bc091e8a0f07c","Updated":"2016-09-16T16:57:26.30909Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Rindu+Tarigan+Indosat+Ooredoo","SourceList":[]}<br />
    {"Key":"IDaec2f04742efc165","FirstName":"Djie","LastName":"Merie","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"FM Group Indonesia","Position":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-17T01:26:14.95928Z"},{"Title":"Consultant","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-09-17T01:26:17.428004Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Djie+Merie+FM+Group+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec2d5768cae15c7","FirstName":"Sani","LastName":"Kurniawan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-18T21:58:49","HQCompanyName":"PT Pangansari Utama","Position":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"HQCompanyId":"XXc43ca4f532d93106","Experience":[{"HQCompanyId":"XXc43ca4f532d93106","Title":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","SecondaryCompanyId":"XXc43ca4f532d93106","Updated":"2016-10-27T15:30:30.332807Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sani+Kurniawan+PT+Pangansari+Utama","SourceList":[]}<br />
    {"Key":"IDaec2ad4ade70d967","FirstName":"Albert","LastName":"Prabowo","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:39","HQCompanyName":"Fashion Photographer","Position":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Experience":[{"Title":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","EmailAddress":"","Updated":null},{"HQCompanyId":"CN14282ad89ed4b365","Title":"Technical Team Leader VAS Engineer","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"November 2009","End":"January 2018","Duration":"8 Years 2 months","SecondaryCompanyId":"CN14282ad89ed4b365","Updated":"2016-10-27T12:54:51.181502Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Albert+Prabowo+Fashion+Photographer","SourceList":[]}<br />
    {"Key":"IDaec27ee0121967d7","FirstName":"Zami","LastName":"Zen","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"potrait","Position":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"Start":"October 2015","End":"Present","Duration":"11 months","Updated":"2016-12-07T04:10:48.705501Z"},{"Title":"Student","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T04:11:03.346252Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Zami+Zen+potrait","SourceList":[]}<br />
    {"Key":"IDaec278ea5aebe9a3","FirstName":"Agustinus","LastName":"Edo","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"PT. Sigma Metrasys Solution","Position":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"HQCompanyId":"ID3bc190ebfc539b69","Experience":[{"HQCompanyId":"ID3bc190ebfc539b69","Title":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"Start":"July 2013","End":"Present","Duration":"3 Years 2 months","SecondaryCompanyId":"ID3bc190ebfc539b69","Updated":"2016-12-07T09:22:25.825471Z"},{"HQCompanyId":"ID3bc190ebfc539b69","Title":"Internship Program","DecisionMaker":false,"Start":"June 2012","End":"November 2012","Duration":"5 months","Updated":"2016-12-07T09:22:30.387929Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Agustinus+Edo+PT.+Sigma+Metrasys+Solution","SourceList":[]}<br />
    {"Key":"IDaec1c2006dd22bfa","FirstName":"Anggie","LastName":"Buntoro","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-20T18:43:46","HQCompanyName":"PT.APL Logistics","Position":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 11 months","Updated":"2016-10-28T13:20:37.602039Z"},{"HQCompanyId":"SG781880de3052a221","Title":"warehouse analyst","DecisionMaker":false,"Start":"December 2009","End":"Present","Duration":"6 Years 6 months","Updated":"2016-10-28T13:20:38.081021Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggie+Buntoro+PT.APL+Logistics","SourceList":[]}<br />
    {"Key":"IDaec1b6fc0d739f26","FirstName":"Bambang","LastName":"Wahyu","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:58","HQCompanyName":"The Trans Luxury Hotel","Position":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Experience":[{"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Title":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"December 2011","End":"Present","Duration":"4 Years 9 months","SecondaryCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Updated":"2016-12-07T15:24:25.677779Z"},{"HQCompanyId":"154a343b-88ce-421e-b444-574474e9b3ea","Title":"Engineering Technician","DecisionMaker":false,"Start":"2003","End":"2010","Updated":"2016-12-07T15:24:25.912165Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Bambang+Wahyu+The+Trans+Luxury+Hotel","SourceList":[]}<br />
    {"Key":"IDaec18daced53216e","FirstName":"Gebreine Jessyca","LastName":"SE MM","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:46","HQCompanyName":"PT Kreasi Cemerlang Lestari, Gajah Tunggal Group (Fashion Retail Company)","Position":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"Start":"July 2014","End":"Present","Duration":"1 Year 10 months","Updated":"2016-09-14T06:01:28.168302Z"},{"HQCompanyId":"DE3b7431aab5afd0e9","Title":"Business, Brand, and Marketing Freelance Consultant","DecisionMaker":false,"Start":"July 2011","End":"May 2014","Duration":"2 Years 10 months","Updated":"2016-09-14T06:01:31.855765Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Gebreine+Jessyca+SE+MM+PT+Kreasi+Cemerlang+Lestari,+Gajah+Tunggal+Group+(Fashion+Retail+Company)","SourceList":[]}<br />
    {"Key":"IDaec1793cac70cd03","FirstName":"Yuliati","LastName":"Noeriman","City":"Jawa","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.914720","Longitude":"107.630830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:27:33","HQCompanyName":"Paxel","Position":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDf572612d5ca2b9f6","Title":"GM of Sales Training and Development","Level":"Director","Department1":"HR","Department2":"Sales","FunctionalArea":"training","DecisionMaker":true,"Start":"December 2011","End":"September 2017","Duration":"5 Years 9 months","SecondaryCompanyId":"IDf572612d5ca2b9f6","Updated":"2016-11-24T15:41:06.250065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yuliati+Noeriman+Paxel","SourceList":[]}<br />
    {"Key":"IDaec165e886db96a3","FirstName":"Leila","LastName":"Ruwaidah","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Phone":"","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2018-02-06T17:42:29","HQCompanyName":"PT. Sigma Cipta Caraka (Telkomsigma)","Position":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"IDdff5ea184ffc7c9f","Experience":[{"HQCompanyId":"IDdff5ea184ffc7c9f","Title":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"IDdff5ea184ffc7c9f","Updated":"2016-10-27T19:09:11.66686Z"},{"HQCompanyId":"ID9ad9575f43590343","Title":"Assessment Center Staff","DecisionMaker":false,"Start":"2002","End":"2007","Updated":"2016-10-27T19:09:12.510604Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Leila+Ruwaidah+PT.+Sigma+Cipta+Caraka+(Telkomsigma)","SourceList":[]}<br />
    {"Key":"IDaec15555d8f6d001","FirstName":"Dedy","LastName":"Prasetyono","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T09:46:34","HQCompanyName":"selular","Position":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"Start":"April 2005","End":"Present","Duration":"11 Years 1 month","Updated":"2016-09-15T15:21:43.891635Z"},{"Title":"pic sales telkom flexi","DecisionMaker":false,"Start":"March 2003","End":"June 2006","Duration":"3 Years 3 months","Updated":"2016-09-15T15:21:45.172879Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dedy+Prasetyono+selular","SourceList":[]}<br />
    {"Key":"IDaec134a6a5ed1dc2","FirstName":"Lenny","LastName":"Iod","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-25T18:21:18","HQCompanyName":"Pt. Indofood CBP Sukses Makmur Tbk.","Position":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"End":"Present","Updated":"2016-11-24T13:37:21.841804Z"},{"Title":"Regional Manager (Pacific and South America Region)","DecisionMaker":false,"Start":"January 2008","End":"Present","Duration":"8 Years 7 months","Updated":"2016-11-24T13:37:22.654297Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Lenny+Iod+Pt.+Indofood+CBP+Sukses+Makmur+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec11de108d114a9","FirstName":"Anis","LastName":"Soyyati","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:37","HQCompanyName":"detikcom","Position":"Social Media","Level":"General","Department1":"Marketing","DepartmentFunction":"Social","DecisionMaker":false,"HQCompanyId":"ID53f2a78f4a31b2b9","Experience":[{"HQCompanyId":"ID53f2a78f4a31b2b9","Title":"Social Media","Level":"General","Department1":"Marketing","FunctionalArea":"Social","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"ID53f2a78f4a31b2b9","Updated":"2016-09-16T13:32:38.638812Z"},{"HQCompanyId":"XX872fb88b1920a258","Title":"HRD GA","DecisionMaker":false,"Start":"October 2011","End":"April 2012","Duration":"6 months","Updated":"2016-09-16T13:32:39.357547Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anis+Soyyati+detikcom","SourceList":[]}<br />
    {"Key":"IDaec112db7df1e5a4","FirstName":"Mariesa","LastName":"Handayani","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:25:51","HQCompanyName":"PT.Pertamina (Persero)","Position":"-","Level":"General","Department1":"general","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fe939f8c979b8d9fd0969f909a9f879f9097be8e9b8c8a9f9397909fd09d9193">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-03-03T06:23:11","HQCompanyId":"ID080fe301945f4f70","Experience":[{"HQCompanyId":"ID080fe301945f4f70","Title":"-","Level":"General","Department1":"general","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"ID080fe301945f4f70","Updated":"2016-09-13T23:50:33.161596Z"},{"HQCompanyId":"ID080fe301945f4f70","Title":"Assistant Economy &amp; Policy - Corporate Strategic Planning","DecisionMaker":false,"Start":"January 2011","End":"January 2012","Duration":"1 Year","Updated":"2016-09-13T23:50:35.72405Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Mariesa+Handayani+PT.Pertamina+(Persero)","SourceList":[]}<br />
    {"Key":"IDaec0e16edee655ef","FirstName":"Sanda","LastName":"Redman","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:48","HQCompanyName":"International Organization for Migration (IOM)","Position":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"CH0605c865fa324d07","Experience":[{"HQCompanyId":"CH0605c865fa324d07","Title":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"Start":"June 2006","End":"June 2011","Duration":"5 Years","SecondaryCompanyId":"CH0605c865fa324d07","Updated":"2016-10-27T18:56:50.117866Z"},{"Title":"Graphic Designer","DecisionMaker":false,"Start":"November 2004","End":"May 2006","Duration":"1 Year 6 months","Updated":"2016-10-27T18:56:50.289713Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sanda+Redman+International+Organization+for+Migration+(IOM)","SourceList":[]}<br />
    {"Key":"IDaec0b6a25116fccb","FirstName":"Falah","LastName":"Azmi","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T09:46:36","HQCompanyName":"PT Kencana Trans Wisata","Position":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":null},{"Title":"Manager","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":"2016-09-15T13:59:28.021962Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Falah+Azmi+PT+Kencana+Trans+Wisata","SourceList":[]}<br />
    {"Key":"IDaec0aa2b82ab5ed6","FirstName":"Ritter","LastName":"Dante","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-05-31T03:24:36","HQCompanyName":"Teleplan International","Position":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="44362d303021366a20252a302104302128213428252a6a272b29">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-02-16T15:06:00","HQCompanyId":"NL002000c570268aec","Experience":[{"HQCompanyId":"NL002000c570268aec","Title":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"March 2014","End":"Present","Duration":"2 Years 2 months","SecondaryCompanyId":"NL002000c570268aec","Updated":"2016-09-14T23:38:46.545336Z"},{"HQCompanyId":"MY0fd181d432ffe31f","Title":"ICT Administrator - Network","DecisionMaker":false,"Start":"April 2012","End":"February 2014","Duration":"1 Year 10 months","Updated":"2016-09-14T23:38:47.717177Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ritter+Dante+Teleplan+International","SourceList":[]}<br />
    {"Key":"IDaec0a2cf3196ac38","FirstName":"Faheem","LastName":"Khan","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:46","HQCompanyName":"PT Ascenta Group","Position":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T10:23:17.136269Z"},{"Title":"Business Development","DecisionMaker":false,"Start":"January 2015","End":"September 2017","Duration":"2 Years 8 months","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Faheem+Khan+PT+Ascenta+Group","SourceList":[]}<br />
    {"Key":"IDaec09acfd6feb5c8","FirstName":"Prasasti","LastName":"Dinar","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T02:32:05","HQCompanyName":"PT HM Sampoerna Tbk.","Position":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"IDe55fa88903bd39c6","Experience":[{"HQCompanyId":"IDe55fa88903bd39c6","Title":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"Start":"August 2008","End":"Present","Duration":"8 Years","SecondaryCompanyId":"IDe55fa88903bd39c6","Updated":"2016-11-24T20:49:25.674919Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Prasasti+Dinar+PT+HM+Sampoerna+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec09a0e25208c10","FirstName":"Merryntan","LastName":"Delima","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-20T14:30:13","HQCompanyName":"PT Forisa Nusapersada","Position":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"XXa1b6a80cecb3cb5e","Experience":[{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"XXa1b6a80cecb3cb5e","Updated":null},{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","DecisionMaker":false,"Start":"November 2007","End":"November 2012","Duration":"5 Years","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Merryntan+Delima+PT+Forisa+Nusapersada","SourceList":[]}<br />
    {"Key":"IDaec080f3c1a06167","FirstName":"Made","LastName":"Ari Puspita Sari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:16","HQCompanyName":"Sale Stock","Position":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"XX62ed1a82872fc897","Experience":[{"HQCompanyId":"XX62ed1a82872fc897","Title":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"July 2015","End":"Present","Duration":"11 months","SecondaryCompanyId":"XX62ed1a82872fc897","Updated":"2016-09-16T19:39:59.253217Z"},{"HQCompanyId":"AU779e74ff0dbd83c8","Title":"Test Lead","DecisionMaker":false,"Start":"January 2015","End":"June 2015","Duration":"5 months","Updated":"2016-09-16T19:40:00.206327Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Made+Ari+Puspita+Sari+Sale+Stock","SourceList":[]}<br />
    {"Key":"IDaec069c3d4427717","FirstName":"Isidorus","LastName":"Ariyanto","City":"Yogyakarta","RegionCode":"10","RegionName":"Yogyakarta","Country":"Indonesia","Latitude":"-7.782780","Longitude":"110.360830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-01T16:27:07","HQCompanyName":"Maesindo Indonesia, Ltd","Position":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"End":"Present","Updated":"2016-06-26T18:22:59.667065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Isidorus+Ariyanto+Maesindo+Indonesia,+Ltd","SourceList":[]}<br />
    {"Key":"IDaec0671dd16ec00f","FirstName":"Dewi","LastName":"Sugiharti","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"PT.A.J.Manulife Indonesia","Position":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"Start":"2005","End":"Present","Updated":"2016-09-16T12:28:20.269948Z"},{"Title":"accounting","DecisionMaker":false,"Start":"2000","End":"2000","Updated":"2016-09-16T12:28:20.535554Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dewi+Sugiharti+PT.A.J.Manulife+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec04504c00835bf","FirstName":"Ampu","LastName":"Resmanto","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:26:59","HQCompanyName":"PT Reckitt Benckiser Indonesia","Position":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDe6499abd1663cb98","Title":"TPM Manager at TA-Brewery","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2014","End":"September 2017","Duration":"3 Years","SecondaryCompanyId":"IDe6499abd1663cb98","Updated":"2016-10-28T06:59:00.924465Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ampu+Resmanto+PT+Reckitt+Benckiser+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec03a0815453494","FirstName":"Nadya","LastName":"Lupita","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT Antam Tbk","Position":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aac4cbced3cb84c6dfdac3decbeacbc4decbc784c9c5c7">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2017-04-05T13:55:56","HQCompanyId":"ID321b32dec7d18c8b","Experience":[{"HQCompanyId":"ID321b32dec7d18c8b","Title":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"January 2015","End":"Present","Duration":"1 Year 4 months","SecondaryCompanyId":"ID321b32dec7d18c8b","Updated":"2016-09-13T23:48:42.319372Z"},{"HQCompanyId":"ID9a11f8867bff4c72","Title":"Secretary of CEO","DecisionMaker":false,"Start":"August 2014","End":"December 2014","Duration":"4 months","Updated":"2016-09-13T23:48:43.053732Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nadya+Lupita+PT+Antam+Tbk","SourceList":[]}<br />
    {"Key":"IDaec0343c7485dba1","FirstName":"Surya","LastName":"Febianto","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-21T16:40:57","HQCompanyName":"PT. Agung Sedayu Group","Position":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID08710b895fe19eb7","Experience":[{"HQCompanyId":"ID08710b895fe19eb7","Title":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"2010","End":"Present","SecondaryCompanyId":"ID08710b895fe19eb7","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Surya+Febianto+PT.+Agung+Sedayu+Group","SourceList":[]}<br />
    {"Key":"IDaec02d845f729852","FirstName":"Arianto Teddy","LastName":"Wibowo","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T00:22:41","HQCompanyName":"Mango Terrace Restaurant","Position":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"Start":"September 2014","End":"Present","Duration":"1 Year 11 months","Updated":"2016-11-24T13:34:59.693143Z"},{"Title":"tidak bekerja","DecisionMaker":false,"Start":"January 2014","End":"September 2014","Duration":"8 months","Updated":"2016-11-24T13:35:00.230168Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Arianto+Teddy+Wibowo+Mango+Terrace+Restaurant","SourceList":[]}<br />
    {"Key":"IDaec0234a72a88b32","FirstName":"Iin Azairin","LastName":"Aziz","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-09-14T11:37:43","HQCompanyName":"PT Bakrie Metal Industries","Position":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T00:53:30.894808Z"},{"Title":"Assisstant to CEO - Business Process Development","DecisionMaker":false,"Start":"August 2014","End":"Present","Duration":"2 Years 1 month","Updated":"2016-12-07T00:53:38.848008Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Iin+Azairin+Aziz+PT+Bakrie+Metal+Industries","SourceList":[]}<br />
    {"Key":"IDaec00c9d182a1877","FirstName":"Kiagus","LastName":"Firmansyah","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-25T17:15:48","HQCompanyName":"PT. Trans Retail Indonesia","Position":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","DepartmentFunction":"creative","DecisionMaker":false,"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Experience":[{"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Title":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","FunctionalArea":"creative","DecisionMaker":false,"Start":"February 2010","End":"Present","Duration":"6 Years 6 months","SecondaryCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Updated":"2016-11-24T09:46:10.797726Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Kiagus+Firmansyah+PT.+Trans+Retail+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec0034a7587853d","FirstName":"Houtman","LastName":"Simanjuntak","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-19T03:39:55","HQCompanyName":"Virtus and Varda as newly established company offering environmental solutions to the industries.","Position":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Experience":[{"Title":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T15:11:54.946605Z"},{"HQCompanyId":"ID325cb8f3d7bd7ef8","Title":"President Director &amp; CEO","DecisionMaker":false,"Start":"January 1997","End":"March 2015","Duration":"18 Years 2 months","Updated":"2016-09-15T15:12:00.243412Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Houtman+Simanjuntak+Virtus+and+Varda+as+newly+established+company+offering+environmental+solutions+to+the+industries.","SourceList":[]}<br />
    {"Key":"IDaec003092517f6af","FirstName":"Nena","LastName":"Ermila","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT. Asuransi Jasa Indonesia","Position":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID8ec56f05a752fc4b","Experience":[{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2016","End":"Present","Duration":"4 months","SecondaryCompanyId":"ID8ec56f05a752fc4b","Updated":"2016-09-15T04:07:01.514989Z"},{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Sub Division Head","DecisionMaker":false,"Start":"October 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-09-15T04:07:02.811851Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nena+Ermila+PT.+Asuransi+Jasa+Indonesia","SourceList":[]}<br />
    {"Key":"IDaebff7f35e83819d","FirstName":"Didik","LastName":"Wibawanto","City":"Bandar Lampung","RegionCode":"15","RegionName":"Lampung","Country":"Indonesia","Latitude":"-5.425440","Longitude":"105.258030","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-26T20:10:55","HQCompanyName":"Private Corporation","Position":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Experience":[{"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Title":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"5 months","SecondaryCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Updated":"2016-11-24T17:01:02Z"},{"Title":"Chief Information Officer","DecisionMaker":false,"Start":"September 2015","End":"Present","Duration":"11 months","Updated":"2016-11-24T17:01:02.814897Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Didik+Wibawanto+Private+Corporation","SourceList":[]}<br />
    {"Key":"IDaebff37ce8ef65d7","FirstName":"Elin-Psg","LastName":"Herliana","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T03:24:35","HQCompanyName":"Olympus Property","Position":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4d28212423603d3e2a6325283f21242c232c0d222134203d383e3d3f223d283f3934632e2220">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3833261+00:00","HQCompanyId":"US21d063d73525fb16","Experience":[{"HQCompanyId":"US21d063d73525fb16","Title":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 10 months","SecondaryCompanyId":"abc284e2-5a4a-43d4-8468-1cee07fe4fb5","Updated":"2016-09-15T03:14:55.432942Z"},{"HQCompanyId":"ID47b7a4355d2abb19","Title":"Koodinator Kantor Kas","DecisionMaker":false,"Start":"1999","End":"2007","Updated":"2016-09-15T03:14:56.636055Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Elin-Psg+Herliana+Olympus+Property","SourceList":[]}<br />
    {"Key":"IDaebfef534eac0d49","FirstName":"Yulnia","LastName":"Azriani","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T21:10:41","HQCompanyName":"PT Putra Taro Paloma (subsidiary of PT Tiga Pilar Sejahtera)","Position":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"Start":"November 2012","End":"April 2015","Duration":"2 Years 5 months","Updated":"2016-09-15T18:39:52.681431Z"},{"Title":"Marketing Supervisor for RoC","DecisionMaker":false,"Start":"February 2010","End":"August 2011","Duration":"1 Year 6 months","Updated":"2016-09-15T18:39:54.71263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yulnia+Azriani+PT+Putra+Taro+Paloma+(subsidiary+of+PT+Tiga+Pilar+Sejahtera)","SourceList":[]}<br />
    {"Key":"IDaebfd4becc131607","FirstName":"MizanStore","LastName":".Com","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-16T21:08:41","HQCompanyName":"PT Mizan Digital Publishing","Position":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"June 2013","End":"Present","Duration":"3 Years","Updated":"2016-10-27T05:59:56.131533Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=MizanStore+.Com+PT+Mizan+Digital+Publishing","SourceList":[]}<br />
    {"Key":"IDaebfb9cd79b65f90","FirstName":"Riadi","LastName":"Wirawan","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T21:10:34","HQCompanyName":"MMC Hospital","Position":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"End":"Present","Updated":"2016-09-15T23:51:32.140538Z"},{"Title":"Dr","DecisionMaker":false,"Start":"January 1990","End":"Present","Duration":"26 Years 4 months","Updated":"2016-09-15T23:51:32.140538Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Riadi+Wirawan+MMC+Hospital","SourceList":[]}<br />
    {"Key":"IDaebf803066abb18a","FirstName":"Anna","LastName":"Myr","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:30","HQCompanyName":"Smart Advert","Position":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-10-27T19:07:16.619651Z"},{"Title":"Administration Staff","DecisionMaker":false,"Start":"November 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-10-27T19:07:25.260324Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anna+Myr+Smart+Advert","SourceList":[]}<br />
    {"Key":"IDaebf7fa59c3f2c61","FirstName":"Herman","LastName":"Tea","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-08-26T20:11:14","HQCompanyName":"smpn 1 gununghalu","Position":"staf","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"staf","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2004","End":"Present","Duration":"12 Years 7 months","Updated":"2016-11-25T02:05:46.310689Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Herman+Tea+smpn+1+gununghalu","SourceList":[]}<br />
    {"Key":"IDaebf6eeabefb13b1","FirstName":"Anggun","LastName":"Triadi","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T03:24:38","HQCompanyName":"Dwisapta Advertising","Position":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"February 2011","End":"Present","Duration":"5 Years 3 months","Updated":"2016-09-15T02:10:36.579721Z"},{"HQCompanyId":"IDda4ac54b00ab8257","Title":"Account Director","DecisionMaker":false,"Start":"January 2009","End":"January 2011","Duration":"2 Years","Updated":"2016-09-15T02:10:39.970247Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggun+Triadi+Dwisapta+Advertising","SourceList":[]}<br />
    {"Key":"IDaebf4c097ed370c9","FirstName":"Hans","LastName":"Ferdinan","City":"Makassar","RegionCode":"38","RegionName":"South Sulawesi","Country":"Indonesia","Latitude":"-5.140000","Longitude":"119.422100","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-19T19:57:40","HQCompanyName":"PT Bank Nationalnobu Tbk","Position":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"April 2014","End":"Present","Duration":"2 Years 2 months","Updated":"2016-10-27T18:52:30.413971Z"},{"HQCompanyId":"ID67b4599c6320e3f7","Title":"Marketing Manager","DecisionMaker":false,"Start":"April 2012","End":"April 2014","Duration":"2 Years","Updated":"2016-10-27T18:52:30.913991Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Hans+Ferdinan+PT+Bank+Nationalnobu+Tbk","SourceList":[]}<br />
    {"Key":"IDaebf415f88033514","FirstName":"Yessie Afriana","LastName":"Wulandari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"PT PEMBANGUNAN PERUMAHAN (PERSERO)","Position":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-16T10:38:42.422819Z"},{"Title":"Civil Engineer","DecisionMaker":false,"Start":"May 2013","End":"January 2014","Duration":"8 months","Updated":"2016-09-16T10:38:46.110263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yessie+Afriana+Wulandari+PT+PEMBANGUNAN+PERUMAHAN+(PERSERO)","SourceList":[]}<br />
    {"Key":"IDaebf1453d77ae08c","FirstName":"Debby Niken","LastName":"Kartika W","City":"Surabaya","RegionCode":"08","RegionName":"East Java","Country":"Indonesia","Latitude":"-7.249170","Longitude":"112.750830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-02T14:44:18","HQCompanyName":"Cv. BM Surabaya","Position":"IA","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"IA","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"3 months","Updated":"2016-09-16T13:11:39.999845Z"},{"Title":"Senior Staf","DecisionMaker":false,"Start":"September 2015","End":"January 2016","Duration":"4 months","Updated":"2016-09-16T13:11:43.99979Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Debby+Niken+Kartika+W+Cv.+BM+Surabaya","SourceList":[]}<br />
    {"Key":"IDaebf000ee0827443","FirstName":"Vebi","LastName":"Nadhira","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:29","HQCompanyName":"Institut Teknologi Bandung","Position":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"HQCompanyId":"IDc5a1b238422cffa9","Experience":[{"HQCompanyId":"IDc5a1b238422cffa9","Title":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"IDc5a1b238422cffa9","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Vebi+Nadhira+Institut+Teknologi+Bandung","SourceList":[]}<br />
    {"Key":"IDaebed0315a11669b","FirstName":"Ratu","LastName":"Wijaksana","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:26","HQCompanyName":"Smilebuilderz LLC","Position":"dentist, health team","Level":"General","Department1":"Medical","DepartmentFunction":"Dentist","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b3c1d2c7c6c4f3c0dedadfd6d1c6dadfd7d6c1c99dd0dcde">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"US08bccec1e3cec938","Experience":[{"HQCompanyId":"US08bccec1e3cec938","Title":"dentist, health team","Level":"General","Department1":"Medical","FunctionalArea":"Dentist","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"US08bccec1e3cec938","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ratu+Wijaksana+Smilebuilderz+LLC","SourceList":[]}<br />
    {"Key":"IDaebeca27f944b5ff","FirstName":"Budi","LastName":"Telly","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-01T21:27:04","HQCompanyName":"PT. Tirtakencana Tatawarna","Position":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"ID5d4a1a67c8710963","Experience":[{"HQCompanyId":"ID5d4a1a67c8710963","Title":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"ID5d4a1a67c8710963","Updated":"2016-09-16T21:17:15.12617Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Budi+Telly+PT.+Tirtakencana+Tatawarna","SourceList":[]}</code></div></div><br />
    1 Million records<br />
    [Hidden Content]<br />
    <br />
    <br />
    2- Other 500Million Data<br />
    <br />
    <div class="codeblock"><div class="body" dir="ltr"><code>100M-LINKEDIN.zip<br />
    35M LINKEDIN CONTACT (WITH COMPANY) B2B.zip<br />
    2.5M US B2B Linkedin.zip<br />
    25M-Linkedin.zip<br />
    Australia Linkedin 194K.zip<br />
    Linkedin - 250 758 057.zip<br />
    Linkedin 34 Million Linkedin Emails.zip<br />
    linkedin 37 million db-16M.zip<br />
    Linkedin 45k With Full Details.zip<br />
    linkedin db 35M.zip<br />
    Linkedin DB with Profile URLS 21M.zip<br />
    Linkedin Dehased 1GB.zip<br />
    Linkedin Pakistan.zip<br />
    Linkedin sorted by Titles.zip<br />
    Linkedin-Company-Education_FR.zip<br />
    LinkedIn.rar<br />
    Linkedin2.zip<br />
    LinkedInMain 16M.zip</code></div></div><img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" alt="[Image: dqJxEFX.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" data-image-modal-original="https://i.imgur.com/dqJxEFX.png" data-image-modal-safe="1" /><br />
    <br />
    <br />
    <br />
    for more detail PM me on telegram: @<a href="https://raidforums.com/User-TomLiner" class="mycode_mention" target="_blank"><span class="rf_i rf_god">TomLiner</span></a><br />
    <hr class="mycode_hr" />
    Give me Positive(+) Reputation<br />
    Step by step<br />
    <br />
    1- <br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/oGBmrni.png" alt="[Image: oGBmrni.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/oGBmrni.png" data-image-modal-original="https://i.imgur.com/oGBmrni.png" data-image-modal-safe="1" /><br />
    <br />
    2- <br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/RM6c7G0.png" alt="[Image: RM6c7G0.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/RM6c7G0.png" data-image-modal-original="https://i.imgur.com/RM6c7G0.png" data-image-modal-safe="1" /><br />
    <br />
    3-<br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/7ElzEeH.png" alt="[Image: 7ElzEeH.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/7ElzEeH.png" data-image-modal-original="https://i.imgur.com/7ElzEeH.png" data-image-modal-safe="1" /></blockquote>Thanks for you bro it is to much 🙂
    </div>
    <div class="post_meta" id="post_meta_3652198">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3652198" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3652340" id="pid3652340"></a>
    <div class="post " style="" id="post_3652340">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-hawaii"><span class="rf_i rf_god">hawaii</span></a></div>
    <a href="User-hawaii" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar1-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">GOD User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/s/ranks/god.png" alt="GOD Upgraded Member" title="GOD Upgraded Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">4</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2020</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121812041"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <span class="user_service" data-years="1">1 Year of service</span>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=1" title="GOD"><span class="rf_i rf_god rf_awardsi huge fitted link icon"></span></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3652340#pid3652340" title="RE: LinkedIn 1Billion(1000Million) Record">#6</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 01:14 AM <span class="post_edit" id="edited_by_3652340"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3652340">
    left you a rep, may share the fb and LinkedIn link?
    </div>
    <div class="post_meta" id="post_meta_3652340">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3652340" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3653025" id="pid3653025"></a>
    <div class="post " style="" id="post_3653025">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-EduardoCAstillo21"><span class="rf_noob">EduardoCAstillo21</span></a></div>
    <a href="User-EduardoCAstillo21" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar1-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">New User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_yfVa.png" alt="Member" title="Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">3</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=122035385"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3653025#pid3653025" title="RE: LinkedIn 1Billion(1000Million) Record">#7</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 02:40 AM <span class="post_edit" id="edited_by_3653025"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3653025">
    Goddd tux very nice XDXDXDXD
    </div>
    <div class="post_meta" id="post_meta_3653025">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3653025" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3653958" id="pid3653958"></a>
    <div class="post " style="" id="post_3653958">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-TomLiner"><span class="rf_i rf_god">TomLiner</span></a></div>
    <a href="User-TomLiner" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar1-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">GOD User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/s/ranks/god.png" alt="GOD Upgraded Member" title="GOD Upgraded Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">16</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">6</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Feb 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121989907"><strong class="reputation_positive">254</strong></a>
    </span>
    </div>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=1" title="GOD"><span class="rf_i rf_god rf_awardsi huge fitted link icon"></span></a><a href="https://raidforums.com/awards.php?view=20" title="Refer 100 people to RF."><img src="https://cdn.raidforums.com/s/shop/cancerino.png" alt="Refer 100 people to RF." /></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3653958#pid3653958" title="RE: LinkedIn 1Billion(1000Million) Record">#8</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 04:44 AM <span class="post_edit" id="edited_by_3653958"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3653958">
    <blockquote class="mycode_quote"><cite><span> (April 03, 2021 at 04:57 PM)</span>warri0r23 Wrote: <a rel="nofollow" href="misc.php?action=safelinks&url=https%3A%2F%2Fraidforums.com%2FThread-SELLING-LinkedIn-1Billion-1000Million-Record%3Fpid%3D3649749%23pid3649749" class="quick_jump"><i class="fas fa-long-arrow-alt-right"></i></a></cite>Thank you for sharing it... how is this data is????<br />
    As LinkedIn got data breach in 2016...</blockquote><br />
    No <br />
    My data date: 2019-2020
    </div>
    <div class="post_meta" id="post_meta_3653958">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3653958" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3654501" id="pid3654501"></a>
    <div class="post " style="" id="post_3654501">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="postbitbg" style="background-image: url(https://cdn.raidforums.com/uploads/postbitbgs/avatar_121647080.gif?dateline=1617327857)"></div>
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-All3in"><i class="rf_i rf_god"></i><span class="rf_godx" style="color: #95bfc4;"> All3in</span></a></div>
    <a href="User-All3in" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/uploads/avatars/avatar_121647080.jpg?dateline=1617326216" alt="" width="104" height="130" /></a>
    </div>
    <div class="post__user-title">Data Raper
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge"></div>
    </div>
    <div class="socialsites socialsites--postbit rounded"><span class="socialsites__icon"><a href="https://www.instagram.com/instagram" title="Instagram" rel="nofollow" target="_blank"><i class="fab fa-instagram" style="color: #e1306c;"></i></a></span><span class="socialsites__icon"><a href="https://www.youtube.com/channel/youtube" title="YouTube" rel="nofollow" target="_blank"><i class="fab fa-youtube" style="color: #ff0000;"></i></a></span><span class="socialsites__icon"><a href="https://www.flickr.com/photos/flickr" title="Flickr" rel="nofollow" target="_blank"><i class="fab fa-flickr" style="color: #ff0084;"></i></a></span></div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">162</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">17</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Sep 2019</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121647080"><strong class="reputation_positive">337</strong></a>
    </span>
    </div>
    <span class="user_service" data-years="1">1 Year of service</span>
    <div class="post__user-awards"><br class="ougc_awards_postbit_maxperline" /><a href="https://raidforums.com/awards.php?view=1" title="GOD"><span class="rf_i rf_god rf_awardsi huge fitted link icon"></span></a><a href="https://raidforums.com/awards.php?view=28" title="Achieve 1 month of online time."><img src="https://cdn.raidforums.com/s/shop/addicted.png" alt="Achieve 1 month of online time." /></a><a href="https://raidforums.com/awards.php?view=16" title="Has extended contribution to the Leaks subforum."><img src="https://cdn.raidforums.com/s/shop/0lgtsy5v71.png" alt="Has extended contribution to the Leaks subforum." /></a><a href="https://raidforums.com/awards.php?view=36" title="Is often seen conversing in the shoutbox."><img src="https://cdn.raidforums.com/s/shop/sb.svg" alt="Is often seen conversing in the shoutbox." /></a><a href="https://raidforums.com/awards.php?view=32" title="Keep RF clean by reporting posts and threads, generally over 100 valid reports."><img src="https://cdn.raidforums.com/s/shop/reporter.png" alt="Keep RF clean by reporting posts and threads, generally over 100 valid reports." /></a></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3654501#pid3654501" title="RE: LinkedIn 1Billion(1000Million) Record">#9</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 05:47 AM <span class="post_edit" id="edited_by_3654501"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3654501">
    you already broke the rule 2 dude<br />
    <a rel="nofollow" href="misc.php?action=safelinks&url=https%3A%2F%2Fraidforums.com%2Fmisc.php%3Faction%3Dhelp%26hid%3D12" target="_blank" rel="noopener" class="mycode_url">https://raidforums.com/misc.php?action=help&amp;hid=12</a>
    </div>
    <div class="post_meta" id="post_meta_3654501">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3654501" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3654544" id="pid3654544"></a>
    <div class="post " style="" id="post_3654544">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-eilonl"><span class="rf_noob">eilonl</span></a></div>
    <a href="User-eilonl" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar1-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">New User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_yfVa.png" alt="Member" title="Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">2</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=122036552"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3654544#pid3654544" title="RE: LinkedIn 1Billion(1000Million) Record">#10</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 05:51 AM <span class="post_edit" id="edited_by_3654544"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3654544">
    + 1 on the rep. Good stuff
    </div>
    <div class="post_meta" id="post_meta_3654544">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3654544" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3654672" id="pid3654672"></a>
    <div class="post " style="" id="post_3654672">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-natz"><span class="rf_noob">natz</span></a></div>
    <a href="User-natz" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">New User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_yfVa.png" alt="Member" title="Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">1</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">0</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Apr 2021</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=122036850"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3654672#pid3654672" title="RE: LinkedIn 1Billion(1000Million) Record">#11</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 06:02 AM <span class="post_edit" id="edited_by_3654672"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3654672">
    Do u have data of VietNam <img src="https://cdn.raidforums.com/images/rf/smilies/biggrin.png" alt="Biggrin" title="Biggrin" class="smilie smilie_113" /><br />
    <blockquote class="mycode_quote"><cite><span> (April 03, 2021 at 01:41 PM)</span>TomLiner Wrote: <a rel="nofollow" href="misc.php?action=safelinks&url=https%3A%2F%2Fraidforums.com%2FThread-SELLING-LinkedIn-1Billion-1000Million-Record%3Fpid%3D3649114%23pid3649114" class="quick_jump"><i class="fas fa-long-arrow-alt-right"></i></a></cite>I have 520Million +500Million Other Data<br />
    <br />
    <br />
    1- 520Million data:<br />
    50 records as sample:<br />
    <div class="codeblock"><div class="body" dir="ltr"><code>{"Key":"IDaec32d2de20b3b87","FirstName":"Nur","LastName":"Slamet","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2015-12-15T13:03:43","HQCompanyName":"pt. dasaplast nusantara","Position":"tax","Level":"General","Department1":"Finance","DepartmentFunction":"Tax","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"tax","Level":"General","Department1":"Finance","FunctionalArea":"Tax","DecisionMaker":false,"End":"Present","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nur+Slamet+pt.+dasaplast+nusantara","SourceList":[]}<br />
    {"Key":"IDaec31c1df35c7515","FirstName":"Raden","LastName":"Prima","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:18","HQCompanyName":"PT Adaro Energy, Tbk","Position":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="14667570717a3a64667d797554757075667b3a777b79">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"XXdb5ff904529c27f8","Experience":[{"HQCompanyId":"XXdb5ff904529c27f8","Title":"Human Resource Supervisor | PT. Jasapower Indonesia, Subsidiary of PT. Adaro Energy, Tbk.","Level":"General","Department1":"HR","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"XXdb5ff904529c27f8","Updated":"2016-09-15T14:20:47.879374Z"},{"Title":"People Development Officer","DecisionMaker":false,"Start":"January 2013","End":"January 2014","Duration":"1 Year","Updated":"2016-09-15T14:20:49.269986Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Raden+Prima+PT+Adaro+Energy,+Tbk","SourceList":[]}<br />
    {"Key":"IDaec31367e617538f","FirstName":"Jimmi","LastName":"Huang","City":"Medang","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.357780","Longitude":"106.654720","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-19T19:57:39","HQCompanyName":"PT Aplaus Duta Kreasi","Position":"Web Development","Level":"General","Department1":"Technology","DepartmentFunction":"Web Development","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Web Development","Level":"General","Department1":"Technology","FunctionalArea":"Web Development","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","Updated":"2016-10-27T23:26:48.308924Z"},{"Title":"Brand Analyst","DecisionMaker":false,"Start":"January 2011","End":"December 2012","Duration":"1 Year 11 months","Updated":"2016-10-27T23:26:48.726943Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Jimmi+Huang+PT+Aplaus+Duta+Kreasi","SourceList":[]}<br />
    {"Key":"IDaec30d78223c1126","FirstName":"Yohanes","LastName":"Agung","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T19:57:59","HQCompanyName":"HANS PRODUCTION PHOTOGRAPHY","Position":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner &amp; fotografer","Level":"Owner","Department1":"Executive","DecisionMaker":true,"End":"Present","Updated":"2016-10-27T18:38:36.599078Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yohanes+Agung+HANS+PRODUCTION+PHOTOGRAPHY","SourceList":[]}<br />
    {"Key":"IDaec30b62244d0e4d","FirstName":"Rindu","LastName":"Tarigan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"Indosat Ooredoo","Position":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bbc9d2d5dfce95cfdac9d2dcdad5fbd2d5dfd4c8dacf95d8d4d6">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.1957124+00:00","HQCompanyId":"ID962bc091e8a0f07c","Experience":[{"HQCompanyId":"ID962bc091e8a0f07c","Title":"Engineer","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"2003","End":"2015","SecondaryCompanyId":"ID962bc091e8a0f07c","Updated":"2016-09-16T16:57:26.30909Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Rindu+Tarigan+Indosat+Ooredoo","SourceList":[]}<br />
    {"Key":"IDaec2f04742efc165","FirstName":"Djie","LastName":"Merie","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"FM Group Indonesia","Position":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Distributor","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-17T01:26:14.95928Z"},{"Title":"Consultant","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-09-17T01:26:17.428004Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Djie+Merie+FM+Group+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec2d5768cae15c7","FirstName":"Sani","LastName":"Kurniawan","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-18T21:58:49","HQCompanyName":"PT Pangansari Utama","Position":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"HQCompanyId":"XXc43ca4f532d93106","Experience":[{"HQCompanyId":"XXc43ca4f532d93106","Title":"baker","Level":"General","Department1":"Culinary","DecisionMaker":false,"Start":"January 2012","End":"Present","Duration":"4 Years 5 months","SecondaryCompanyId":"XXc43ca4f532d93106","Updated":"2016-10-27T15:30:30.332807Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sani+Kurniawan+PT+Pangansari+Utama","SourceList":[]}<br />
    {"Key":"IDaec2ad4ade70d967","FirstName":"Albert","LastName":"Prabowo","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:39","HQCompanyName":"Fashion Photographer","Position":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Experience":[{"Title":"Creative Art Director","Level":"Director","Department1":"Design","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","EmailAddress":"","Updated":null},{"HQCompanyId":"CN14282ad89ed4b365","Title":"Technical Team Leader VAS Engineer","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"November 2009","End":"January 2018","Duration":"8 Years 2 months","SecondaryCompanyId":"CN14282ad89ed4b365","Updated":"2016-10-27T12:54:51.181502Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Albert+Prabowo+Fashion+Photographer","SourceList":[]}<br />
    {"Key":"IDaec27ee0121967d7","FirstName":"Zami","LastName":"Zen","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"potrait","Position":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"anggota","Level":"General","Department1":"General","DecisionMaker":false,"Start":"October 2015","End":"Present","Duration":"11 months","Updated":"2016-12-07T04:10:48.705501Z"},{"Title":"Student","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T04:11:03.346252Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Zami+Zen+potrait","SourceList":[]}<br />
    {"Key":"IDaec278ea5aebe9a3","FirstName":"Agustinus","LastName":"Edo","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-09-14T11:36:57","HQCompanyName":"PT. Sigma Metrasys Solution","Position":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"HQCompanyId":"ID3bc190ebfc539b69","Experience":[{"HQCompanyId":"ID3bc190ebfc539b69","Title":"SAP HCM Consultant","Level":"General","Department1":"Consultant","Department2":"Technology","DecisionMaker":false,"Start":"July 2013","End":"Present","Duration":"3 Years 2 months","SecondaryCompanyId":"ID3bc190ebfc539b69","Updated":"2016-12-07T09:22:25.825471Z"},{"HQCompanyId":"ID3bc190ebfc539b69","Title":"Internship Program","DecisionMaker":false,"Start":"June 2012","End":"November 2012","Duration":"5 months","Updated":"2016-12-07T09:22:30.387929Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Agustinus+Edo+PT.+Sigma+Metrasys+Solution","SourceList":[]}<br />
    {"Key":"IDaec1c2006dd22bfa","FirstName":"Anggie","LastName":"Buntoro","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-20T18:43:46","HQCompanyName":"PT.APL Logistics","Position":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Warehouse Analyst","Level":"General","Department1":"Warehousing","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 11 months","Updated":"2016-10-28T13:20:37.602039Z"},{"HQCompanyId":"SG781880de3052a221","Title":"warehouse analyst","DecisionMaker":false,"Start":"December 2009","End":"Present","Duration":"6 Years 6 months","Updated":"2016-10-28T13:20:38.081021Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggie+Buntoro+PT.APL+Logistics","SourceList":[]}<br />
    {"Key":"IDaec1b6fc0d739f26","FirstName":"Bambang","LastName":"Wahyu","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-09-14T11:36:58","HQCompanyName":"The Trans Luxury Hotel","Position":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Experience":[{"HQCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Title":"Spv engineering","Level":"General","Department1":"Engineering","DecisionMaker":false,"Start":"December 2011","End":"Present","Duration":"4 Years 9 months","SecondaryCompanyId":"923b92c7-e731-4482-9b37-1bbe59c6742f","Updated":"2016-12-07T15:24:25.677779Z"},{"HQCompanyId":"154a343b-88ce-421e-b444-574474e9b3ea","Title":"Engineering Technician","DecisionMaker":false,"Start":"2003","End":"2010","Updated":"2016-12-07T15:24:25.912165Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Bambang+Wahyu+The+Trans+Luxury+Hotel","SourceList":[]}<br />
    {"Key":"IDaec18daced53216e","FirstName":"Gebreine Jessyca","LastName":"SE MM","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:46","HQCompanyName":"PT Kreasi Cemerlang Lestari, Gajah Tunggal Group (Fashion Retail Company)","Position":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Brand, Marketing and Operational Manager","Level":"Manager","Department1":"Marketing","Department2":"Operations","DecisionMaker":false,"Start":"July 2014","End":"Present","Duration":"1 Year 10 months","Updated":"2016-09-14T06:01:28.168302Z"},{"HQCompanyId":"DE3b7431aab5afd0e9","Title":"Business, Brand, and Marketing Freelance Consultant","DecisionMaker":false,"Start":"July 2011","End":"May 2014","Duration":"2 Years 10 months","Updated":"2016-09-14T06:01:31.855765Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Gebreine+Jessyca+SE+MM+PT+Kreasi+Cemerlang+Lestari,+Gajah+Tunggal+Group+(Fashion+Retail+Company)","SourceList":[]}<br />
    {"Key":"IDaec1793cac70cd03","FirstName":"Yuliati","LastName":"Noeriman","City":"Jawa","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.914720","Longitude":"107.630830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:27:33","HQCompanyName":"Paxel","Position":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Customer Journey &amp; People Experience","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDf572612d5ca2b9f6","Title":"GM of Sales Training and Development","Level":"Director","Department1":"HR","Department2":"Sales","FunctionalArea":"training","DecisionMaker":true,"Start":"December 2011","End":"September 2017","Duration":"5 Years 9 months","SecondaryCompanyId":"IDf572612d5ca2b9f6","Updated":"2016-11-24T15:41:06.250065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yuliati+Noeriman+Paxel","SourceList":[]}<br />
    {"Key":"IDaec165e886db96a3","FirstName":"Leila","LastName":"Ruwaidah","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Phone":"","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2018-02-06T17:42:29","HQCompanyName":"PT. Sigma Cipta Caraka (Telkomsigma)","Position":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"IDdff5ea184ffc7c9f","Experience":[{"HQCompanyId":"IDdff5ea184ffc7c9f","Title":"HC Recruitment &amp; Relationship","Level":"General","Department1":"HR","Department2":"Marketing","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"IDdff5ea184ffc7c9f","Updated":"2016-10-27T19:09:11.66686Z"},{"HQCompanyId":"ID9ad9575f43590343","Title":"Assessment Center Staff","DecisionMaker":false,"Start":"2002","End":"2007","Updated":"2016-10-27T19:09:12.510604Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Leila+Ruwaidah+PT.+Sigma+Cipta+Caraka+(Telkomsigma)","SourceList":[]}<br />
    {"Key":"IDaec15555d8f6d001","FirstName":"Dedy","LastName":"Prasetyono","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T09:46:34","HQCompanyName":"selular","Position":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"HQCompanyId":"","Experience":[{"Title":"Owner","Level":"Owner","Department1":"General","DecisionMaker":true,"Start":"April 2005","End":"Present","Duration":"11 Years 1 month","Updated":"2016-09-15T15:21:43.891635Z"},{"Title":"pic sales telkom flexi","DecisionMaker":false,"Start":"March 2003","End":"June 2006","Duration":"3 Years 3 months","Updated":"2016-09-15T15:21:45.172879Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dedy+Prasetyono+selular","SourceList":[]}<br />
    {"Key":"IDaec134a6a5ed1dc2","FirstName":"Lenny","LastName":"Iod","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-25T18:21:18","HQCompanyName":"Pt. Indofood CBP Sukses Makmur Tbk.","Position":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Regional Manager (Pacific area and South America region)","Level":"Manager","Department1":"Management","DecisionMaker":false,"End":"Present","Updated":"2016-11-24T13:37:21.841804Z"},{"Title":"Regional Manager (Pacific and South America Region)","DecisionMaker":false,"Start":"January 2008","End":"Present","Duration":"8 Years 7 months","Updated":"2016-11-24T13:37:22.654297Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Lenny+Iod+Pt.+Indofood+CBP+Sukses+Makmur+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec11de108d114a9","FirstName":"Anis","LastName":"Soyyati","RegionCode":"00","RegionName":"","Country":"Indonesia","Phone":"","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2018-02-06T17:42:37","HQCompanyName":"detikcom","Position":"Social Media","Level":"General","Department1":"Marketing","DepartmentFunction":"Social","DecisionMaker":false,"HQCompanyId":"ID53f2a78f4a31b2b9","Experience":[{"HQCompanyId":"ID53f2a78f4a31b2b9","Title":"Social Media","Level":"General","Department1":"Marketing","FunctionalArea":"Social","DecisionMaker":false,"Start":"January 2018","End":"Present","Duration":"1 month","PhoneNumber":"","SecondaryCompanyId":"ID53f2a78f4a31b2b9","Updated":"2016-09-16T13:32:38.638812Z"},{"HQCompanyId":"XX872fb88b1920a258","Title":"HRD GA","DecisionMaker":false,"Start":"October 2011","End":"April 2012","Duration":"6 months","Updated":"2016-09-16T13:32:39.357547Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anis+Soyyati+detikcom","SourceList":[]}<br />
    {"Key":"IDaec112db7df1e5a4","FirstName":"Mariesa","LastName":"Handayani","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:25:51","HQCompanyName":"PT.Pertamina (Persero)","Position":"-","Level":"General","Department1":"general","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="dcb1bdaeb5b9afbdf2b4bdb2b8bda5bdb2b59cacb9aea8bdb1b5b2bdf2bfb3b1">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-03-03T06:23:11","HQCompanyId":"ID080fe301945f4f70","Experience":[{"HQCompanyId":"ID080fe301945f4f70","Title":"-","Level":"General","Department1":"general","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","SecondaryCompanyId":"ID080fe301945f4f70","Updated":"2016-09-13T23:50:33.161596Z"},{"HQCompanyId":"ID080fe301945f4f70","Title":"Assistant Economy &amp; Policy - Corporate Strategic Planning","DecisionMaker":false,"Start":"January 2011","End":"January 2012","Duration":"1 Year","Updated":"2016-09-13T23:50:35.72405Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Mariesa+Handayani+PT.Pertamina+(Persero)","SourceList":[]}<br />
    {"Key":"IDaec0e16edee655ef","FirstName":"Sanda","LastName":"Redman","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:48","HQCompanyName":"International Organization for Migration (IOM)","Position":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"CH0605c865fa324d07","Experience":[{"HQCompanyId":"CH0605c865fa324d07","Title":"In-House Visual and Graphic Designer","Level":"General","Department1":"Design","DecisionMaker":false,"Start":"June 2006","End":"June 2011","Duration":"5 Years","SecondaryCompanyId":"CH0605c865fa324d07","Updated":"2016-10-27T18:56:50.117866Z"},{"Title":"Graphic Designer","DecisionMaker":false,"Start":"November 2004","End":"May 2006","Duration":"1 Year 6 months","Updated":"2016-10-27T18:56:50.289713Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Sanda+Redman+International+Organization+for+Migration+(IOM)","SourceList":[]}<br />
    {"Key":"IDaec0b6a25116fccb","FirstName":"Falah","LastName":"Azmi","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T09:46:36","HQCompanyName":"PT Kencana Trans Wisata","Position":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Manager","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":null},{"Title":"Manager","DecisionMaker":false,"Start":"December 2012","End":"Present","Duration":"3 Years 5 months","Updated":"2016-09-15T13:59:28.021962Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Falah+Azmi+PT+Kencana+Trans+Wisata","SourceList":[]}<br />
    {"Key":"IDaec0aa2b82ab5ed6","FirstName":"Ritter","LastName":"Dante","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-05-31T03:24:36","HQCompanyName":"Teleplan International","Position":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="44362d303021366a20252a302104302128213428252a6a272b29">[email&#160;protected]</a>","EmailValidationStatus":"Success","EmailValidationDate":"2017-02-16T15:06:00","HQCompanyId":"NL002000c570268aec","Experience":[{"HQCompanyId":"NL002000c570268aec","Title":"APAC Regional - IT Infrastructure Specialist","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"March 2014","End":"Present","Duration":"2 Years 2 months","SecondaryCompanyId":"NL002000c570268aec","Updated":"2016-09-14T23:38:46.545336Z"},{"HQCompanyId":"MY0fd181d432ffe31f","Title":"ICT Administrator - Network","DecisionMaker":false,"Start":"April 2012","End":"February 2014","Duration":"1 Year 10 months","Updated":"2016-09-14T23:38:47.717177Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ritter+Dante+Teleplan+International","SourceList":[]}<br />
    {"Key":"IDaec0a2cf3196ac38","FirstName":"Faheem","LastName":"Khan","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-29T09:27:46","HQCompanyName":"PT Ascenta Group","Position":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"PT Ascenta Group Indonesia","Level":"General","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T10:23:17.136269Z"},{"Title":"Business Development","DecisionMaker":false,"Start":"January 2015","End":"September 2017","Duration":"2 Years 8 months","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Faheem+Khan+PT+Ascenta+Group","SourceList":[]}<br />
    {"Key":"IDaec09acfd6feb5c8","FirstName":"Prasasti","LastName":"Dinar","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T02:32:05","HQCompanyName":"PT HM Sampoerna Tbk.","Position":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"IDe55fa88903bd39c6","Experience":[{"HQCompanyId":"IDe55fa88903bd39c6","Title":"Scientist","Level":"General","Department1":"General","DecisionMaker":false,"Start":"August 2008","End":"Present","Duration":"8 Years","SecondaryCompanyId":"IDe55fa88903bd39c6","Updated":"2016-11-24T20:49:25.674919Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Prasasti+Dinar+PT+HM+Sampoerna+Tbk.","SourceList":[]}<br />
    {"Key":"IDaec09a0e25208c10","FirstName":"Merryntan","LastName":"Delima","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-20T14:30:13","HQCompanyName":"PT Forisa Nusapersada","Position":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"XXa1b6a80cecb3cb5e","Experience":[{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","Level":"General","Department1":"General","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"XXa1b6a80cecb3cb5e","Updated":null},{"HQCompanyId":"XXa1b6a80cecb3cb5e","Title":"Human Capital","DecisionMaker":false,"Start":"November 2007","End":"November 2012","Duration":"5 Years","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Merryntan+Delima+PT+Forisa+Nusapersada","SourceList":[]}<br />
    {"Key":"IDaec080f3c1a06167","FirstName":"Made","LastName":"Ari Puspita Sari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:16","HQCompanyName":"Sale Stock","Position":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"XX62ed1a82872fc897","Experience":[{"HQCompanyId":"XX62ed1a82872fc897","Title":"Quality Assurance","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"July 2015","End":"Present","Duration":"11 months","SecondaryCompanyId":"XX62ed1a82872fc897","Updated":"2016-09-16T19:39:59.253217Z"},{"HQCompanyId":"AU779e74ff0dbd83c8","Title":"Test Lead","DecisionMaker":false,"Start":"January 2015","End":"June 2015","Duration":"5 months","Updated":"2016-09-16T19:40:00.206327Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Made+Ari+Puspita+Sari+Sale+Stock","SourceList":[]}<br />
    {"Key":"IDaec069c3d4427717","FirstName":"Isidorus","LastName":"Ariyanto","City":"Yogyakarta","RegionCode":"10","RegionName":"Yogyakarta","Country":"Indonesia","Latitude":"-7.782780","Longitude":"110.360830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-01T16:27:07","HQCompanyName":"Maesindo Indonesia, Ltd","Position":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Export","Level":"General","Department1":"Marketing","Department2":"Procurement","DecisionMaker":false,"End":"Present","Updated":"2016-06-26T18:22:59.667065Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Isidorus+Ariyanto+Maesindo+Indonesia,+Ltd","SourceList":[]}<br />
    {"Key":"IDaec0671dd16ec00f","FirstName":"Dewi","LastName":"Sugiharti","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-01T21:26:45","HQCompanyName":"PT.A.J.Manulife Indonesia","Position":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"financial planner","Level":"General","Department1":"Finance","DecisionMaker":false,"Start":"2005","End":"Present","Updated":"2016-09-16T12:28:20.269948Z"},{"Title":"accounting","DecisionMaker":false,"Start":"2000","End":"2000","Updated":"2016-09-16T12:28:20.535554Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Dewi+Sugiharti+PT.A.J.Manulife+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec04504c00835bf","FirstName":"Ampu","LastName":"Resmanto","City":"Banten","RegionCode":"33","RegionName":"Banten","Country":"Indonesia","Latitude":"-6.031670","Longitude":"106.202780","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2017-10-29T09:26:59","HQCompanyName":"PT Reckitt Benckiser Indonesia","Position":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Experience":[{"Title":"Manufacturing Manager Household","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":null},{"HQCompanyId":"IDe6499abd1663cb98","Title":"TPM Manager at TA-Brewery","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"September 2014","End":"September 2017","Duration":"3 Years","SecondaryCompanyId":"IDe6499abd1663cb98","Updated":"2016-10-28T06:59:00.924465Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ampu+Resmanto+PT+Reckitt+Benckiser+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec03a0815453494","FirstName":"Nadya","LastName":"Lupita","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT Antam Tbk","Position":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6e000f0a170f40021b1e071a0f2e0f001a0f03400d0103">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2017-04-05T13:55:56","HQCompanyId":"ID321b32dec7d18c8b","Experience":[{"HQCompanyId":"ID321b32dec7d18c8b","Title":"IT Service Management","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"January 2015","End":"Present","Duration":"1 Year 4 months","SecondaryCompanyId":"ID321b32dec7d18c8b","Updated":"2016-09-13T23:48:42.319372Z"},{"HQCompanyId":"ID9a11f8867bff4c72","Title":"Secretary of CEO","DecisionMaker":false,"Start":"August 2014","End":"December 2014","Duration":"4 months","Updated":"2016-09-13T23:48:43.053732Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nadya+Lupita+PT+Antam+Tbk","SourceList":[]}<br />
    {"Key":"IDaec0343c7485dba1","FirstName":"Surya","LastName":"Febianto","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-21T16:40:57","HQCompanyName":"PT. Agung Sedayu Group","Position":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID08710b895fe19eb7","Experience":[{"HQCompanyId":"ID08710b895fe19eb7","Title":"marketing","Level":"General","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"2010","End":"Present","SecondaryCompanyId":"ID08710b895fe19eb7","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Surya+Febianto+PT.+Agung+Sedayu+Group","SourceList":[]}<br />
    {"Key":"IDaec02d845f729852","FirstName":"Arianto Teddy","LastName":"Wibowo","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-26T00:22:41","HQCompanyName":"Mango Terrace Restaurant","Position":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Restaurant Manager","Level":"Manager","Department1":"Operations","Department2":"Management","DecisionMaker":false,"Start":"September 2014","End":"Present","Duration":"1 Year 11 months","Updated":"2016-11-24T13:34:59.693143Z"},{"Title":"tidak bekerja","DecisionMaker":false,"Start":"January 2014","End":"September 2014","Duration":"8 months","Updated":"2016-11-24T13:35:00.230168Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Arianto+Teddy+Wibowo+Mango+Terrace+Restaurant","SourceList":[]}<br />
    {"Key":"IDaec0234a72a88b32","FirstName":"Iin Azairin","LastName":"Aziz","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-09-14T11:37:43","HQCompanyName":"PT Bakrie Metal Industries","Position":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Corporate Management Representative","Level":"Manager","Department1":"General","DecisionMaker":false,"Start":"August 2015","End":"Present","Duration":"1 Year 1 month","Updated":"2016-12-07T00:53:30.894808Z"},{"Title":"Assisstant to CEO - Business Process Development","DecisionMaker":false,"Start":"August 2014","End":"Present","Duration":"2 Years 1 month","Updated":"2016-12-07T00:53:38.848008Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Iin+Azairin+Aziz+PT+Bakrie+Metal+Industries","SourceList":[]}<br />
    {"Key":"IDaec00c9d182a1877","FirstName":"Kiagus","LastName":"Firmansyah","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-08-25T17:15:48","HQCompanyName":"PT. Trans Retail Indonesia","Position":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","DepartmentFunction":"creative","DecisionMaker":false,"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Experience":[{"HQCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Title":"Marketing Creative &amp; Production manager","Level":"Manager","Department1":"Marketing","FunctionalArea":"creative","DecisionMaker":false,"Start":"February 2010","End":"Present","Duration":"6 Years 6 months","SecondaryCompanyId":"5bfbf5ae-1e08-452b-a8f1-bc06566ef029","Updated":"2016-11-24T09:46:10.797726Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Kiagus+Firmansyah+PT.+Trans+Retail+Indonesia","SourceList":[]}<br />
    {"Key":"IDaec0034a7587853d","FirstName":"Houtman","LastName":"Simanjuntak","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"0","Longitude":"0","TimeZone":"","IsCASL":false,"Updated":"2017-10-19T03:39:55","HQCompanyName":"Virtus and Varda as newly established company offering environmental solutions to the industries.","Position":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Experience":[{"Title":"Chief Executive Officer of Virtus and Varda: Environmental Solution Companies","Level":"Executive","Department1":"General","DecisionMaker":true,"Start":"September 2017","End":"Present","Duration":"1 month","Updated":"2016-09-15T15:11:54.946605Z"},{"HQCompanyId":"ID325cb8f3d7bd7ef8","Title":"President Director &amp; CEO","DecisionMaker":false,"Start":"January 1997","End":"March 2015","Duration":"18 Years 2 months","Updated":"2016-09-15T15:12:00.243412Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Houtman+Simanjuntak+Virtus+and+Varda+as+newly+established+company+offering+environmental+solutions+to+the+industries.","SourceList":[]}<br />
    {"Key":"IDaec003092517f6af","FirstName":"Nena","LastName":"Ermila","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-30T16:52:25","HQCompanyName":"PT. Asuransi Jasa Indonesia","Position":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"EmailAddress":"","HQCompanyId":"ID8ec56f05a752fc4b","Experience":[{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Optimalisasi Asset - Biro Umum","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2016","End":"Present","Duration":"4 months","SecondaryCompanyId":"ID8ec56f05a752fc4b","Updated":"2016-09-15T04:07:01.514989Z"},{"HQCompanyId":"ID8ec56f05a752fc4b","Title":"Sub Division Head","DecisionMaker":false,"Start":"October 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-09-15T04:07:02.811851Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Nena+Ermila+PT.+Asuransi+Jasa+Indonesia","SourceList":[]}<br />
    {"Key":"IDaebff7f35e83819d","FirstName":"Didik","LastName":"Wibawanto","City":"Bandar Lampung","RegionCode":"15","RegionName":"Lampung","Country":"Indonesia","Latitude":"-5.425440","Longitude":"105.258030","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-08-26T20:10:55","HQCompanyName":"Private Corporation","Position":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Experience":[{"HQCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Title":"Satellite Tracker","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"5 months","SecondaryCompanyId":"04d96802-df86-448e-a41d-88699da0d1c4","Updated":"2016-11-24T17:01:02Z"},{"Title":"Chief Information Officer","DecisionMaker":false,"Start":"September 2015","End":"Present","Duration":"11 months","Updated":"2016-11-24T17:01:02.814897Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Didik+Wibawanto+Private+Corporation","SourceList":[]}<br />
    {"Key":"IDaebff37ce8ef65d7","FirstName":"Elin-Psg","LastName":"Herliana","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T03:24:35","HQCompanyName":"Olympus Property","Position":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="20454c494e0d5053470e4845524c49414e41604f4c594d50555350524f50455254590e434f4d">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3833261+00:00","HQCompanyId":"US21d063d73525fb16","Experience":[{"HQCompanyId":"US21d063d73525fb16","Title":"Admin &amp; Kasir","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"Start":"July 2011","End":"Present","Duration":"4 Years 10 months","SecondaryCompanyId":"abc284e2-5a4a-43d4-8468-1cee07fe4fb5","Updated":"2016-09-15T03:14:55.432942Z"},{"HQCompanyId":"ID47b7a4355d2abb19","Title":"Koodinator Kantor Kas","DecisionMaker":false,"Start":"1999","End":"2007","Updated":"2016-09-15T03:14:56.636055Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Elin-Psg+Herliana+Olympus+Property","SourceList":[]}<br />
    {"Key":"IDaebfef534eac0d49","FirstName":"Yulnia","LastName":"Azriani","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-05-31T21:10:41","HQCompanyName":"PT Putra Taro Paloma (subsidiary of PT Tiga Pilar Sejahtera)","Position":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Assistant Brand Manager (Product Development)","Level":"Manager","Department1":"Marketing","DecisionMaker":false,"Start":"November 2012","End":"April 2015","Duration":"2 Years 5 months","Updated":"2016-09-15T18:39:52.681431Z"},{"Title":"Marketing Supervisor for RoC","DecisionMaker":false,"Start":"February 2010","End":"August 2011","Duration":"1 Year 6 months","Updated":"2016-09-15T18:39:54.71263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yulnia+Azriani+PT+Putra+Taro+Paloma+(subsidiary+of+PT+Tiga+Pilar+Sejahtera)","SourceList":[]}<br />
    {"Key":"IDaebfd4becc131607","FirstName":"MizanStore","LastName":".Com","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-16T21:08:41","HQCompanyName":"PT Mizan Digital Publishing","Position":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"MIZANSTORE, Toko Buku ONLINE","Level":"General","Department1":"Technology","DecisionMaker":false,"Start":"June 2013","End":"Present","Duration":"3 Years","Updated":"2016-10-27T05:59:56.131533Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=MizanStore+.Com+PT+Mizan+Digital+Publishing","SourceList":[]}<br />
    {"Key":"IDaebfb9cd79b65f90","FirstName":"Riadi","LastName":"Wirawan","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T21:10:34","HQCompanyName":"MMC Hospital","Position":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Prof dr","Level":"General","Department1":"Education","DecisionMaker":false,"End":"Present","Updated":"2016-09-15T23:51:32.140538Z"},{"Title":"Dr","DecisionMaker":false,"Start":"January 1990","End":"Present","Duration":"26 Years 4 months","Updated":"2016-09-15T23:51:32.140538Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Riadi+Wirawan+MMC+Hospital","SourceList":[]}<br />
    {"Key":"IDaebf803066abb18a","FirstName":"Anna","LastName":"Myr","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-19T21:59:30","HQCompanyName":"Smart Advert","Position":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Marketing Admin","Level":"Administrative","Department1":"General","Department2":"Marketing","DecisionMaker":false,"Start":"September 2013","End":"Present","Duration":"2 Years 9 months","Updated":"2016-10-27T19:07:16.619651Z"},{"Title":"Administration Staff","DecisionMaker":false,"Start":"November 2012","End":"Present","Duration":"3 Years 7 months","Updated":"2016-10-27T19:07:25.260324Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anna+Myr+Smart+Advert","SourceList":[]}<br />
    {"Key":"IDaebf7fa59c3f2c61","FirstName":"Herman","LastName":"Tea","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-08-26T20:11:14","HQCompanyName":"smpn 1 gununghalu","Position":"staf","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"staf","Level":"General","Department1":"General","DecisionMaker":false,"Start":"January 2004","End":"Present","Duration":"12 Years 7 months","Updated":"2016-11-25T02:05:46.310689Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Herman+Tea+smpn+1+gununghalu","SourceList":[]}<br />
    {"Key":"IDaebf6eeabefb13b1","FirstName":"Anggun","LastName":"Triadi","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-05-31T03:24:38","HQCompanyName":"Dwisapta Advertising","Position":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Strategic Planning Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"February 2011","End":"Present","Duration":"5 Years 3 months","Updated":"2016-09-15T02:10:36.579721Z"},{"HQCompanyId":"IDda4ac54b00ab8257","Title":"Account Director","DecisionMaker":false,"Start":"January 2009","End":"January 2011","Duration":"2 Years","Updated":"2016-09-15T02:10:39.970247Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Anggun+Triadi+Dwisapta+Advertising","SourceList":[]}<br />
    {"Key":"IDaebf4c097ed370c9","FirstName":"Hans","LastName":"Ferdinan","City":"Makassar","RegionCode":"38","RegionName":"South Sulawesi","Country":"Indonesia","Latitude":"-5.140000","Longitude":"119.422100","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-19T19:57:40","HQCompanyName":"PT Bank Nationalnobu Tbk","Position":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"Branch Manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"Start":"April 2014","End":"Present","Duration":"2 Years 2 months","Updated":"2016-10-27T18:52:30.413971Z"},{"HQCompanyId":"ID67b4599c6320e3f7","Title":"Marketing Manager","DecisionMaker":false,"Start":"April 2012","End":"April 2014","Duration":"2 Years","Updated":"2016-10-27T18:52:30.913991Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Hans+Ferdinan+PT+Bank+Nationalnobu+Tbk","SourceList":[]}<br />
    {"Key":"IDaebf415f88033514","FirstName":"Yessie Afriana","LastName":"Wulandari","City":"Republic of Indonesia","RegionCode":"00","RegionName":"","Country":"Indonesia","Latitude":"-5.000000","Longitude":"120.000000","TimeZone":"","IsCASL":false,"Updated":"2016-06-02T14:44:17","HQCompanyName":"PT PEMBANGUNAN PERUMAHAN (PERSERO)","Position":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"QUALITY SURVERYOR (ENGINEERING)","Level":"General","Department1":"QA","DecisionMaker":false,"Start":"January 2014","End":"Present","Duration":"2 Years 5 months","Updated":"2016-09-16T10:38:42.422819Z"},{"Title":"Civil Engineer","DecisionMaker":false,"Start":"May 2013","End":"January 2014","Duration":"8 months","Updated":"2016-09-16T10:38:46.110263Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Yessie+Afriana+Wulandari+PT+PEMBANGUNAN+PERUMAHAN+(PERSERO)","SourceList":[]}<br />
    {"Key":"IDaebf1453d77ae08c","FirstName":"Debby Niken","LastName":"Kartika W","City":"Surabaya","RegionCode":"08","RegionName":"East Java","Country":"Indonesia","Latitude":"-7.249170","Longitude":"112.750830","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-06-02T14:44:18","HQCompanyName":"Cv. BM Surabaya","Position":"IA","Level":"General","Department1":"General","DecisionMaker":false,"HQCompanyId":"","Experience":[{"Title":"IA","Level":"General","Department1":"General","DecisionMaker":false,"Start":"March 2016","End":"Present","Duration":"3 months","Updated":"2016-09-16T13:11:39.999845Z"},{"Title":"Senior Staf","DecisionMaker":false,"Start":"September 2015","End":"January 2016","Duration":"4 months","Updated":"2016-09-16T13:11:43.99979Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Debby+Niken+Kartika+W+Cv.+BM+Surabaya","SourceList":[]}<br />
    {"Key":"IDaebf000ee0827443","FirstName":"Vebi","LastName":"Nadhira","City":"Bandung","RegionCode":"30","RegionName":"West Java","Country":"Indonesia","Latitude":"-6.903890","Longitude":"107.618610","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:29","HQCompanyName":"Institut Teknologi Bandung","Position":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"HQCompanyId":"IDc5a1b238422cffa9","Experience":[{"HQCompanyId":"IDc5a1b238422cffa9","Title":"Assistant Lecturer","Level":"Administrative","Department1":"Administrative","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"IDc5a1b238422cffa9","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Vebi+Nadhira+Institut+Teknologi+Bandung","SourceList":[]}<br />
    {"Key":"IDaebed0315a11669b","FirstName":"Ratu","LastName":"Wijaksana","City":"Jakarta","RegionCode":"04","RegionName":"Jakarta","Country":"Indonesia","Latitude":"-6.214620","Longitude":"106.845130","TimeZone":"Asia/Jakarta","IsCASL":false,"Updated":"2016-03-28T06:14:26","HQCompanyName":"Smilebuilderz LLC","Position":"dentist, health team","Level":"General","Department1":"Medical","DepartmentFunction":"Dentist","DecisionMaker":false,"EmailAddress":"<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ef9d8e9b9a98af9c8286838a8d9a86838b8a9d95c18c8082">[email&#160;protected]</a>","EmailValidationStatus":"AcceptAll","EmailValidationDate":"2018-02-12T00:14:42.3207468+00:00","HQCompanyId":"US08bccec1e3cec938","Experience":[{"HQCompanyId":"US08bccec1e3cec938","Title":"dentist, health team","Level":"General","Department1":"Medical","FunctionalArea":"Dentist","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"US08bccec1e3cec938","Updated":null}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Ratu+Wijaksana+Smilebuilderz+LLC","SourceList":[]}<br />
    {"Key":"IDaebeca27f944b5ff","FirstName":"Budi","LastName":"Telly","City":"Langowan","RegionCode":"31","RegionName":"North Sulawesi","Country":"Indonesia","Latitude":"1.155300","Longitude":"124.840700","TimeZone":"Asia/Makassar","IsCASL":false,"Updated":"2016-06-01T21:27:04","HQCompanyName":"PT. Tirtakencana Tatawarna","Position":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"HQCompanyId":"ID5d4a1a67c8710963","Experience":[{"HQCompanyId":"ID5d4a1a67c8710963","Title":"Branch manager","Level":"Manager","Department1":"Operations","DecisionMaker":false,"End":"Present","SecondaryCompanyId":"ID5d4a1a67c8710963","Updated":"2016-09-16T21:17:15.12617Z"}],"Education":[],"SearchUrl":"https://www.google.com/#newwindow=1&amp;q=Budi+Telly+PT.+Tirtakencana+Tatawarna","SourceList":[]}</code></div></div><br />
    1 Million records<br />
    [Hidden Content]<br />
    <br />
    <br />
    2- Other 500Million Data<br />
    <br />
    <div class="codeblock"><div class="body" dir="ltr"><code>100M-LINKEDIN.zip<br />
    35M LINKEDIN CONTACT (WITH COMPANY) B2B.zip<br />
    2.5M US B2B Linkedin.zip<br />
    25M-Linkedin.zip<br />
    Australia Linkedin 194K.zip<br />
    Linkedin - 250 758 057.zip<br />
    Linkedin 34 Million Linkedin Emails.zip<br />
    linkedin 37 million db-16M.zip<br />
    Linkedin 45k With Full Details.zip<br />
    linkedin db 35M.zip<br />
    Linkedin DB with Profile URLS 21M.zip<br />
    Linkedin Dehased 1GB.zip<br />
    Linkedin Pakistan.zip<br />
    Linkedin sorted by Titles.zip<br />
    Linkedin-Company-Education_FR.zip<br />
    LinkedIn.rar<br />
    Linkedin2.zip<br />
    LinkedInMain 16M.zip</code></div></div><img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" alt="[Image: dqJxEFX.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/dqJxEFX.png" data-image-modal-original="https://i.imgur.com/dqJxEFX.png" data-image-modal-safe="1" /><br />
    <br />
    <br />
    <br />
    for more detail PM me on telegram: @<a href="https://raidforums.com/User-TomLiner" class="mycode_mention" target="_blank"><span class="rf_i rf_god">TomLiner</span></a><br />
    <hr class="mycode_hr" />
    Give me Positive(+) Reputation<br />
    Step by step<br />
    <br />
    1- <br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/oGBmrni.png" alt="[Image: oGBmrni.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/oGBmrni.png" data-image-modal-original="https://i.imgur.com/oGBmrni.png" data-image-modal-safe="1" /><br />
    <br />
    2- <br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/RM6c7G0.png" alt="[Image: RM6c7G0.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/RM6c7G0.png" data-image-modal-original="https://i.imgur.com/RM6c7G0.png" data-image-modal-safe="1" /><br />
    <br />
    3-<br />
    <img loading="lazy" src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/7ElzEeH.png" alt="[Image: 7ElzEeH.png]" class="mycode_img modal_image" data-image-modal="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=https://i.imgur.com/7ElzEeH.png" data-image-modal-original="https://i.imgur.com/7ElzEeH.png" data-image-modal-safe="1" /></blockquote>
    </div>
    <div class="post_meta" id="post_meta_3654672">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3654672" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    <a name="pid3655216" id="pid3655216"></a>
    <div class="post " style="" id="post_3655216">
    <div class="post__author scaleimages">
    <div class="post__author-info">
    <div class="post__user">
    <div class="post__user-profile largetext"><a href="https://raidforums.com/User-hahahahahaha"><span class="rf_noob">hahahahahaha</span></a></div>
    <a href="User-hahahahahaha" class="post__user-avatar"><img loading="lazy" src="https://cdn.raidforums.com/s/mascot/avatar/raidAvatar2-portrait.png" alt="" width="120" height="120" /></a>
    </div>
    <div class="post__user-title">New User
    <span class="post__buddy-status"><a href="javascript:void(0)" title="Offline" class="post__status post__status--offline"></a></span>
    </div>
    <div class="post__user-stars hidden-md"></div>
    <div class="post__user-badge">
    <img src="https://cdn.raidforums.com/i/RF_yfVa.png" alt="Member" title="Member" />
    <br /></div>
    </div>
    <div class="post__author-stats">
    <div class="post__stats-bit group">
    <span class="float_left">Posts</span>
    <span class="float_right">27</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Threads</span>
    <span class="float_right">2</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Joined</span>
    <span class="float_right">Jun 2020</span>
    </div>
    <div class="post__stats-bit group">
    <span class="float_left">Reputation</span>
    <span class="float_right">
    <a href="reputation.php?uid=121866143"><strong class="reputation_neutral">0</strong></a>
    </span>
    </div>
    <div class="post__user-awards"></div>
    <div class="post__user-awards"></div>
    </div>
    </div>
    <div class="post_whole">
    <div class="post_content">
    <div class="post_head">
    <div class="float_right" style="vertical-align: top">
    <strong><a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?pid=3655216#pid3655216" title="RE: LinkedIn 1Billion(1000Million) Record">#12</a></strong>
    </div>
    <span class="post_date">April 04, 2021 at 06:56 AM <span class="post_edit" id="edited_by_3655216"> </span>
    </span>
    </div>
    <div class="post_body scaleimages" id="pid_3655216">
    will need 2 more credits for this
    </div>
    <div class="post_meta" id="post_meta_3655216">
    <div class="float_right">
    </div>
    </div>
    </div>
    <div class="post_controls">
    <div class="postbit_buttons author_buttons float_left">
    </div>
    <div class="postbit_buttons post_management_buttons float_right">
    <a href="newreply.php?tid=131302&amp;replyto=3655216" title="Quote this message in a reply" class="postbit_quote postbit_mirage"><i class="fas fa-reply"></i><span>Reply</span></a>
    </div>
    </div>
    </div>
    </div>
    </div>
    </td>
    </tr>
    <tr>
    <td class="tfoot">
    <div class="hidden-sm" style="margin-left:8px">
    <strong>&laquo; <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?action=nextoldest">Next Oldest</a> | <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?action=nextnewest">Next Newest</a> &raquo;</strong>
    </div>
    </td>
    </tr>
    </table>
    </section>
    <section id="thread-bottom-navigation" class="group">
    <div class="float-left">
    <div class="pagination talign-mleft">
    <span class="pages">Pages (3):</span>
    <span class="pagination_current">1</span>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=2" class="pagination_page">2</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=3" class="pagination_page">3</a>
    <a href="Thread-SELLING-LinkedIn-1Billion-1000Million-Record?page=2" class="pagination_next">Next &raquo;</a>
    </div>
    </div>
    </section>
    <br />
    <table border="0" cellspacing="0" cellpadding="5" class="tborder table-responsive">
    <tr>
    <td class="thead" colspan="5"><strong>Possibly Related Threads&hellip;</strong></td>
    </tr>
    <tr>
    <td class="tcat"><span class="smalltext"><strong>Thread</strong></span></td>
    <td class="tcat" align="center"><span class="smalltext"><strong>Author</strong></span></td>
    <td class="tcat" align="center"><span class="smalltext"><strong>Replies</strong></span></td>
    <td class="tcat" align="center"><span class="smalltext"><strong>Views</strong></span></td>
    <td class="tcat" align="right"><span class="smalltext"><strong>Last Post</strong></span></td>
    </tr>
    <tr>
    <td class="trow1"><span class="rf_tprefix" style="background-color: #D7A847;">SELLING</span>&nbsp;<a href="Thread-SELLING-100-000-000-Linkedin-Full-Information-List">100 000 000 Linkedin Full Information List</a></td>
    <td align="center" class="trow1"><a href="https://raidforums.com/User-Silent-Plug">Silent-Plug</a></td>
    <td align="center" class="trow1"><a href="https://raidforums.com/misc.php?action=whoposted&tid=129923" onclick="MyBB.whoPosted(129923); return false;">3</a></td>
    <td align="center" class="trow1">709</td>
    <td class="trow1" align="right" style="white-space: nowrap">
    <span class="smalltext"><span title="April 08, 2021 at 08:36 AM">1 hour ago</span><br />
    <a href="Thread-SELLING-100-000-000-Linkedin-Full-Information-List?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Silent-Plug">Silent-Plug</a></span>
    </td>
    </tr>
    <tr>
    <td class="trow2"><span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook">Companies DB from linkedin or facebook</a></td>
    <td align="center" class="trow2"><a href="https://raidforums.com/User-jcanale13">jcanale13</a></td>
    <td align="center" class="trow2"><a href="https://raidforums.com/misc.php?action=whoposted&tid=132073" onclick="MyBB.whoPosted(132073); return false;">1</a></td>
    <td align="center" class="trow2">173</td>
    <td class="trow2" align="right" style="white-space: nowrap">
    <span class="smalltext"><span title="April 08, 2021 at 07:10 AM">2 hours ago</span><br />
    <a href="Thread-BUYING-Companies-DB-from-linkedin-or-facebook?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-billion025">billion025</a></span>
    </td>
    </tr>
    <tr>
    <td class="trow1"><span class="rf_tprefix" style="background-color: #2857B8;">BUYING</span>&nbsp;<a href="Thread-BUYING-I-am-collecting-user-data-of-LinkedIn-Facebook-Instagram-YouTube-etc-Profile">I am collecting user data of LinkedIn, Facebook, Instagram, YouTube,etc.Profile</a></td>
    <td align="center" class="trow1"><a href="https://raidforums.com/User-Yolandepkeener">Yolandepkeener</a></td>
    <td align="center" class="trow1"><a href="https://raidforums.com/misc.php?action=whoposted&tid=131991" onclick="MyBB.whoPosted(131991); return false;">2</a></td>
    <td align="center" class="trow1">349</td>
    <td class="trow1" align="right" style="white-space: nowrap">
    <span class="smalltext"><span title="April 07, 2021 at 10:25 PM">11 hours ago</span><br />
    <a href="Thread-BUYING-I-am-collecting-user-data-of-LinkedIn-Facebook-Instagram-YouTube-etc-Profile?action=lastpost">Last Post</a>: <a href="https://raidforums.com/User-Sandra999">Sandra999</a></span>
    </td>
    </tr>
    </table>
    <section id="thread-tools" class="group talign-pleft talign-pright">
    <div class="float-left">
    <ul class="thread-tools__options nav-columns">
    <li><a href="printthread.php?tid=131302"><i class="fas fa-print fa-fw"></i>View a Printable Version</a></li>
    </ul>
    </div>
    <div class="float-right" style="text-align: right;">
    </div>
    </section>
    <br />
    <section id="users-browsing" class="smalltext"><i class="fas fa-street-view"></i> &nbsp;Users browsing this thread: <a href="User-cynthiabgc" title="Reading&hellip; (09:37 AM)"><span class="rf_noob">cynthiabgc</span></a>, <a href="User-NewmanZhou" title="Reading&hellip; (09:01 AM)"><span class="rf_noob">NewmanZhou</span></a>, 5 Guest(s)</section>
    </main> 
    <footer id="footer">
    <div class="footer__upper">
    <div class="wrapper talign-pright talign-pleft" style="">
    <ul class="footer__general-links nav">
    <li><a href="https://raidforums.com"><i class="fa fa-home footicon"></i>Raid Forums</a></li>
    <li><a href="./misc.php?action=help&hid=24"><i class="fa fa-envelope footicon"></i>Contact Us</a></li>

    <li><a href="misc.php?action=help"><i class="fa fa-briefcase footicon"></i>Legal Policies</a></li>

    <li><a href="https://raidforums.com/misc.php?action=syndication"><i class="fa fa-rss footicon"></i>RSS Syndication</a></li>
    </ul>
    <ul class="footer__social-links nav">
    <li><a href="https://rf.ws/keybase" target="_blank" class="footer__keybase"><i class="fab fa-keybase"></i></a></li>
    <li><a href="https://rf.ws/telegram" target="_blank" class="footer__telegram"><i class="fab fa-telegram-plane"></i></a></li>
    <li><a href="https://rf.ws/facebook" target="_blank" class="footer__facebook"><i class="fab fa-facebook-f"></i></a></li>
    <li><a href="https://rf.ws/youtube" target="_blank" class="footer__youtube"><i class="fab fa-youtube"></i></a></li>
    <li><a href="https://rf.ws/twitter" target="_blank" class="footer__twitter"><i class="fab fa-twitter"></i></a></li>
    </ul>
    </div>
    </div>
    <div class="footer__lower">
    <div class="wrapper talign-pright talign-pleft" style="">
    <div class="footer__datetime"><strong>Current time:</strong> April 08, 2021, 09:38 AM</div>
    <div class="footer__copyright">
    Powered By <a href="https://raidforums.com/User-Omnipotent" target="_blank">Omnipotent</a>, &copy; <a href="//www.dmca.com/Protection/Status.aspx?ID=c9c968fb-e6df-4653-ac37-89cc29dea488&refurl=https://raidforums.com/" target="_blank">2015-2021</a>
    </div>
    </div>
    </div>
    </footer>
    </div> 
    <div id="guest-alert" class="guest-alert rounded hidden-md" style="display:none">
    <div class="guest-alert__head">Guest Alert!</div>
    <a href="member.php?action=register" class="smalltext">Join today to experience everything we have to offer such as Leaks, Database Breaches, Adult Content and much more.</a>
    <a nohref title="Close Welcome Message" class="guest-alert__close hide-parent-onclick">x</a>
    </div>
    <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="https://cdn.raidforums.com/jscripts/raid.js?v=1.3" defer></script>
    <div id="scrolltop" title="Jump Up" style="display:none"></div>
    <script src="https://cdn.raidforums.com/jscripts/raid_scrolltop.js" async defer></script>
    <div id="thread_modes_popup" class="popup_menu" style="display: none;"><div class="popup_item_container"><a href="showthread.php?mode=linear&amp;tid=131302&amp;pid=3649114#pid3649114" class="popup_item">Linear Mode</a></div><div class="popup_item_container"><a href="showthread.php?mode=threaded&amp;tid=131302&amp;pid=3649114#pid3649114" class="popup_item">Threaded Mode</a></div></div>
    <script type="text/javascript">
    	// <!--
    		if(use_xmlhttprequest == "1")
    		{
    			$("#thread_modes").popupMenu();
    		}
    	// -->
    	</script>
    <script type="text/javascript">
    		var thread_deleted = "";
    		if(thread_deleted == "1")
    		{
    			$("#quick_reply_form, .new_reply_button, .thread_tools, .inline_rating").hide();
    			$("#moderator_options_selector option.option_mirage").attr("disabled","disabled");
    		}
    	</script>
    </body>
    </html>
    '''
    content_url = 'https://raidforums.com/Thread-SELLING-LinkedIn-1Billion-1000Million-Record'
    xp = create_response(content_url,content_html)
    imgs = xp('//div[@class="post_body scaleimages"]/img[@loading="lazy"]/@src')
    for img in imgs:
        print(img.extract())

    content = xp('string(//div[@class="post_body scaleimages"])')
    print(content.extract_first())
if __name__ == '__main__':
    parse_content()