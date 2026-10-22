# __The Number Systems as Algebras with and without Nontrivial Idempotents__

## Introduction

The number systems of the shared conventions — the real numbers $\mathbb{R}$, the complex numbers $\mathbb{C}$, the split complex numbers $\mathbb{D}=\mathbb{R}[j]$ with $j^2=+1$, the dual numbers $\mathbb{D}'=\mathbb{R}[\varepsilon]$ with $\varepsilon^2=0$, the quaternions $\mathbb{H}$, the split biquaternions $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_\mathbb{R}\mathbb{H}$, and the biquaternions $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ — look alike as vector spaces and differ sharply as algebras. This article compares them through one invariant: the set of idempotents. The comparison is a small dictionary of structural algebra. The idempotents of $\mathbb{D}$ are four and all central; the idempotents of $\mathbb{H}_{\mathbb{D}}$ are four and all central; the idempotents of $\mathbb{B}$ are a two-parameter family and almost all noncentral; the idempotents of $\mathbb{C}$ and $\mathbb{H}$ are only $0$ and $1$; and the idempotents of the dual numbers $\mathbb{D}'$ are also only $0$ and $1$, although $\mathbb{D}'$ is not a division algebra.

The last example is the point of the article. "No nontrivial idempotents" is not the same as "division algebra". The division algebras have no nontrivial idempotents because they have no zero divisors; the dual numbers have no nontrivial idempotents because they are local, with the nilpotent ideal $(\varepsilon)$ and the unit $1$ primitive. The matrix algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has many nontrivial idempotents although it is simple. The split complex numbers $\mathbb{D}$ have two nontrivial central idempotents and decompose as $\mathbb{R}\times\mathbb{R}$; the split biquaternions $\mathbb{H}_{\mathbb{D}}$ have two nontrivial central idempotents and decompose as $\mathbb{H}\times\mathbb{H}$. The invariant that decides the question is the existence of a proper direct summand of the algebra as a left module over itself, equivalently the primitivity of the unit.

The article is the comparative companion of *Examples of Algebras*, *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, *Division Algebras*, *Split Complex Idempotents and Projections*, *Split-Biquaternion Idempotents and Projections*, and *Square Roots of One and the Idempotents of the Quaternion Algebra*. The detailed idempotent computations of the biquaternion algebra are *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the Peirce decomposition is *Hermitian Idempotents and the Peirce Decomposition* and *The Centraliser and the Diagonal Peirce Part*; and the roots of one are *Roots of the Identity, Split Algebras and Nontrivial Idempotents*. The article uses no form and no topology.

**Conventions.** The algebras are over $\mathbb{R}$ unless a different field is stated. The split complex numbers are $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$; the dual numbers are $\mathbb{D}'=\mathbb{R}[\varepsilon]/(\varepsilon^2)$; the quaternions are $\mathbb{H}$ with the usual division product; the split biquaternions are $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_\mathbb{R}\mathbb{H}\cong\mathbb{H}\times\mathbb{H}$; and the biquaternions are $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$. The idempotents are written $e,f,\Pi_\pm$; the two idempotents of $\mathbb{D}$ are

$$
\Pi_+=\tfrac12(1+j), \qquad \Pi_-=\tfrac12(1-j).
$$

An idempotent is **nontrivial** when it is neither $0$ nor $1$; two idempotents are **orthogonal** when $ef=fe=0$; a family is **complete** when the sum of its members is $1$. The unit is **primitive** when it is not the sum of two nonzero orthogonal idempotents. The left regular module is $A$ with the left multiplication action of $A$; a direct summand of it is a left ideal $Ae$ with $e$ idempotent.

## The Halving Bijection

### Roots of one and idempotents

**Theorem.** In every unital algebra $A$ over a field of characteristic not two, the map

$$
\xi\longmapsto e=\tfrac12(1+\xi)
$$

is a bijection from the roots of $1$ onto the idempotents, with inverse

