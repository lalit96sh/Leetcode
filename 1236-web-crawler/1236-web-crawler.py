# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def get_hostname(url):
            
            x = url.replace("http://","")
            
            return x.split("/")[0]
        
        
        start_host = get_hostname(startUrl)
        
        
        
        q = [startUrl]
        ans = []
        vis = set()
        vis.add(startUrl)
        while q:
            url = q.pop(0)
            ans.append(url)
            
            for child_url in htmlParser.getUrls(url):
                if child_url in vis or start_host != get_hostname(child_url):
                    continue
                vis.add(child_url)
                q.append(child_url)
                
            
            
            
            
            
        return ans