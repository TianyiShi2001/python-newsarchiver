from news import *

class Scmp(News):

    @titleLogger
    def get_title(self):
        self.title = self.html.xpath('(//h1)[1]/text()')[0]
    
    @abstractLogger
    def get_abstract(self):
        self.abstract = '\n\n'.join(self.html.xpath('(//ul[contains(@class, "summary")])[1]/li/text()'))

    @textLogger
    def get_text(self):
        sel = webdriver.Chrome()
        sel.get(self.url)
        time.sleep(3)
        text_s = sel.find_elements_by_xpath('//div[contains(@class, "details__body body")]//p')
        print(text_s)
        self.text = '\n\n'.join(list(map(lambda e: e.text, text_s)))


if __name__ == "__main__":
    import sys
    a = Scmp(sys.argv[1])
    print(a.title)
    print('\n')
    print(a.abstract)
    print(a.text)