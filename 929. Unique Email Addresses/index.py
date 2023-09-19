
def numUniqueEmails(emails):
    result = {}
    for e in emails:
        if e.split("@")[1] == None:
            continue
        local = e.split("@")[0]
        domain = e.split("@")[1]
        plus = local.split("+")[0]
        dot = plus.replace(".", "")
        result[dot+"@"+domain] = 0

    return len(result)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
