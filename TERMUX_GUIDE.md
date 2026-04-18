# 📱 Termux Step-by-Step Installation Guide (Roman Hindi/Urdu)

OmniOperator AI ko Termux mein install karne ke liye ye steps follow karein. Har command ko ek-ek karke copy-paste karein.

### ⚠️ Shuru karne se pehle:
- Termux ko **F-Droid** se download karein (Play Store wala version purana hai).
- Internet connection fast hona chahiye.
- Phone mein kam se kam 2GB free space honi chahiye.

---

### Step 1: Termux ko Update aur Upgrade karein
Sabse pehle system ko latest packages pe lana zaroori hai. Termux kholte hi ye commands chalayein:

```bash
# Package list update karein
pkg update -y

# Packages upgrade karein (Agar koi sawal puche toh 'y' ya 'Enter' dabayein)
pkg upgrade -y
```

### Step 2: Storage Permission dein
Termux ko phone ki files access karne ki permission deni hogi:

```bash
termux-setup-storage
```
*(Phone screen pe pop-up aayega, 'Allow' par click karein)*

### Step 3: Zaroori Tools install karein
Ab hum Python aur doosre tools install karenge jo ONAIO ke liye zaroori hain:

```bash
# Zaroori system tools
pkg install python git nmap termux-api openssl libffi libcrypt clang make -y

# Python pip ko update karein
pip install --upgrade pip
```

### Step 4: Repository Clone karein
Ab project ko GitHub se apne Termux mein download karein:

```bash
git clone https://github.com/abdulraheemnohri/OmniNetworkAI.git
cd OmniNetworkAI
```

### Step 5: Requirements Install karein
Ab hum project ki sari libraries install karenge. Isme 2-5 minute lag sakte hain:

```bash
pip install -r requirements.txt
```

### Step 6: Configuration (Optional but Recommended)
Agar aapke paas AI API keys hain, toh unhe file mein save karein:

```bash
# File ko edit karne ke liye (nano editor use karein)
pkg install nano -y
# Phir 'nano config.json' likhein, keys daalein aur save karein
```
*(Save karne ke liye: Ctrl + O, Enter. Exit karne ke liye: Ctrl + X)*

---

### 🚀 Step 7: ONAIO Start Karein!
Sab kuch setup ho gaya hai. Ab aap system chala sakte hain:

```bash
# Hybrid Version chalane ke liye (Default)
python main.py --version 3
```

---

### ❓ Sawal aur Jawab (FAQs)

**Q: Kya mujhe naya tab kholna padega?**
A: Sirf tab jab aap Dashboard ya API server ko background mein chalana chahte hain. Default mode ke liye ek hi tab kaafi hai.

**Q: Agar 'Ollama' use karna ho?**
A: Termux mein Ollama thoda mushkil hai, lekin aap `scripts/setup_ollama.sh` try kar sakte hain agar aapka phone powerful hai.

**Q: Command ruk jaye toh kya karu?**
A: 'Ctrl + C' dabayein aur command ko dubara chalayein.

**Q: App band ho jaye toh?**
A: Termux khol kar dubara `cd OmniNetworkAI` aur phir `python main.py` chalayein.
