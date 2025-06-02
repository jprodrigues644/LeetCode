function produitFait60(T) {
  const n = T.length;

  // On teste toutes les combinaisons possibles de 3 éléments
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if (T[i] * T[j] * T[k] === 60) {
          return true;
        }
      }
    }
  }

  return false;
}

// Exemples d'utilisation :
console.log(produitFait60([1, 3, 4, 5]));        // true (3*4*5 = 60)
console.log(produitFait60([2, 6, 10, 1]));       // true (1*6*10 = 60)
console.log(produitFait60([1, 2, 3]));           // false
console.log(produitFait60([-3, -4, 5]));         // true (-3 * -4 * 5 = 60)
