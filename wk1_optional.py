import re

"""
Optional:
Read about Regex. There's a nice cheatsheet interactive website https://pythrex.org where you can figure out how that works roughly.
Implement the words analysis prblem from yesterday with regex too (this won't exclude the original non-regex assignment)
"""

def get_phone(file):
    phone = r"(07\d{2}\ ?\d{6})"

    with open(file, "r") as f:
        article = f.readlines()

    whole_article = "".join(article)
    #string = "All phones 0744 000121, 0725 111188, 0744214587"
    #regex_pattern = re.compile(phone)
    #result = regex_pattern.findall(content)

    result = re.findall(phone, whole_article, flags=re.MULTILINE)
    return result


phone_list = get_phone("article.txt")
print("\nOptional 1")
print("Phone numbers found are:")
for idx, nr in enumerate(phone_list):
    print(f"{idx+1} -> {nr}")
print("*"*15)

"""
Given a list of software versions such as the one in this example, choose the latest(biggest version)
versions = ["1.1.2", "1.2.3", "1.19.3", "1.19.8", "1.193.5", "1.193.4"]
The significance of the numbers is MAJOR.MINOR.PATCH, by which rule, the highest version is 1.193.5 in this example
"""

versions = ["1.1.2", "1.2.3", "1.19.3", "1.19.8", "1.193.5", "1.193.4"]


def major_minor_patch(versions):
    pattern = '(\d+)\.(\d+)\.(\d+)'
    major, minor, patch = re.search(pattern, versions).groups()

    return int(major), int(minor), int(patch)


latest = max(versions, key=major_minor_patch)

print("Optional 2")
print(f"Greatest version is \n {latest} ")
print("*"*15)