#
# @lc app=leetcode id=2353 lang=python3
#
# [2353] Design a Food Rating System
#

# @lc code=start
import heapq
from collections import defaultdict
from typing import List


class Food:
    name: str
    cuisine: str
    rating: int

    def __init__(self, name: str, cuisine: str, rating: int):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating

    def __lt__(self, other: 'Food'):
        if self.rating == other.rating:
            return self.name < other.name
        return self.rating > other.rating


class FoodRatings:
    mapping: dict[Food] = {}
    cuisine_mapping: dict[str, Food] = defaultdict(list)

    def __init__(
        self,
        names: List[str],
        cuisines: List[str],
        ratings: List[int],
    ):
        self.mapping = {}
        self.cuisine_mapping = defaultdict(list)

        for name, cuisine, rating in zip(names, cuisines, ratings):
            food = Food(name, cuisine, rating)
            self.mapping[name] = food
            heapq.heappush(self.cuisine_mapping[cuisine], food)

    def changeRating(self, name: str, newRating: int) -> None:
        old = self.mapping[name]
        new = Food(name, old.cuisine, newRating)

        self.mapping[name] = new
        heapq.heappush(self.cuisine_mapping[old.cuisine], new)

    def highestRated(self, cuisine: str) -> str:
        highest = self.cuisine_mapping[cuisine][0]

        while highest != self.mapping[highest.name]:
            heapq.heappop(self.cuisine_mapping[cuisine])
            highest = self.cuisine_mapping[cuisine][0]

        return highest.name


# @lc code=end
