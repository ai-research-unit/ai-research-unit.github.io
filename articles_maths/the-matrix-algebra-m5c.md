# __The Matrix Algebra $M_5(\mathbb{C})$__

## Introduction

The algebra $M_5(\mathbb{C})$ is the algebra of complex $5\times5$ matrices with the ordinary product. It is the model on which every structure of this category is read: the root $H$, the Lagrange idempotents, the Peirce lines, the frame, the spin chain and the adjoint action are all structures on this one algebra. This article fixes the algebra itself: the matrix units and their product rule, the trace and the determinant, the centre, the simplicity, the real dimension $50$, the unit group $GL_5(\mathbb{C})$, the projective group $PGL_5(\mathbb{C})$ of complex dimension $24$, and the reading of the algebra as the complexification of the real Lie algebra $\mathfrak{u}(5)$.

The article uses **no form and no topology**. The conjugate transpose appears only to exhibit the real form $\mathfrak{u}(5)$ and the Hermitian and skew-Hermitian parts; the positive definite trace form, the Frobenius norm and the $*$-unitary group as a metric object are *The Involution and the Hermitian Structure*. The determinant is used as a polynomial and as the criterion of invertibility, not as a volume. The root and the idempotents are later articles; the algebra is their common ground.

The article assumes the general theory of associative algebras of *Associative Algebras* and *Matrix Algebras*: the matrix units, the trace, the determinant, the centre and the two-sided ideals. It proves the facts in the case $n=5$ so that the rest of the category can cite them without returning to the general theory.

## The Algebra and the Matrix Units

### The Definition

**Definition.** The **matrix algebra** $M_5(\mathbb{C})$ is the set of $5\times5$ arrays $A=(A_{ij})_{1\le i,j\le5}$ with entries in $\mathbb{C}$, with the sum $(A+B)_{ij}=A_{ij}+B_{ij}$, the scalar product $(\lambda A)_{ij}=\lambda A_{ij}$, and the product

$$
(AB)_{ij}=\sum_{k=1}^{5}A_{ik}B_{kj}.
$$

The **unit** is the identity matrix $I=(\delta_{ij})$.

**Definition.** The **matrix unit** $E_{ij}$ is the matrix with entry $1$ in position $(i,j)$ and $0$ elsewhere.

**Proposition.** The twenty-five matrix units form a basis of $M_5(\mathbb{C})$, and every $A$ has the unique expansion

$$
A=\sum_{i,j=1}^{5}A_{ij}E_{ij}.
$$

**Proof.** The matrix $E_{ij}$ has a single nonzero entry, so the expansion with the entries of $A$ reproduces $A$. If $\sum_{i,j}a_{ij}E_{ij}=0$, looking at the entry $(i,j)$ gives $a_{ij}=0$. The dimension is $25$ over $\mathbb{C}$.

### The Multiplication

**Proposition (the product rule).** For all indices,

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

**Proof.** The $(a,b)$ entry of $E_{ij}E_{kl}$ is $\sum_c\delta_{a,i}\delta_{c,j}\delta_{c,k}\delta_{b,l}=\delta_{a,i}\delta_{j,k}\delta_{b,l}$, which is the $(a,b)$ entry of $\delta_{jk}E_{il}$.

**Corollary.** The product of two matrices is the double sum

$$
AB=\sum_{i,j,k,l}A_{ij}B_{kl}E_{ij}E_{kl}=\sum_{i,j,l}A_{ij}B_{jl}E_{il},
$$

which is the coordinate rule of the definition.

**Proposition (associativity).** For all $A,B,C$,

$$
(AB)C=A(BC).
$$

**Proof.** Both sides have the $(i,l)$ entry $\sum_{j,k}A_{ij}B_{jk}C_{kl}$, by the associativity of the sum and the product in $\mathbb{C}$. In the matrix units, $(E_{ij}E_{kl})E_{mn}=\delta_{jk}\delta_{lm}E_{in}=E_{ij}(E_{kl}E_{mn})$, so the identity holds on the basis and hence everywhere by trilinearity.

