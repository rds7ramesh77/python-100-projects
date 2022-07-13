#Python program to extract keyword

""" There are so many Python libraries for the task of extracting keywords, the best ones are spaCy, Rake-Nltk, YAKE. Here I will use Rake-NLTK"""



from rake_nltk import Rake
rake_nltk_var=Rake()

MyText="""Python is a high-level, interpreted, 
general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected."""

rake_nltk_var.extract_keywords_from_text(MyText)
keyword_extracted=rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)
