# 🌱 Pandas Functions and Methods Guide 🌱

## 📊 DataFrame & Series Creation

### **Creation**

- `pd.DataFrame(data)` — Create a DataFrame from a dictionary, list, or NumPy array.
- `pd.Series(data)` — Create a Series.
- `pd.read_csv(filepath)` — Read a CSV file into a DataFrame.
- `df.to_csv(filepath)` — Write a DataFrame to a CSV file.
- `pd.read_excel(filepath)` — Read an Excel file into a DataFrame.
- `df.to_excel(filepath)` — Write a DataFrame to an Excel file.
- `pd.read_sql(query, con)` — Read SQL query results into a DataFrame.
- `df.to_sql(name, con)` — Write a DataFrame to a SQL database.

---

## 🧐 Data Inspection

### **Basic Inspection**

- `df.head(n)` — Return the first `n` rows (default is 5).
- `df.tail(n)` — Return the last `n` rows (default is 5).
- `df.shape` — Return a tuple representing the dimensionality of the DataFrame.
- `df.columns` — Return the column labels.
- `df.index` — Return the row labels (indices).
- `df.dtypes` — Return data types of each column.
- `df.info()` — Display summary information about DataFrame.
- `df.describe()` — Generate descriptive statistics for numeric columns.
- `df.memory_usage()` — Get memory usage of DataFrame columns.
- `df.sample(n)` — Return `n` random rows from the DataFrame.
- `df.value_counts()` — Count occurrences of unique values in a Series.
- `df.nunique()` — Count unique values per column.

---

## 🔎 Selecting Data

### **Column/Row Selection**

- `df['column']` — Select a column by name.
- `df[['col1', 'col2']]` — Select multiple columns.
- `df.iloc[]` — Access rows and columns by integer position.
- `df.loc[]` — Access rows and columns by label.
- `df.at[]` — Access a single value by row label and column label.
- `df.iat[]` — Access a single value by row index and column index.
- `df['column'] == value` — Filter rows based on column value.
- `df.query('condition')` — Query the DataFrame using a condition (e.g., `df.query('Age > 30')`).

### **Slicing**

- `df[2:5]` — Slice the DataFrame from row 2 to row 4.
- `df.iloc[1:3, 2:4]` — Slice rows and columns by index position.
- `df.loc[1:3, 'col1':'col3']` — Slice rows and columns by label.

---

## 🧹 Data Manipulation

### **Data Cleaning**

- `df.isnull()` — Check for missing values (NaN).
- `df.notnull()` — Check for non-missing values.
- `df.dropna()` — Remove rows with missing values.
- `df.fillna(value)` — Fill missing values with a specified value.
- `df.replace(to_replace, value)` — Replace values in a DataFrame.
- `df.rename(columns={'old_name': 'new_name'})` — Rename columns.
- `df.astype('new_dtype')` — Convert a column to a different data type.
- `df.duplicated()` — Check for duplicate rows.
- `df.drop_duplicates()` — Remove duplicate rows.
- `df.apply(func)` — Apply a function to each element of a column.
- `df.applymap(func)` — Apply a function element-wise for the entire DataFrame.
- `df.map(func)` — Map values to a series.

### **Dealing with Time Series**

- `pd.to_datetime(df['col'])` — Convert a column to datetime format.
- `df['col'].dt.year` — Extract the year from a datetime column.
- `df['col'].dt.month` — Extract the month from a datetime column.
- `df['col'].dt.weekday` — Extract the weekday from a datetime column.
- `df.resample('M').sum()` — Resample data by month and calculate sum.

---

## 🧮 Aggregation

### **Groupby Operations**

- `df.groupby('col')` — Group data by a column.
- `df.groupby('col').sum()` — Sum grouped values.
- `df.groupby('col').mean()` — Mean of grouped values.
- `df.groupby('col').agg({'col1': 'sum', 'col2': 'mean'})` — Multiple aggregations.
- `df.groupby('col').size()` — Count the number of rows in each group.

### **Descriptive Statistics**

- `df.mean()` — Mean of each column.
- `df.median()` — Median of each column.
- `df.std()` — Standard deviation of each column.
- `df.var()` — Variance of each column.
- `df.min()` — Minimum of each column.
- `df.max()` — Maximum of each column.
- `df.sum()` — Sum of each column.
- `df.cumsum()` — Cumulative sum.
- `df.cumprod()` — Cumulative product.

---

## 🔄 Data Transformation

### **Sorting**

- `df.sort_values(by='column')` — Sort by a column.
- `df.sort_index()` — Sort by index.
- `df.sort_values(by='column', ascending=False)` — Sort in descending order.

### **Reshaping**

- `df.pivot()` — Reshape the DataFrame by making one column the new index and another column as values.
- `df.pivot_table()` — Create a pivot table, which allows aggregation.
- `df.melt()` — Unpivot DataFrame from wide format to long format.
- `df.stack()` — Stack the columns into rows.
- `df.unstack()` — Unstack rows back into columns.
- `df.transpose()` — Transpose the DataFrame (flip rows and columns).

### **Concatenation & Joining**

- `pd.concat([df1, df2])` — Concatenate DataFrames along a particular axis.
- `df.join(df2)` — Join two DataFrames by index.
- `pd.merge(df1, df2, on='col')` — Merge two DataFrames on a common column.
- `pd.merge(df1, df2, left_on='col1', right_on='col2')` — Merge two DataFrames on different columns.

---

## 🎨 Visualization

- `df.plot()` — Plot data (default is line plot).
- `df.plot(kind='bar')` — Bar plot.
- `df.plot(kind='scatter', x='col1', y='col2')` — Scatter plot.
- `df.plot(kind='hist')` — Histogram.
- `df.plot(kind='box')` — Box plot.
- `df.plot(kind='area')` — Area plot.
- `df.plot(kind='pie')` — Pie plot.

---

## 📈 Statistical Operations

- `df.corr()` — Calculate correlation between columns.
- `df.cov()` — Calculate covariance.
- `df.skew()` — Skewness of each column.
- `df.kurt()` — Kurtosis of each column.
- `df.cumsum()` — Cumulative sum.
- `df.cumprod()` — Cumulative product.
- `df.rank()` — Rank data.

---

## 🔗 Working with Multiple DataFrames

- `df1.append(df2)` — Append DataFrame `df2` to `df1`.
- `df1.merge(df2)` — Merge two DataFrames.
- `df1.join(df2)` — Join DataFrame `df2` to `df1` on index.

---

## ⚙️ Advanced Indexing

- `df.set_index('col')` — Set a column as the index of the DataFrame.
- `df.reset_index()` — Reset the index of the DataFrame.
- `df.set_index(['col1', 'col2'])` — Set multiple columns as the index.

---

## ❌ Handling Missing Data

- `df.isnull()` — Return a DataFrame of boolean values indicating if data is missing.
- `df.fillna(value)` — Fill missing values with a given value.
- `df.dropna()` — Drop rows with missing values.
- `df.dropna(axis=1)` — Drop columns with missing values.
- `df.interpolate()` — Perform linear interpolation to fill missing values.

---

## 🛠️ Miscellaneous

- `df.crosstab()` — Create a cross-tabulation of two or more data columns.
- `df.pct_change()` — Percentage change between the current and previous element.
- `df.diff()` — Difference between current and previous row/column.
