# WorkflowEngine
An implementation of a workflow engine built with Python that allows us to build and publish a workflow by adding 
a trigger, tasks/actions and conditional nodes.

To build a workflow, we start by adding a trigger (we do not add any trigger after this)
We continue by adding actions and conditional nodes to determine if the actions downstream should be executed.
##

Below is a list of supported triggers, actions and conditional nodes(case sensitive!)

Actions:

- SendEmail
- AddToList
- WebinarAutoRegister
- RemoveFromList
- EjectfromJourney
- Adddelay

Conditionals:
- Campaign(status)
- Is_OnList(status)
- CheckField(status)
- Check_Purchasestatus(status)
- Has_Visitedpage(status)
- Check_Webinar(status)

Triggers:
-  optin
- time_trigger
- campaign_activity
- remove_from_list
- purchase_acitivity
- page_visited_trigger
- list_trigger


##
To test the workflow, clone this repository:
```
git clone https://github.com/harryportal/WorkflowEngine
```

To test with unit test:
```
python -m unittest test
```

Below I a detailed instruction on how to test the work engine manually 

