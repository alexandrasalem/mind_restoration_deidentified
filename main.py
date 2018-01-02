import re

def main(filepath):
    with open(filepath, "r") as f1:
        with open(str(filepath)[:-4] + "_new.txt", "w+") as f2:
            pattern1 = re.compile("^([=ECO])")
            pattern2 = re.compile("(?<!\))_(?!\()")
            for line in f1:
                current_line = line
                if re.match(pattern1, row):
                    current_line = re.sub(pattern2, "", current_line)
                    current_line = current_line.replace("-", "")
                    current_line = current_line.upper()
                    f2.write(current_line)
                else:
                    f2.write(current_line)
                    
#now, just have to account for "counting"--harder part. 