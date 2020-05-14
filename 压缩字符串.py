class Solution:
    def compress(self, chars) -> int:
        i = 0
        count = 1
        cur_char = ''
        while i<len(chars):
            if chars[i] != cur_char:
                cur_char = chars[i]
                if count == 1:
                    i+= 1
                else:
                    l_count = str(count)
                    for j in range(len(l_count)):
                        chars.insert(i+j,l_count[j])
                    count = 1
                    i += len(l_count)+1
            else:
                chars.pop(i)
                count += 1
        if count >1:
            l_count = str(count)
            for j in range(len(l_count)):
                chars.insert(i+j,l_count[j])
        # print(chars)
        return len(chars)


if __name__ == "__main__":
    a = Solution()
    print(a.compress(["a","a","b","b","c","c","c"]))
    print(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))