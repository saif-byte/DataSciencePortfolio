from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self , *star_values):
        star_filtration_box = self.driver.find_element_by_css_selector('div[data-filters-group="class"]')
        star_child_elements =  star_filtration_box.find_elements_by_css_selector('*')
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                     star_element.click()
                     

    def click_lowest_price(self):
        select_element = self.driver.find_element_by_css_selector(
            'li[data-id="review_score_and_price"]')
        select_element.click()
        