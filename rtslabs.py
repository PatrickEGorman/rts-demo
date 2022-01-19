class CodeDemo():
    def aboveBelow(self, int_list, int_compare):
        above = 0
        below = 0
        for it in int_list:
            if(it>int_compare):
                above += 1
            elif(it<int_compare):
                below +=1
        return {"above": above, "below": below}
    
    def stringRotation(self, string, num):
        return "%s%s"%(string[-num:],string[:-num])
