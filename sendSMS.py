def sendSMS():
    import totalMessage
    from main import nums 
    from main import scrips
    for i in range(len(nums)):
        from twilio.rest import Client
        client = Client("AC0f742cb0a43176b34f73d596b5f03846", "83ac639663e8244498a8b512029e45a6")
        client.messages.create(to = [nums[i]], from_ = "+12019776138", body = totalMessage.totalMessage)
