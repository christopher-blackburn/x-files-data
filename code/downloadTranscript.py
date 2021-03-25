import time
import requests
from bs4 import BeautifulSoup

# Create a dictionary with the episode counts for each season
episode_count = {'1':23,'2':25,'3':24,'4':24,
                '5':20,'6':22,'7':22,'8':21,'9':20}

saveDir = '_path_to_directory_'


mulder_list = []
scully_list = []
episode_list = []



for season in range(1,10):
    
    max_episode = episode_count[str(season)] + 1
    
    for episode in range(1,max_episode):
        
        
        if episode < 10:
    
            url = 'http://www.insidethex.co.uk/transcrp/scrp{}0{}.htm'.format(season,episode)
        
        else:
            
            url = 'http://www.insidethex.co.uk/transcrp/scrp{}{}.htm'.format(season,episode)
            
        page = requests.get(url)
        
        print('Received response {} for {}-{}'.format(page,season,episode),end='...')
        
        soup = BeautifulSoup(page.text,'lxml')
        
        episode_text = [t.getText() for t in soup.findAll('p')]

        episode_transcript.append(pd.DataFrame.from_dict(
            {'episode_transcript': [' '.join(episode_text)], 'season':[season],'episode':[episode]}))

        
        mulder_lines = [text.replace('\n',' ') for text in episode_text if text[0:6] == 'MULDER']
        
        scully_lines = [text.replace('\n',' ') for text in episode_text if text[0:6] == 'SCULLY']
        
        mulderDF = pd.DataFrame(mulder_lines,columns=['mulder_lines'])
        
        mulderDF['season'] = season
        
        mulderDF['episode'] = episode

        scullyDF = pd.DataFrame(scully_lines,columns=['scully_lines'])
        
        scullyDF['season'] = season
        
        scullyDF['episode'] = episode
        
        mulder_list.append(mulderDF)
        
        scully_list.append(scullyDF)
        
        print('Successfully finished {}-{}'.format(season,episode))
        
        
        time.sleep(5)
        
        
            
mulder_lines = pd.concat(mulder_list)
scully_lines = pd.concat(scully_list)
episode_lines = pd.concat(epsiode_transcript)

mulder_lines.to_csv(saveDir + 'mulder_lines.csv',index=False)
scully_lines.to_csv(saveDir + 'scully_lines.csv',index=False) 
episode_lines.to_csv(saveDir + 'episode_lines.csv',index=False) 
        
    



