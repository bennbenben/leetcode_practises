class Solution:
  def reformatDate(self, date:str) -> str:
    date_elements = date.split(' ')

    months = {"Jan": "01", 
              "Feb": "02", 
              "Mar": "03", 
              "Apr": "04", 
              "May": "05", 
              "Jun": "06", 
              "Jul": "07", 
              "Aug": "08", 
              "Sep": "09", 
              "Oct": "10", 
              "Nov": "11", 
              "Dec": "12"}
    DD = date_elements[0][:-2]
    if len(DD) == 1:
      DD = "0" + DD
    MM = months[date_elements[1]]
    YYYY = date_elements[2]

    return YYYY+"-"+MM+"-"+DD

s = Solution()
print(s.reformatDate("20th Oct 2052"))
print(s.reformatDate("6th Jun 1933"))