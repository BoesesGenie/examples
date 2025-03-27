areAnagrams('abdcef', 'abcdef'); // true
areAnagrams('a', ''); // false
areAnagrams('aabdcef', 'abcddef'); // false
areAnagrams('abdcedf', 'abdcdef'); // true
areAnagrams('abdcef', 'abcdefabcdef'); // false
areAnagrams('abcdefabcdef', 'abdcef'); // false

function areAnagrams(a, b) {
    const dictA = toDict(a);
	const dictB = toDict(b);
	
	if (Object.keys(dictA).length !== Object.keys(dictB).length) {
	    return false;
	}

	for (let letter in dictA) {
        if (!dictB[letter]) {
		    return false;
		}
		
		if (dictA[letter] !== dictB[letter]) {
		    return false;
		}
	}
	
	return true;
}

function toDict(str) {
    const dict = Object.create(null);
	const arr = str.split('');

	for (let letter of arr) {
	    dict[letter] = dict[letter] ? ++dict[letter] : 1;
		
	}

	return dict;
}