**Proposition (the unit).** The identity matrix satisfies $IA=AI=A$ for every $A$.

**Proof.** $(IA)_{ij}=\sum_k\delta_{ik}A_{kj}=A_{ij}$; the right identity is the same.

### Non-Commutativity

**Proposition.** The algebra is not commutative for $n=5\ge2$.

**Proof.** $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$, and $E_{11}\ne E_{22}$.

**Corollary.** The centre is a proper subspace, and the algebra is not a field. The centre is computed in §*The Centre and Simplicity*.

## The Trace and the Determinant

### The Trace

**Definition.** The **trace** of $A$ is

$$
\operatorname{tr}A=\sum_{i=1}^{5}A_{ii}.
$$

**Proposition.** The trace is linear and satisfies

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA),\qquad
\operatorname{tr}(ABC)=\operatorname{tr}(BCA)=\operatorname{tr}(CAB)
$$

for all $A,B,C$.

**Proof.** $\operatorname{tr}(AB)=\sum_i\sum_kA_{ik}B_{ki}=\sum_k\sum_iB_{ki}A_{ik}=\operatorname{tr}(BA)$. The cyclic invariance follows by applying the two-term identity twice.

**Corollary.** The trace of a commutator is zero: $\operatorname{tr}[A,B]=0$. The trace of a matrix unit is $\operatorname{tr}E_{ij}=\delta_{ij}$.

### The Trace Pairing

**Definition.** The **trace pairing** is the complex bilinear form

$$
\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB).
$$

**Proposition.** The trace pairing is nondegenerate and symmetric.

**Proof.** It is symmetric because $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. If $\operatorname{tr}(AB)=0$ for every $B$, choose $B=E_{ji}$; then $\operatorname{tr}(AE_{ji})=A_{ij}$, so every entry of $A$ is zero. The same argument with $A$ and $B$ exchanged gives nondegeneracy in the second slot.

**Remark.** The pairing is **not** positive definite, and it is not a Hermitian form: it is complex bilinear, and $\operatorname{tr}(A^2)$ can vanish for a nonzero $A$. The positive definite form $\operatorname{tr}(A^*B)$ is a different object, defined with the conjugate transpose in *The Involution and the Hermitian Structure*. The trace pairing is the algebraic pairing of the Frobenius algebra $M_5(\mathbb{C})$; the definite form is the metric of the Hilbert space.

### The Determinant

**Definition.** The **determinant** is

$$
\det A=\sum_{\sigma\in S_5}\operatorname{sgn}(\sigma)\prod_{i=1}^{5}A_{i,\sigma(i)}.
$$

**Proposition.** The determinant is multiplicative, $\det(AB)=\det A\det B$, homogeneous of degree $5$, $\det(\lambda A)=\lambda^5\det A$, and it satisfies $\det I=1$. An element $A$ is invertible if and only if $\det A\ne0$.

**Proof.** The multiplicativity is the standard theorem of determinants; the homogeneity follows from the five factors in each product, and $\det I=1$ from the identity permutation. The inverse is given by the adjugate, $A^{-1}=(\det A)^{-1}\operatorname{adj}A$, when $\det A\ne0$; if $\det A=0$, the columns are linearly dependent and $A$ is not invertible.

**Corollary.** The **special linear group** $SL_5(\mathbb{C})=\{A:\det A=1\}$ is a subgroup of $GL_5(\mathbb{C})$, and $GL_5(\mathbb{C})=\{A:\det A\ne0\}$ is the group of units of the algebra.

## The Centre and Simplicity

### The Centre

**Theorem.** The centre of $M_5(\mathbb{C})$ is the line of scalar matrices:

$$
Z(M_5(\mathbb{C}))=\mathbb{C}I .
$$

