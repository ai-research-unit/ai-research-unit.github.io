# __The Regular Representation in Dimension $n$__

## Introduction

**The question.** An algebra acts on itself by multiplication, on the left and on the right. The two actions are the smallest faithful representations the algebra has, and every operator article of the corpus uses them. This article states the construction once, for an algebra of dimension $N$, and fixes the three nested sets it produces: the one-sided family, the sum of the two one-sided families, and the whole endomorphism algebra. The two-sided products are a cone inside the third and are the subject of the companion articles.

**The result in one line.** The left multiplications fill a copy of the algebra, the right multiplications fill a copy of its opposite, the two copies commute and are the centralisers of each other, and the ambient space has dimension $N^{2}$ against the dimension $N$ of the algebra.

**The four numbers.** For $A=M_{n}(\mathbb{C})$ the algebra has complex dimension $N=n^{2}$ and the ambient space has complex dimension $N^{2}=n^{4}$. The scalars are a line, the one-sided family is a subspace of dimension $n^{2}$, the cone of two-sided products has dimension $2n^{2}-1$, and the ambient is the whole. The chain
$$
1,\ n^{2},\ 2n^{2}-1,\ n^{4}
$$
is the ladder of the category. At $n=2$ it is $1,4,7,16$, the ladder of the biquaternion algebra, and there it is written in the four articles of the biquaternion operators.

**Boundaries.** The algebra itself, its units, its trace and its determinant are *The Matrix Algebra $M_n(\mathbb{C})$*. The one-sided families and their matrices are *The One-Sided Operators of $M_n(\mathbb{C})$*; the two-sided products and their cone are *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*; the length is *The Length and the Two Ranks on $M_n(\mathbb{C})$*; the adjoints, the sandwich and the difference family are *The Sandwich, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*. At $n=2$ the same objects in the Peirce frame are *$M_4(\mathbb{C})$ Standard Peirce Representation : Operators*, and the abstract family is *Two-Sided Operators on the Biquaternion Algebra*.

**Conventions.** The algebra is $A$, of complex dimension $N$, associative, unital, over $\mathbb{C}$. An element is written $A$, $B$, $C$; the unit is $I$; the matrices of $M_{n}(\mathbb{C})$ are written with the letter $n$ in the subscript and the matrices of the operator space with the dimension $N$ of that space. The left multiplication is $L_{A}$, the right multiplication is $R_{B}$, the two-sided operator is $T_{A,B}=L_{A}R_{B}$, and $\operatorname{End}(A)=\operatorname{End}_{\mathbb{C}}(A)$. A matrix of an operator is written in the column-stacking basis, in which an element $X$ of $A$ is the column $\operatorname{vec}X$ of its $N$ coordinates and an operator is an $N\times N$ matrix. The trace of a matrix is $\operatorname{tr}$; the trace of an operator is the trace of its matrix.

## The Two Multiplications

### The Left Multiplication

**Definition.** The **left multiplication** by $A$ is the map
$$
L_{A}:A\longrightarrow A,\qquad L_{A}(X)=AX .
$$

**Proposition (the map is a representation).** The assignment $A\mapsto L_{A}$ is a homomorphism of algebras,
$$
L_{A}L_{B}=L_{AB},\qquad L_{I}=\mathrm I_{N},
$$
and it is injective.

*Proof.* The associativity gives $L_{A}L_{B}(X)=A(BX)=(AB)X=L_{AB}(X)$. The unit acts as the identity. If $L_{A}=0$ then $AX=0$ for every $X$, and with $X=I$ this gives $A=0$.

**The image is a copy of the algebra.** The proposition says that the image $\operatorname{End}_{L}(A)=\{L_{A}\}$ is a subalgebra of $\operatorname{End}(A)$ isomorphic to $A$, of complex dimension $N$. The word *regular* names exactly this: the algebra acts on itself, and the action loses nothing.

### The Right Multiplication

**Definition.** The **right multiplication** by $B$ is the map
$$
R_{B}:A\longrightarrow A,\qquad R_{B}(X)=XB .
$$

