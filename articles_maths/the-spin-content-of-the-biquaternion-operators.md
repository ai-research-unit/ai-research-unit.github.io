# __The Spin Content of the Biquaternion Operators: Spin $\tfrac32$ on the Module and $0,1,2,3$ on the Algebra__

## Introduction

**The subject.** This article puts the whole operator row in one place: the space of complex dimension sixteen, its slot $\tfrac32$, its four carriers of dimensions seven, five, three and one, the weights, the Casimir eigenvalues and their multiplicities, the reality type of each carrier, the two readings, the table of the row against the row of the elements, and the two open ends.

**The order of the article.** The weights and the Casimir come first. The carriers and their reality types follow, then the two readings, the comparison with the row of the elements, and the two open ends, the products and the strata.

**It assumes** the four introductions to the carriers and *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*. **The row of the elements is** where the slot is $\tfrac12$, the labels are zero and one, and the weight zero occurs once.

**The result in one line.** The row is complete as a decomposition — $16=7+5+3+1$ — and incomplete as a multiplication, since the product of two elements of the top carrier has a component in the middle carrier.

**Boundaries.** The carriers are treated one by one in the four introductions; the general law is *The Law of the Module and the Chain of Carriers at Every Order*; the comparison of the three rows is *The Three Rows of the Tower*.

## The Weights and Their Multiplicities

**Theorem.** The weights of the sixteen, counted with multiplicity, are
$$
0\ \text{four times},\qquad \pm1\ \text{three times each},\qquad \pm2\ \text{two times each},\qquad \pm3\ \text{once each}.
$$

*Proof.* The sixteen is the square of the module, so its weights are the sixteen ordered sums $a+b$ of two module weights. The sum $3$ arises once, $2$ twice, $1$ three times, $0$ four times, and the negative sums by symmetry; the total is $1+2+3+4+3+2+1=16$.

**Proposition.** The Casimir eigenvalues of the four carriers are $12,6,2,0$, with multiplicities the dimensions of the carriers, $7,5,3,1$.

*Proof.* The Casimir of a carrier of label $k$ is $k(k+1)$, which at $k=3,2,1,0$ gives twelve, six, two and zero. Each label occurs once in the addition rule, so each eigenvalue occurs on one carrier, and its multiplicity is the dimension of that carrier: seven, five, three and one, which add to sixteen.

**Corollary.** The sum of the weights is zero, the sum of their squares is zero, and the Casimir eigenvalue is not linear in the weight.

*Proof.* The multiset is symmetric about zero, so both sums vanish. The Casimir is quadratic in the label and constant on a carrier, whereas the weights of a carrier run over $2k+1$ values.

**The reading.** The weights and the Casimir are two different memories of the same string. The weights count the positions, the Casimir records the length, and the four eigenvalues twelve, six, two and zero are the four lengths.

## The Four Carriers and Their Reality Types

**Proposition.** The four carriers have dimensions $7,5,3,1$, and each is of real type with a real form of the same dimension.

*Proof.* The dimensions are $2k+1$; the indicator of the carrier of label $k$ is $(-1)^{2k}=+1$, so each carrier has an invariant antilinear involution with square $+1$ and a real form whose real dimension equals the complex dimension.

**Corollary.** The real dimensions of the carriers are seven, five, three and one, and the real dimension of the module is eight.

*Proof.* The carriers are of real type; the module has label $\tfrac32$, its indicator is $-1$, and it is quaternionic, so its real dimension is twice its complex dimension.

**The reading.** The reality type separates the module from its square. The module is quaternionic and the four summands of its square are real, which is the passage from the half-integer label to the integer ones.

## The Two Readings

**Proposition.** The same sixteen decomposes in two ways:
$$
\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0
\qquad\text{and}\qquad
(V_1\oplus V_0)\otimes(V_1\oplus V_0)=V_2\oplus 3V_1\oplus 2V_0 .
$$

*Proof.* The first is the addition rule for the principal copy. The second is the addition rule applied to the square of the module of the algebra read by its own units, which is $V_1\oplus V_0$.

**Corollary.** The multiplicities of the labels in the two readings are

| label | principal | conjugation |
|---|---|---|
| $3$ | $1$ | $0$ |
| $2$ | $1$ | $1$ |
| $1$ | $1$ | $3$ |
| $0$ | $1$ | $2$ |

