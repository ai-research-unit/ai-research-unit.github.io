# __Relations between the Modulus and Spectral Regularity and Degeneracy__

## Introduction

The complex algebra $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ carries two quadratic conditions on one element. The **modulus squared** is

$$
M(z)=|z|^2=z\bar z=t^2+b^2,
$$

it is multiplicative, and it vanishes only at the origin. The **square of the imaginary part** is $B(z)=b^2$; it is not multiplicative, and it vanishes on the real axis. The first condition decides invertibility: $z$ is **modulus-regular** when $M\neq0$ and **modulus-degenerate** when $M=0$. The second decides whether the two eigenvalues are distinct: $z$ is **spectrally regular** when $B\neq0$ and **spectrally degenerate** when $B=0$. The two conditions are studied one at a time in *Complex Norm and Invertibility* and *Spectral Regularity and Degeneracy in the Complex Algebra*; this article compares them.

The comparison has a definite shape. As functions, $M$ and $B$ are independent: neither determines the other. As vanishing conditions they are nested: $B\neq0$ implies $M\neq0$, because $M=B+t^2$. The nesting is strict, its strictness is the punctured real axis, and it is the content of the relation.

**Conventions.** The element is $z=t+bi$ with $t,b\in\mathbb{R}$, the conjugation is $\bar z=t-bi$, the modulus squared is $|z|^2=z\bar z=t^2+b^2$, and the modulus is $|z|=\sqrt{t^2+b^2}$. The companion articles write $Q=q+iq'$ and $\langle Q\rangle_*=Q\bar Q$; the translation is $t=q$, $b=q'$, $|z|^2=\langle Q\rangle_*$. The spectral criterion and the cells are those of *Spectral Regularity and Degeneracy in the Complex Algebra* and *The Three Sectors of the Complex Algebra*.

## The Two Invariants

**Definition.** The **modulus squared** is $M(z)=z\bar z=t^2+b^2$; the **modulus** is $|z|=\sqrt{M(z)}$. The **square of the imaginary part** is $B(z)=b^2$.

**Proposition (the modulus).** $M$ is real and non-negative, $M(z)=0$ exactly when $z=0$, it is multiplicative, $M(zw)=M(z)M(w)$, and it is invariant under conjugation.

*Proof.* $M=t^2+b^2$ is a sum of two squares. Multiplicativity is $(zw)\overline{(zw)}=z\bar z\,w\bar w$, and conjugation fixes $t^2+b^2$.

**Proposition (the imaginary square).** $B$ is real and non-negative, $B(z)=0$ exactly when $z$ is real, and $B$ is not multiplicative.

*Proof.* $B=b^2$ vanishes exactly when $b=0$. For non-multiplicativity, $B(i)=1$ and $B(i\cdot i)=B(-1)=0$, while $B(i)B(i)=1$.

**Proposition (the comparison).** For every $z$,

$$
0\leq B(z)\leq M(z),
$$

with $B=M$ exactly on the imaginary axis and $B=0$ exactly on the real axis.

*Proof.* $M-B=t^2\geq0$, and $t^2=0$ exactly when $t=0$.

**Remark (the level sets).** The set $M=r^2$ is the circle of radius $r$, and the set $B=c$ is the pair of horizontal lines $b=\pm\sqrt c$, coincident at $c=0$. The map $(t,b)\mapsto(M,B)$ has Jacobian determinant $4tb$, which vanishes on both axes: the invariants are not a coordinate system, and their level curves are tangent on the imaginary axis.

## Independence and Nesting

**Theorem (the functions are independent).** Neither invariant is a function of the other.

*Proof.* The elements $1+i$ and $2+i$ have the same $B=1$ and different $M=2$ and $5$. The elements $1$ and $i$ have the same $M=1$ and different $B=0$ and $1$.

**Theorem (the predicates are nested).** The conditions satisfy

$$
B(z)\neq0\ \Longrightarrow\ M(z)\neq0,\qquad M(z)\neq0\ \not\Longrightarrow\ B(z)\neq0 .
$$

*Proof.* If $B\neq0$ then $M=B+t^2\geq B>0$. The converse fails at $z=1$, where $M=1$ and $B=0$.

**Corollary (the logical table).**

| $M\neq0$ | $B\neq0$ | example | status |
|---|---|---|---|
| yes | yes | $i$ | non-empty |
| yes | no | $1$ | non-empty |
| no | no | $0$ | non-empty |
| no | yes | none | empty |

*Proof.* The first three rows are the examples. The fourth is impossible by the implication.

**Remark (what independence means).** The invariants are independent as functions and nested as vanishing predicates. The phrase *the two conditions are independent* is therefore true of $M$ and $B$ as functions on the plane, and false of the sets $\{M\neq0\}$ and $\{B\neq0\}$, which are ordered by inclusion. This distinction is the content of the comparison.

