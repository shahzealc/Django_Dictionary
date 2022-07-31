from django.shortcuts import render
import bs4
import requests


# Create your views here.


def home(request):
    return render(request, 'home.html')

def word(request):
        if request.GET.get('word'):
            word = request.GET.get('word')

            res = requests.get('https://www.dictionary.com/browse/'+word)
            res2 = requests.get('https://www.thesaurus.com/browse/'+word)
            

            if res:
                soup = bs4.BeautifulSoup(res.text, 'lxml')

                meaning = soup.find_all('div', {'value': '1'})
                meaning1 = meaning[0].getText()
            else:
                word = 'Sorry, '+ word + ' Is Not Found In Our Database'
                meaning = ''
                meaning1 = ''

            if res2:
                soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

                synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
                ss = []
                for b in synonyms[0:]:
                    re = b.text.strip()
                    ss.append(re)
                se = ss
                

                

                antonyms = soup2.find_all('a', {'class': 'css-15bafsg eh475bn0'})
                aa = []
                for c in antonyms[0:]:
                    r = c.text.strip()
                    aa.append(r)
                ae = aa
            else:
                se = ''
                ae = ''


            results = {
                'word' : word,
                'meaning' : meaning1,
            }


            return render(request, 'word.html', {'se': se, 'ae': ae, 'results': results})
           

def english_hindi(request):
    return render(request,'english_hindi.html')

def hindi_word(request):

     if request.GET.get('word'):
        word = request.GET.get('word')
        res = requests.get('https://dict.hinkhoj.com/shabdkhoj.php?word='+word)

        if res:
            soup = bs4.BeautifulSoup(res.text, 'lxml')

            meaning = soup.find_all('span', {'class': 'tlr'})
            ss = []
            for b in meaning[0:5]:
                re = b.text.strip()
                ss.append(re.capitalize())
            se = ss
        else:
            word = 'Sorry, '+ word + ' Is Not Found In Our Database'
            meaning = ''
            meaning1 = ''
            
        return render(request, 'hindi_word.html', {'word': word,'se':se})


def about(request):
    return render(request, 'about.html')
