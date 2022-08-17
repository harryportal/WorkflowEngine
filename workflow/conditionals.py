def Webinar_Status(status)->bool:
    condition_dict = {'Not registered':False,'Registered':True,
                      'Attended':True, 'did not attend':False}
    return condition_dict.get(status, True)

def Check_Purchasestatus(status)-> bool:
    condition_dict = {'Has purchased':True, 'Has not purchased':False, 'Abandoned':False,
                      'cart checkout':True}
    return condition_dict.get(status, True)

def CheckField(status)-> bool:
    # status to check not provided in the documentation
    return True

def Has_Visitedpage(status)-> bool:
    # status to check not provided in the documentation
    return True

def Is_OnList(status)-> bool:
    condition_dict = {'Is on this list or segment':True, 'Is not on this list or segment':False}
    return condition_dict.get(status, True)

def CampaignStatus(status)-> bool:
    condition_dict = {'Has opened': True, 'Has not opened': False, 'Has replied': True,
                      'Has not replied': False, 'Has clicked': True, 'Has not clicked': False,
                      'Has been sent': True, 'Has not been sent': False}
    return condition_dict.get(status, True)