STARTING_YEAR = 2015
N_YEARS = 9
N_DAYS = 5

with open("README.md", "a") as f:
    for year in range(STARTING_YEAR + N_YEARS - 1, STARTING_YEAR - 1, -1):
        f.writelines([f"\n### [{year}]({year})\n\n",
                      "|  Day  | Part one | Part two | Language(s) |\n",
                      "| :---: | :------: | :------: | :---------: |\n"])
        rows = ["| [{}]({}/day_{:02}.py) | | | python |\n"
                .format(day, year, day)
                for day in range(1, N_DAYS + 1)]
        f.writelines(rows)