**Proposition (the map is an anti-representation).** The assignment $B\mapsto R_{B}$ satisfies
$$
R_{B}R_{C}=R_{CB},\qquad R_{I}=\mathrm I_{N},
$$
and it is injective.

*Proof.* $R_{B}R_{C}(X)=(XC)B=X(CB)=R_{CB}(X)$, and the injectivity is the argument of the left case with $X=I$.

**The order is reversed, and the reversal is the whole difference between the two sides.** The image $\operatorname{End}_{R}(A)=\{R_{B}\}$ is a subalgebra isomorphic to the **opposite algebra** $A^{\mathrm{opp}}$, which is the same vector space with the product $B\cdot C=CB$. For a commutative algebra the two copies coincide; for a matrix algebra they do not, and the failure of coincidence is what the two-sided products measure.

### The Two Copies Commute

**Proposition (the two multiplications commute).** For every $A$ and every $B$,
$$
L_{A}R_{B}=R_{B}L_{A},\qquad L_{A}R_{B}(X)=AXB .
$$

*Proof.* Both sides send $X$ to $AXB$, and the associativity makes the two readings equal.

**The commutativity is the reason a two-sided product is a single operator and not a pair of successive actions.** The order of the factors does not matter, so the product $T_{A,B}=L_{A}R_{B}$ is well defined by the pair, and no extra datum of ordering is carried.

## Faithfulness, the Commutant and the Ladder

### The Double Centraliser

**Theorem (the centraliser of one copy is the other).** For $A=M_{n}(\mathbb{C})$,
$$
\{F\in\operatorname{End}(A):FL_{C}=L_{C}F\ \text{for all }C\}=\operatorname{End}_{R}(A),
$$
and symmetrically with the two sides exchanged. Each copy is the commutant of the other.

*Proof.* A right multiplication commutes with every left multiplication by the proposition above, so $\operatorname{End}_{R}(A)$ lies in the commutant. Conversely let $F$ commute with every $L_{C}$ and put $B=F(I)$. Then for every $X$,
$$
F(X)=F(L_{X}(I))=L_{X}(F(I))=XB=R_{B}(X),
$$
so $F=R_{B}$, and $F$ is in the right copy.

**The two copies are mutual centralisers, and the intersection is the centre.** A map that is both a left and a right multiplication satisfies $AX=XB$ for every $X$. With $X=I$ this gives $A=B$, and then $AX=XA$ for every $X$, so $A$ is central. Hence
$$
\operatorname{End}_{L}(A)\cap\operatorname{End}_{R}(A)=\mathbb{C}\cdot\mathrm I_{N}
$$
for $A=M_{n}(\mathbb{C})$, whose centre is $\mathbb{C}I$.

### The Ladder of the Sets

**The four sets.** The construction produces a chain of subsets of the ambient space, and the chain is the ladder of the category:

| Set | Definition | Complex dimension for $A=M_{n}(\mathbb{C})$ |
|---|---|---|
| the scalars | $\mathbb{C}\cdot\mathrm I_{N}$ | $1$ |
| the left copy | $\operatorname{End}_{L}(A)=\{L_{A}\}$ | $n^{2}$ |
| the right copy | $\operatorname{End}_{R}(A)=\{R_{B}\}$ | $n^{2}$ |
| the sum of the two copies | $\operatorname{End}_{L}(A)+\operatorname{End}_{R}(A)$ | $2n^{2}-1$ |
| the ambient | $\operatorname{End}(A)$ | $n^{4}$ |

**The sum is not the union and is not the ambient.** The two copies meet in the scalars, so the sum has dimension $n^{2}+n^{2}-1=2n^{2}-1$, one more than either copy. The ambient has dimension $n^{4}$, and for $n\ge2$ the inequality $2n^{2}-1<n^{4}$ holds: at $n=2$ it reads $7<16$, at $n=3$ it reads $17<81$.

**The two-sided products are not in the table as a subspace.** The set $\{L_{A}R_{B}\}$ is a cone of dimension $2n^{2}-1$, the same dimension as the sum of the two copies, and it is not a subspace. It contains both copies, since $T_{A,I}=L_{A}$ and $T_{I,B}=R_{B}$, and it is strictly larger than their sum: a generic product is neither a left nor a right multiplication. This is the reason the ladder has four rungs and not five.

