class Solution:
    def findRestaurant(self, list1, list2):
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        min_ = len(list1)+len(list2)
        ret = []
        for i in range(len(list2)):
            if list2[i] in d:
                if min_ > d[list2[i]]+i:
                    min_ = d[list2[i]] + i
                    ret = [list2[i]]
                elif min_ == d[list2[i]] + i:
                    ret.append(list2[i])
        return ret



if __name__ == "__main__":
    l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    l2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    print(Solution().findRestaurant(l1,l2))