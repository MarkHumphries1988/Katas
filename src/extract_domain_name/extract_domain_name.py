import re

def extract_domain_name(url):
	domain=re.search(r"[\w\d]+\.(com|co\.uk)",url, re.IGNORECASE).group(0)
	return domain
	pass
