# Welcome to APIs
#### Here you will get some free APIs. Feel free to use
**(Please use alternative domain in case heroku is not working: https://virajapi.vercel.app/)** 

* **WebToPDF: Converts web pages into PDF**
  * Base Link = https://virajapi.herokuapp.com/webtopdf/?url={Your- URL}
  * Example =  https://virajapi.herokuapp.com/webtopdf/?url=https://www.google.com

* **Bank IFSC Info: Provides Bank Information From IFSC Code**
  * Base Link = https://virajapi.herokuapp.com/ifsc/?query={IFSC-Code}
  * Example =  https://virajapi.herokuapp.com/ifsc/?query=PYTM0123456 \
  ```
    {
        "ADDRESS": "B-121, Sector-5,Noida-201301",
        "BANK": "Paytm Payments Bank",
        "BANKCODE": "PYTM",
        "BRANCH": "Noida Branch",
        "CENTRE": "NOIDA",
        "CITY": "NOIDA",
        "CONTACT": "01133996699",
        "DISTRICT": "Gautam Buddh Nagar",
        "IFSC": "PYTM0123456",
        "IMPS": true,
        "MICR": "NA",
        "NEFT": true,
        "RTGS": true,
        "STATE": "UTTAR PRADESH",
        "UPI": true
      }
  ```
* **Random Person Info: Gives random information about random person**
  * Base Link = https://virajapi.herokuapp.com/random/
  * Example =  https://virajapi.herokuapp.com/random/
  ```
  { "person":{"education":{"certificate":"PhD","university":"Sharif University"},"marriage":{"children":4,"married":true,"spouse_name":"Kitti"},"online_info":{"email":"18u0zw@riseup.net","ip_address":"58.154.71.127","ipv6_address":"d832:7e34:d8ef:745f:f388:e98e:f13a:b4fc","password":"U6eyCln9T5","password_md5":"e526c41e93760bda7ff46ca8602dabbd","user_agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.3.172 Yowser/2.5 Safari/537.36","username":"u1l913"},"personal":{"age":43,"blood":"B+","born":null,"born_place":"Hong Kong","cellphone":"+3744860329","city":"Venice","country":"Armenia","eye_color":"Green","father_name":"Hesther","gender":"Female","height":"1.73","last_name":"Stewart","name":"Daffi","national_code":"6571503451","religion":"Muslim","system_id":"a300e77f-6276-482f-b5b2-d5bf4759125e","weight":124},"work":{"country_code":"AL","insurance":true,"position":"Graphist","salary":"$11.200"}}}
  ```
  
* **URL Shortner: Shortens the URL**
  * Base Link = https://virajapi.herokuapp.com/url/?url={Your- URL}
  * Example =  https://virajapi.herokuapp.com/url/?url=https://www.facebook.com
  ```
  {"result_url":"https://cleanuri.com/a79JWN"}
  ```
* **Movie API: Provides information about movies from their name**
  * Base Link = https://virajapi.herokuapp.com/movie/?query={Movie-Name}
  * Example =  https://virajapi.herokuapp.com/movie/?query=Alive
  ```
  {"Response":"True","Search":[{"Poster":"https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg","Title":"Harry Potter and the Deathly Hallows: Part 2","Type":"movie","Year":"2011","imdbID":"tt1201607"},{"Poster":"https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SX300.jpg","Title":"Harry Potter and the Sorcerer's Stone","Type":"movie","Year":"2001","imdbID":"tt0241527"},{"Poster":"https://m.media-amazon.com/images/M/MV5BMTcxODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_SX300.jpg","Title":"Harry Potter and the Chamber of Secrets","Type":"movie","Year":"2002","imdbID":"tt0295297"},{"Poster":"https://m.media-amazon.com/images/M/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_SX300.jpg","Title":"Harry Potter and the Prisoner of Azkaban","Type":"movie","Year":"2004","imdbID":"tt0304141"},{"Poster":"https://m.media-amazon.com/images/M/MV5BMTI1NDMyMjExOF5BMl5BanBnXkFtZTcwOTc4MjQzMQ@@._V1_SX300.jpg","Title":"Harry Potter and the Goblet of Fire","Type":"movie","Year":"2005","imdbID":"tt0330373"},{"Poster":"https://m.media-amazon.com/images/M/MV5BMTM0NTczMTUzOV5BMl5BanBnXkFtZTYwMzIxNTg3._V1_SX300.jpg","Title":"Harry Potter and the Order of the Phoenix","Type":"movie","Year":"2007","imdbID":"tt0373889"},{"Poster":"https://m.media-amazon.com/images/M/MV5BMTQ2OTE1Mjk0N15BMl5BanBnXkFtZTcwODE3MDAwNA@@._V1_SX300.jpg","Title":"Harry Potter and the Deathly Hallows: Part 1","Type":"movie","Year":"2010","imdbID":"tt0926084"},{"Poster":"https://m.media-amazon.com/images/M/MV5BNzU3NDg4NTAyNV5BMl5BanBnXkFtZTcwOTg2ODg1Mg@@._V1_SX300.jpg","Title":"Harry Potter and the Half-Blood Prince","Type":"movie","Year":"2009","imdbID":"tt0417741"},{"Poster":"https://m.media-amazon.com/images/M/MV5BNTM4NzQ2NjA4NV5BMl5BanBnXkFtZTgwODAwMjE4MDE@._V1_SX300.jpg","Title":"Harry Potter and the Chamber of Secrets","Type":"game","Year":"2002","imdbID":"tt0304140"},{"Poster":"https://m.media-amazon.com/images/M/MV5BNDM0YzMyNGUtMTU1Yy00OTE2LWE5NzYtZDZhMTBmN2RkNjg3XkEyXkFqcGdeQXVyMzU5NjU1MDA@._V1_SX300.jpg","Title":"Harry Potter and the Forbidden Journey","Type":"movie","Year":"2010","imdbID":"tt1756545"}],"totalResults":"98"}
  ```
* **Songs API: Search Songs and get direct download link with other info**
  * Base Link = https://virajapi.herokuapp.com/songs/?query={Song-Name}
  * Example =  https://virajapi.herokuapp.com/songs/?query=Alone
  ```
  {
    "song1": {
        "Artist": "Marshmello, Pritam",
        "Description": "2019 · Hindi Film · Marshmello, Pritam",
        "Image": "https://c.saavncdn.com/987/BIBA-Unknown-2019-20200813225958-50x50.jpg",
        "Title": "BIBA",
        "URL": "https://aac.saavncdn.com/987/03f9cd50555cbf24f251b195afaceb92_96.mp4"
      },
    "song2": {
        "Artist": "Marshmello",
        "Description": "2019 · English Album · Marshmello",
        "Image": "https://c.saavncdn.com/783/Rescue-Me-English-2019-20190702093952-50x50.jpg",
        "Title": "Rescue Me",
        "URL": "https://aac.saavncdn.com/783/b1de9ca6c09a7661c36ddfc56d473808_96.mp4"
      }
  }
  ```
* **Corona API: Provides information about Alive, Confirmed, Death cases country-wise**
  * Base Link = https://virajapi.herokuapp.com/corona/?query={country-name}
  * Example =  https://virajapi.herokuapp.com/corona/?query=india
  ```
  {"Active Cases ":"9,636,849","Death Cases ":"140,072","Recovered ":"9,091,418"}
  ```
* **Message Encryption API: Encrypts and decrypts messages**
  * Base Link
  * Encryption = https://virajapi.herokuapp.com/message/?encrypt={Your-Message}
  * Example = https://virajapi.herokuapp.com/message/?encrypt=Hello
  ```
  {"encrypted_message":"b'gAAAAABfy_r6QHzWMTn4RgswjhOAGhMvC4-nEX7q76ku4Dlp3O215khP4OZtYiIfWGHTb197lQch_B5Zx3qMXg3m0hxgCFLDMw==' b'SlVQlv2zDu4kfyUqaIyksZ19rRgmcQHGSf7-r9-B21M='"}
  ```
  * Decryption = https://virajapi.herokuapp.com/message/?decrypt={Encrypted-Message}
  ```
  {"decrypted_message":"hi"}
  ```
* **Instant Mail API: you can instantly generate disposable temporary email address and immediately receive emails, including attachments**
  * Generate Email
    * Base URL = https://virajapi.herokuapp.com/mail/gen/ 
    ```
    {"mail":"2aampa4ibja@1secmail.org"}
    ```
  * Read Mail:
    * Base URL = https://virajapi.herokuapp.com/mail/msg/?email={Email}
    * Example =  https://virajapi.herokuapp.com/mail/msg/?email=zdd60gc43g@1secmail.com
