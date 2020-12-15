def line_to_dict(line: str):
    line_vals = line.strip().split()
    return { val.split(":")[0]: val.split(":")[1] for val in line_vals}


def merge_dict(dict1, dict2):
    new_dict = dict(dict1)
    for key in dict2:
        new_dict[key] = dict2[key]
    return new_dict


def check_passport_validity(passport):
    req_keys = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
    
    for key in req_keys:
        if key not in passport:
            return False
    return True


def check_birth_year(passport):
    if "byr" not in passport:
        print("Missing birth year")
        return False

    byr = passport["byr"]
    if len(byr) != 4:
        print(f"Birth year {byr} is too short")
        return False
    try:
        byr_int = int(byr)
    except Exception:
        print(f"Birth year {byr} is not an integer")
        return False
    
    if byr_int < 1920:
        print(f"Birth year {byr} is too small")
        return False

    if byr_int > 2002:
        print(f"Birth year {byr} is too large")
        return False
    
    return True


def check_issue_year(passport):
    if "iyr" not in passport:
        print("Missing issue year")
        return False

    iyr = passport["iyr"]
    if len(iyr) != 4:
        print(f"Issue year {iyr} is too short")
        return False
    try:
        iyr_int = int(iyr)
    except Exception:
        print(f"Issue year {iyr} is not an integer")
        return False
    
    if iyr_int < 2010:
        print(f"Issue year {iyr} is too small")
        return False

    if iyr_int > 2020:
        print(f"Issue year {iyr} is too large")
        return False
    
    return True


def check_exp_year(passport):
    if "eyr" not in passport:
        print("Missing expiration year")
        return False

    eyr = passport["eyr"]
    if len(eyr) != 4:
        print(f"Expiration year {eyr} is too short")
        return False
    try:
        eyr_int = int(eyr)
    except Exception:
        print(f"Expiration year {eyr} is not an integer")
        return False
    
    if eyr_int < 2020:
        print(f"Expiration year {eyr} is too small")
        return False

    if eyr_int > 2030:
        print(f"Expiration year {eyr} is too large")
        return False
    
    return True


def check_height(passport):
    if "hgt" not in passport:
        print("Missing height")
        return False

    hgt = passport["hgt"]
    if len(hgt) < 3:
        print(f"Invalid height {hgt}")
        return False
    unit = hgt[-2:]
    if unit == "cm":
        try:
            hgt_val = int(hgt[:-2])
        except Exception:
            print(f"Invalid height {hgt}")
            return False
        if hgt_val < 150:
            print(f"Height of {hgt} is too small")
            return False
        if hgt_val > 193:
            print(f"Height of {hgt} is too large")
            return False
        return True
    elif unit == "in":
        try:
            hgt_val = int(hgt[:-2])
        except Exception:
            print(f"Invalid height {hgt}")
            return False
        if hgt_val < 59:
            print(f"Height of {hgt} is too small")
            return False
        if hgt_val > 76:
            print(f"Height of {hgt} is too large")
            return False
        return True
    else:
        print(f"Height {hgt} has invalid unit {unit}")
        return False


def check_hair_color(passport):
    if "hcl" not in passport:
        print("Missing hair color")
        return False

    hcl = passport["hcl"]
    if len(hcl) != 7:
        print(f"Invalid hair color {hcl}")
        return False
    if hcl[0] != "#":
        print(f"Invalid hair color {hcl}")
        print("Missing leading #-sign")
        return False
    valid_vals = [format(x, "x") for x in range(16)]
    for x in hcl[1:]:
        if x not in valid_vals:
            print(f"Invalid hair color {hcl}")
            print(f"{x} is not a valid hex value")
            return False
        
    return True


def check_eye_color(passport):
    if "ecl" not in passport:
        print("Missing eye color")
        return False

    ecl = passport["ecl"]
    
    valid_ecls = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]
    if ecl not in valid_ecls:
        print(f"Invalid eye color {ecl}")
        return False
    return True


def check_passport_id(passport):
    if "pid" not in passport:
        print("Missing passport id")
        return False

    pid = passport["pid"]
    if len(pid) != 9:
        print(f"Invalid pid length for {pid}")
        return False
        
    
    valid_vals = [format(x, "x") for x in range(10)]
    for x in pid:
        if x not in valid_vals:
            print(f"Invalid pid {pid}")
            print(f"{x} is not a valid digit")
            return False
        
    return True


def check_passport_validity_full(passport):
    return check_birth_year(passport) and check_issue_year(passport) and check_exp_year(passport) and check_height(passport) and check_hair_color(passport) and check_eye_color(passport) and check_passport_id(passport)
            
