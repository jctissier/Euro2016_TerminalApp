from flask import Flask, request, render_template, redirect, url_for
import praw
import re
import requests
from bs4 import BeautifulSoup
import random
import time
from app.content_management import content, league, user_agent

TAG_DICT = content()
leagues = league()
agent = user_agent()
agent = random.choice(agent)
r = praw.Reddit(user_agent=agent)


app = Flask(__name__)


@app.route("/")
@app.route("/live", methods=['GET'])
def live_games():
    html = requests.get("http://www.espnfc.us/scores")
    soup = BeautifulSoup(html.content, "lxml")
    live = []
    count = 0
    title = "Live Matches"
    live_active = True
    no_matches = False
    fixtures_table = False
    live_streams = False
    redirect = 'http://footylinks.herokuapp.com/live-match-details?gameid='

    print(soup.find_all("div",{"data-league-id":"9"}))
    if len(soup.find_all("div", {"class": "scorebox-container live"})) != 0:
        for x in range(len(soup.find_all("div",{"data-league-id":"9"}))):
            team_name = soup.find_all("div", {"class": "scorebox-container live"})[x].text
            team_img = soup.find_all("div", {"class": "scorebox-container live"})[x]
            if len(team_img.div.div.div.find_all("img")) != 0:
                children = team_img.div.div.find_all("img")
                append_to = [team.replace("\n", " ").strip() for team in team_name.split("\n\n") if team is not ""]
                if append_to[5] != "Game Details":
                    del append_to[5]
                append_to.append(children[0].get('src'))
                append_to.append(children[1].get('src'))
                container = soup.find_all("div", {"class": "scorebox-container live"})[x]
                container = container.find_all("a", {"data-no-ajaxify": "true"})
                detail_link = container[0].get('href')
                detail_link = detail_link[detail_link.index("=") + 1:]
                print(detail_link)
                append_to.append(detail_link)
                # try:
                #     container = soup.find_all("div", {"class": "scorebox-container live"})
                #     detail_link = container[x].find_all("a")[0].get('href')
                #     print(detail_link)
                #     detail_link = detail_link[detail_link.index("=") + 1:]
                #     append_to.append(detail_link)
                # except:
                #     print("No game Id")
                #     pass
                live.append(append_to)

    print(live)
    if len(live) == 0:
        no_matches = True
        fixtures_table = []
        pre_link = "https://www.theguardian.com/football/"
        post_link = "/fixtures"
        leagues = ["championsleague", "uefa-europa-league", "premierleague", "laligafootball"]

        for loop in range(len(leagues)):
            html = requests.get(pre_link + leagues[loop] + post_link)
            soup = BeautifulSoup(html.content, "lxml")
            try:
                next_fixtures = soup.find("div", {"class": "football-matches__day"})
                name = next_fixtures.find("caption", {"class": "table__caption table__caption--top"}).a.text
                date = next_fixtures.find("div", {"class": "date-divider"}).text
                games = next_fixtures.find("tbody").find_all("tr")
            except IndexError:
                break
            y = 0
            if len(games) >= 2:
                size = True
            else:
                size = False
            try:
                for x in range(2):
                    game_time = games[x].td.text.strip()
                    logos = next_fixtures.find_all("span", {"class": "team-crest"})
                    img1 = logos[y].get("style")
                    img1 = img1[img1.index("(") + 1:img1.index(")")]
                    teams = next_fixtures.find_all("span", {"class": "team-name__long"})
                    home_team = teams[y].text.strip()
                    away_team = teams[y + 1].text.strip()
                    img2 = logos[y + 1].get("style")
                    img2 = img2[img2.index("(") + 1:img2.index(")")]
                    y += 2
                    if x == 0:
                        fixtures_table.append([[name, date, size],[game_time, img1, home_team, away_team, img2]])
                    else:
                        fixtures_table.append([[False, False, size], [game_time, img1, home_team, away_team, img2]])
                    continue
            except IndexError:
                print("Only 1 game")

    else:
        subreddit_streams = r.get_subreddit('soccerstreams')
        for submission in subreddit_streams.get_hot(limit=20):
            if "vs" in submission.title:
                live_streams = True
                count += 1
    print(fixtures_table)

    return render_template("live.html", title=title, live_active=live_active, live=live,
                           no_matches=no_matches, home_page=True, fixtures_table=fixtures_table,
                           live_streams=live_streams, count=count )


