/** Flat array without recursion */

function arrayFlat(arr) {
    let result = [...arr];
	let idx;

	while((idx = result.findIndex(item => Array.isArray(item))) !== -1) {
	    result = result.slice(0, idx).concat(result[idx]).concat(result.slice(idx + 1));
	}

	return result;
}

const a = [1,2,3,[4,5,[6,7,8,9]],10,11,12,13,[14,15]];
arrayFlat(a);
