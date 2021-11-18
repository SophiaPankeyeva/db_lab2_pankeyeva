-- Кількість їжі кожного типу
SELECT DISTINCT(ft.food_type_name),COUNT(f.food_name) FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id   GROUP BY ft.food_type_name

--Кількість калорій по кожному продукту

SELECT f.food_name, SUM(Cals_per100grams) AS sum_of_calories  FROM food f  JOIN energy_values_of_food e  ON f.food_id = e.food_id
GROUP BY f.food_name

--Зв'язок між типом їжі і кількістю калорій
SELECT ft.food_type_name,e.Cals_per100grams FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id JOIN energy_values_of_food e ON  f.food_id = e.food_id  
