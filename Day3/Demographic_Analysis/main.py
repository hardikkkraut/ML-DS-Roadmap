from demographic_data_analyzer import demographic_data_analyzer

# Run the analysis
result = demographic_data_analyzer()

# Print results
for key, value in result.items():
    print(f"{key}:")
    print(value)
    print()