$$
e\longmapsto \xi=2e-1.
$$

The idempotents $0$ and $1$ correspond to the roots $-1$ and $+1$.

*Proof.* If $\xi^2=1$, then

$$
e^2=\tfrac14(1+2\xi+\xi^2)=\tfrac14(2+2\xi)=\tfrac12(1+\xi)=e.
$$

If $e^2=e$, then

$$
(2e-1)^2=4e^2-4e+1=1.
$$

The two maps are inverse to each other: $\frac12(1+(2e-1))=e$ and $2\cdot\frac12(1+\xi)-1=\xi$.

**Corollary.** An algebra has a nontrivial idempotent exactly when it has a root of $1$ other than $\pm1$. In a division algebra the only roots of $1$ are $\pm1$, so the only idempotents are $0$ and $1$.

*Proof.* The first statement is the theorem. In a division algebra, $\xi^2=1$ gives $(\xi-1)(\xi+1)=0$, and there are no zero divisors, so $\xi=\pm1$.

**Remark.** The corollary is the cleanest proof that a division algebra has no nontrivial idempotents, and it explains why the idempotent question is a question about the roots of the polynomial $x^2-1$. In a field the polynomial has at most two roots, so the idempotents are $0,1$; in a product of two fields the polynomial has four roots, and the two extra ones give the two nontrivial idempotents; in a matrix algebra the polynomial has many roots, and the idempotents are many. The dual numbers are the case in which the polynomial still has only two roots, although the algebra is not a field: the nilpotent direction does not solve $x^2=1$.

### The roots of one in the number systems

The following table records the roots of $1$ and the idempotents. The count "many" means a positive-dimensional family; the precise parameterization is in the sections below.

| Algebra | Roots of $1$ | Idempotents |
|---|---|---|
| $\mathbb{R}$ | $\pm1$ | $0,1$ |
| $\mathbb{C}$ | $\pm1$ | $0,1$ |
| $\mathbb{H}$ | $\pm1$ | $0,1$ |
| $\mathbb{D}$ | $\pm1,\ \pm j$ | $0,1,\ \Pi_+,\ \Pi_-$ |
| $\mathbb{D}'$ | $\pm1$ | $0,1$ |
| $\mathbb{H}_{\mathbb{D}}$ | $(\pm1,\pm1)$ | $0,1,\ \Pi_+,\ \Pi_-$ |
| $\mathbb{B}$ | many | many |

The table is the skeleton of the article. The first three rows are the division algebras; the fourth and sixth are the split algebras; the fifth is the local algebra; the last is the matrix algebra.

## Division Algebras Have None

### The theorem

**Theorem.** A division algebra has no nontrivial idempotents.

*Proof.* Let $e^2=e$. Then $e(e-1)=0$. If $e\neq0$ and $e\neq1$, both factors are nonzero, contradicting the absence of zero divisors. Hence $e=0$ or $e=1$.

**Corollary.** The algebras $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ have exactly the idempotents $0$ and $1$.

*Proof.* Each is a division algebra: $\mathbb{R}$ and $\mathbb{C}$ are fields, and $\mathbb{H}$ is a division algebra by the quaternion norm. The theorem applies.

**Remark.** The theorem is one-directional. The converse is false, and the dual numbers are the counterexample: they have no nontrivial idempotents and are not a division algebra. The correct converse is local, not division: a finite-dimensional local algebra has no nontrivial idempotents, and a finite-dimensional commutative algebra with no nontrivial idempotents is local. The noncommutative matrix algebra is the case in which neither converse holds: it is simple, not local, and has nontrivial idempotents.

### The quaternions

The quaternion algebra is the most instructive division algebra of the list. Its idempotents are $0$ and $1$, and the roots of $1$ are $\pm1$; the roots of $-1$ are the unit sphere of the pure imaginary subspace,