**Proof.** Let $A$ be central. For every pair $(i,j)$, the identity $AE_{ij}=E_{ij}A$ holds. The left side has entries $(AE_{ij})_{ab}=A_{ai}\delta_{bj}$, and the right side has entries $(E_{ij}A)_{ab}=\delta_{ai}A_{jb}$. At $(a,b)=(i,j)$ the left side is $A_{ii}$ and the right side is $A_{jj}$; hence all diagonal entries are equal. At $(a,b)=(k,j)$ with $k\ne i$, the left side is $A_{ki}$ and the right side is $0$; hence every off-diagonal entry in column $i$ is zero. As $i$ ranges, $A$ is scalar. Conversely every scalar matrix is central.

**Corollary.** The centre is one-dimensional over $\mathbb{C}$ and two-dimensional over $\mathbb{R}$. The algebra is **central** over $\mathbb{C}$: the structure map $\mathbb{C}\to Z(M_5)$, $\lambda\mapsto\lambda I$, is an isomorphism onto the centre.

### Simplicity

**Definition.** A two-sided ideal of $M_5(\mathbb{C})$ is a subspace $J$ with $AJ\subseteq J$ and $JA\subseteq J$ for every $A$.

**Theorem.** The algebra $M_5(\mathbb{C})$ is **simple**: its only two-sided ideals are $0$ and $M_5(\mathbb{C})$.

**Proof.** Let $J\ne0$ and let $0\ne A\in J$. Choose $(i,j)$ with $A_{ij}\ne0$. Then

$$
E_{ii}AE_{jj}=A_{ij}E_{ij}\in J,
$$

so $E_{ij}\in J$ because $A_{ij}\ne0$. For every pair $(k,l)$,

$$
E_{ki}E_{ij}E_{jl}=E_{kl}\in J .
$$

Hence $J$ contains every matrix unit, and therefore $J=M_5(\mathbb{C})$.

**Corollary.** The algebra is **central simple** over $\mathbb{C}$: simple with centre $\mathbb{C}I$. It is therefore a full matrix algebra over a division ring, and the division ring is $\mathbb{C}$ itself, by the finite-dimensional version of the Wedderburn theorem; conversely every central simple algebra of degree $5$ over $\mathbb{C}$ is isomorphic to $M_5(\mathbb{C})$. The general theory is *Central Simple Algebras and the Brauer Group*.

**Remark.** **The simplicity is a two-sided statement.** The algebra has many one-sided ideals: the minimal left ideals are the spaces $M_5P$ for rank-one idempotents $P$, of dimension $5$, and the minimal right ideals are the spaces $PM_5$. The two-sided ideals are only $0$ and the whole algebra. The one-sided ideals are the modules of *The Modules and the Minimal Left Ideals*.

## The Unit Group and the Projective Group

### The Unit Group

**Theorem.** The group of units of $M_5(\mathbb{C})$ is

$$
GL_5(\mathbb{C})=\{A\in M_5(\mathbb{C}):\det A\ne0\}.
$$

It is a complex Lie group of complex dimension $25$ and real dimension $50$.

**Proof.** A matrix is invertible if and only if its determinant is nonzero, by the adjugate formula. The determinant is a polynomial on $M_5(\mathbb{C})\cong\mathbb{C}^{25}$, not identically zero, so its nonvanishing locus is a nonempty Zariski open set, of complex dimension $25$. The real dimension is twice the complex dimension, $50$.

**Corollary.** The Lie algebra of $GL_5(\mathbb{C})$ is $M_5(\mathbb{C})$ itself, of real dimension $50$, with the commutator bracket $[A,B]=AB-BA$.

**Proof.** The tangent space at the identity of an open subset of a vector space is the vector space; the bracket of the matrix group is the commutator.

### The Special Linear Group

**Proposition.** The special linear group

$$
SL_5(\mathbb{C})=\{A:\det A=1\}
$$

is a closed complex subgroup of $GL_5(\mathbb{C})$ of complex dimension $24$ and real dimension $48$.