@app.route("/live-match-details", methods=['GET'])
def live_details():
    pre_link = 'http://www.espnfc.us/match?gameId='
    full_link = ""
    error = True
    header_data = []
    home_data = []
    away_data = []
    goals_home = []
    goals_away = []
    size = 0
    game_id = ""

    if request.args.get('gameid', None) is not None:
        error = False
        game_id = request.args.get('gameid', None)
        print(game_id)
        full_link = pre_link + str(game_id)
        html = requests.get(full_link)
        soup = BeautifulSoup(html.content, "lxml")
        try:
            match_detail_header = soup.find("div", {"class": "game-details header"}).text.strip()
            main_detail_format = soup.find_all("div", {"class": "competitors sm-score"})
            # Data for left
            team_away = main_detail_format[0].div.div
            away_team_name = team_away.div.div.span.text
            away_team_logo = team_away.picture.img.get("data-default-src")
            away_team_score = team_away.find("span", {"class": "score icon-font-after"}).text.strip()
            away_data.append([away_team_name, away_team_logo, away_team_score])
            # Data for middle
            game_status = main_detail_format[0].find("div", {"class": "game-status"}).text.split("\n")
            game_status = [game for game in game_status if len(game) != 0]
            if 1 < len(game_status) <= 2:
                live_time = game_status[0]
                aggregate = game_status[1]
                header_data.append([match_detail_header, live_time, aggregate])
            elif len(game_status) == 1:
                live_time = game_status[0]
                header_data.append([match_detail_header, live_time, False])
            # Data for right
            home_team = main_detail_format[0].div.find_next_sibling().find_next_sibling().div
            home_team_score = home_team.div.span.text.strip()
            home_team_logo = home_team.picture.img.get("data-default-src")
            home_team_name = home_team.find("span", {"class": "long-name"}).text
            home_data.append([home_team_name, home_team_logo, home_team_score])
            # Data for bottom
            try:
                try:
                    for x in range(10):
                        print(soup.find("div", {"class": "team away"}).div.ul)
                        if soup.find("div", {"class": "team away"}).div.ul.get("data-event-type") == "redCard":
                            print("Red card")
                            goal_details_away = soup.find("div", {"class": "team away"}).div.ul.find_all("li")[
                                x].text.strip().split()
                            goal_details_away.insert(0, "Red Card: ")
                            goals_away.append(goal_details_away)
                        else:
                            goal_details_away = soup.find("div", {"class": "team away"}).div.ul.find_all("li")[
                                x].text.strip().split()
                            goals_away.append(goal_details_away)
                except AttributeError:
                    pass
            except IndexError:
                pass

            try:
                for x in range(10):
                    try:
                        goal_details_home = soup.find("div", {"class": "team home"}).div.ul.find_all("li")[
                            x].text.strip().split()
                        goals_home.append(goal_details_home)
                    except AttributeError:
                        pass
            except IndexError:
                pass
        except IndexError:
            print("Index Error")
            return redirect(url_for("livestreams"))

    if len(goals_home) > len(goals_away):
        size = len(goals_home)
    else:
        size = len(goals_away)
    print(size)
    print(header_data)
    print(home_data)
    print(away_data)
    print(goals_home)
    print(goals_away)
    print(error)

    return render_template("live-match-details.html", error=error, header_data=header_data, home_data=home_data,
                           away_data=away_data, goals_home=goals_home, goals_away=goals_away, size=size,
                           home_page=False, game_id=game_id)


