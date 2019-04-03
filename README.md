# nint

1. Cover

## 2. Vision of the project

To create a fast, frictionless, natural interface programming language for data manipulation, and vectorised operations.


## 3. Language main objective, including category (area)

**nint**'s main objective is to improves the data manipulation process by providing a frictionless interface that significantly simplifies the developer or statistician's life and reduces the time spent in the process of data wrangling, and performing common vectorised operations and statistical analysis. The idea is to have data frames (two-dimensional collections of data) as first-class citizens in the languange, and providing a piping system to manipulate and transform them.

## 4. Language requirements

### 4.1 Tokens (lexemes)

- Modules
	- `function`: defines a function
	- `return`: returns whatever follows to the main execution thread
	- `::`: specifies return type for funcction
	- `>>`: Pipe operator to pipe results of functions as input to other functions
- Conditionals
	- `if`
	- `else`
- Data types
	- `bool`: boolean (`true` or `false`)
	- `data.frame`: 2D collection of vectors (rows & columns) where each column has a single type
	- `factor`: collection of categorical data
	- `[ ]`: vectors
	- `float`: floating values
	- `int`: integers
	- `string`: collection of characters
	- `null`: empty data type
- Range
	- `[m: int]..[n: int]`: defines a range (integer vector) that goes from `m` to `n`-1.
- Loops
	- `for`
	- `while`
- Logical operators
	- `&&`: and
	- `||`: or
	- `!`: not (negation)
- `=` (**Assignment**)
- Read/write
	- `input`: Function to read from stdin
	- `print`: Function to print to stdout
- Arithmetic
	- `+`
	- `-`
	- `/`
	- `*`: multiplication
	- `**`: exponentiation
- Relational
	- `>`
	- `<`
	- `<=`
	- `>=`
	- `==`
	- `!=`
- Scope delimiters
	- `{`: opening brace
	- `}`: closing brace
	- `;`: end of statement
- Identifiers
	- `[A-Za-z][A-za-z0-9]*`
- String constant
	- `'[A-Za-z0-9]+'`
- Int constant
	- `[0-9]+`
- Float constant
	- `[0-9]+.[0-9]+`
- Comment
	- `[A-Za-z0-9]*`




### 4.2 Syntax diagrams for all the structures in your language



### 4.3 Main semantic characteristics

#### 4.3.1 Program structure

Programs written in **nite** will run as separate scripts where the user can define and execute variables and functions. The whole program will execute in a single main thread, sequentially. This makes sense as we want to privliege a pipes and filters architecture, which is how most data wrangling procedures are executed.

#### 4.3.2 Piping

A particular feature of the language is that it allows for piping data frames. This means that one can pass the result of a function call (that returns a data frame) to another function and "concatenate" the calls in this way (as opposed to nesting function calls).

```R
> x = read.table('some_file.csv', ',', false);
> result = x >> select(somenames) >> filter(x['somename'] == 3)
```

### 4.4 Special functions

| Function signature | Description |
| ------------------ | ----------- |
| `str(data.frame) :: void` | Shows a quick description of the data: the column names, types, and the first 6 elements |
| `cats(factor) :: string[]` | Shows the category (unique entries) for a factor |
| `read.table(string, delim : string, headers : bool) :: data.frame` | Reads a table into from a filename. File is a text file with columns separated by `delim` and `headers` specifies whether to read the first line as column names.s |
| `write.table(data.frame, filename : string, delim : string) :: bool` | Writes a data frame to a text file, with columns separated by `delim`. |
| `colnames(data.frame) :: string[]` | Returns the colum names of the data frame |
| `dim(data.frame) :: int[2]` | Returns the dimensions (rows and columns) of a data frame |
| `summary(data.frame) :: void` | Returns a basic statistical summary for numerical columns in the data frame. |
| `sum(int[] || float[] || bool[]) :: int || float ` | Returns the sum of a numeric (or parseable) vector |
| `map(vector, function) :: <type of vector>` | Applies a function succesively to all elements of a vector and returns the transformed vector |
| `len(vector) :: int` | Returns the length of a vector |
| `ls(void) :: string[]` | Returns the variable names in the current scope |
| `clear(void) :: void` | Clears the variable table for the current scope |
| `table(vector) :: void` | Returns a table with the frequencies of unique entries for a given vector. |
| `lin.reg(numeric[m], numeric[m]) :: float[2]` | Returns the linear regression coefficients for a given data set (x and y values) |
| `hist(x : vector, y : vector) :: void` | Prints a histogram to default GUI driver for x and y axis vectors. |
| `select(x: data.frame, names: string[])` | Do a projection of the column names in `names` on `x` |
| `filter(x: data.frame, condition : bool[] | bool)` | Return the rows in `x` where `condition` is `true` (or subset by the `true` values in the condition if it returns a vector of booleans) |


### 4.5 Data types

- floats: floating point numbers
- integers: integers
- strings: collection of arbitrary characters
- factors: one-dimensional structure for storing categorical data
- data frames: collection of vectors into a 2D structure with rows and columns with attributes
- vectors: one-dimensional collection of homogenous elements
- booleans: `true` or `false`
- `null`: non-value (empty or missing data)


## 5. Tech stack

The project will be developed in Python, using antlr as a parser generator and built on a machine running Windows 10.