### The Two Slots

**The pair is read in two slots, and the slots are not interchangeable.** The left slot carries an element of $A$ and the right slot an element of $A^{\mathrm{opp}}$; the product $T_{A,B}$ is bilinear in the pair and satisfies
$$
T_{\lambda A,B}=T_{A,\lambda B}=\lambda T_{A,B}
$$
for every scalar $\lambda$. **The scalar can be moved from one slot to the other, and this single freedom is the fibre of the parametrisation**, of complex dimension one. The effective number of parameters is therefore $2N-1$, and not $2N$.

## The Tensor Form

### The Isomorphism

**Theorem (the two-sided operators are the tensor square of the algebra).** The linear map
$$
A\otimes A^{\mathrm{opp}}\longrightarrow\operatorname{End}(A),\qquad A\otimes B^{\mathrm{opp}}\longmapsto L_{A}R_{B},
$$
is a homomorphism of algebras, and for $A=M_{n}(\mathbb{C})$ it is an isomorphism.

*Proof.* The product rule is $L_{A}R_{B}L_{C}R_{D}=L_{AC}R_{DB}$, which is the product in $A\otimes A^{\mathrm{opp}}$ read on the two factors. For the bijectivity, take the $n^{4}$ tensors $E_{ij}\otimes E_{kl}^{\mathrm{opp}}$; their images $T_{E_{ij},E_{kl}}$ have the coefficient array $E_{ij}$ in the row index and $E_{kl}$ in the column index, and the $n^{4}$ arrays $E_{ij}\otimes E_{kl}$ are a basis of the space of $n^{2}\times n^{2}$ arrays. Independence follows, and the dimensions agree:
$$
\dim\bigl(A\otimes A^{\mathrm{opp}}\bigr)=N^{2}=\dim\operatorname{End}(A).
$$

**Two readings of one statement.** The isomorphism says that **an endomorphism of a matrix algebra is a sum of two-sided multiplications**, and it says that **the operator space is the tensor square of the algebra**. The second reading is the one that makes the coefficient array of the companion articles natural: the array is the tensor, and the length is its rank.

### What the Isomorphism Requires

**The isomorphism is a property of the algebra and not of the notation.** For a commutative algebra $A^{\mathrm{opp}}=A$ and $L_{A}R_{B}=L_{AB}$, so the image is the one-sided family alone, of dimension $N$ and not $N^{2}$; the kernel of the map is then of dimension $N^{2}-N$, and the tensor form loses all its information.

**The criterion.** The map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}(A)$ is injective exactly when $A$ is a **central simple algebra**, and every such algebra is a matrix algebra over a division ring. Over $\mathbb{C}$ the central simple algebras are the algebras $M_{n}(\mathbb{C})$, so **the exactness of the construction is the exactness of the matrix case**: it holds for $M_{n}(\mathbb{C})$ at every $n$ and fails for every algebra that is a product of two factors.

**The three algebras to keep apart.** The scalars $\mathbb{C}$ have $N=1$ and no room for a failure. The dual numbers and the split-complex numbers are commutative and collapse to the one-sided family. The biquaternion algebra $\mathbb{B}$ is $M_{2}(\mathbb{C})$, so it is central simple and does not collapse; the reduced biquaternion algebra is $\mathbb{C}\times\mathbb{C}$, so it does. **The same complex dimension four is carried by two algebras of which one is central simple and the other is not, and the operator theory of the two differs at its first theorem.**

## The Cases

**The table.** The construction at the algebras the corpus uses, with the dimension $N$ of the algebra, the dimension $N^{2}$ of the ambient, and the dimension $2N-1$ of the cone.

