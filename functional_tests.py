from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invted to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types 'Buy peacock feathers" into a  text box
        inputbox.send_keys('Buy peacock feathers')

        # When they hit enter, the page updates, and now the page lists
        # 1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item. They 
        # enter "Use peacock feathers to makea fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on their list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # User wonders wither the site will remember her list. Then they see that the site has generated 
        # a unique URL for them -- there is some explanatory text to that effect.
        self.fail('Finis the test!')

        # They visit that URL, and their to-do list is still there

if __name__ == '__main__':
    unittest.main()

