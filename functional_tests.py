from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # Must have firefox installed in applications
        # use `cd /Applications && ln -s ~/Applications/Firefox.app` if firefox is installed elsewhere
        self.browser = webdriver.Firefox() 
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User visits the home page
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invted to enter a to-do item straight away

        # User types 'Buy peacock feathers" into a  text box

        # When they hit enter, the page updates, and now the page lists
        # 1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. They 
        # enter "Use peacock feathers to makea fly"

        # The page updates again, and now shows both items on their list

        # User wonders wither the site will remember her list. Then they see that the site has generated 
        # a unique URL for them -- there is some explanatory text to that effect.

        # They visit that URL, and their to-do list is still there

if __name__ == '__main__':
    unittest.main()

