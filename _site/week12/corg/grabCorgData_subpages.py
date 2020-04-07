# base page: http://www.cardiped.net/browseDogs.php?start=0&p_f=0&sortBy=name&alpha=a

# outputs are:
#  FULL dataset of corgis
saveFileName = 'corgiData_countries_full.json'


# for web scraping
import bs4
from urllib.request import Request, urlopen
# pause
import time

# were are we saving data?
saveFileDir = '/Users/jillnaiman/spring2020/week12/corg/'

sleepTime = 2 # sec

#-----------------------------------------------------------


names = []
sires = []
dams = []
sexes = []
years = []
siblings = []
countries = []
# save country id to put on a map
country_id = []


import pandas as pd
df = pd.read_csv(saveFileDir + 'world_population.tsv', sep="\t")   # read dummy .tsv file into memory

# convert to array
import numpy as np
data = np.array(df)

country_codes = data[:,0]
country_names = data[:,1]


# grab all names on this list
import string
alphas = list(string.ascii_lowercase)

for al in alphas:

    print('-------')
    print('On alphabetic page = ' + al)

    # webparsing numbers
    startSmall=0
    startLarge=0

    # parse
    w = 'http://www.cardiped.net/browseDogs.php?start='+\
        str(int(startSmall))+\
        '&p_f='+\
        str(int(startLarge))+\
        '&sortBy=name&alpha='+al
    #page = requests.get(w)
    #soup = bs4.BeautifulSoup(page.text, 'html.parser')
    req = Request(w, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = bs4.BeautifulSoup(page, 'html.parser')
    soup = str(soup)

    
    # figuring out from webpage how many doggos
    x = soup.split('Displaying')[1]
    x = x.split('</b>')[0]
    x = x.split('of ')[1]
    numberOfDoggos = int(x)

    print('Grabbing ' + str(numberOfDoggos) + ' corgos')

    while startSmall < numberOfDoggos:
        time.sleep(sleepTime) # pause
        
        w = 'http://www.cardiped.net/browseDogs.php?start='+\
            str(int(startSmall))+\
            '&p_f='+\
            str(int(startLarge))+\
            '&sortBy=name&alpha='+\
            al

        print(w)

        # parse
        #page = requests.get(w)
        #soup = bs4.BeautifulSoup(page.text, 'html.parser')
        req = Request(w, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = bs4.BeautifulSoup(page, 'html.parser')
        soup = str(soup)

        # split by details
        splitSoup = soup.split('<a href="details.php?id=')
        # ignore top
        splitSoup = splitSoup[1:]
        # take out last bit from last one
        x = splitSoup[-1]
        y = x.split('</table>')
        splitSoup[-1] = y[0]


        # loop and append
        for s in splitSoup:
            time.sleep(0.25)
            #print(s)
            #print('---')

            # navigate to details page
            myid = s.split('">')[0]
            w_details = 'http://www.cardiped.net/details.php?id=' + str(myid)
            req_details = Request(w_details, headers={'User-Agent': 'Mozilla/5.0'})
            page_details = urlopen(req_details).read()
            soup_details = bs4.BeautifulSoup(page_details, 'html.parser')

            #page_details = requests.get(w_details)
            #soup_details = bs4.BeautifulSoup(page_details.text, 'html.parser')
            soup_details = str(soup_details)
            # name
            name = ((soup_details.split('Registered Name:')[1]).split('<td>')[1]).split('</td>')[0]
            # Dad
            sire = ((soup_details.split('Sire:')[1]).split('<td>')[1]).split('</td>')[0]
            #   listed?
            if len(sire) > 0:
                sire = (sire.split('>')[1]).split('<')[0]
            else:
                sire = ''
            # Mom
            dam = ((soup_details.split('Dam:')[1]).split('<td>')[1]).split('</td>')[0]
            if len(dam) > 0:
                dam = (dam.split('>')[1]).split('<')[0]
            else:
                dam = ''
            # Sex
            sex = ((soup_details.split('Sex:')[1]).split('<td>')[1]).split('</td>')[0]
            # Birthday
            dob = ((soup_details.split('Date of Birth:')[1]).split('<td>')[1]).split('</td>')[0]
            # listed?
            if len(dob.split()) > 0:
                #  just grab year
                year = dob.split()[-1]
            else:
                year = ''
            # nationality
            country = ((soup_details.split('Country of Birth:')[1]).split('<td>')[1]).split('</td>')[0]
            # siblings
            # do we have them listed?
            if len(soup_details.split('Siblings:')) > 1:
                sibs =  ((soup_details.split('Siblings:')[1])).split('</td>')[0]
                sibs = sibs.split('">')[1:]
                # loop and update
                for i in range(len(sibs)):
                    sibs[i] = sibs[i].split('<')[0]
            else:
                sibs = []

            names.append(name)
            sires.append(sire)
            dams.append(dam)
            sexes.append(sex)
            years.append(year)
            siblings.append(sibs)
            countries.append(country)



        startSmall += 20
        if startSmall%100 == 0:
            startLarge += 100




# now, save this dataset
def replaceWeird(st):
    sto = st.replace("'","")
    sto = st.replace('"','')
    sto = st.replace("'",'')
    return sto

# loop through things and replace any weirdos
for i in range(len(names)):
    names[i] = replaceWeird(names[i])
    dams[i] = replaceWeird(dams[i])
    sires[i] = replaceWeird(sires[i])
    sexes[i] = replaceWeird(sexes[i])
    years[i] = replaceWeird(years[i])
    countries[i] = replaceWeird(countries[i])
    for j in range(len(siblings[i])):
        siblings[i][j] = replaceWeird(siblings[i][j])

# now associate country names with country codes for plotting with d3.js
#  give each a country id
import re
country_id = []
for i in range(len(names)):
    myId = ''
    for j in range(len(country_names)):
        #if (countries[i].find('Germany') != -1) and (country_names[j].find('Germany') != -1):
        #    print(countries[i], country_names[j])
        if re.search(countries[i], country_names[j], re.IGNORECASE) or \
           (countries[i].find(country_codes[j]) != -1):
            myId = country_codes[j]
        
            
    country_id.append(myId)
            
# save to json
import json

v = []
for i in range(len(names)):
    v.append( {"name":names[i], "dam":dams[i], "sire":sires[i], "sex":sexes[i],
               "year":years[i], "countries":countries[i], "siblings":siblings[i],
               "country_id":country_id[i]} )

# dump to file
saveFilejson = saveFileDir + saveFileName
f = open(saveFilejson,'w')
f.write(json.dumps(v,indent=2))
f.close()
    
