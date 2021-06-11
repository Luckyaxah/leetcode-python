class Solution:
    def subdomainVisits(self, cpdomains):
        def parsedomain(s):
            ret = []
            temp = s.split('.')
            domain = ''
            for ele in temp[::-1]:
                if domain == '':
                    domain = ele
                else:
                    domain = ele + '.' + domain
                ret.append(domain)
            return ret
        
        d = {}
        for domain in cpdomains:
            time, s = domain.split(' ')
            time = int(time)
            l = parsedomain(s)
            print(l)
            for ele in l:
                if ele in d:
                    d[ele] += time
                else:
                    d[ele] = time
        ret = []
        for key, val in d.items():
            ret.append("%d %s"%(val, key))
        return ret


print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))

print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))