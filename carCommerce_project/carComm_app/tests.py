import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTestCase(TestCase):

    #On start
    def setUp(self):
        self.browser = webdriver.ChromiumEdge()

    #Check homepage for expected elements in each section, such as title text
    def test_homepage_content(self):
        #Get base URL
        self.browser.get("http://localhost:8000")
        #Check for company name
        self.assertIn('CarCommerce', self.browser.page_source)
        #Check for carousel title
        self.assertIn('Quality second-hand cars', self.browser.page_source)
        #Check for Recently added section title (only instance of 'recently added' appearing in title case)
        self.assertIn('Recently Added', self.browser.page_source)
        #Check for About us section title (Only instance of 'about us' appearing in title case)
        self.assertIn('About Us', self.browser.page_source)
        #Check for content in about us section
        self.assertIn('Friendly sales team', self.browser.page_source)
        #Check for content in footer
        self.assertIn('Copyright', self.browser.page_source)

    #Check listings for common elements, such as company name, and information relating to cars currently in database
    def test_listings_content(self):
        #Get baseURL/listings
        self.browser.get("http://localhost:8000/listings")
        #Check for company name
        self.assertIn('CarCommerce', self.browser.page_source)
        #Check for page title
        self.assertIn("All Cars", self.browser.page_source)
        #Check that various attributes of cars in database are being displayed
        self.assertIn("Scirocco", self.browser.page_source)
        self.assertIn("140,000", self.browser.page_source)
        self.assertIn("pending payment", self.browser.page_source)
        self.assertIn("1969", self.browser.page_source)
        self.assertIn("Rolls-Royce", self.browser.page_source)
        self.assertIn("Challenger", self.browser.page_source)
        #Check for content in footer
        self.assertIn('Copyright', self.browser.page_source)

    #Check for error message when listing page is retrieved with mileage filter set to a maximum 1 miles (no listings should be present)
    def test_listings_empty(self):
        #Get baseURL/listing + filter string
        self.browser.get("http://127.0.0.1:8000/listings/?make=&colour=&mileage__lt=1&price_lt=&ordering_filters=")
        #Check for error message
        self.assertIn("No listings match", self.browser.page_source)

    #Check contact for common elements, such as company name, and page-specific elements
    def test_contact_content(self):
        #Get baseURL/contact
        self.browser.get("http://localhost:8000/contact")
        #Check for company name
        self.assertIn('CarCommerce', self.browser.page_source)
        #Check for page title
        self.assertIn("Contact Us", self.browser.page_source)
        #Check for input field (contactForm)
        self.assertIn("<input", self.browser.page_source)

    #Check form functionality with captcha unchecked (check for error message)
    def test_contact_form_captcha_unchecked(self):
        #Get baseURL/contact
        self.browser.get("http://localhost:8000/contact")
        #Find text input for name
        nameinput = self.browser.find_element(By.ID, 'id_name')
        #Enter some text
        nameinput.send_keys('TEST NAME')
        #Find text input for email address
        emailinput = self.browser.find_element(By.ID, 'id_email_address')
        #Enter some text
        emailinput.send_keys('TESTEMAIL@EMAIL.UK')
        #Find text input for subject
        subjectinput = self.browser.find_element(By.ID, 'id_subject')
        #Enter some text
        subjectinput.send_keys('TEST SUBJECT')
        #Find text input for message
        subjectinput = self.browser.find_element(By.ID, 'id_message')
        #Enter some text
        subjectinput.send_keys('TEST MESSAGE')
        #Find submit button
        submitbutton = self.browser.find_element(By.ID, 'id_submit')
        #Click submit
        submitbutton.click()
        #Wait .5 secs
        time.sleep(0.5)
        #Check for reloaded page with updated message
        self.assertIn('Did you complete the reCAPTCHA', self.browser.page_source)

        ###Due to the nature of captchas, testing with ticked checkbox will have to be performed manually

    #Check cardetails page for unsold car shows purchase button and car's details
    def test_cardetails_available(self):
        #Get baseURL/carDetails + reg of unsold car
        self.browser.get("http://localhost:8000/carDetails/F454%20DEY/")
        #Check for car name
        self.assertIn('Volkswagen Scirocco', self.browser.page_source)
        #Check for purchase button text
        self.assertIn('Purchase', self.browser.page_source)

    #Check cardetails page for unsold car doesn't show a purchase button, instead shows error message
    def test_cardetials_unavailable(self):
        #Get baseURL/carDetails + reg of sold (pending) car
        self.browser.get("http://localhost:8000/carDetails/N211%20WKL/")
        #Check for car name
        self.assertIn('Volkswagen Corrado', self.browser.page_source)
        #Check there's no purchase button text
        self.assertNotIn('Purchase', self.browser.page_source)
        #Check the sold message is present
        self.assertIn('Sold, pending payment', self.browser.page_source)

    #Check purchase form for expected content
    def test_purchaseform(self):
        #Get baseURL/purchaseForm + car reg
        self.browser.get("http://127.0.0.1:8000/purchaseForm/F454%20DEY/")
        #Check for title text, including name of vehicle
        self.assertIn('Purchase Volkswagen Scirocco', self.browser.page_source)
        #Check error message not present
        self.assertNotIn('Your purchase request has been sent', self.browser.page_source)
        #Check confirmation message not present
        self.assertNotIn('we were unable to sbmit this purchase request', self.browser.page_source)
    
    #Check form functionality with captcha unchecked (check for error message)
    def test_pruchaseform_captcha_unchecked(self):
        #Get baseURL/purchaseForm + car reg
        self.browser.get("http://127.0.0.1:8000/purchaseForm/F454%20DEY/")
        #Find text input for name
        nameinput = self.browser.find_element(By.ID, 'id_name')
        #Enter some text
        nameinput.send_keys('TEST NAME')
        #Find text input for email
        emailinput = self.browser.find_element(By.ID, 'id_email_address')
        #Enter some text
        emailinput.send_keys('TESTEMAIL@EMAIL.UK')
        #Find text input for phone number
        phoneinput = self.browser.find_element(By.ID, 'id_phone')
        #Enter a valid phone number
        phoneinput.send_keys('+447123456789')
        #Find submit button
        submitbutton = self.browser.find_element(By.ID, 'id_submit')
        #Click submit button
        submitbutton.click()
        #Wait for 0.5 secs
        time.sleep(0.5)
        #Check for error message
        self.assertIn('we were unable to submit this purchase request', self.browser.page_source)

    #On finish
    def tearDown(self):
        #Close browser
        self.browser.quit()
    

    