$$
\{q\in\mathbb{H}:q^2=-1\}=\{q:\operatorname{Re}q=0,\ |q|=1\},
$$

which is a two-sphere. The halving map sends the roots of $1$ to idempotents and the roots of $-1$ to elements of square $\frac12\xi$, not to idempotents. The contrast with the split complex numbers is exactly the sign: in $\mathbb{D}$ the element $j$ has square $+1$ and gives the idempotent $\frac12(1+j)$; in $\mathbb{H}$ the pure imaginary units have square $-1$ and give no idempotent. The quaternion algebra is a division algebra, the split complex algebra is not, and the sign of the square is the algebraic reason.

## Local Algebras Have None

### The dual numbers

Let $\mathbb{D}'=\mathbb{R}[\varepsilon]/(\varepsilon^2)$. An element is $a+b\varepsilon$, with $a,b\in\mathbb{R}$. Its square is $a^2+2ab\varepsilon$, so the idempotents satisfy

$$
a^2=a, \qquad 2ab=b.
$$

If $a=0$, then $b=0$; if $a=1$, then $2b=b$, so $b=0$ in characteristic not two. Hence the only idempotents are $0$ and $1$. The algebra has a nonzero nilpotent $\varepsilon$, so it is not a division algebra; it is not a field; it has zero divisors; but it has no nontrivial idempotents.

**Theorem.** The algebra $\mathbb{D}'$ is local with maximal ideal $(\varepsilon)$, and a local algebra has no nontrivial idempotents.

*Proof.* The ideal $(\varepsilon)$ is the set of nonunits: $a+b\varepsilon$ is a unit exactly when $a\neq0$, with inverse $a^{-1}-a^{-2}b\varepsilon$. The quotient $\mathbb{D}'/(\varepsilon)\cong\mathbb{R}$ is a field, so $(\varepsilon)$ is the unique maximal ideal. If $e$ is an idempotent in a local algebra with maximal ideal $\mathfrak{m}$, then $e$ and $1-e$ cannot both lie in $\mathfrak{m}$, because their sum is $1\notin\mathfrak{m}$; hence one of them is a unit. If $e$ is a unit and $e^2=e$, then $e=1$; if $1-e$ is a unit and $e(1-e)=0$, then $e=0$. Hence $e=0$ or $1$.

**Corollary.** The dual numbers have exactly the idempotents $0$ and $1$, and the unit $1$ is primitive.

*Proof.* The theorem gives the idempotents; $1$ is not the sum of two nonzero orthogonal idempotents because there are no nonzero idempotents other than $1$.

**Remark.** The dual numbers are the standard example of an algebra that is indecomposable but not simple and not a division algebra. The left ideals are $0$, $(\varepsilon)$ and $\mathbb{D}'$; the ideal $(\varepsilon)$ is nilpotent, so it is not a direct summand, and the algebra is local. The example shows that "no nontrivial idempotents" is a statement about the absence of direct sum decompositions, not about the absence of zero divisors.

## The Split Complex Numbers

### The four idempotents

Let $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$. An element is $a+bj$, and the idempotent equations are

$$
a^2+b^2=a, \qquad 2ab=b.
$$

If $b=0$, then $a=0$ or $a=1$. If $b\neq0$, then $a=\frac12$ and $b^2=\frac14$, so $b=\pm\frac12$. Hence the idempotents are

$$
0, \qquad 1, \qquad \Pi_+=\tfrac12(1+j), \qquad \Pi_-=\tfrac12(1-j).
$$

They satisfy $\Pi_+^2=\Pi_+$, $\Pi_-^2=\Pi_-$, $\Pi_+\Pi_-=0$ and $\Pi_++\Pi_-=1$. The two nontrivial idempotents are orthogonal and complete; they are the units of the two factors in the isomorphism

$$
\mathbb{D}\longrightarrow\mathbb{R}\times\mathbb{R}, \qquad a+bj\longmapsto(a+b,a-b).
$$