## The Unit Circle

**Definition.** The **unit circle** is $\mathrm{U}(1)=\{z:M(z)=1\}=\{t+bi:t^2+b^2=1\}$. Every point of it is modulus-regular and a unit, with inverse $\bar z$.

**Theorem (the intersection with the real axis).** The unit circle meets the real axis exactly at $z=1$ and $z=-1$. There $M=1$ and $B=0$: the two points are modulus-regular and spectrally degenerate, not doubly regular. The doubly regular points of the circle are the complement $\mathrm{U}(1)\setminus\{1,-1\}$, the two open arcs $b>0$ and $b<0$.

*Proof.* On the real axis $M=t^2$; $M=1$ gives $t=\pm1$, and $B=0$ there. Off the axis $b\neq0$, so $B>0$ and $M=1$; both conditions hold.

**Remark (the arcs).** The two open arcs are the connected components of the doubly regular part of the circle, and the spectral condition is constant on each. Degeneration is concentrated at the two real points.

The phrase *the unit circle meets the real axis at $\pm1$* might suggest that the intersection points are doubly regular. They are the opposite: they are the spectrally degenerate points of the circle.

## The Origin and the Empty Cell

**Theorem (the vanishing locus of the modulus).** For $z\in\mathbb{C}$, $M(z)=0$ exactly when $z=0$. There is no non-zero modulus-degenerate element, every non-zero complex number is a unit, and the zero-divisor class is empty.

*Proof.* $t^2+b^2=0$ forces $t=b=0$. The inverse of $z\neq0$ is $\bar z/M(z)$. If $ab=0$ with $a,b\neq0$, multiplicativity gives $M(a)M(b)=0$, hence $M(a)=0$ or $M(b)=0$, hence $a=0$ or $b=0$, a contradiction.

**Corollary (the only doubly degenerate point).** The origin is the only element that is both modulus-degenerate and spectrally degenerate.

*Proof.* $M(z)=0$ forces $z=0$, and $B(0)=0$. Conversely $B=0$ alone does not force $M=0$: every other real number is a counterexample.

**Corollary (the empty cell).** No element has $M=0$ and $B\neq0$.

*Proof.* $M=0$ forces $z=0$, and $B(0)=0$.

**Remark (three-way classification).** An element is a unit, a zero divisor, or zero. The zero-divisor class is empty, so the classification has two non-empty classes, the units and the origin. The modulus makes the classification; the spectral invariant plays no part in it. The detail is *Complex Norm and Invertibility*, §*The Three-Way Classification*.

## The Chain of Invariants

**Theorem (what each invariant separates).**

| invariant | data | patterns | what it separates |
|---|---|---|---|
| modulus squared | $M=t^2+b^2$ | 2 | the origin from the rest |
| imaginary square | $B=b^2$ | 2 | the real axis from the rest |
| characteristic polynomial | $(2t,M)$ | 3 | the three cells |
| minimal polynomial | $X-t$ or $(X-t)^2+b^2$ | 2 | the real axis from its complement |

*Proof.* The modulus vanishes only at the origin and $B$ only on the real axis. The characteristic polynomial is $X^2-2tX+M$: two distinct roots with non-zero product on $\Sigma_{11}$, a double non-zero root on $\Sigma_{10}$, and a double root at zero on $\Sigma_{00}$. The minimal polynomial is $X-t$ on the real axis and the characteristic polynomial off it.

**Corollary (the spectral data do not see the conjugation).** The elements $z$ and $\bar z$ have the same $M$, the same $B$, the same characteristic polynomial, the same spectrum and the same minimal polynomial. The invariants determine $z$ only up to the sign of $b$.

*Proof.* All the listed quantities depend on $t$ and $b^2$ only, and $z$ and $\bar z$ share both.

**Remark (the chain stops).** The modulus separates the origin from the rest, the imaginary square separates the real axis from the rest, and the characteristic polynomial separates the three cells. The minimal polynomial refines nothing: off the real axis it is the characteristic polynomial, and on it, it is the degree-one reduction. The chain has three cell-separating invariants and no fourth; the spectral invariant $B$ is the discriminant of the characteristic polynomial. In the biquaternion algebra the chain continues, because the minimal polynomial separates the nilpotent and unipotent strata of the degenerate cone; here there are no such strata.

## The Place among the Algebras

**The complex case is the smallest definite algebra in which the spectral condition is not automatic.**

