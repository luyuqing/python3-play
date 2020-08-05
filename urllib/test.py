import urllib.parse   # https://www.urlencoder.io/python/


print(urllib.parse.quote('/ad bd='))  # /ad%20bd%3D
print(urllib.parse.quote('/ad bd=', safe=''))  # %2Fad%20bd%3D
print(urllib.parse.quote_plus('ab cd'))  # %2Fad%20bd%3D

print(urllib.parse.quote("https://ammattilaisettesti.terveyskyla.fi/covid-19-n%C3%A4ytteenottobotti-hus-alueen-ammattilaisille"))
# https%3A//ammattilaisettesti.terveyskyla.fi/covid-19-n%25C3%25A4ytteenottobotti-hus-alueen-ammattilaisille

print(urllib.parse.unquote("https%3A//ammattilaisettesti.terveyskyla.fi/covid-19-n%25C3%25A4ytteenottobotti-hus-alueen-ammattilaisille"))
# https://ammattilaisettesti.terveyskyla.fi/covid-19-n%C3%A4ytteenottobotti-hus-alueen-ammattilaisille