@app.route("/highlights", methods=['GET', 'POST'])
def match_highlights():
    filter_size = 100
    if request.method == 'POST':
        match_name = request.form['match_name']

    elif request.method == 'GET':
        match_name = ""

    if request.args.get('tag', None) is not None:
        match_name = request.args.get('tag', None)

    all_match_titles = []
    all_highlights_url = []
    all_match_dates = []
    all_highlights_titles = []
    all_highlights_href = []
    highlights_active = "true"
    title = "Football Highlights"
    subreddit = r.get_subreddit("footballhighlights")

    for submission in subreddit.get_hot(limit=int(filter_size)):
        if re.search(match_name, submission.title, re.IGNORECASE):
            if "vs" in submission.title:
                if "request" not in submission.title:
                    date = submission.title[-11:].title()
                    game_name = submission.title[:-13].title()
                    html_tag = submission.selftext_html
                    try:
                        soup = BeautifulSoup(html_tag, "lxml")
                        tag_href = soup.a['href']
                        tag_text = soup.a.text
                    except TypeError:
                        print("Caught a Type Error")

                    for highlight in leagues:
                        if highlight in submission.title:
                            if "–" in game_name:
                                all_match_titles.append(game_name[:game_name.index('–')])
                            elif "-" in game_name:
                                all_match_titles.append(game_name[:game_name.index('-')])
                            elif "," in game_name:
                                all_match_titles.append(game_name[:game_name.index(',')])
                            all_highlights_url.append(submission.url)
                            all_match_dates.append(date)
                            all_highlights_href.append(tag_href)
                            all_highlights_titles.append(tag_text)

    zipped_data = zip(all_match_titles, all_highlights_url, all_match_dates, all_highlights_href,
                      all_highlights_titles)

    return render_template('highlights.html', match_name=match_name, zipped_data=zipped_data, TAG_DICT=TAG_DICT,
                           highlights_active=highlights_active, title=title, home_page=False)


@app.route("/livestreams", methods=['GET'])
def livestreams():
    streams = []
    streams_active = "true"
    title = "Live Streams"
    current_time = time.gmtime()
    current_time = time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)
    subreddit = r.get_subreddit('soccerstreams')
    no_matches = False
    date_regex = r"\[(.*?)\]"
    redirect = ""

    for submission in subreddit.get_hot(limit=20):
        if "vs" in submission.title:
            try:
                game_title = submission.title[submission.title.index(']') + 1:].lstrip().replace(":","")
                direct = game_title.split("vs")
                redirect = direct[0].strip()
                dates = re.findall(date_regex, submission.title)
                streams.append(["".join(dates), game_title, submission.url, redirect])
            except ValueError:
                print("Live Stream didn't have the correct format")
                continue

    print(streams)

    if len(streams) == 0:
        no_matches = True

    return render_template("livestreams.html", streams_active=streams_active, title=title, streams=streams,
                           current_time=current_time, no_matches=no_matches, home_page=False, redirect=redirect)


@app.route("/links", methods=['GET', 'POST'])
def stream_links():
    regex = r"\[(.*?)\]\((.*?)\)"
    streams_active = "true"
    links = []
    game_title = ""
    kick_off = ""
    nation = ""
    competition = ""
    redirect = ""
    no_games = True
    current_time = time.gmtime()
    current_time = time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)

    if request.args.get('stream', None) is not None:
        stream_name = request.args.get('stream', None)
        subreddit = r.get_subreddit('soccerstreams')
        for submission in subreddit.get_hot(limit=20):
            if re.search(stream_name, submission.title, re.IGNORECASE):
                details = submission.selftext_html
                soup = BeautifulSoup(details, "lxml")
                kick_off = soup.find_all("p")[1].text
                competition = soup.find_all("p")[2].text
                nation = soup.find_all("p")[3].text
                comments = submission.comments
                for comment in comments[0:20]:
                    matches = re.findall(regex, comment.body)
                    for link in matches:
                        if "soccerstreams" not in link[1]:
                            if "old version" not in link[0]:
                                game_title = submission.title[submission.title.index(']') + 1:].lstrip().replace(":","")
                                direct = game_title.split("vs")
                                redirect = direct[0].strip()
                                links.append([submission.url, link[0], link[1]])
                                no_games = False

    print(links)

    return render_template("links.html", streams_active=streams_active, links=links, home_page=False,
                           game_title=game_title, no_games=no_games,title=game_title, kick_off=kick_off, nation=nation,
                           competition=competition, redirect=redirect, current_time=current_time)


