import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#		URL : https://www.bordeaux-tourisme.com/ville-patrimoine/sites-monuments.html
#		liste des sites et monuments en gironde 


#		exemple d'un élément à scope : 
#		.ListSit-item.js-list-sit-item

#		<div class="ListSit-item js-list-sit-item" data-id="2864">
#			<a href="https://www.bordeaux-tourisme.com/patrimoine-culturel/darwin-caserne-niel.html" class="Card  isLeaf">
#							<div class="Card-durable">
#						<svg>
#							<use xlink:href="/themes/bordeaux_tourisme/assets/img/symbols.svg#leaf"></use>
#						</svg>
#					</div>
#						<div class="Card-img">
#					<img class="swiper-lazy lazyloaded ls-is-cached" width="328" height="222" alt="" title="Nicolas-Duffaure" loading="lazy" src="/sites/bordeaux_tourisme/files/styles/sit_teaser_image/public/externals/25f234dc328caa891076ece47ada6e4d.jpg.webp?itok=6TjW6kVC">
#
#				</div>
#				<div class="Card-bodyWrapper">
#
#					<div class="Card-body">
#						<p class="Card-title">Darwin / Caserne Niel</p>
#
#						<div class="Card-label">
#							Site / monument
#						</div>
#					</div>
#				</div>
#			</a>
#		</div>


url = "https://www.bordeaux-tourisme.com/ville-patrimoine/sites-monuments.html"
headers = {
	#		faux user agent 
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


#		raw html de la page
response = requests.get (url , headers = headers)
raw = BeautifulSoup (response.text , 'html.parser')


#		éléments à scope
scope_el = raw.select ('.ListSit-item.js-list-sit-item')

#		object avec les données 
result = [ ]
for el in scope_el : 
	title = el.select_one ('.Card-title').text.strip ()
    label = el.select_one ('.Card-label').text.strip ()
    
	result.append ({
        "nom" : title ,
        "categorie" : label
    })