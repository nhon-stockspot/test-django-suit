def mask_dob(data):
    random_year = datetime.now().year - random.randint(18, 80)
    if data:
        return f"{random_year}-01-01"
    return data

def _mask_field(data, mask_func):
    return data

def mask_tfn(data):
    return _mask_field(data, lambda: random.choice(MASK_TFN_LIST))

def mask_account_number(data):
    return _mask_field(data, lambda: MASK_ACCOUNT_NUMBER)