@app.route("/standings", methods=['GET'])
def stats():
    pre_link = "http://ca.soccerway.com/"
    epl = "national/england/premier-league/20162017/regular-season/r35992/tables/?ICID=PL_3N_03"
    title = "Football Standings"
    stats_active = True
    stats_data = []
    premier_league = True           # determine active tab
    bundesliga = False
    ligue1 = False
    liga = False
    seriea = False

    league_name = epl                # default stats table

    if request.args.get('league', None) is not None:
        link_league = request.args.get('league', None)
        if link_league == "epl":
            print("Yes")
            pass
        elif link_league == "bundesliga":
            bundesliga = True
            premier_league = False
            league_name = 'national/germany/bundesliga/20162017/regular-season/r35823/tables/?ICID=PL_3N_03'
        elif link_league == "ligue1":
            ligue1 = True
            premier_league = False
            league_name = 'national/france/ligue-1/20162017/regular-season/r35879/?ICID=TN_02_01_05'
        elif link_league == "liga":
            liga = True
            premier_league = False
            league_name = 'national/spain/primera-division/20162017/regular-season/r35880/?ICID=TN_02_01_03'
        elif link_league == "seriea":
            seriea = True
            premier_league = False
            league_name = 'national/italy/serie-a/20162017/regular-season/r36003/?ICID=SN_01_03'

    html = requests.get(pre_link + league_name)
    soup = BeautifulSoup(html.content, "lxml")
    try:
        for x in range(0, 21):
            team_name = soup.find_all("td", {"class": "text team large-link"})[x].text
            match_played = soup.find_all("td", {"class": "number total mp"})[x].text
            wins = soup.find_all("td", {"class": "number total won total_won"})[x].text
            draws = soup.find_all("td", {"class": "number total drawn total_drawn"})[x].text
            losses = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
            goal_diff = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
            points = soup.find_all("td", {"class": "number points"})[x].text
            if team_name or match_played or wins or draws or losses or goal_diff or points is not None:
                stats_data.append([str(x+1)+".", team_name.replace(":", "").lstrip(), match_played, wins, draws, losses,
                                  goal_diff, points])
    except IndexError:
        print("Caught Index Error, table has less than 20 teams")

    return render_template("stats.html", title=title, stats_active=stats_active, stats=stats_data,
                           premier_league=premier_league, bundesliga=bundesliga, ligue1=ligue1, liga=liga,
                           seriea=seriea, home_page=False)


@app.route("/topscorer", methods=['GET'])
def topscorer():
    pre_link = "http://ca.soccerway.com/"
    epl = "national/england/premier-league/20162017/regular-season/r35992/players/?ICID=PL_3N_04"
    title = "Player Stats"
    stats_active = True
    topscorer_list = []
    premier_league = True
    bundesliga = False
    ligue1 = False
    liga = False
    seriea = False
    league_name = epl                # default stats table

    if request.args.get('topscorer', None) is not None:
        link_league = request.args.get('topscorer', None)
        if link_league == "epl":
            pass
        elif link_league == "bundesliga":
            bundesliga = True
            premier_league = False
            league_name = 'national/germany/bundesliga/20162017/regular-season/r35823/players/?ICID=PL_3N_04'
        elif link_league == "ligue1":
            ligue1 = True
            premier_league = False
            league_name = 'national/france/ligue-1/20162017/regular-season/r35879/players/?ICID=PL_3N_04'
        elif link_league == "liga":
            liga = True
            premier_league = False
            league_name = 'national/spain/primera-division/20162017/regular-season/r35880/players/?ICID=PL_3N_04'
        elif link_league == "seriea":
            seriea = True
            premier_league = False
            league_name = 'national/italy/serie-a/20162017/regular-season/r36003/players/?ICID=PL_3N_04'

    html = requests.get(pre_link + league_name)
    soup = BeautifulSoup(html.content, "lxml")
    try:
        for x in range(0, 20):
            player_name = soup.find_all("td", {"class": "player large-link"})[x].text
            team_name = soup.find_all("td", {"class": "team large-link"})[x].text
            goals_count = soup.find_all("td", {"class": "number goals"})[x].text
            penalties = soup.find_all("td", {"class": "number penalties"})[x].text
            topscorer_list.append([str(x+1)+".", player_name, team_name, penalties, goals_count])
    except IndexError:
        print("Index Error, less than 20 players")

    return render_template("topscorer.html", title=title, stats_active=stats_active, topscorer_list=topscorer_list,
                           premier_league=premier_league, bundesliga=bundesliga, ligue1=ligue1, liga=liga,
                           seriea=seriea, home_page=False )


