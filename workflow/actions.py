class BaseAction:
    def __init__(self):
        self.conditional_node = True

    def add_condition(self, condition):
        self.conditional_node = condition

    def run(self):
        return self.conditional_node


class SendEmail(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Sending Email to User'
        else:
            return 'Cannot execute send email Task, Moving to the next task'


class Adddelay(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Adding Delay to Workflow'
        else:
            return 'Cannot execute Adddelay Task, Moving to the next task'

class AddToList(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Adding AddToList to Workflow'
        else:
            return 'Cannot execute AddToList Task, Moving to the next task'


class RemoveFromList(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Adding RemoveFromList to Workflow'
        else:
            return 'Cannot execute RemoveFromList Task, Moving to the next task'

class EjectfromJourney(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Adding Delay to Workflow'
        else:
            return 'Cannot execute Adddelay Task, Moving to the next task'


class WebinarAutoRegister(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)

    def action(self):
        if self.run():
            return 'Adding WebinarAutoRegister to Workflow'
        else:
            return 'Cannot execute WebinarAutoRegister Task, Moving to the next task!'

