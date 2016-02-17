#coding:utf8
import html_outputer,html_parser,url_manage,html_downloader

class Spider_main(object):
    def __init__(self):
        self.outputer = html_outputer.HtmlOutPuter()
        self.parser = html_parser.HtmlParser()
        self.url = url_manage.Url_Manage()
        self.downloader = html_downloader.HtmlDownloader()
    
    
    def craw(self ,root_url):
        count = 1
        
        self.url.add_new_url(root_url)
        
        while self.url.has_new_url():
            try:
                new_url = self.url.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_url,new_data = self.parser.parse(new_url, html_cont)
                self.url.add_new_urls(new_url)
                self.outputer.collect_data(new_data)#收集新的数据
                if count == 100:
                    break
                count+=1
            except Exception as e:
                print 'craw failed--',e
        self.outputer.output_html()
if __name__=="__main__":
    root_url="http://baike.baidu.com/view/4072022.htm"#入口url
    obj_spider = Spider_main()
    obj_spider.craw(root_url)