# Smart parse JSON to Go struct

Takes a `.json` file and generates a Go struct from it in a new `.go` file. The code in the go file is currently not
formatted and the case that a variable name starts with a number is not handled. Also, maps and UUIDs are not handled yet.
