const solution1 = (my_string) => my_string.split("").filter(char => !"aeiou".includes(char)).join("");

const solution2 = (my_string) => my_string.replace(/[aeious]/g, '');