with open("system_log.txt", "w") as f:
    f.writelines([
        "name, phone\n",
        "Rahul, 9988776655",
        "Aisha, 9987654321",
        "Kabir, 1234567890"
    ])
count_type = lambda lines, level: sum(1 for l in lines if l.startswith(level))
with open("system_log.txt") as f:
    lines = f.readlines()
errors = count_type(lines, "ERROR")
warnings = count_type(lines, "WARNING")
infos = count_type(lines, "INFO")

with open("system_log.txt", "w") as s:
    s.write("log summary\n")
    s.write(f"ERROR: {errors} \nWARNING: {warnings} \nINFO: {infos}\n")
print("log_summary.txt created!")