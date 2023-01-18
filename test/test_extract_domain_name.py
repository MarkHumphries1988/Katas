from src.extract_domain_name.extract_domain_name import extract_domain_name


def test_extracts_from_just_short_string():
    expected="reddit.com"
    result=extract_domain_name("https://www.reddit.com/")
    assert expected==result

def test_extracts_without_www():
    expected="github.com"
    result=extract_domain_name("https://github.com/northcoders/de-py-katas")
    assert expected==result

def test_extracts_from_long():
    expected="google.com"
    result=extract_domain_name("https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2")
    assert expected==result

def test_extracts_co_uk():
    expected="amazon.co.uk"
    result=extract_domain_name('https://www.amazon.co.uk/Sony-WH-1000XM5-Cancelling-Wireless-Headphones-Silver/dp/B09Y2LL45F/?_encoding=UTF8&pd_rd_w=S7y1R&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=94J35DEK7D4MYSBSEKTR&pd_rd_wg=0CYcs&pd_rd_r=d4a7fdb2-0248-4994-bc62-368d4678c422&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1')
    assert expected==result