**Proof.** The determinant is a holomorphic function with derivative $\operatorname{tr}$ at the identity, which is nonzero (it is the trace, a nonzero linear functional); the level set $\det=1$ is therefore a smooth hypersurface, of dimension $25-1=24$. The group structure is inherited.

### The Projective Group

**Definition.** The **projective linear group** is the quotient

$$
PGL_5(\mathbb{C})=GL_5(\mathbb{C})/\mathbb{C}^\times I,
$$

where $\mathbb{C}^\times I$ is the group of nonzero scalar matrices, the centre of $GL_5$.

**Theorem.** $PGL_5(\mathbb{C})$ is a complex Lie group of complex dimension $24$ and real dimension $48$. It is isomorphic to $SL_5(\mathbb{C})/\mu_5$, where $\mu_5$ is the group of fifth roots of unity acting by scalar multiplication.

**Proof.** The centre of $GL_5$ is $\mathbb{C}^\times I$, of complex dimension $1$; the quotient has dimension $25-1=24$. The map $SL_5\to PGL_5$ is surjective: every class $[A]$ has a representative with determinant $1$, namely $A/(\det A)^{1/5}$ for any chosen fifth root, and two such representatives differ by a fifth root of unity. The kernel is $\mu_5$.

**Remark.** **The dimension $24$ is the complex dimension.** The real dimension of $PGL_5(\mathbb{C})$ is $48$, not $24$. The root set of *Roots of Unity and the Lagrange Idempotents* is $PGL_5/T$, of complex dimension $20$; the gauge torus $T$ is complex dimension $4$; the sum is $24$. The real dimensions are $40$, $8$ and $48$.

### The Counting Table

| Group | Complex dimension | Real dimension |
|---|---|---|
| $M_5(\mathbb{C})$ | $25$ | $50$ |
| $GL_5(\mathbb{C})$ | $25$ | $50$ |
| $SL_5(\mathbb{C})$ | $24$ | $48$ |
| $PGL_5(\mathbb{C})$ | $24$ | $48$ |
| $PGL_5/T$ (root set) | $20$ | $40$ |
| $T$ (gauge) | $4$ | $8$ |

## The Hermitian and Skew-Hermitian Parts

### The Conjugate Transpose

**Definition.** The **conjugate transpose** of $A$ is

$$
A^*=\bar A^{\mathsf T},\qquad (A^*)_{ij}=\overline{A_{ji}}.
$$

**Proposition.** The conjugate transpose is an involutive anti-automorphism of the real algebra:

$$
(A+B)^*=A^*+B^*,\qquad (\lambda A)^*=\bar\lambda A^*,\qquad (AB)^*=B^*A^*,\qquad (A^*)^*=A .
$$

**Proof.** The entries are conjugated and transposed; the reversal of the order in the product is the rule $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$ together with the conjugation of the entries.

**Remark.** The star is an involution of the **real** algebra, not of the complex algebra: it is conjugate-linear, $(\lambda A)^*=\bar\lambda A^*$. The complex-linear anti-automorphism is the transpose $A^{\mathsf T}$, which is not involutive on the complex algebra in the same Hermitian sense. The star is the involution of *The Involution and the Hermitian Structure*.

### The Two Real Subspaces

**Definition.** An element $A$ is **Hermitian** if $A^*=A$ and **skew-Hermitian** if $A^*=-A$. The real vector spaces are

$$
\mathfrak{u}(5)=\{A:A^*=-A\},\qquad
i\mathfrak{u}(5)=\{A:A^*=A\}=\{iX:X\in\mathfrak{u}(5)\}.
$$

**Theorem.** The algebra decomposes as a real direct sum

$$
M_5(\mathbb{C})=\mathfrak{u}(5)\oplus i\mathfrak{u}(5),
$$

and the two summands have real dimension $25$ each. The decomposition of an element is

$$
A=\underbrace{\tfrac12(A-A^*)}_{\text{skew-Hermitian}}+\underbrace{\tfrac12(A+A^*)}_{\text{Hermitian}} .
$$

