from flask import Flask, render_template, request

app = Flask(__name__)

# Friends list for Deepak and Dheeraj
DEEPAK_FRIENDS = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun",
    "Sai", "Aryan", "Krishna", "Ishaan", "Kabir",
    "Rohan", "Neha", "Meera", "Tanvi", "Siddharth"
]
DHEERAJ_FRIENDS = [
    "Kabir", "Arjun", "Aryan", "Krishna", "Ishaan",
    "Rohan", "Neha", "Saanvi", "Myra", "Diya",
    "Aanya", "Anaya", "Vihaan", "Vivaan", "Siddharth"
]

def find_common_friends():
    return list(set(DEEPAK_FRIENDS) & set(DHEERAJ_FRIENDS))

@app.route('/', methods=['GET', 'POST'])
def index():
    common_friends = []
    searched_common = []
    if request.method == 'POST':
        search_name = request.form.get('search_name', '').strip()
        common_friends = find_common_friends()
        
        if search_name in common_friends:
            searched_common.append(search_name)
    
    return render_template('index.html', 
                           deepak_friends=DEEPAK_FRIENDS, 
                           dheeraj_friends=DHEERAJ_FRIENDS, 
                           common_friends=common_friends, 
                           searched_common=searched_common)

if __name__ == '__main__':
    app.run(debug=True)
