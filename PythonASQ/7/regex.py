import re

string = """The top-level domains (TLDs) such as com, net and org are the highest level of domain names of the Internet. Top-
level domains form the DNS root zone of the hierarchical Domain Name System. Every domain name ends with a
top-level domain label. When the Domain Name System was devised in the 1980s, the domain name space was
divided into two main groups of domains [7]. The country code top-level domains (ccTLD) were primarily based on
the two-character territory codes of ISO-3166 country abbreviations. In addition, a group of seven generic top-level
domains (gTLD) was implemented which represented a set of categories of names and multi-organizations [8,9,14].
These were the domains gov, edu, com, mil, org, net, and int. During the growth of the Internet, it became
desirable to create additional generic top-level domains. As of October 2009, 21 generic top-level domains and 250
two-letter country-code top-level domains existed [9-12]. In addition, the ARPA domain serves technical purposes
in the infrastructure of the Domain Name System [13,14,20-25,30,32].
Examples of some high ranking top-level domains are:
www.google.com, www.youtube.com, www.facebook.com, www.baidu.com, www.bahn.de, www.yahoo.com,
www.reddit.com, labanquepostale.fr, www.qq.com, www.taobao.com, www.free.fr, www.tmall.com,
www.amazon.com, www.duden.de, lemonade.fr, www.twitter.com, www.live.com, www.vk.com,
www.instagram.com, www.jd.com, www.sohu.com, www.web.de."""

# Define a regular expression pattern
capitalFirst = re.compile(r'\b[A-Z]\w*')
citationNumbers = re.compile(r'\[\d+((,|-)\d+)*\]')
germanOrFranceWebsite = re.compile(r'(www\.)?\w+\.(de|fr)(\/\w+)*')

print(re.findall(capitalFirst, string))
print(re.findall(citationNumbers, string))
print(re.findall(germanOrFranceWebsite, string))