| Algebra | $N$ | $\dim\operatorname{End}(A)$ | $\dim(\text{cone})$ | the ladder |
|---|---|---|---|---|
| $\mathbb{C}$ | $1$ | $1$ | $1$ | $1$ |
| the dual numbers | $2$ | $4$ | collapses | $1,2$ |
| $\mathbb{C}\times\mathbb{C}$ | $2$ | $4$ | collapses | $1,2$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $4$ | $16$ | $7$ | $1,4,7,16$ |
| $\mathbb{B}=M_{2}(\mathbb{C})$ | $4$ | $16$ | $7$ | $1,4,7,16$ |
| $M_{n}(\mathbb{C})$ | $n^{2}$ | $n^{4}$ | $2n^{2}-1$ | $1,n^{2},2n^{2}-1,n^{4}$ |

**The case of the real quaternions is the biquaternion case read over another field.** The algebra $\mathbb{H}$ is central simple over $\mathbb{R}$ and has real dimension four; the operator space has real dimension sixteen and the cone real dimension seven. The complex biquaternion algebra has the same three numbers over $\mathbb{C}$, because the complexification doubles both the algebra and the operator space. **The ladder is insensitive to the field, and this is why one set of numbers serves the two categories.**

**The case $n=1$.** The algebra is $\mathbb{C}$, the operator space is $\mathbb{C}$, and the left and right multiplications coincide with the scalar action. The cone is the whole space, the length is $0$ or $1$, and the ladder has a single rung. **The case is degenerate and is kept only to fix the low end of the formulas.**

## Summary

The left multiplications $L_{A}(X)=AX$ form a copy of the algebra $A$ inside $\operatorname{End}(A)$, faithful and of dimension $N=\dim A$; the right multiplications $R_{B}(X)=XB$ form a copy of the opposite algebra, and the two copies commute, each being the commutant of the other, with intersection the scalars. The product $T_{A,B}=L_{A}R_{B}$ is the single operator $X\mapsto AXB$, bilinear in the pair, constant on the scaling orbits $(\lambda A,\lambda^{-1}B)$, and the set of products is a cone of dimension $2N-1$ inside the ambient space of dimension $N^{2}$.

For $A=M_{n}(\mathbb{C})$ the numbers are $N=n^{2}$ and $N^{2}=n^{4}$, and the ladder is $1,n^{2},2n^{2}-1,n^{4}$: the scalars, the one-sided family, the cone, the ambient. At $n=2$ the ladder is $1,4,7,16$, the biquaternion ladder, and the two-sided products are the pure tensors of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$.

The isomorphism $A\otimes A^{\mathrm{opp}}\to\operatorname{End}(A)$ holds exactly for the central simple algebras, that is for the matrix algebras; for a commutative or split algebra the image falls back to the one-sided family, the tensor form loses its information, and the two-sided operator is the multiplication by the product of the two parameters. **The exactness of the operator theory of a category is the centrality and simplicity of its algebra, and not the size of its dimension.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | the algebra, of complex dimension $N$, associative and unital |
| $N$ | the complex dimension of $A$ |
| $n$ | the size, $A=M_{n}(\mathbb{C})$, $N=n^{2}$ |
| $I$ | the unit of the algebra |
| $L_{A}$ | the left multiplication $X\mapsto AX$ |
| $R_{B}$ | the right multiplication $X\mapsto XB$ |
| $T_{A,B}=L_{A}R_{B}$ | the two-sided operator $X\mapsto AXB$ |
| $\operatorname{End}_{L}(A)$ | the set of left multiplications, a copy of $A$ |
| $\operatorname{End}_{R}(A)$ | the set of right multiplications, a copy of $A^{\mathrm{opp}}$ |
| $A^{\mathrm{opp}}$ | the opposite algebra |
| $\mathrm I_{N}$ | the identity of $\operatorname{End}(A)$ |
| $\operatorname{vec}X$ | the column of the $N$ coordinates of $X$ |
| $c(M)$ | the coefficient array of an operator |

## Further Reading

- Israel Nathan Herstein, *Noncommutative Rings* (Carus Mathematical Monographs, 1968), for the double centraliser theorem and the central simple algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representation and the opposite algebra.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra, its centre and its simplicity.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the two copies as matrices.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the cone of products.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the coefficient array and the length.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family at $n=2$.