@app.route("/match-details", methods=['GET'])
def match_details():
    pre_link = "http://ca.soccerway.com/"
    epl = "national/england/premier-league/20162017/regular-season/r35992/?ICID=PL_3N_02"
    title = "Match Details"
    stats_active = True
    details = []
    premier_league = True
    bundesliga = False
    ligue1 = False
    liga = False
    seriea = False
    league_name = epl  # default stats table

    if request.args.get('details', None) is not None:
        link_league = request.args.get('details', None)
        if link_league == "epl":
            pass
        elif link_league == "bundesliga":
            bundesliga = True
            premier_league = False
            league_name = 'national/germany/bundesliga/20162017/regular-season/r35823/?ICID=PL_3N_02'
        elif link_league == "ligue1":
            ligue1 = True
            premier_league = False
            league_name = 'national/france/ligue-1/20162017/regular-season/r35879/?ICID=PL_3N_02'
        elif link_league == "liga":
            liga = True
            premier_league = False
            league_name = 'national/spain/primera-division/20162017/regular-season/r35880/?ICID=PL_3N_02'
        elif link_league == "seriea":
            seriea = True
            premier_league = False
            league_name = 'national/italy/serie-a/20162017/regular-season/r36003/?ICID=PL_3N_02'

    for x in reversed(range(0, 10, 1)):
        data = match_details_helper(x=x, league_name=pre_link + league_name)
        print(data)
        if data is not None:
            details.append(data)
        else:
            print("None Type found ")

    return render_template("match-details.html", title=title, stats_active=stats_active, details=details,
                           premier_league=premier_league, bundesliga=bundesliga, ligue1=ligue1, liga=liga,
                           seriea=seriea, home_page=False )


def match_details_helper(x, league_name):
    html = requests.get(league_name)
    soup = BeautifulSoup(html.content, "lxml")
    try:
        day = soup.find_all("td", {"class": "day no-repetition"})[x].text
        date = soup.find_all("td", {"class": "date no-repetition"})[x].text
        team_a = soup.find_all("td", {"class": "team team-a "})[x].text
        score = soup.find_all("td", {"class": "score-time score"})[x].text
        team_b = soup.find_all("td", {"class": "team team-b "})[x].text
        game_details = [day, date, team_a.strip(), score.strip(), team_b.strip()]

        get_href = soup.find_all("td", {"class": "events-button button first-occur"})[x]
        for link in soup.find_all('a'):
            if link in get_href:
                html_2 = requests.get('http://ca.soccerway.com/' + link.get('href'))
                soup = BeautifulSoup(html_2.content, "lxml")
                try:
                    for y in range(0, 15):
                        player_left = soup.find_all("td", {"class": "player player-a"})[y].text
                        detail_score = soup.find_all("td", {"class": "event-icon"})[y].text
                        player_right = soup.find_all("td", {"class": "player player-b"})[y].text
                        if hasattr(player_left, 'property'):  # Avoids attribute exceptions
                            pass
                        if hasattr(player_right, 'property'):  # Avoids attribute exceptions
                            pass
                        game_details.append([player_left.strip(), detail_score, player_right.strip()])
                except IndexError:
                        continue

        return game_details
    except IndexError:
        pass


