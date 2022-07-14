class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_to_account_index_map = collections.defaultdict(list)
        
        for idx,ac in enumerate(accounts):
            emails = ac[1:]
            
            for email in emails:
                email_to_account_index_map[email].append(idx)
                
        vis = set()
        def dfs(idx,emails):
            
            if idx in vis:
                return
            vis.add(idx)
            
            for email in accounts[idx][1:]:
                emails.add(email)
                
                for account_idx in email_to_account_index_map[email]:
                    dfs(account_idx,emails)
                    
        ans = []
        for idx,account in enumerate(accounts):
            if idx in vis:
                continue
                
            name,emails = account[0],set()
            
            dfs(idx,emails)
            
            ans.append([name]+sorted(emails))
            
        return ans
        