**Proof.** The two projections are idempotent and sum to the identity; the first is skew-Hermitian, the second Hermitian, and the intersection is zero because a matrix that is both Hermitian and skew-Hermitian is zero. The real dimension of $\mathfrak{u}(5)$ is $25$: a skew-Hermitian matrix has purely imaginary diagonal entries (five real parameters) and arbitrary complex entries above the diagonal ($10$ complex $=20$ real), total $5+20=25$; the Hermitian part has real diagonal entries (five) and arbitrary complex entries above the diagonal (twenty), also $25$.

**Corollary.** The **special $*$-unitary** algebra

$$
\mathfrak{su}(5)=\{A\in\mathfrak{u}(5):\operatorname{tr}A=0\}
$$

has real dimension $24$. The trace is a real linear functional on $\mathfrak{u}(5)$ (the diagonal entries are purely imaginary, and the trace is their sum), and its kernel has dimension $24$.

**Proof.** The trace of a skew-Hermitian matrix is purely imaginary; the condition $\operatorname{tr}A=0$ is one real linear equation on the $25$-dimensional space.

### The Complexification of $\mathfrak{u}(5)$

**Theorem.** The complexification of the real Lie algebra $\mathfrak{u}(5)$ is the complex Lie algebra $\mathfrak{gl}_5(\mathbb{C})=M_5(\mathbb{C})$:

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{u}(5)\cong\mathfrak{gl}_5(\mathbb{C}),\qquad
X\otimes(a+ib)\longmapsto aX+b\,iX .
$$

Similarly, $\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{su}(5)\cong\mathfrak{sl}_5(\mathbb{C})$.

**Proof.** The map is complex bilinear and surjective: every $A$ is $X+iY$ with $X=\frac12(A-A^*)\in\mathfrak{u}(5)$ and $Y=\frac12(A+A^*)\in i\mathfrak{u}(5)$, and $Y=i(-iY)$ with $-iY\in\mathfrak{u}(5)$. The complex dimensions are both $25$, so the surjection is an isomorphism. The traceless case is the same with the trace condition, and the complex dimension $24$ matches.

**Corollary.** The algebra $M_5(\mathbb{C})$ is the **complexification of the compact real form** $\mathfrak{u}(5)$. The Hermitian and skew-Hermitian parts are the two real halves of the complexification; the compact real form is the skew-Hermitian half, and the Hermitian half is its image under multiplication by $i$.

**Remark.** The reading is a reading of the **real** algebra. The complex algebra $M_5(\mathbb{C})$ does not see the star: the same complex algebra is the complexification of several real forms, and the choice of $\mathfrak{u}(5)$ is the choice of the compact one. The other real forms, and the Cartan involution that selects them, are *Real Forms of a Complex Lie Group and the Cartan Involution*.

## The Absence of a Form and a Topology

The algebra $M_5(\mathbb{C})$ is defined by its product alone. The trace, the determinant and the centre are polynomial functions of the entries, and they belong to the algebra; the conjugate transpose is an extra involution, used here only to exhibit the real form. **No positive definite form and no topology are used in this article.** In particular:

- The trace pairing $\operatorname{tr}(AB)$ is a complex bilinear pairing, nondegenerate but indefinite; it is not the metric of a Hilbert space.
- The determinant is a polynomial and a multiplicative character; the locus $\det=0$ is the singular set of *The Forms, the Norms and the Singular Set*, and its topology is not used here.
- The group $GL_5(\mathbb{C})$ is treated as an algebraic group, not as a topological group; its connected components and its homotopy type are *The Topology of $M_5(\mathbb{C})$*.
- The exponential, the polar decomposition and the analysis on the algebra are later articles; the Lie algebra structure used here is only the commutator.

