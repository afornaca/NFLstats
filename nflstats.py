
from tkinter import *
from tkinter.ttk import *
from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule


class NflStatsGUI:
    def __init__(self, master):
        self.master = master
        master.title("NFL SHIT HOMIE")
        master.geometry("500x500")

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

        # GRID LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.team_combo.grid(row=0, column=1)
        self.year_label.grid(row=1, column=0, sticky=W)
        self.year_entry.grid(row=1, column=1, sticky=E)
        self.sched_button.grid(row=2, column=1, sticky=E)
        self.close_button.grid(row=5, column=0)
        self.charger_button.grid(row=3, column=0)

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
        print(teamname, year, 'schedule:')
        team_schedule = Schedule(team_abbrev, year)
        for game in team_schedule:
            print(game.date + ': ', game.opponent_name)


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
