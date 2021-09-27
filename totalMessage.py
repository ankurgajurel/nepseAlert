def totalMessage():
    from main import scrips
    from unitMessage import unitMessage
    global allMessage
    allMessage = ""
    for i in range(10):
        allMessage = allMessage + unitMessage(scrips[i])
    return allMessage
