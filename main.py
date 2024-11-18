from flask import Flask

import random

rasgele_bilgiler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
                        "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
                        "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
                        "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor."]

yazi_tura = ["yazi","tura"]

app = Flask(__name__)

@app.route("/")

def hello_world():

    return '<h1>Ana Sayfaya Hoşgeldin!</h1><a href="/ikinci">Rastgele Bir Gerçeği Görüntülek İçin Tıklayınız!</a>'

@app.route("/ikinci")

def ikinci():

    return f'<p>{random.choice(rasgele_bilgiler)}</p><a href="/">Ana Sayfaya Geri Dönmek İçin Tıklayınız!</a>'

@app.route("/yazitura")

def  yazı_tura():

    return '<h1>Yazı Turaya Hoşgeldin!</h1><a href="/yazituraikinci">Yazı Mı Tura Mı Görmek İçin Tıklayınız!</a>'

@app.route("/yazituraikinci")

def yazi_tura_ikinci():

    return f'<p>{random.choice(yazi_tura)}''<h1>Sonuç!</h1>'

app.run(debug=True)