@app.route("/fixtures",  methods=['GET'])
def fixtures():
    pre_link = "https://www.theguardian.com/football/"
    post_link = "/fixtures"
    leagues_links = ["premierleague", "laligafootball", "bundesligafootball", "serieafootball", "ligue1football"]
    title = "League Fixtures"
    stats_active = True
    fixtures_data = []
    premier_league = True
    bundesliga = False
    ligue1 = False
    liga = False
    seriea = False
    league_name = leagues_links[0]

    if request.args.get('fixtures', None) is not None:
        link_league = request.args.get('fixtures', None)
        if link_league == "epl":
            pass
        elif link_league == "bundesliga":
            bundesliga = True
            premier_league = False
            league_name = leagues_links[2]
        elif link_league == "ligue1":
            ligue1 = True
            premier_league = False
            league_name = leagues_links[4]
        elif link_league == "liga":
            liga = True
            premier_league = False
            league_name = leagues_links[1]
        elif link_league == "seriea":
            seriea = True
            premier_league = False
            league_name = leagues_links[3]

    html = requests.get(pre_link + league_name + post_link)
    soup = BeautifulSoup(html.content, "lxml")
    next_fixtures = soup.find("div", {"class": "football-matches__day"})
    date = next_fixtures.find("div", {"class": "date-divider"}).text
    games = next_fixtures.find("tbody").find_all("tr")
    y = 0
    try:
        for x in range(10):
            game_time = games[x].td.text.strip()
            logos = next_fixtures.find_all("span", {"class": "team-crest"})
            img1 = logos[y].get("style")
            img1 = img1[img1.index("(") + 1:img1.index(")")]
            teams = next_fixtures.find_all("span", {"class": "team-name__long"})
            home_team = teams[y].text.strip()
            away_team = teams[y + 1].text.strip()
            img2 = logos[y + 1].get("style")
            img2 = img2[img2.index("(") + 1:img2.index(")")]
            if x == 0:
                fixtures_data.append([date[:-4], game_time, img1, home_team, away_team, img2])
            else:
                fixtures_data.append([False, game_time, img1, home_team, away_team, img2])
            y += 2
            continue
    except IndexError:
        if x < 2:
            next_games = next_fixtures.findNext("div", {"class": "football-matches__day"})
            date = next_games.find("div", {"class": "date-divider"}).text
            games = next_games.find("tbody").find_all("tr")
            y = 0
            try:
                for x in range(6):
                    game_time = games[x].td.text.strip()
                    logos = next_games.find_all("span", {"class": "team-crest"})
                    img1 = logos[y].get("style")
                    img1 = img1[img1.index("(") + 1:img1.index(")")]
                    teams = next_games.find_all("span", {"class": "team-name__long"})
                    home_team = teams[y].text.strip()
                    away_team = teams[y + 1].text.strip()
                    img2 = logos[y + 1].get("style")
                    img2 = img2[img2.index("(") + 1:img2.index(")")]
                    if x == 0:
                        fixtures_data.append([date[:-4], game_time, img1, home_team, away_team, img2])
                    else:
                        fixtures_data.append([False, game_time, img1, home_team, away_team, img2])
                    y += 2
                    continue
            except IndexError:
                print("Done")

    return render_template("fixtures.html", title=title, stats_active=stats_active, fixtures_data=fixtures_data,
                           premier_league=premier_league, bundesliga=bundesliga, ligue1=ligue1, liga=liga,
                           seriea=seriea, home_page=False)


@app.errorhandler(404)
def page_not_found(e):
    title = "404 Error"
    return render_template('404.html', title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    title = "500 Error"
    return render_template('404.html', title=title), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, threaded=True)