The inverse is $(x,y)\mapsto\frac12(x+y)+\frac12(x-y)j$. The idempotents $\Pi_+$ and $\Pi_-$ are the images of $(1,0)$ and $(0,1)$, so they are central: $\mathbb{D}$ is commutative.

### The Peirce decomposition

With $e=\Pi_+$ and $f=\Pi_-$, the Peirce corners are

$$
e\mathbb{D}e=\mathbb{R}\Pi_+, \qquad f\mathbb{D}f=\mathbb{R}\Pi_-, \qquad e\mathbb{D}f=f\mathbb{D}e=0,
$$

because $ef=0$ and the algebra is commutative. The Peirce decomposition is the direct sum of the two lines, and the algebra is the product of the two copies of $\mathbb{R}$. The two nontrivial idempotents are primitive: each factor is a field, and the only idempotent of a field is $0$ or $1$. The algebra is semisimple, not simple, and it is not a division algebra.

**Remark.** The split complex numbers are the smallest algebra with a nontrivial idempotent. The idempotent $\Pi_+$ is a zero divisor, and its complementary idempotent $\Pi_-$ is the other factor; the pair $\Pi_+,\Pi_-$ is the algebraic model of the two-point space. The example is the prototype of the split algebras: a split algebra is one that contains a nontrivial idempotent, equivalently one whose identity has a proper direct sum decomposition.

## The Biquaternions

### The matrix algebra

The biquaternions are

$$
\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C}).
$$

The isomorphism is the standard one: choose a representation of the quaternion units by the Pauli matrices, and let the complex scalars act on the tensor factor. The algebra is simple, its centre is $\mathbb{C}$, and its only two-sided ideals are $0$ and $\mathbb{B}$. It is not a division algebra: it has zero divisors, beginning with the idempotents.

### The idempotents

An idempotent in $M_2(\mathbb{C})$ is a projection: a matrix $e$ with $e^2=e$. The trivial idempotents are $0$ and $I$. The nontrivial idempotents are the rank-one projections. A rank-one projection is the projection onto a line $L$ along a complementary line $K$, with $V=L\oplus K$; it has the form

$$
e=u\varphi, \qquad \varphi(u)=1,
$$

where $u$ spans $L$ and $\varphi$ is the linear functional with kernel $K$. The pair $(L,K)$ of complementary lines in $\mathbb{C}^2$ is the parameter, so the rank-one projections form a two-complex-parameter family; equivalently, the pairs of distinct points of $\mathbb{C}P^1$. The two matrix units

$$
E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix}, \qquad E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}
$$

are the rank-one projections onto the coordinate lines along the other coordinate lines; they are orthogonal and complete, $E_{11}+E_{22}=I$. The off-diagonal matrix units $E_{12},E_{21}$ are not idempotents: $E_{12}^2=0$.

**Theorem.** The central idempotents of $\mathbb{B}$ are $0$ and $1$; every other idempotent is noncentral.

*Proof.* The centre of $M_2(\mathbb{C})$ is $\mathbb{C}I$. An idempotent in the centre is a scalar $\lambda I$ with $\lambda^2=\lambda$, so $\lambda=0$ or $1$. A rank-one projection is not scalar, so it is not central.

**Remark.** The theorem is the precise form of the statement that a simple algebra can have many idempotents. The centre is a field, so the only central idempotents are $0$ and $1$; the algebra is a full matrix algebra of size at least two, so it has noncentral idempotents. The contrast with the quaternions is the contrast between a division algebra and a full matrix algebra: $\mathbb{H}$ has no nontrivial idempotents, and $\mathbb{B}\cong M_2(\mathbb{C})$ has many. Both are central simple, of degree two over their centres $\mathbb{R}$ and $\mathbb{C}$ respectively; the difference is that the first is a division algebra and the second is split.

### The Peirce decomposition

With $e=E_{11}$ and $f=E_{22}$, the four Peirce corners are

