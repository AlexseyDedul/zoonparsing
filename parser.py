import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Firefox

TABS = ['restaurants/', 'medical/', 'beauty/', 'trainings/', 'shops/', 'entertainment/', 'autoservice/']
items = []

def pars(url):
    for tab in TABS:
        browser = Firefox()

        # for link in links:
        # browser.get(link['href'])
        browser.get(url + tab)

        catalogTitle = browser.find_element_by_class_name('new_filters_block__title')

        filtersBlockCount = browser.find_element_by_class_name('new_filters_block__count')

        # Array items
        items.append({
            f'catalogTitle': catalogTitle.text.strip(),
            f'filterBlockCount': filtersBlockCount.text.strip()
        })

        browser.execute_script("window.scrollTo(0, 200)")
        y = 1000
        for timer in range(0, 50):
            browser.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 500
            time.sleep(0.5)

        liTag = browser.find_elements_by_class_name("minicard-item")
        print(len(liTag))

        for li in liTag:
            # Get title link for parse
            titleLink = li.find_element_by_class_name("title-link").get_attribute("href")
            print(titleLink)

            response2 = requests.get(titleLink)
            soup2 = BeautifulSoup(response2.text, 'lxml')

            # Get title
            title = soup2.find('span', attrs={'itemprop': 'name'}).text.strip().replace('\xa0', ' ')

            # Get address
            address = soup2.find('address', class_='iblock').text

            # Get description selected of item
            description = soup2.find('div', class_='pull-left service-description-box') \
                .findAll('p', class_='description-text')
            descr = []
            for desc in description:
                descr.append(desc.text.replace('\xa0', '').strip())

            # Get services of item
            services = soup2.find('div', class_='service-description-block invisible-links').findAll('dl')
            servsDesc = {}
            for service in services:
                servsDesc.update({service.find('dt').text.replace(' ', ''): service.find('dd')
                                 .text.replace('\xa0', '')
                                 .strip().replace('\n', '')})

            # Get contacts of item
            phones = []
            try:
                for contact in soup2.find('div', class_='service-phones-list')\
                        .findAll('a', class_='tel-phone js-phone-number'):
                    cont = re.findall(r'\+\d+', contact['href'])
                    phones.append(cont)
            except:
                phones = []

            # Get services description
            serviceBoxDescription = soup2.find('div', class_='service-box-description box-padding btop')
            workTime = serviceBoxDescription.find('dd', class_='upper-first')  # .text.replace('\n', '')
            if workTime is not None:
                workTime = workTime.text.replace('\n', ' ')
            else:
                workTime = ''

            price = serviceBoxDescription.find('span', attrs={'itemprop': 'priceRange'})
            if price is not None:
                price = price.text
            else:
                price = ""

            # Get links by websites
            websites = soup2.findAll('div', class_='service-website')
            websitesList = []
            for web in websites:
                for link in web.findAll('a'):
                    websitesList.append(link['href'])

            # Get images from site
            imagesLinksArray = []
            galleryControls = soup2.find('div', class_='gallery-controls')
            if galleryControls is not None:
                imagesHref = galleryControls.findAll('a', class_='s-icons-white-dot-opacity')
                if imagesHref is not None:
                    for imgHref in imagesHref:
                        imagesLinksArray.append(imgHref['href'])

            # Get map position
            mapPositionLink = soup2.find('div', class_='main-map-view')['data-original']
            mapPosition = re.findall(r'\d+\.\d+', mapPositionLink)

            items.append({
                'itemTitle': title,
                'address': address,
                'contacts': phones,
                'description': descr,
                'workTime': workTime,
                'price': price,
                'links': websitesList,
                'imagesLinks': imagesLinksArray,
                'mapPosition': mapPosition
            })

            items[-1].update(servsDesc)
        browser.close()
    return items
