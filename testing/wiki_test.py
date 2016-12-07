import wikipedia
import codecs #for encoding file in UTF-8


try :
    page = wikipedia.page('Martensite')
    #find the page on the wikipedia
    summary = wikipedia.summary('Martensite',sentences = 2)
    #finding summary of the page
    header = page.title
    #from page using title to get header
    
    with codecs.open('output.txt','w','utf-8') as text_file:
        text_file.write("%s \n%s \n" % (header, summary))
        #output the result in output.txt
    
except wikipedia.exceptions.DisambiguationError as e :
    print e.options
    #printing other information regarding search if search is not specific   
