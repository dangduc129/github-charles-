class Playlist: 
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description 
        self.rating = rating 
        self.videos = videos

class Video: 
    def __init__(self, title, link): 
        self.title = title
        self.link = link 

def read_video(): # input title, link
    title = input('Enter title: ') + '\n'
    link = input('Enter link: ') + '\n'
    video = Video(title, link)
    return video

def print_video(video):
    print('Video title: ', video.title, end ="" ) 
    print('Video link: ', video.link, end = "") 

def write_video_txt(video, file):  
    file.write(video.title )
    file.write(video.link )

def read_video_from_txt(file):  
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video
    
def read_videos(): #create list 
    videos = []
    total_video = int(input('How many video: '))
    for i in range(total_video): 
        print("Video ", i+1)
        vid = read_video()
        videos.append(vid)
    return videos

def write_videos_txt(videos,file):
    file.write(str(len(videos)) + '\n')
    for i in range(len(videos)): 
        write_video_txt(videos[i], file)

def read_videos_from_txt(file): 
    videos = []
    Total = file.readline()
    for i in range(int(Total)): 
    return videos

def print_videos(videos): 
    for i in range(len(videos)):
        print("Video", i+1)
        print_video(videos[i])

def read_playlist():
    playlist_name = input("Enter playlist name: ") +'\n' #backwark slash/ forword slash /
    playlist_description = input("Enter playlist description: ") + '\n'
    playlist_rating = input("Enter playlist rating (1-5): ") + '\n'
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def write_playlist_txt(playlist): 
    with open("data.txt", 'w') as file: 
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_videos_txt(playlist.videos, file)
    print("Successfully write playlist to text")

def read_playlist_from_txt(): 
    with open('data.txt', 'r') as file: 
        playlist_name = file.readline() 
        playlist_description = file.readline()
        playlist_rating = file.readline()
        playlist_videos = read_videos_from_txt(file)
        playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def print_playlist(playlist): 
    print("-------------")
    print('Playlist name: ',playlist.name, end="")
    print('Playlist description: ',playlist.description, end="")
    print('Playlist rating: ',playlist.rating, end="")
    print_videos(playlist.videos)

def show_menu(): 
    print("Main menu: ")
    print("|--------------------------|")
    print("|Option 1: Create playlist |")
    print("|Option 2: Show playlist   |")
    print("|Option 3: Play a video    |")
    print("|Option 7: Save and exit   |")
    print("|--------------------------|")

def select_in_range(prompt, min, max): 
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max: 
        choice = input(prompt)

    choice = int(choice)
    return choice 

def play_video(playlist): 
    print_videos(playlist.videos)
    total = len(playlist.videos)

    choice = select_in_range("Select a video : ", 1, total)
    print("Open video: " + playlist.videos[choice-1].title + '-' + playlist.videos[choice-1].link, end="")
def main():
    # videos = read_videos()
    # write_videos_txt(videos)
    # videos = read_videos_from_txt()
    # print_videos(videos)
    
    # playlist = read_playlist()
    # write_playlist_txt(playlist)
    # playlist = read_playlist_from_txt()
    # print_playlist(playlist)
    try: 
        playlist = read_playlist_from_txt()
        print("Loaded data successfully")
    except: 
        print("Welcome first user !!!")
    while True: 
        show_menu()
        choice = select_in_range("Select an option (1-7): ", 1, 7)
        if choice == 1: 
            playlist = read_playlist()
            input("\nPress Enter to continue \n")
        elif choice == 2: 
            print_playlist(playlist)
            input("\nPress Enter to continue \n")
        elif choice == 3: 
            play_video(playlist)
            input("\nPress Enter to continue \n")
        # elif choice == 4: 
        #     menu_option_4()
        # elif choice == 5: 
        #     menu_option_5()
        # elif choice == 6: 
        #     menu_option_6()
        elif choice == 7: 
            write_playlist_txt(playlist)
            input("\nPress Enter to continue.")
            break
        else: 
            print("Wrong Input, Exist.")
            break 
main()