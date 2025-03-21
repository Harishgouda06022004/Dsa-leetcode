class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)  # Convert supplies to a set for quick lookups
        possible_recipes = set()      # Store recipes that can be made
        remaining = set(recipes)      # Keep track of recipes that are not yet made

        while True:
            new_recipes = set()
            for i, recipe in enumerate(recipes):
                if recipe in possible_recipes:  # Skip already made recipes
                    continue
                if all(ingredient in supplies_set for ingredient in ingredients[i]):
                    new_recipes.add(recipe)
            
            if not new_recipes:  # If no new recipes can be made, stop
                break

            supplies_set.update(new_recipes)  # Add newly made recipes to supplies
            possible_recipes.update(new_recipes)  # Store recipes that can be made
            remaining -= new_recipes  # Remove from remaining recipes

        return list(possible_recipes)
       
        