$$
e\mathbb{B}e=\mathbb{C}E_{11}, \quad e\mathbb{B}f=\mathbb{C}E_{12}, \quad f\mathbb{B}e=\mathbb{C}E_{21}, \quad f\mathbb{B}f=\mathbb{C}E_{22}.
$$

All four are one-dimensional, and the multiplication table is $E_{ij}E_{kl}=\delta_{jk}E_{il}$. The Peirce decomposition is the decomposition of the matrix algebra into its matrix units; the diagonal corners are the two lines of diagonal matrices, and the off-diagonal corners are the two lines of off-diagonal matrices. The idempotent $E_{11}$ is primitive, and the left ideal $\mathbb{B}E_{11}$ is the first column, a minimal left ideal isomorphic to $\mathbb{C}^2$. The algebra is simple, so all the minimal left ideals are isomorphic, and the primitive idempotents are all the rank-one projections.

**Remark.** The biquaternion idempotents are the model of the noncentral idempotents of a simple algebra. The rank-one projections are the primitive idempotents; the two matrix units $E_{11},E_{22}$ are a complete orthogonal pair; and the Peirce decomposition is the finest decomposition of the matrix algebra. The central idempotents are only $0,1$, so the algebra is not a product of two smaller algebras; the noncentral idempotents decompose it as a left module, not as an algebra.

## The Split Biquaternions

### The product of two quaternion algebras

The split biquaternions are

$$
\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_\mathbb{R}\mathbb{H}\cong\mathbb{H}\times\mathbb{H}.
$$

The isomorphism is the split-complex decomposition $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$: the tensor product of $\mathbb{H}$ with a product is the product of two copies of $\mathbb{H}$. The centre is $\mathbb{D}$, and the two factors are the two maximal ideals. The algebra is semisimple, not simple, and it is not a division algebra.

### The four idempotents

An idempotent of a product $A_1\times A_2$ is a pair $(e_1,e_2)$ with $e_i$ idempotent in $A_i$. Each $A_i$ is the quaternion division algebra, whose only idempotents are $0$ and $1$; hence the product has exactly four idempotents:

$$
(0,0)=0, \qquad (1,1)=1, \qquad (1,0)=\Pi_+, \qquad (0,1)=\Pi_-.
$$

All four are central, because they are the characteristic functions of the two factors. The two nontrivial idempotents are the images of the two idempotents $\Pi_\pm$ of the centre $\mathbb{D}$ under the isomorphism, and they satisfy $\Pi_++\Pi_-=1$, $\Pi_+\Pi_-=0$, $\Pi_+^2=\Pi_+$, $\Pi_-^2=\Pi_-$.

**Theorem.** The split biquaternions have exactly four idempotents, all central. There are no noncentral idempotents.

*Proof.* The idempotents of the product are the pairs of idempotents of the factors, and each factor is a division algebra with only $0,1$. The four pairs are central because each factor is a division algebra and its idempotents are central.

**Remark.** The split biquaternions are the opposite extreme from the biquaternions among the eight-dimensional algebras: $\mathbb{B}\cong M_2(\mathbb{C})$ has many noncentral idempotents and only two central ones, while $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\times\mathbb{H}$ has four idempotents, all central, and no noncentral ones. The difference is the difference between a simple matrix algebra and a product of two division algebras. The split biquaternion idempotents are treated in detail in *Split-Biquaternion Idempotents and Projections*.

### The Peirce decomposition

With $e=\Pi_+$ and $f=\Pi_-$, the Peirce corners are

$$
e\mathbb{H}_{\mathbb{D}}e\cong\mathbb{H}, \qquad f\mathbb{H}_{\mathbb{D}}f\cong\mathbb{H}, \qquad e\mathbb{H}_{\mathbb{D}}f=f\mathbb{H}_{\mathbb{D}}e=0.
$$

