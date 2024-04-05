class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<bool>> is_pal(n, vector<bool>(n, false));
        vector<int> dp(s.size(), s.size()); // Initialize with s.size() for the maximum cuts
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j >=0; j--) {
                if (s[i] == s[j] && (i - j <= 2 || is_pal[i-1][j+1])) {
                    is_pal[i][j] = true;
                }
            }
        }

        dp[0] = 0;
        for (int i = 1; i < s.size(); i++) {
            if (is_pal[i][0]) {
                dp[i] = 0;
                continue;
            }
            
            for (int j = 0; j < i; j++) {
                if (is_pal[i][j+1]) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp.back();
    }
};