# -*- coding: utf-8 -*-
__author__ = 'gerson64'

from stemming.porter2 import stem
import twitterImport


def unique(inList):
    return list(set(inList))

    food_words = ["Acidic", "Acrid", "Aged", "Bitter", "Bittersweet", "Bland", "Burnt", "Buttery", "Chalky", "Cheesy",
                  "Chewy",
                  "Chocolaty", "Citrusy", "Cool", "Creamy", "Crispy", "Crumbly", "Crunchy", "Crusty", "Doughy", "Dry",
                  "Earthy", "Eggy",
                  "Fatty", "Fermented", "Fiery", "Fishy", "Fizzy", "Flakey", "Flat", "Flavorful", "Fresh", "Fried",
                  "Fruity",
                  "Full-bodied", "Gamey", "(refers", "to", "the", "flavor", "or", "strong", "odor", "of", "game,",
                  "like", "Elk", "or",
                  "Deer.", "Garlicky", "Gelatinous", "Gingery", "Glazed", "Grainy", "Greasy", "Gooey", "Gritty",
                  "Harsh", "Hearty",
                  "Heavy", "Herbal", "Hot", "Icy", "Infused", "Juicy", "Lean", "Light", "Lemony", "Malty", "Mashed",
                  "Meaty", "Mellow",
                  "Mild", "Minty", "Moist", "Mushy", "Nutty", "Oily", "Oniony", "Overripe", "Pasty", "Peppery",
                  "Pickled", "Plain",
                  "Powdery", "Raw", "Refreshing", "Rich", "Ripe", "Roasted", "Robust", "Rubbery", "Runny", "Salty",
                  "Sautéed", "Savory",
                  "Seared", "Seasoned", "Sharp", "Silky", "Slimy", "Smokey", "Smothered", "Smooth", "Soggy", "Soupy",
                  "Sour", "Spicy",
                  "Spongy", "Stale", "Sticky", "Stale", "Stringy", "Strong", "Sugary", "or", "sweet", "Sweet-and-sour",
                  "Syrupy",
                  "Tangy", "Tart", "Tasteless", "Tender", "Toasted", "Tough", "Unflavored", "Unseasoned", "Velvety",
                  "Vinegary",
                  "Watery", "Whipped", "Woody", "Yeasty", "Zesty", "Zingy"]
    food_words = [stem(word) for word in food_words]


def foodwordList(keyword):
    tweets = twitterImport.getTweets(keyword)
    tmpList = []
    for tweet in tweets['statuses']:
        tmpList.append([stem(word) for word in tweet['text'].split(" ")])
    finalList = []
    for list in tmpList:
        finalList = finalList + list
    return finalList