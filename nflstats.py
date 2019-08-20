from tkinter import *
from tkinter.ttk import *
import re
from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule
from sportsreference.nfl.boxscore import Boxscores
from sportsreference.nfl.boxscore import Boxscore

team_elo_list = []


class NflTeam:
    name = ""
    abbrev = ""
    elo = 1500

    def __init__(self, name, abbreviation, elo):
        self.name = name
        self.abbreviation = abbreviation
        self.elo = elo


class NflStatsGUI:
    def __init__(self, master):
        self.master = master
        master.title("STILL TESTING STUFF OUT :)")
        master.geometry("750x750")

        team_dict = {'Kansas City Chiefs': 'KAN', 'Los Angeles Rams': 'RAM', 'New Orleans Saints': 'NOR',
                     'New England Patriots': 'NWE', 'Indianapolis Colts': 'CLT', 'Pittsburgh Steelers': 'PIT',
                     'Seattle Seahawks': 'SEA', 'Los Angeles Chargers': 'SDG', 'Chicago Bears': 'CHI',
                     'Atlanta Falcons': 'ATL', 'Houston Texans': 'HTX', 'Tampa Bay Buccaneers': 'TAM',
                     'Baltimore Ravens': 'RAV', 'Carolina Panthers': 'CAR', 'Green Bay Packers': 'GNB',
                     'New York Giants': 'NYG', 'Cincinnati Bengals': 'CIN', 'Philadelphia Eagles': 'PHI',
                     'Minnesota Vikings': 'MIN', 'Cleveland Browns': 'CLE', 'San Francisco 49ers': 'SFO',
                     'Detroit Lions': 'DET', 'Miami Dolphins': 'MIA', 'Tennessee Titans': 'OTI',
                     'Oakland Raiders': 'RAI', 'Washington Redskins': 'WAS', 'Buffalo Bills': 'BUF',
                     'Jacksonville Jaguars': 'JAX', 'Arizona Cardinals': 'CRD', 'Denver Broncos': 'DEN'
                     }

        # GUI ELEMENTS
        self.label = Label(master, text="Select a team:")
        self.team_combo = Combobox(master, values=list(team_dict.keys()))
        self.year_label = Label(master, text="Enter a year:")
        self.year_entry = Entry(master, width=4)

        self.sched_button = Button(master, text="Get Schedule", command=lambda: self.schedule(self.team_combo.get(),
                                                                                              self.year_entry.get(),
                                                                                              team_dict))
        self.close_button = Button(master, text="Close", command=master.quit)
        self.charger_button = Button(master, text="Chargers", command=self.chargers)
        self.select_week = Button(master, text="WEEK TEST", command=lambda: self.week_schedule(2018, 1, team_dict))
        self.gen_elo_button = Button(master, text="Generate Elo Rankings", command=lambda: self.generate_elo(team_dict))
        self.output_text = Text(master, height=30, width=50)

        # GRID LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.team_combo.grid(row=0, column=1)
        self.year_label.grid(row=1, column=0, sticky=W)
        self.year_entry.grid(row=1, column=1, sticky=E)
        self.sched_button.grid(row=2, column=1, sticky=E)
        self.close_button.grid(row=5, column=0)
        self.charger_button.grid(row=3, column=0)
        self.select_week.grid(row=6, column=0)
        self.gen_elo_button.grid(row=7, column=0)
        self.output_text.grid(row=8, column=0)

    # TEST METHOD
    def chargers(self):
        for team in Teams('2018'):
            schedule = team.schedule
            if 'Chargers' in team.name:
                print(team.name)
                for game in schedule:
                    print(str(game.date) + ": PF: ", str(game.points_scored) + " | PA: ",
                          str(game.points_allowed) + " vs. ", game.opponent_name)

    def schedule(self, teamname, year, team_dict):
        team_abbrev = ''
        for key, value in team_dict.items():
            if key == teamname:
                team_abbrev = team_dict[key]
        self.output_text.delete(1.0, "end-1c")
        self.output_text.insert("end-1c", teamname + " " + year + " Schedule:\n")
        team_schedule = Schedule(team_abbrev, year)
        for game in team_schedule:
            self.output_text.insert("end-1c", game.date + ": " + game.opponent_name + "\n")

    def week_schedule(self, year, week, team_dict):
        winner_name = ""
        loser_name = ""
        p = re.compile("'(2018\\d+\\w+)'")
        selected_week = Boxscores(week, year)
        game_codes = p.findall(str(selected_week.games.values()))

        self.output_text.delete(1.0, "end-1c")
        for code in game_codes:
            game_data = Boxscore(code)
            for name, abbrev in team_dict.items():
                if abbrev == game_data.winning_abbr:
                    winner_name = name
            for name, abbrev in team_dict.items():
                if abbrev == game_data.losing_abbr:
                    loser_name = name
            self.output_text.insert("end-1c", winner_name + " " + str(game_data.home_points) + " " +
                                    loser_name + " " + str(game_data.away_points) + "\n")

    def generate_elo(self, team_dict):
        temp_name = ""
        p = re.compile("'(2018\\d+\\w+)'")
        selected_week = Boxscores(1, 2018)
        game_codes = p.findall(str(selected_week.games.values()))

        self.output_text.delete(1.0, "end-1c")
        for code in game_codes:
            game_data = Boxscore(code)
            for name, abbrev in team_dict.items():
                if abbrev == game_data.winning_abbr:
                    temp_name = name
            new_team = NflTeam(temp_name, game_data.winning_abbr, 1500)
            team_elo_list.append(new_team)

            for name, abbrev in team_dict.items():
                if abbrev == game_data.losing_abbr:
                    temp_name = name
            new_team = NflTeam(temp_name, game_data.losing_abbr, 1500)
            team_elo_list.append(new_team)

        for i in team_elo_list:
            if i.name == "New England Patriots":
                i.elo = 1700
        team_elo_list.sort(key=lambda x: x.elo, reverse=True)
        for z in team_elo_list:
            self.output_text.insert("end-1c", str(z.name) + " " + str(z.abbreviation) + " " + str(z.elo) + '\n')



root = Tk()
my_gui = NflStatsGUI(root)
root.mainloop()

######################################################################################
# Adds teams and their total yards to a dictionary and prints them in ordered form
######################################################################################
# from sportsreference.nfl.teams import Teams
# Ordered = {}
# for team in Teams('2018'):
#     Ordered[team.yards] = team.name
#
# for key in sorted(Ordered.keys(), reverse=True):
#     print(str(key) + ' ' + Ordered[key])


# from sportsreference.nfl.teams import Teams
# from sportsreference.nfl.roster import Player
#
# for team in Teams('2018'):
#     for player in team.roster.players(slim=False):
#         for i in player:
#             plyr = Player(i.player_id)
#             # if plyr.passing_yards > 100:
#             #     print(plyr.name + plyr.passing_yards)
#             print(plyr.name + str(plyr.passing_yards))

# from sportsreference.nfl.roster import Player
#
# sqn = Player('ZuerGr00')
# print(sqn.fourty_to_fourty_nine_yard_field_goal_attempts)
# print(sqn.fourty_to_fourty_nine_yard_field_goals_made)
