import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

quotes = {
    "quote1": {
        "author": "Joseph B. Wirthlin",
        "source": "Shall He Find Faith on the Earth?",
        "text": "Faith is not so much something we believe; faith is something we live."
    },
    "quote2": {
        "author": "Sheri L. Dew",
        "source": "If Life Were Easy, It Wouldn't Be Hard: And Other Reassuring Truths",
        "text": "We're not alone--at least, we're alone only if we choose to be alone. We're alone only if we choose to go through life relying solely on our own strength rather than learning to draw upon the power of God."
    },
    "quote3": {
        "author": "Henry B. Eyring",
        "source": "A Life Founded in Light and Truth",
        "text": "God not only loves the obedient - He enlightens them."
    },
    "quote4": {
        "author": "Joseph Smith",
        "source": "Times and Seasons, Aug. 15, 1842, 889",
        "text": "The exaltation and happiness of any community, goes hand in hand with the knowledge possessed by the people, when applied to laudable ends; whereupon we can exclaim like the wise man; righteousness exalteth a nation; for righteousness embraces knowledge and knowledge is power."
    },
    "quote5": {
        "author": "Brigham Young",
        "source": "Brigham Young: The Man and His Work",
        "text": "The worst fear that I have about [members of this Church] is that they will get rich in this country, forget God and his people, wax fat, and kick themselves out of the Church and go to hell. This people will stand mobbing, robbing, poverty, and all manner of persecution, and be true. But my greater fear for them is that they cannot stand wealth; and yet they have to be tried with riches"
    },
    "quote6": {
        "author": "Robert D. Hales",
        "source": "Waiting upon the Lord: Thy Will Be Done",
        "text": "Every one of us is more beloved than we can possibly understand or imagine. Let us therefore be kinder to one another and kinder to ourselves."
    },
    "quote7": {
        "author": "Thomas S. Monson",
        "source": "The Call for Courage",
        "text": "All men have their FEARS. But those who face their fears with FAITH have COURAGE as well."
    },
    "quote8": {
        "author": "Spencer W. Kimball",
        "source": "Modern Scientific Findings Harmonize with Revelation through the Ages (Salt Lake City: Deseret Book, 1962)",
        "text": "Modern scientific findings harmonize with revelation through the ages. No conflict exists between the gospel and any truth .... All true principles are a part of the gospel of Jesus Christ. There is no principle that we need to fear."
    },
    "quote9": {
        "author": "Brigham Young",
        "source": "Teachings of Presidents of the Church: Brigham Young (MSS, 15:48)",
        "text": "How do you feel, Saints, when you are filled with the power and love of God? You are just as happy as your bodies can bear."
    },
    "quote10": {
        "author": "Brigham Young",
        "source": "Teachings of Presidents of the Church: Brigham Young (DNSW, 30 June 1874, 1)",
        "text": "I say, if you want to enjoy exquisitely, become a Latter-day Saint, and then live the doctrine of Jesus Christ."
    }
}

def pick():       
    return random.choice(list(quotes.values()))

@app.get("/")
def read_root():
    return {
        "/quotes": "All quotes .json",
        "/randomquote": "Random quote .json"
    }

@app.get("/randomquote")
async def root():
    return pick()

@app.get("/quotes")
async def root():
    return quotes