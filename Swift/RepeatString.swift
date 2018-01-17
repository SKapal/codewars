func repeatStr(_ n: Int, _ string: String) -> String {
	// Code here:
  	var result = ""
  	for i in stride(from: 0, to: n, by: 1) {
    	result += string
  	}
  	return result
}