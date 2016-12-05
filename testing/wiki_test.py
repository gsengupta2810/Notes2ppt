import wikipedia
# Search for an article 
search=wikipedia.search("Martensite")
print search
# finding the title of the page with the search 
title=wikipedia.suggest('Iron')
print title  # seems to be working very poorly, try to avoid using this 
# finding the summery of the page 
summary=wikipedia.summary(search[0], sentences=1) #can remove the sentence attribute to get the whole summery 
print summary