| algebra | modulus or norm | spectral condition | $\Sigma_{01}$ | cells |
|---|---|---|---|---|
| $\mathbb{R}$ | $t^2$, definite | never holds (always degenerate) | empty | 2 |
| $\mathbb{C}$ | $t^2+b^2$, definite | $b^2$ | empty | 3 |
| $\mathbb{H}$ | $t^2+\lvert\vec v\rvert^2$, definite | $\lvert\vec v\rvert^2$ | empty | 3 |
| $\mathbb{D}$ | $t^2-b^2$, indefinite | $b^2$ | non-empty | 4 |
| $\mathbb{B}$ | $Q_t^2+B^2$, complex | $B^2$ | non-empty | 4 |

*Proof.* In $\mathbb{R}$ the regular matrix is $(t)$, so the spectrum is $\{t\}$ and the spectral condition never holds. In $\mathbb{C}$ the criterion is this article. In $\mathbb{H}$ the eigenvalues of the regular representation are $t\pm i\lvert\vec v\rvert$, each twice, so the condition is $\vec v\neq0$ and the norm is definite. In $\mathbb{D}$ the norm is $t^2-b^2$, zero on the lines $t=\pm b$, and the spectral condition is $b\neq0$; the point $1+j$ has norm $0$ and $b=1$. In $\mathbb{B}$ the norm is $Q_t^2+B^2$, zero on non-zero elements, and the spectral condition is $B^2\neq0$; the details are *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

**Corollary (the meaning of the empty cell).** A definite modulus forces $\Sigma_{01}$ to be empty; an indefinite or complex-valued modulus allows it to be non-empty. The complex algebra is definite, so it has three cells, and it is the first definite algebra in which the spectral condition is not automatic.

*Proof.* Definiteness says $M=0$ only at the origin, which is spectrally degenerate; hence no point has $M=0$ and $B\neq0$. The second sentence is the table.

## Summary

The complex algebra carries the modulus squared $M=t^2+b^2$ and the square of the imaginary part $B=b^2$. The modulus is multiplicative and vanishes only at the origin; $B$ is not multiplicative and vanishes on the real axis. They satisfy $0\leq B\leq M$, with $M-B=t^2$.

As functions, $M$ and $B$ are independent: $1+i$ and $2+i$ have the same $B$ and different $M$, while $1$ and $i$ have the same $M$ and different $B$. As vanishing conditions they are nested: $B\neq0$ implies $M\neq0$, and the implication is strict at every non-zero real number. The four logical combinations are three non-empty cases and the empty case $M=0$, $B\neq0$.

The unit circle meets the real axis at $\pm1$. These points are modulus-regular and spectrally degenerate, not doubly regular; the doubly regular points of the circle are the two open arcs between them. The origin is the only doubly degenerate point, and there is no non-zero modulus-degenerate element, so every non-zero complex number is a unit and the zero-divisor class is empty.

The characteristic polynomial $X^2-2tX+M$ separates the three cells; the minimal polynomial adds no cell. The spectral data determine $z$ only up to the sign of $b$, so $z$ and $\bar z$ are spectrally indistinguishable. Among the algebras of the corpus the complex case is the smallest definite case with three cells: $\mathbb{R}$ has two, $\mathbb{H}$ has three, and the split and biquaternion algebras have four because their norms are indefinite or complex.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ | the complex algebra |
| $z=t+bi$ | a complex number |
| $\bar z=t-bi$ | complex conjugation |
| $M(z)=\lvert z\rvert^2=z\bar z=t^2+b^2$ | the modulus squared, the natural norm |
| $B(z)=b^2$ | the square of the imaginary part |
| modulus-regular / degenerate | $M\neq0$ / $M=0$ |
| spectrally regular / degenerate | $B\neq0$ / $B=0$ |
| $\mathrm{U}(1)=\{M=1\}$ | the unit circle |
| $\Sigma_{ij}$ | the cell with $M\neq0$ iff $i=1$ and $B\neq0$ iff $j=1$ |
| $\Sigma_{01}$ | the empty cell |

## Further Reading

- [Spectral Regularity and Degeneracy in the Complex Algebra](spectral-regularity-and-degeneracy-in-the-complex-algebra.html), for the characteristic polynomial, the discriminant and the spectral criterion.
- [Eigenvalue Decomposition and Eigenbasis of a Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-complex-number.html), for the eigenbasis, the spectral idempotents and the polar reading.
- [The Three Sectors of the Complex Algebra](the-three-sectors-of-the-complex-algebra.html), for the partition into cells, their closure and their dimension.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), for the modulus, multiplicativity, the inverse and the three-way classification.
- [Complex Algebra](complex-algebra.html), for the algebra and its real and imaginary subspaces.
- [Modulus–Unit Polar Decomposition of Complex Numbers](modulus-unit-polar-decomposition-of-complex-numbers.html), for the unit circle and the polar form.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four-sector case in the biquaternion algebra.
