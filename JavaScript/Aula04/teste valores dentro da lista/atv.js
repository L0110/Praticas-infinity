const notas = [10, 2.4,5.3, 4.4, 4.5];
console.log(notas);

console.log(
    notas.every(
        element => element === 10
    )
);
console.log(
    notas.every(
        element => element <= 10
    )
);

console.log(
    notas.some(
        element => element === 10
    )
);

console.log(
    notas.some(
        element => element < 10
    )
);