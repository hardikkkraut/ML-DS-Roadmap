import pandas as pd

def demographic_data_analyzer():
    df = pd.read_csv("adult_sample.csv")

    # ✅ Strip whitespace from all string columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # ✅ Debug: Show cleaned salary values
    print("Unique salary values:", df["salary"].unique())

    # 1. Race count
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelors degree
    percentage_bachelors = round((df["education"] == "Bachelors").sum() / len(df) * 100, 1)

    # 4. Advanced education and >50K
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round(df[higher_education]["salary"].eq(">50K").mean() * 100, 1)

    # 5. Without advanced education and >50K
    lower_education_rich = round(df[~higher_education]["salary"].eq(">50K").mean() * 100, 1)

    # 6. Min work hours
    min_work_hours = df["hours-per-week"].min()

    # 7. % earning >50K among those who work min hours
    rich_percentage = round(
        df[df["hours-per-week"] == min_work_hours]["salary"].eq(">50K").mean() * 100, 1)

    # 8. Country with highest % earning >50K
    country_earnings = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack().fillna(0)

    # Debug: Check columns in country_earnings
    print("Columns in country_earnings:", country_earnings.columns)

    # ✅ Find correct '>50K' column even if there's a space
    salary_column = [col for col in country_earnings.columns if ">50K" in col][0]
    highest_earning_country = country_earnings[salary_column].idxmax()
    highest_earning_country_percentage = round(country_earnings[salary_column].max() * 100, 1)

    # 9. Top occupation for those >50K in India
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
