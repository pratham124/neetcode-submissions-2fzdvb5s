class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [i for i in range(len(accounts) + 1)]
        rank = [1] * (len(accounts) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        email_acc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_acc:
                    union(i, email_acc[e])
                else:
                    email_acc[e] = i
        
        account_to_emails = defaultdict(list)
        for email in email_acc:
            acc = email_acc[email]
            parent = find(acc)
            account_to_emails[parent].append(email)
        
        res = []
        for i, emails in account_to_emails.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

        
