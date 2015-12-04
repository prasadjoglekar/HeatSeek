with open("nyc_neighborhood_zip_pivoted.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        splits = line.split(",")
        neighborhood = splits[0]
        
        for zip in splits[1:]:
            zip = zip.strip()
            print ",".join((neighborhood,zip))