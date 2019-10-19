/** Flat array without recursion */

function arrayFlat(arr) {
    let result = [...arr];

    while (part = result.find(item => Array.isArray(item))) {
        const index = result.indexOf(part);

        result = result.slice(0, index).concat(part).concat(result.slice(index + 1));
    }

    return result;
}

const a = [1,2,3,[4,5,[6,7,8,9]],10,11,12,13,[14,15]];
arrayFlat(a);
