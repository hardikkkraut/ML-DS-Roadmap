import pandas as pd

def demographic_data_analyzer():
    df = pd.read_csv("adult_sample.csv")

    # ✅ Strip whitespace from all object (string) columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # ✅ Debug: Check salary values
    print("Unique salary values:", df["salary"].unique())

    # 1. Race count
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelors degree
    percentage_bachelors = round((df["education"] == "Bachelors").sum() / len(df) * 100, 1)

    # 4. Advanced education and >50K
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round(
        df[higher_education]["salary"].eq(">50K").mean() * 100, 1
    ) if ">50K" in df["salary"].unique() else 0.0

    # 5. Without advanced education and >50K
    lower_education_rich = round(
        df[~higher_education]["salary"].eq(">50K").mean() * 100, 1
    ) if ">50K" in df["salary"].unique() else 0.0

    # 6. Minimum work hours
    min_work_hours = df["hours-per-week"].min()

    # 7. % earning >50K among those who work minimum hours
    min_hour_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        min_hour_workers["salary"].eq(">50K").mean() * 100, 1
    ) if not min_hour_workers.empty and ">50K" in df["salary"].unique() else 0.0

    # 8. Country with highest % earning >50K
    country_earnings = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack().fillna(0)
    print("Columns in country_earnings:", country_earnings.columns)

    if ">50K" in country_earnings.columns:
        highest_earning_country = country_earnings[">50K"].idxmax()
        highest_earning_country_percentage = round(country_earnings[">50K"].max() * 100, 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0.0

    # 9. Most popular occupation for those >50K in India
    india_high_earners = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_high_earners["occupation"].mode()[0] if not india_high_earners.empty else None

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
