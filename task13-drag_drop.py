import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class DragTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_drag_drop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://jqueryui.com/draggable/')
        driver.switch_to.frame(0)
        source1 = driver.find_element_by_id('draggable')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        time.sleep(5)
        driver.get('https://jqueryui.com/droppable/')
        driver.switch_to.frame(0)
        source1 = driver.find_element_by_id('draggable')
        target1 = driver.find_element_by_id('droppable')
        actions2 = ActionChains(driver)
        actions2.drag_and_drop(source1, target1).perform()
        time.sleep(5)
        self.assertEqual("Dropped!", target1.text)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()