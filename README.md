# Final Task of Automata Theory

* Habib Bahruddin (1301174412)
* Muhammad Kana Riskilah (1301174186)
* Evan Hisyam Aradhana (1301174432)

### Screenshot
<img src="https://user-images.githubusercontent.com/13828056/50467713-fa63b300-09d6-11e9-8dc7-fba64db7d26c.png" width="60%"></img>

### Rancangan Finite Automata
<img src="https://user-images.githubusercontent.com/13828056/50467318-ee76f180-09d4-11e9-8389-1365f3ce3d1d.png" width="60%"></img>

### Rancangan Context Free Grammar
> M = (S, Σ, √, δ, q0, {q2,q3,q4,q4,q5})
```
S = {q0,q1,q2,q3,q4,q5}
Σ = {S,P,O,K}
√ = {S,P,O} # Limited word to PDL (Push Down Language)

δ merupakan mapping dari S x ( Σ U {e} ) x √
```

```
Hasil dari δ sebagai berikut:

δ(q0, λ,λ; q1,#)
δ(q1, S,λ; q1,S)
δ(q1, P,S; q2,P)
δ(q2, P,S; q2,P)
δ(q2, O,P; q3,O)
δ(q2, O,P; q3,O)
δ(q3, O,P; q3,O)
δ(q3, K,O; q4,K)
δ(q4, K,O; q4,λ)
δ(q4, λ,#; q5,λ)
```

```
Maka didapat CFG sebagai berikut:

q0 -> Sq1
q1 -> Pq2
q2 -> Oq3 | Kq4 | λ
q3 -> Kq4 | λ
q4 -> λ
```

### Rancangan Push Down Automata
<img src="https://user-images.githubusercontent.com/13828056/50467844-92fa3300-09d7-11e9-8070-17b652a815d0.png" width="60%"></img>