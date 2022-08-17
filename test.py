from unittest import TestCase
from builder import *


class TestSum(TestCase):
    def test_create_trigger(self):
        new = BuildWorkflow()
        new.add_trigger(optin)
        self.assertTrue(new.trigger)


    def test_create_task_before_trigger(self):
        new = BuildWorkflow()
        new.add_action(SendEmail)
        self.assertFalse(new.workflowlist)

    def test_create_task_with_trigger(self):
        new = BuildWorkflow()
        new.add_trigger(optin)
        new.add_action(SendEmail)
        self.assertTrue(new.workflowlist)

    def test_create_conditional_before_trigger(self):
        new = BuildWorkflow()
        new.add_condition(Webinar_Status('Not registered'))
        self.assertFalse(new.workflowlist)

    def test_action_after_false_condition(self):
        new = BuildWorkflow()
        new.add_trigger(time_trigger)
        new.add_condition(Check_Purchasestatus('Has not purchased'))
        new.add_action(SendEmail)
        self.assertEqual(new.workflowlist[0],
                    'Cannot execute send email Task, Moving to the next task')



if __name__ == '__main__':
    unittest.main()
