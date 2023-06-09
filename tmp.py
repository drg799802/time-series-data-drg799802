# Test package imports - DO NOT MODIFY THIS CELL!
import_answer_points = 3

# Check that pandas has been imported properly
try:
    na_val = pd.NA
    print("\u2705 Score! Pandas has been imported as a pd!")
    import_answer_points += 2
except NameError:
    print(
        "\u274C Pandas has not been imported as a pd, please make "
        "sure to import it properly."
    )

# Subtract one point for any PEP-8 errors
tmp_path = "tmp.py"
with open(tmp_path, "w") as tmp_file:
    tmp_file.write(In[-2])
ignore_flake8 = 'W292,F401,E302'
flake8_out = subprocess.run(
    ['flake8', 
     '--ignore', ignore_flake8, 
     '--import-order-style', 'edited',
     '--count', 
     tmp_path],
    stdout=subprocess.PIPE,
).stdout.decode("ascii")
print(flake8_out)
import_answer_points -= int(flake8_out.splitlines()[-1])

print(
    "\n \u27A1 You received {} out of 5 points.".format(import_answer_points)
)

import_answer_points