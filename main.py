import os
import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import gps
from gtts import gTTS
from kivy.utils import platform
BUS_STOPS = [
    {"name": "145 ဂိတ်", "lat": 17.0005490, "lon": 96.0519671},
    {"name": "ကွက်သစ်", "lat": 17.0010347, "lon": 96.0565487},
    {"name": "ဒဒွေး", "lat": 17.0013467, "lon": 96.0591484},
    {"name": "လှော်ကားအောက်ဂိတ်", "lat": 17.0013002, "lon": 96.0676077},
    {"name": "မိုးဆန်း", "lat": 16.9986156, "lon": 96.0683363},
    {"name": "တရုံးရှေ့", "lat": 16.9955385, "lon": 96.0693421},
    {"name": "အိမ်မဲကြီး", "lat": 16.9922302, "lon": 96.0702993},
    {"name": "အောင်မေတ္တာ", "lat": 16.9905484, "lon": 96.0707754},
    {"name": "အောင်ချမ်းသာ", "lat": 16.9889449, "lon": 96.0712669},
    {"name": "ဏဈေး(အောင်သုခ)", "lat": 16.9875042, "lon": 96.0717554},
    {"name": "ငြိမ်းချမ်းရေး", "lat": 16.9864332, "lon": 96.0718869},
    {"name": "အမိုးကြီး", "lat": 16.9845138, "lon": 96.0715663},
    {"name": "ဏကွေ့", "lat": 16.9829978, "lon": 96.0712378},
    {"name": "ရုံးရှေ့", "lat": 16.9825838, "lon": 96.0727847},
    {"name": "ကိုးသုံးလုံး", "lat": 16.9822946, "lon": 96.0742935},
    {"name": "ဆင်နှစ်ကောင်", "lat": 16.9818902, "lon": 96.0758270},
    {"name": "၃ ထိပ်", "lat": 16.9815590, "lon": 96.0774414},
    {"name": "ငမောက်ဈေး", "lat":16.9799746 , "lon": 96.0770193},
    {"name": "ဂိတ်ဟောင်း", "lat": 16.9779721, "lon": 96.0764248},
    {"name": "ရေချမ်းစင်", "lat": 16.9763729, "lon": 96.0760446},
    {"name": "နဝရတ်ဈေး", "lat": 16.9730094, "lon": 96.0759176},
    {"name": "ကျော်စွာ", "lat": 16.9714936, "lon": 96.0762921},
    {"name": "တော်ဝင်", "lat": 16.9686521, "lon": 96.0772094},
    {"name": "ရွှေညာမောင်", "lat": 16.9657951, "lon": 96.0783336},
    {"name": "ကားကြီးဂိတ်", "lat": 16.9631456, "lon": 96.0783855},
    {"name": "ဆေးခန်း", "lat": 16.9601426, "lon": 96.0773525},
    {"name": "ထန်းခြောက်ပင်", "lat": 16.9564017, "lon": 96.0778642},
    {"name": "ကားလေးဂိတ်", "lat": 16.9562433, "lon": 96.0807707},
    {"name": "၈၁ ဂိတ်", "lat": 16.9518063, "lon": 96.0821202},
    {"name": "ပျော်ဘွယ်", "lat": 16.9491281, "lon": 96.0827217},
    {"name": "ဇင်ယော်", "lat": 16.9473032, "lon": 96.0832752},
    {"name": "ပုလဲလမ်းဆုံ", "lat": 16.9439802, "lon": 96.0846498},
    {"name": "ဘုန်းကြီးကျောင်းကွေ့", "lat": 16.9409872, "lon": 96.0857851},
    {"name": "တံတားထိပ်", "lat": 16.9402483, "lon": 96.0868449},
    {"name": "၁၉၉ ဂိတ်ဟောင်း", "lat": 16.9389246, "lon": 96.0868536},
    {"name": "၁၄ လမ်းဆုံ", "lat": 16.9334433, "lon": 96.0878453},
    {"name": "ဒညင်းကုန်းဘူတာဈေး", "lat": 16.9334827, "lon": 96.0897202},
    {"name": "ဒညင်းကုန်းလမ်းဆုံ", "lat": 16.9323935, "lon": 96.1014552},
    {"name": "ဘိုခြံ", "lat": 16.9298904, "lon": 96.1010586},
    {"name": "ရွာသစ်", "lat": 16.9244537, "lon": 96.0981802},
    {"name": "အောင်ဆန်းဈေး", "lat": 16.9210970, "lon": 96.0974822},
    {"name": "ကျောင်းဂိတ်", "lat": 16.9189520, "lon": 96.0975057},
    {"name": "၁ ဂိတ်", "lat": 16.9150560, "lon": 96.0973189},
    {"name": "စောင်စက်ရုံ(၂)", "lat": 16.9106517, "lon": 96.0973145},
    {"name": "ဖော့ကန်ဈေး", "lat": 16.9080079, "lon": 96.0975670},
    {"name": "ဂျပန်လမ်း", "lat": 16.9045700, "lon": 96.0976267},
    {"name": "ပြည်တော်သာ", "lat": 16.9013800, "lon": 96.0969209},
    {"name": "သရက်တော", "lat": 16.9026783, "lon": 96.1040134},
    {"name": "ဘိုကုန်း", "lat": 16.9015725, "lon": 96.1060404},
    {"name": "ဟိုက်ပက်", "lat": 16.8991579, "lon": 96.1056881},
    {"name": "မညက", "lat": 16.8965995, "lon": 96.1051097},
    {"name": "အင်းစိန်ဆေးရုံ", "lat": 16.8923036, "lon": 96.1056555},
    {"name": "အင်းစိန်ပန်းခြံ", "lat": 16.8895709, "lon": 96.1066875},
    {"name": "ဘီအိုစီ", "lat": 16.8843092, "lon": 96.1103145},
    {"name": "ကြို့ကုန်း", "lat": 16.8787810, "lon": 96.1127976},
    {"name": "ဘီပီအိုင်(YTU)", "lat": 16.8744628, "lon": 96.1165456},
    {"name": "ခဝဲခြံ", "lat": 16.8696158, "lon": 96.1196523},
    {"name": "ကုလားကျောင်း", "lat": 16.8654996, "lon": 96.1207956},
    {"name": "သမိုင်းလမ်းဆုံ(Junction)", "lat": 16.8636165, "lon": 96.1213260},
    {"name": "ဘုရားလမ်း", "lat": 16.8581233, "lon": 96.1232917},
    {"name": "အုတ်ကျင်း", "lat": 16.8551274, "lon": 96.1238664},
    {"name": "ဘာတာ", "lat": 16.8506986, "lon": 96.1246429},
    {"name": "သံလမ်း", "lat": 16.8465900, "lon": 96.1255267},
    {"name": "သုခလမ်း", "lat": 16.8412539, "lon": 96.1265677},
    {"name": "ဘူတာရုံလမ်း", "lat": 16.8372032, "lon": 96.1277606},
    {"name": "ဆင်ရေတွင်း", "lat": 16.8344296, "lon": 96.1286199},
    {"name": "စံရိပ်ငြိမ်", "lat": 16.8309577, "lon": 96.1296026},
    {"name": "လှည်းတန်း", "lat": 16.8282177, "lon": 96.1304274},
    {"name": "စိုက်ပျိုးရေး", "lat": 16.8183331, "lon": 96.1330298},
    {"name": "ဟံသာဝတီအဝိုင်း", "lat": 16.8120222, "lon": 96.134900},
    {"name": "မဟာမြိုင်", "lat": 16.8085071, "lon": 96.1358887},
    {"name": "မြေနီကုန်း", "lat": 16.8069932, "lon": 96.1363390},
    {"name": "မြေနီကုန်း", "lat": 16.8037563, "lon": 96.1380197},
    {"name": "လင့်လမ်း", "lat": 16.8061382, "lon": 96.1473659},
    {"name": "အုတ်လမ်း", "lat": 16.8044615, "lon": 96.1515860},
    {"name": "ရွှေဂုံတိုင်", "lat": 16.8066738, "lon": 96.1560509},
    {"name": "ဗန်ဒါပင်", "lat": 16.8100111, "lon": 96.1601315},
    {"name": "၅ ထပ်ကြီး", "lat": 16.8104078, "lon": 96.1625214},
    {"name": "၆ ထပ်ကြီး", "lat":16.8112143 , "lon": 96.1654584},
    {"name": "တာမွေအဝိုင်း", "lat": 16.8116871, "lon": 96.1701338},
    {"name": "တာမွေပလာဇာ", "lat": 16.8107287, "lon": 96.1748337},
    {"name": "တာမွေဈေး", "lat": 16.8077057, "lon": 96.1762694},
    {"name": "ကျောက်မြောင်းဈေး", "lat": 16.8032935, "lon": 96.1747828},
    {"name": "သီတာ", "lat": 16.7994769, "lon": 96.1756954},
    {"name": "အောင်မင်္ဂလာ", "lat": 16.7964030, "lon": 96.1767646},
    {"name": "ယုဇနပလာဇာ", "lat": 16.7942316, "lon": 96.1753853},
    {"name": "မင်္ဂလာဈေး", "lat": 16.7919434, "lon": 96.1745353},
    {"name": "ပုဇွန်တောင်စာတိုက်", "lat": 16.7846653, "lon": 96.1750607},
    {"name": "ပုဇွန်တောင်ဈေး", "lat": 16.7817584, "lon": 96.1747154},
    {"name": "၅၀ ကွေ့", "lat": 16.7787943, "lon": 96.1716255},
    {"name": "ဗိုလ်တထောင်ဘုရား", "lat": 16.7693729, "lon": 96.1758332}
]
class BusAnnouncerApp(App): 
    def build(self): 
         self.announced_stops = set() 
         self.layout = BoxLayout(orientation='vertical', padding=20) 
         self.status_label = Label(text="၁၄၅ လမ်းကြောင်း GPS စနစ် စတင်နေပါသည်...", font_size='16sp')
         self.layout.add_widget(self.status_label) 
         if platform == "android":
             self.request_android_permissions() 
         try:
             gps.configure(on_location=self.on_location, on_status=self.on_status)
             gps.start(minTime=1000, minDistance=1)
         except NotImplementedError: self.status_label.text = "GPS စနစ် မရရှိနိုင်ပါ (Windows/Emulator ဖြစ်နိုင်ပါသည်)"
         return self.layout
    def request_android_permissions(self):
         from kivy.utils import platform
         if platform == "android":
                android_permissions = __import__('android.permissions', fromlist=['request_permissions', 'Permission'])
                request_permissions = android_permissions.request_permissions
                Permissions = android_permissions.Permission
                request_permissions([Permissions.ACCESS_FINE_LOCATION, Permissions.ACCESS_COARSE_LOCATION, Permissions.ACCESS_BACK16.GROUND_LOCATION])
    def on_status(self, stype, status): 
        self.status_label.text = f"GPS အခြေအနေ: {status}"
    def on_location(self, **kwargs): 
        current_lat = kwargs.get('lat') 
        current_lon = kwargs.get('lon') 
        self.status_label.text = f"လက်ရှိနေရာ - Lat: {current_lat:.4f}, Lon: {current_lon:.4f}"
        for stop in BUS_STOPS:
            if stop["lat"] == 0.0 and stop["lon"] == 0.0:
                continue
            distance = self.calculate_distance(current_lat, current_lon, stop["lat"], stop["lon"])
            if distance <= 0.07 and stop["name"] not in self.announced_stops:
                 self.speak(f"နောက်မှတ်တိုင်သည် {stop['name']} ဖြစ်ပါသည်") 
                 self.announced_stops.add(stop["name"])
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)
        a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance
    def speak(self, text):
        tts = gTTS(text=text, lang='my')
        audio_file = "announcement.mp3"
        tts.save(audio_file)
        if platform == "android":
            os.system(f"start -a android.intent.action.VIEW -d file://{os.path.abspath(audio_file)} -t audio/mp3")
        else:
            os.system(f"start {audio_file}")
if __name__ == "__main__":
    BusAnnouncerApp().run()