import os

from selene.support.shared import browser
from selene import be, have


def test_fill_form(open_browser_for_form):
    # Steps
    browser.element('#firstName').should(be.blank).type('yashaka')
    browser.element('#lastName').should(be.blank).type('selene')
    browser.element('#userEmail').should(be.blank).type('yashaka@selene.com')
    browser.element('[for="gender-radio-1"]').should(have.text('Male')).click()
    browser.element('#userNumber').should(be.blank).type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="3"]').should(have.text('April')).click()
    browser.element('.react-datepicker__year-select option[value="2001"]').should(have.text('2001')).click()
    browser.element('.react-datepicker__day--018').should(have.text('18')).click()
    browser.element('#subjectsInput').should(be.blank).type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').should(have.text('Reading')).click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/1.png')
    browser.element('#currentAddress').should(be.blank).type('Address')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').should(have.text('NCR')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.text('Delhi')).click()
    browser.element('#submit').click()

    # Assertions
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').element_by_its('td', have.text('Student Name')).all('td')[1].should(have.text('yashaka selene'))
    browser.all('tr').element_by_its('td', have.text('Student Email')).all('td')[1].should(have.text(
        'yashaka@selene.com'))
    browser.all('tr').element_by_its('td', have.text('Gender')).all('td')[1].should(have.text('Male'))
    browser.all('tr').element_by_its('td', have.text('Mobile')).all('td')[1].should(have.text('9876543210'))
    browser.all('tr').element_by_its('td', have.text('Date of Birth')).all('td')[1].should(have.text('18 April,2001'))
    browser.all('tr').element_by_its('td', have.text('Subjects')).all('td')[1].should(have.text('Arts'))
    browser.all('tr').element_by_its('td', have.text('Hobbies')).all('td')[1].should(have.text('Reading'))
    browser.all('tr').element_by_its('td', have.text('Picture')).all('td')[1].should(have.text('1.png'))
    browser.all('tr').element_by_its('td', have.text('Address')).all('td')[1].should(have.text('Address'))
    browser.all('tr').element_by_its('td', have.text('State and City')).all('td')[1].should(have.text('NCR Delhi'))
