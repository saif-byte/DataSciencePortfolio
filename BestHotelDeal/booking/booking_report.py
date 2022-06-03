import os,sys
from selenium.webdriver.remote.webdriver import WebDriver
import csv



class BookingReport:
    def __init__(self , boxes_selection_element:WebDriver):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()
    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements_by_css_selector(
            'div[data-testid="property-card"]')

    def pull_hotel_attributes(self):
        csv_file = open(os.path.join(sys.path[0], "best_hotel_deal.csv") , 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Hotel Name' , "Ratings" , "Price"])
        for deal in self.deal_boxes:
            try:
                hotel_name = deal.find_element_by_css_selector(
                    'div[data-testid="title"]').get_attribute("innerHTML").strip()
                rating = deal.find_element_by_css_selector(
                'div[class="b5cd09854e d10a6220b4"]').get_attribute("innerHTML").strip()
                price = deal.find_element_by_css_selector(
                    'span[class="fcab3ed991 bd73d13072"]'
                    ).get_attribute("innerHTML").strip()
            except Exception as e:
                hotel_name=None
                rating = None
                price=None
            
            csv_writer.writerow([hotel_name , rating , price])

