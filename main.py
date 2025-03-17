import requests
import time

base_url = "https://leetcode-api-faisalshohag.vercel.app/"

def get_user_info(username):
    url = f"{base_url}/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data

    #if response.status_code == 429: print(int(response.headers["Retry-After"]))


def create_output(students):
    c = 1
    wait_for = 4.75

    open("output.txt", "w").close()
    with open("output.txt", "a") as f:

        for student in students:
            objectt = student
            student_info = get_user_info(objectt)

            easy = f'Easy: {student_info["totalSubmissions"][1]["count"]}'
            medium = f'Medium: {student_info["totalSubmissions"][2]["count"]}'
            hard = f'Hard: {student_info["totalSubmissions"][3]["count"]}'

            f.write(f'{student}\n')
            f.write(f'{easy}\n')
            f.write(f'{medium}\n')
            f.write(f'{hard}\n')
            f.write('--------------------------\n')

            print(f'Collecting data... Estimated time - {round(len(students) * wait_for - c * wait_for, 1)} seconds')

            c += 1

            if c <= len(students):
                time.sleep(wait_for)
            else:
                print("Data collected! Check output file.")



users = ["DanzasZ", "BariaA", "marrib", "anastasia_vorontcova", "NataliaKaryakina", "KiselevITU", "NEMO_PETYX", "guess_whxo", "unloquacious", "ivanprokaev", "gtyrhe", "Piledryan", "SofiaRaicheva", "ananam", "skluar", "liuweer", "codedima", "ArianaTolokontseva", "Anna_Trashkova", "Arina_Fedosikhina", "Marina2525", "JustWin4ik", "shafeevaalisa", "ianmiroshnikov1", "Kseniya17"]
create_output(users)



