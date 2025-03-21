#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        can_cook = dict.fromkeys(supplies, True)
        recipe_indexes = {r: i for i, r in enumerate(recipes)}

        def _dfs(recipe: str) -> bool:
            if recipe in can_cook:
                return can_cook[recipe]
            if recipe not in recipe_indexes:
                return False

            can_cook[recipe] = False  # prevent circular dependencies

            for ingredient in ingredients[recipe_indexes[recipe]]:
                if not _dfs(ingredient):
                    return False

            can_cook[recipe] = True
            return True

        return [r for r in recipes if _dfs(r)]


# @lc code=end
