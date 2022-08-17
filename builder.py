from workflow.actions import *
from workflow.workflow_triggers import *
from workflow.conditionals import *
from time import sleep



class BuildWorkflow:
    def __init__(self):
        self.trigger = None
        self.workflowlist = []  # a list of tasks and conditionals to be executed
        self.trigger_list = [optin, time_trigger, campaign_activity, remove_from_list, purchase_acitivity,
                             list_trigger,page_visited_trigger]

    def add_action(self, action):
        # check if last element in the list is a condition by inspecting the return type
        task_list = self.workflowlist
        task = action() # create an instance of the action class
        if not self.trigger:
            return self.raise_workflow_error('A trigger must be added before a task/condition')
        if task_list and isinstance(task_list[-1], bool):
            condition = task_list[-1]
            task_list.pop() # remove the condition from the list before attaching it
            task.add_condition(condition)
            task_list.append(task.action())
        else:
            task_list.append(task.action())

    def add_condition(self, condition):
        if not self.trigger:
            print(self.raise_workflow_error('A trigger must be added before a task/condition'))
            return None
        # condition should be specified with status
        self.workflowlist.append(condition)


    def add_trigger(self, trigger):
        """For this implementation, i am making an assumption
        that only every workflow should have only one trigger"""
        if self.trigger:
            return self.raise_workflow_error('trigger already exists in workflow')
        self.trigger = trigger

    def raise_workflow_error(self, message):
        error = f'WorkFlow Build Error, Reason: {message}'
        return error

    def publish_workflow(self):
        if not self.trigger:
            print(self.raise_workflow_error('No trigger has been configured for Build'))
            return
        print('#############Welcome to Python WorkEngine Simulation by Harry!################')
        for index, task in enumerate(self.workflowlist):
            print(f'Task{index + 1}: {task}')



new = BuildWorkflow()
new.add_trigger(optin)
new.add_condition(Webinar_Status('Not registered'))
new.add_action(SendEmail)
new.add_action(SendEmail)
new.publish_workflow()