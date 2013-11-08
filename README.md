ZimbraSOAP
==========

Description
-----------
Python library for interfacing with [Zimbra's](http://www.zimbra.com) [SOAP API](http://files.zimbra.com/docs/soap_api/8.0/soapapi-zimbra-doc/api-reference/index.html). It's based on [PySimpleSOAP](http://code.google.com/p/pysimplesoap/) and provides a framework to make and respond to any given Zimbra SOAP API request.

Example
-------
    import zimbrasoap

    zimbra = zimbrasoap.admin(server = 'zimbra.example.com')

    # Calls AuthRequest, and stores auth token in zimbrasoap object
    zimbra.Auth(name = 'admin@example.com', password = 'password')

    # Calls GetAccountRequest
    response = zimbra.GetAccount(account = {'by':'name', 'value':'user@example.com'})

    # Reponse looks similar to:
    # <GetAccountResponse xmlns="urn:zimbraAdmin">
    #       <account id="abcde1234-1234-abcd-1234-abcdef123456" name="user@example.com">
    #           <a n="zimbraMailStatus">closed</a>
    #           <a n="givenName">John</a>
    #           [...]
    #           <a n="displayName">John Doe</a>
    #       </account>
    # </GetAccountResponse>

    # Print tag attribute (could also use just response.account['id'])
    print response.GetAccountResponse.account['id']

    # Use ParseAttributes to print a dict of all Zimbra attributes
    # (ie zimbraMailStatus / enabled)
    print zimbra.ParseAttributes(response.account.a)

    # Call ModifyAccountRequest to set "zimbraMailStatus" to "closed"
    #
    # Sends request similar to:
    #
    # <ModifyAccountRequest xmlns="urn:zimbraAdmin">
    #   <a n="zimbraAccountStatus">active</a>
    #   <id>e78b0780-3802-411c-8151-a5a7943cdb41</id>
    # </ModifyAccountRequest>
    zimbra.ModifyAccount(id = response.account['id'], a = {'n':'zimbraAccountStatus', 'value':'active'})

TODO
----
* Could support [XPath-like syntax of zmsoap](http://wiki.zimbra.com/wiki/Zmsoap)
