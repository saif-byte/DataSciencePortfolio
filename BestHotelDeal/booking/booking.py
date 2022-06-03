from selenium import webdriver
from selenium.webdriver.support.select import Select
from booking.booking_report import BookingReport


from booking.BookingFiltration import BookingFiltration
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self , driver_path='C:\\SeleniumDrivers\\chromedriver.exe', teardown = False):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option( 'excludeSwitches' , ['enable-logging'])
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking , self).__init__(options = options ,executable_path=self.driver_path)

        self.implicitly_wait(50)
        self.maximize_window()

    
    def __exit__(self, *args):
        if self.teardown:
            self.quit()
   
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def change_currency(self , currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
            )
        currency_element.click()
        selected_currency = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )

        selected_currency.click()
    
    def search_dest(self , dest = None):
        input_element = self.find_element_by_id('ss')
        input_element.clear()
        input_element.send_keys(f"{dest}")

        first_option = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_option.click()

    def select_date(self , check_in , check_out):
        check_in_element = self.find_element_by_css_selector(f'td[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(f'td[data-date="{check_out}"]')
        check_out_element.click()


    def __decrease_count(self , css_selector , id, attribute , min_count = 1):
        while True:
            decrease_element = self.find_element_by_css_selector(f'button[{css_selector}]')
            decrease_element.click()

            value_element = self.find_element_by_id(id)

            value = value_element.get_attribute(attribute)
            if int(value) == min_count:
                break

            

    def select_adults(self , count = 1):
        selection_element = self.find_element_by_id("xp__guests__toggle")
        selection_element.click()

        self.__decrease_count(
            'aria-label="Decrease number of Adults"',
            "group_adults",
            "value"
            )
        
        increase_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
            )
        for i in range(count-1):
            increase_element.click()

    def __child_age(self , ages ,count):
        for i in range(count):
            for age in ages:
                select = Select(self.find_element_by_xpath(f'//select[@aria-label="Child {i+1} age"]'))
                
                select.select_by_value(str(age))
                ages.pop(0)
                break
                
    def select_children(self ,ages, count = 0 ):
        self.__decrease_count(
            'aria-label="Decrease number of Children"',
            "group_children",
            "value",
            0
            )
        increase_element = self.find_element_by_css_selector(
           'button[aria-label="Increase number of Children"]'
            )
        for i in range(count):
            increase_element.click()
        
        self.__child_age(ages ,count)

        
    
    def select_room(self , count =1):
        self.__decrease_count(
            'aria-label="Decrease number of Rooms"',
            "no_rooms",
            "value"            
        )
        increase_element = self.find_element_by_css_selector(
           'button[aria-label="Increase number of Rooms"]'
            )
        for i in range(count-1):
            increase_element.click()
        


    def click_search(self):
        search_element = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_element.click()

    def filtration(self):
        filtration  = BookingFiltration(driver = self)
        filtration.click_lowest_price()
        filtration.apply_star_rating(4)
    def hotel_result(self):
        hotel_box = self.find_element_by_class_name("d4924c9e74")

        report = BookingReport(hotel_box)
        report.pull_hotel_attributes()




        