**Remark.** **The algebra is central simple of degree $5$.** Its isomorphism class is determined by the degree, because the Brauer group of $\mathbb{C}$ is trivial; every central simple $\mathbb{C}$-algebra of degree $5$ is isomorphic to $M_5(\mathbb{C})$. This is the algebraic content of the model: there is only one such algebra, and the whole category is the study of its structures.

## Summary

The algebra $M_5(\mathbb{C})$ is the algebra of complex $5\times5$ matrices, of complex dimension $25$ and real dimension $50$, with the matrix units $E_{ij}$ as a basis and the product rule $E_{ij}E_{kl}=\delta_{jk}E_{il}$. It is associative, unital and non-commutative; its centre is the line $\mathbb{C}I$; it is simple and central simple of degree $5$.

$$
\boxed{\ M_5(\mathbb{C})\text{ is central simple of degree }5,\ \dim_{\mathbb{C}}=25,\ \dim_{\mathbb{R}}=50,\ Z(M_5)=\mathbb{C}I.\ }
$$

The trace is linear, cyclic and nondegenerate as a complex bilinear pairing; the determinant is multiplicative and detects invertibility. The unit group is $GL_5(\mathbb{C})$, of complex dimension $25$; the special linear group $SL_5(\mathbb{C})$ has dimension $24$; the projective group $PGL_5(\mathbb{C})$ has complex dimension $24$ and real dimension $48$. The conjugate transpose exhibits the real form $\mathfrak{u}(5)$, of real dimension $25$, and $\mathfrak{su}(5)$, of real dimension $24$; the complexification of $\mathfrak{u}(5)$ is the whole algebra.

| Object | Complex dimension | Real dimension |
|---|---|---|
| $M_5(\mathbb{C})$ | $25$ | $50$ |
| $GL_5(\mathbb{C})$ | $25$ | $50$ |
| $SL_5(\mathbb{C})$ | $24$ | $48$ |
| $PGL_5(\mathbb{C})$ | $24$ | $48$ |
| $\mathfrak{u}(5)$ | — | $25$ |
| $\mathfrak{su}(5)$ | — | $24$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_5(\mathbb{C})$ | The algebra of complex $5\times5$ matrices |
| $E_{ij}$ | The matrix unit with $1$ in position $(i,j)$ |
| $I$ | The identity matrix |
| $\operatorname{tr}A$ | The trace, $\sum_iA_{ii}$ |
| $\det A$ | The determinant |
| $A^{\mathsf T}$ | The transpose |
| $A^*=\bar A^{\mathsf T}$ | The conjugate transpose |
| $GL_5(\mathbb{C})$ | The group of invertible matrices |
| $SL_5(\mathbb{C})$ | The group of determinant one |
| $PGL_5(\mathbb{C})$ | The quotient $GL_5/\mathbb{C}^\times I$ |
| $\mathfrak{u}(5)$ | The skew-Hermitian matrices, real dimension $25$ |
| $\mathfrak{su}(5)$ | The traceless skew-Hermitian matrices, real dimension $24$ |
| $\mathfrak{gl}_5(\mathbb{C})$ | The Lie algebra $M_5(\mathbb{C})$ with the commutator |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix units, the simplicity of a full matrix algebra and the Wedderburn theorem.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the centre, the two-sided ideals and the central simple algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the trace, the determinant, the matrix units and the elementary matrices.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for $GL_5$, $SL_5$, $PGL_5$, the $*$-unitary algebra $\mathfrak{u}(5)$ and the complexification of a real Lie algebra.
- [Matrix Algebras](matrix-algebras.html), for the general theory of $M_n(R)$.
- [Central Simple Algebras and the Brauer Group](central-simple-algebras-and-the-brauer-group.html), for the classification and the triviality of the Brauer group of $\mathbb{C}$.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m5c.html), for the coordinates, the trace pairing and the Jordan decomposition.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m5c.html), for the conjugate transpose, the positive definite trace form and the $*$-unitary group.
- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), for the first structure built on the algebra.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the matrix units and the diagonal gauge.
