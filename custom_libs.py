from collections import Counter
import re
import emoji


def counter_fill_key(list):
    cnt = Counter(list)
    max_iter = max(cnt.keys())
    for i in range(0, max_iter+1):
        if cnt.get(i) is None:
            cnt[i] = 0
    return {k: v for k, v in sorted(cnt.items(), key=lambda x:x[0])}

def print_len_set(x: list):
    print(len(set(x)))

def set_sort(x: list):
    return set(sorted(x))

def sub_list(list_x: list, list_y: list):
    return  [x for x in list_x if x not in list_y]

def find_url(string): 
    text = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return "".join(text) # converting return value from list to string

def find_emoji(text):
    emo_text = emoji.demojize(text)
    line = re.findall(r'\:(.*?)\:', emo_text)
    return line

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_html(text):
    html=re.compile(r'<.*?>')
    return html.sub(r'',text)

if __name__ == "__main__":
    hoge = [1,1,3,4,5,6,9,9,9,10]
    print(counter_fill_key(hoge))
    print_len_set(hoge)
    print(set_sort(hoge))
    huga = [1, 2, 3]
    print(sub_list(hoge, huga))
    
    print(find_emoji("ありがとうございます😊"))
    
    html_text = """<div>
<h1>Real or Fake</h1>
<p>Kaggle </p>
<a href="https://www.kaggle.com/c/nlp-getting-started">getting started</a>
</div>"""
    print(remove_html(html_text))
