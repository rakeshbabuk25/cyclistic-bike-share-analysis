# Data Cleaning Documentation

## Steps Performed

1. Merged 12 monthly datasets into a single dataframe
2. Converted started_at and ended_at to datetime format
3. Created new features:
   - ride_length (in minutes)
   - day_of_week
4. Removed:
   - Negative or zero-duration rides
   - Duplicate records
   - Rows with null values in critical columns
5. Exported cleaned dataset for analysis

## Notes
- File naming convention was standardized manually
- No schema inconsistencies detected across files