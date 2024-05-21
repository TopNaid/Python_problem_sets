import re



def main():
    main_url= input("HTML: ")
    print(parse(main_url))


def parse(s):
    pattern = re.search(r'<iframe[^>]*\ssrc="(https?://(?:www\.)?(youtube)\.com/embed/([^"]+))".*?>', s, re.IGNORECASE)
    if pattern:
        full_url = pattern.group(1)
        video_id = full_url.split('/')[-1]
        short_url = 'https://youtu.be/' + video_id
        return short_url

    else:
        return None

if __name__ == "__main__":
    main()


    