The Peirce decomposition is the direct sum of the two copies of $\mathbb{H}$, and the two corners are division algebras. The algebra is the product of the two, and the two idempotents are the units of the factors.

## The Property Ladder

### The table

The following table collects the structural properties. "Local" means a unique maximal left ideal, equivalently a unique maximal ideal in the commutative case; "simple" means no nontrivial two-sided ideals; "semisimple" means zero Jacobson radical, equivalently a product of matrix algebras over division algebras in finite dimension.

| Algebra | Division | Local | Simple | Semisimple | Nontrivial idempotents |
|---|---|---|---|---|---|
| $\mathbb{R}$ | yes | yes | yes | yes | no |
| $\mathbb{C}$ | yes | yes | yes | yes | no |
| $\mathbb{H}$ | yes | yes | yes | yes | no |
| $\mathbb{D}$ | no | no | no | yes | yes |
| $\mathbb{D}'$ | no | yes | no | no | no |
| $\mathbb{B}$ | no | no | yes | yes | yes |
| $\mathbb{H}_{\mathbb{D}}$ | no | no | no | yes | yes |

### The implications

The table is organized by the implications

$$
\text{division}\Longrightarrow\text{local}\Longrightarrow\text{no nontrivial idempotents},
$$

and

$$
\text{division}\Longrightarrow\text{simple}\Longrightarrow\text{semisimple}.
$$

The first chain is the content of §*Division Algebras Have None* and §*Local Algebras Have None*. The second is the standard structure theory: a division algebra is simple, and a finite-dimensional simple algebra is semisimple because its radical is a two-sided ideal. The table respects both chains: every division algebra is local, simple and semisimple, and every local algebra has no nontrivial idempotents.

### The non-implications

The table also records the failures of the converses, and these failures are the reason the article exists.

- **Not division does not imply a nontrivial idempotent.** The dual numbers $\mathbb{D}'$ are not a division algebra, and they have no nontrivial idempotents. They are local.
- **Simple does not imply no nontrivial idempotents.** The biquaternions $\mathbb{B}\cong M_2(\mathbb{C})$ are simple, and they have many nontrivial idempotents. They are a full matrix algebra of size two.
- **Semisimple does not imply no nontrivial idempotents.** The split complex numbers $\mathbb{D}$ and the split biquaternions $\mathbb{H}_{\mathbb{D}}$ are semisimple, and they have nontrivial idempotents. They are products of two algebras.
- **No nontrivial idempotents does not imply simple.** The dual numbers have no nontrivial idempotents and are not simple; the ideal $(\varepsilon)$ is nontrivial.
- **No nontrivial idempotents does not imply division.** The dual numbers are the counterexample.
- **Local does not imply division.** The dual numbers are local and not a division algebra.

The pattern behind the failures is the same: the existence of a nontrivial idempotent is the existence of a proper direct summand of the left regular module. A division algebra has no proper nonzero left ideals at all, so it has no idempotents; a local algebra has proper left ideals, but none is a direct summand, so it has no nontrivial idempotents; a simple matrix algebra has proper left ideals that are direct summands, so it has nontrivial idempotents; a product of two algebras has the two factors as direct summands, so it has central idempotents.

### The exact criterion

**Theorem.** For a finite-dimensional unital algebra $A$, the following are equivalent:

1. $A$ has no nontrivial idempotents;
2. the unit $1$ is primitive;
3. the left regular module $A$ is indecomposable;
4. the only direct summands of the left regular module are $0$ and $A$.

*Proof.* The equivalence of 1 and 2 is the definition of primitivity: a decomposition $1=e+f$ with $e,f$ nonzero orthogonal idempotents is exactly a nontrivial idempotent $e$ with $f=1-e$. The equivalence of 2 and 3 is the correspondence between idempotents and direct summands: a direct summand of $A$ is a left ideal $Ae$ with $e$ idempotent, and $A=Ae\oplus A(1-e)$; the summand is proper and nonzero exactly when $e$ is neither $0$ nor $1$. The equivalence of 3 and 4 is the definition of indecomposability.