*Proof.* The principal reading has each label once. The conjugation reading has the quintet once, from $V_1\otimes V_1$; the triplet three times, once from $V_1\otimes V_1$ and twice from $V_1\otimes V_0$ and $V_0\otimes V_1$; and the singlet twice, from $V_0\otimes V_0$ and from the invariant form inside $V_1\otimes V_1$.

**Corollary.** The two readings agree on the label two and differ elsewhere, and only the principal reading contains the label three.

*Proof.* The table, and the dimension check $5+9+2=16$ against $7+5+3+1=16$.

**The reading.** The two readings are two copies acting on one space. The principal copy sees four simple summands; the conjugation copy sees one simple summand and two repeated ones. The difference of the two decompositions is the difference of the two copies, not of the space.

## The Row against the Row of the Elements

**Proposition.** The two rows compare as follows:

| | row of the elements | row of the operators |
|---|---|---|
| dimension | $4$ | $16$ |
| slot | $\tfrac12$ | $\tfrac32$ |
| labels | $0,1$ | $0,1,2,3$ |
| carriers | $2$ | $4$ |
| weight zero | once | four times |
| singular locus | none but zero | a hypersurface |

*Proof.* The first row is the algebra of dimension four with module the spinor space of dimension two; the second is its endomorphism algebra. The labels and dimensions follow from the two addition rules, the multiplicity of the weight zero from the count of ordered sums, and the singular locus from the degeneracy hypersurface of the algebra against the singular elements of its endomorphism algebra.

**Corollary.** The passage from a row to the next doubles the number of carriers and quadruples the dimension, and it creates a singular locus where the row below had none.

*Proof.* The number of carriers is the dimension of the module, which is two then four; the dimension is the square, four then sixteen; the algebra below has no zero divisors and the algebra above has a hypersurface of them.

**The reading.** The two rows differ in the ways that matter for the geometry: number of carriers, multiplicity of the weight zero, and existence of a singular locus. The dimension and the slot are the two entries that are simply computed from the other.

## Complete and Incomplete

**Proposition.** The row is not closed under composition. The product of the element of weight three with the element of weight one has a component in the top carrier and a component in the middle carrier, the second twice as large as the first; the square of the element of weight one lies entirely in the middle carrier.

*Proof.* The products are computed in the weight basis of the row, where every element is a sum of weight vectors and every product is expanded into the four carriers by the projection of the previous articles. The element of weight three is of rank one and the element of weight one of rank three, and their product has rank at most one but is not a multiple of the first, so it is not in the top carrier.

**Corollary.** The top carrier is complete as a summand and incomplete as an algebra: it is a direct summand of the row and it is not a subalgebra of it.

*Proof.* The decomposition is a statement about the copy, and it holds by the addition rule; the failure of closure is a statement about the multiplication, and it holds by the proposition.

**Corollary.** The strata of the two predicates, the rank and the spectrum, are not stable under composition: a product of two elements of full rank may be singular.

*Proof.* The elements of weight one and of weight three are singular, and their product has rank at most one; two invertible elements can also have a singular product when the row is not closed.

**Theorem.** The row is complete as a decomposition and incomplete as a multiplication, and the two facts are independent.

*Proof.* Completeness is the addition rule, which uses only the copy and the module; incompleteness is the failure of closure, which uses the product of the algebra. Neither statement implies the other, since a decomposition into summands says nothing about products and a failure of closure says nothing about the labels.

**The reading.** The spin content of the row is a statement about the copy, and the multiplication of the row is a statement about the algebra. The row is the endomorphism algebra of a four-dimensional module, and the two structures meet in it without coinciding: the copy decomposes it, and the product does not respect the decomposition.

## Further Reading

- [The Three Rows of the Tower](the-three-rows-of-the-tower.html), for the row in the tower.
- [The Law of the Module and the Chain of Carriers at Every Order](the-law-of-the-module-and-the-chain-of-carriers-at-every-order.html), for the law behind the table.
- [Introduction to the Spin-Three Carrier: the Top of the Chain](introduction-to-the-spin-three-carrier-the-top-of-the-chain.html), for the carrier that carries the weight three.
- [Introduction to the Spin-Two Carrier: the Alternating Square](introduction-to-the-spin-two-carrier-the-alternating-square.html), for the carrier that receives the products.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the addition rule at the first row.
