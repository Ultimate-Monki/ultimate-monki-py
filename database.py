import pymongo
from pymongo import MongoClient


client = MongoClient("MongoDB URI")
db = client.monkibot
member_profiles = db.member_profiles


def members():
    member = list(db.member_profiles.find({}))
    return member


def add_member(profile):
    member_profiles.insert_one(profile)


def find_member(member):
    member = member_profiles.find_one({"member_id": member})
    return member


def inc_bal(member, amt):
    member_profiles.update_one({"member_id": member}, {"$inc": {"balance": amt}})


def set_bal(member, amt):
    member_profiles.update_one({"member_id": member}, {"$set": {"balance": amt}})


def get_bal(member):
    member = member_profiles.find_one({"member_id": member})
    bal = member["balance"]
    return bal


# member_profiles.update_many(
#     {},
#     {"$set": {"welcome_message": "Hey {user.mention} welcome to {guild.name}"}},
#     upsert=False,
#     array_filters=None,
# )

