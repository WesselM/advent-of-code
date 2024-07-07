import os

STARTING_YEAR = 2015
N_YEARS = 9
N_DAYS = 5

for year in range(STARTING_YEAR, STARTING_YEAR + N_YEARS):
    year_path = f"./{year}"
    examples_path = os.path.join(year_path, "examples")
    input_path = os.path.join(year_path, "input")

    os.makedirs(year_path, exist_ok=True)
    os.makedirs(examples_path, exist_ok=True)
    os.makedirs(input_path, exist_ok=True)

    for day in range(1, N_DAYS + 1):
        f_day = "{:02}".format(day)
        open(os.path.join(examples_path, f"ex_{f_day}.txt"), "w").close()
        open(os.path.join(input_path, f"inp_{f_day}.txt"), "w").close()

        with open("template.txt") as f:
            template = f.read()

        with open(os.path.join(year_path, f"day_{f_day}.py"), "w") as f:
            f.write(template.replace("__f_day__", f_day)
                    .replace("__day__", str(day))
                    .replace("__year__", str(year)))

    print("Created directories and files for year", year)
