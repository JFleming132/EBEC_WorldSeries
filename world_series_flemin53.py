"""
Author: Joseph Fleming, flemin53@purdue.edu
Assignment: mm.n - World Series
Date: 11/13/2021

Description:
    This program initializes a database of years and the baseball team that won the world series that year.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

# Import modules below this line (starting with unit 6).


# Write new functions below this line (starting with unit 4).
def load_winners_data():
    winners = {}
    totalWins = {}
    with open("WorldSeriesWinners.txt", "r") as data:
        file = data.read()
    file = file.split("\n")
    while "" in file:
        file.remove("")
    for year in range(1903,2021):
        if year < 1904:
            winners[year]=file[year-1903]
        if year == 1904:
            continue
        if year < 1994 and year > 1904:
            winners[year]=file[year-1904]
        if year == 1994:
            continue
        if year > 1994:
            winners[year] = file[year-1905]
    allTeams = list(set(file))
    for team in allTeams:
        totalWins[team] = file.count(team)
    return totalWins, winners

def main():
    totalWins, winners = load_winners_data()
    year = int(input('Enter a year in the range 1903 -- 2020: '))
    if year <= 1903 or year >= 2020:
        print(f"  Data for the year {year} is not included in this system.")
    elif winners.get(year) == None:
        print(f"  The World Series wasn't played in the year {year}.")
    elif winners.get(year) != "Not Played":
        print(f'  The {winners[year]} won the World Series in {year}.')
        print(f'  They have won the World Series {totalWins[winners[year]]} times.')



if __name__ == '__main__':
    main()
