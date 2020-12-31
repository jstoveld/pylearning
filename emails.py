def email_list(domains):
    emails = []
    for provider, users in domains.items():
        for user in users:
            user=("{}@{} ".format(user, provider))
            emails.append(user)
    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))