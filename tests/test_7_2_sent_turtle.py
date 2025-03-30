import unittest
import importlib.util
import os


# Dynamically load PostOffice class from src/7.2.sent_turtle.py
def load_post_office_class():
    file_path = os.path.join(os.path.dirname(__file__), '../src/7.2.sent_turtle.py')
    spec = importlib.util.spec_from_file_location("sent_turtle_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.PostOffice


PostOffice = load_post_office_class()


class TestPostOffice(unittest.TestCase):

    def setUp(self):
        self.po = PostOffice(["alice", "bob", "carol"])

    def test_send_and_read_message(self):
        msg_id = self.po.send_message("alice", "bob", "Hello", "Hi Bob!")
        self.assertEqual(msg_id, 1)
        inbox = self.po.read_inbox("bob", 1)
        self.assertEqual(len(inbox), 1)
        self.assertEqual(inbox[0]['title'], "Hello")
        self.assertEqual(inbox[0]['body'], "Hi Bob!")
        self.assertFalse(inbox[0]['unread'])

    def test_read_inbox_marks_unread(self):
        self.po.send_message("alice", "bob", "Title", "Body")
        self.assertTrue(self.po.boxes["bob"][0]['unread'])
        _ = self.po.read_inbox("bob", 1)
        self.assertFalse(self.po.boxes["bob"][0]['unread'])

    def test_send_urgent_message(self):
        self.po.send_message("alice", "bob", "First", "First msg")
        self.po.send_message("carol", "bob", "Urgent", "Important!", urgent=True)
        inbox = self.po.read_inbox("bob", 2)
        self.assertEqual(inbox[0]['title'], "Urgent")  # urgent is first

    def test_read_all_messages_when_N_missing(self):
        self.po.send_message("alice", "bob", "1", "one")
        self.po.send_message("alice", "bob", "2", "two")
        messages = self.po.read_inbox("bob")  # no N passed
        self.assertEqual(len(messages), 2)

    def test_search_inbox_by_title_and_body(self):
        self.po.send_message("alice", "bob", "Meeting", "Let's talk tomorrow")
        self.po.send_message("alice", "bob", "Lunch", "Tomorrow at noon")
        results = self.po.search_inbox("bob", "tomorrow")
        self.assertEqual(len(results), 2)
        results = self.po.search_inbox("bob", "Lunch")
        self.assertEqual(len(results), 1)

    def test_send_to_nonexistent_user(self):
        with self.assertRaises(KeyError):
            self.po.send_message("alice", "dave", "Oops", "Should fail")


if __name__ == '__main__':
    unittest.main()