**Corollary.** A finite-dimensional algebra has no nontrivial idempotents exactly when it is local.

*Proof.* A local algebra has no nontrivial idempotents by §*Local Algebras Have None*. Conversely, suppose that $A$ has no nontrivial idempotents. The quotient $A/J(A)$ by the Jacobson radical is semisimple, hence a finite product of matrix algebras $M_{n_i}(D_i)$ over division algebras. A product of two or more factors has the nontrivial central idempotents of the factors, and $M_n(D)$ with $n\ge2$ has the nontrivial idempotent $E_{11}$; both would lift to nontrivial idempotents of $A$, because idempotents lift modulo the nilpotent radical. Hence $A/J(A)$ is a single division algebra $D$. The radical is then the unique maximal left ideal, so $A$ is local.

**Remark.** The corollary is the exact criterion in the finite-dimensional case. It explains the dual numbers, the split complex numbers, the matrix algebra and the division algebras in one statement: the dual numbers are local and have no nontrivial idempotents; the split complex numbers are a product of two local algebras and have the two central idempotents; the matrix algebra $M_n(k)$ for $n\ge2$ is not local and has nontrivial idempotents; and a division algebra is local and has none. The module-theoretic criterion of the theorem is the general form; the local criterion is its finite-dimensional form.

## Summary

The number systems split into two groups by their idempotents. The algebras without nontrivial idempotents are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{D}'$; the algebras with them are $\mathbb{D}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$. The division algebras $\mathbb{R},\mathbb{C},\mathbb{H}$ have none because they have no zero divisors; the dual numbers have none because they are local, with the nilpotent maximal ideal $(\varepsilon)$ and the primitive unit; the split complex numbers have the two central idempotents $\frac12(1\pm j)$ and decompose as $\mathbb{R}\times\mathbb{R}$; the biquaternions $\mathbb{B}\cong M_2(\mathbb{C})$ have a two-parameter family of noncentral rank-one projections and only the central idempotents $0,1$; and the split biquaternions $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\times\mathbb{H}$ have exactly four idempotents, all central, the characteristic functions of the two quaternion factors. The halving bijection $e\mapsto2e-1$ identifies the idempotents with the roots of $1$, so the question is the question of the roots of $x^2-1$: two roots in a division algebra or a local algebra, four in a product of two fields, and many in a matrix algebra. The exact criterion is that the unit is primitive, equivalently the left regular module is indecomposable; for a finite-dimensional algebra this is equivalent to locality. The comparison is the companion of *Examples of Algebras*, *Unital Algebras*, *Division Algebras*, *Split Complex Idempotents and Projections*, *Split-Biquaternion Idempotents and Projections* and *Square Roots of One and the Idempotents of the Quaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R},\mathbb{C},\mathbb{H}$ | the real, complex and quaternion division algebras |
| $\mathbb{D}=\mathbb{R}[j]$, $j^2=1$ | the split complex numbers |
| $\mathbb{D}'=\mathbb{R}[\varepsilon]$, $\varepsilon^2=0$ | the dual numbers |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ | the biquaternions |
| $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_\mathbb{R}\mathbb{H}\cong\mathbb{H}\times\mathbb{H}$ | the split biquaternions |
| $\Pi_\pm=\frac12(1\pm j)$ | the two nontrivial idempotents of $\mathbb{D}$ |
| $e,f$ | orthogonal idempotents, $ef=fe=0$ |
| $Ae$ | the left ideal, a direct summand of the left regular module |
| $1$ primitive | $1$ is not the sum of two nonzero orthogonal idempotents |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the correspondence between idempotents and direct summands, the Peirce decomposition and the structure of finite-dimensional algebras.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the division algebras, the simple algebras and the matrix algebras.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the local rings, the primitive idempotents and the Jacobson radical.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the number systems, their norms and their split forms.
