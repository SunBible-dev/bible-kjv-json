# Bible - King James Version
🍴 forked from https://github.com/aruljohn/Bible-kjv

+ Contains all the 66 books of the Old Testament and New Testament
+ Each book is in a separate JSON file as a JSON object
+ `Books.json` contains all 66 book names as a JSON array

NEW
+ `red-letter-json` - Contains red-letter text references
+ `contents.json` - Contains all the books and chapters and verses in the bible


---

### JSON x SUNBIBLE

as of April 2025 sunbible uses html, I plan to make the move to making a ui that uses this json database. I also want to make this database more accesable over the blockchain and over ipfs.

I want to thank  Arul John making this json database and putting it on github.

how i might use it in my ui
- give every word an id
- create a red letter json


### Who needs an api
when you have the data?
this json contains mininmal data, but for my ui i will be giving every word an id, up to you to decide what id fromat you want to use. but here is an id fromat that i plan to use

b1c1v1w1 = genesis 1:1 word 1

my ui will probably have a lot of code to help define the id's and get the data from this json.


### IPFS

```sh
# ipfs car
ipfs-car pack bible-kjv-json --output bible-kjv-json.car
ipfs-car pack red-letters-kjv-json --output red-letters-kjv-json.car

# w3
w3 space use SUNBIBLE
w3 up bible-kjv-json
w3 up red-letters-kjv-json

# near fs
npx nearfs-upload ./bible-kjv-json.car --account-id sunbible.testnet
npx nearfs-upload ./bible-kjv-json --account-id sunbible.testnet
```

bible-kjv-json
<br/>
bafybeiddtdnmeha6kyusdxpabkjecaxfuiwke57hznv4o4vsrti5l5rqoa
https://w3s.link/ipfs/bafybeiddtdnmeha6kyusdxpabkjecaxfuiwke57hznv4o4vsrti5l5rqoa

red-letters-kjv-json
<br/>
bafybeia3cis7aa523o2alefwkdnolfzpkrxbpy3eizeylgpgflfwlkc6ge
 https://w3s.link/ipfs/bafybeia3cis7aa523o2alefwkdnolfzpkrxbpy3eizeylgpgflfwlkc6ge

 near ipfs
- https://ipfs.web4.testnet.page/ipfs/<CID_here>
- https://<CID_here>.ipfs.web4.testnet.page
- https://ipfs.web4.near.page/ipfs/<CID_here>
- https://<CID_here>.ipfs.web4.near.page

---


copyright 2025 by The SunShining
