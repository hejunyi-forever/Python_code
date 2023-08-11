

with open("D:/snp/geneid.txt", "r") as geneid_repeat:
    with open("D:/snp/newgeneid.txt", "w") as w:
        with open("D:/snp/repeatgeneid.txt", "w") as w2:
            lines_seen = set()
            for line in geneid_repeat:
                if line not in lines_seen:
                    w.write(line)
                    lines_seen.add(line)
                else:
                    w2.write(line)
    w.close()
    w2.close()