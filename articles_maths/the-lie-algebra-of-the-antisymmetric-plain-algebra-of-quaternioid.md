# __The Lie Algebra of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ carries the cross product
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ of
*Introduction to the Antisymmetric Plain Algebra*, which is alternating and satisfies
the Jacobi identity (*The Specificities of the Antisymmetric Plain Algebra*, below this article in
this category). By the definition of the Lie structure it is a **real Lie algebra** of dimension four,
written

$$
\mathfrak{g}=(\mathbb{H},\times).
$$

This article reads its structure: the centre, the derived algebra, the structure constants, the
ideals and the two identifications of the derived algebra with the classical compact Lie algebras
same name.

**This is not the algebra $\mathbb{H}$.** The Lie bracket is the cross product of the vector parts and
ignores the scalars; the associative multiplication of $\mathbb{H}$ plays no role. Throughout, the
natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because
$\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives
nothing new.

The operation and its table are *Introduction to the Antisymmetric Plain Algebra*; the
elements of the structure are *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint
Operators and the Derivations of the Antisymmetric Plain Algebra*, both below this article in this
category, and the general theory of Lie algebras is *Structure of Lie Algebras*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; the cross product of the vector parts is $\vec p\times\vec q$, with
$e_1\times e_2=e_3$ and its cyclic images. The **centre** is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}$, identified with $\mathbb{R}^3$ as a vector space. The
Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$, with $\sigma_j\sigma_k=\delta_{jk}\mathrm{I}_2+i\sum_l\varepsilon_{jkl}\sigma_l$.

## The Lie Algebra and Its Centre

**Theorem.** The space $\mathfrak{g}=\mathbb{H}$ with the bracket $\tilde p\times\tilde q$ is a real
Lie algebra of dimension four. Its bracket vanishes on the scalar direction,

$$
e_0\times\tilde q=0\qquad\text{for every }\tilde q,
$$

and on the pure elements it is the vector product of $\mathbb{R}^3$. Its centre is the scalar line,

$$
\mathfrak{z}(\mathfrak{g})=\{\tilde p:\tilde p\times\tilde q=0\ \text{for every }\tilde q\}=\mathbb{R}e_0 ,
$$

of real dimension one.

*Proof.* The bracket is bilinear and alternating and satisfies the Jacobi identity, which is the Lie
structure. The vanishing on the scalar direction is the table; the fixed elements of the cross product
are the multiples of the scalar direction, since $\vec p\times\vec q=0$ for every $\vec q$
forces $\vec p=0$.

## The Derived Algebra and the Identifications

**Theorem (the derived algebra).** The derived algebra is the vector subspace,

$$
[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{H})=\{\vec q\},
$$

of real dimension three, and it is an ideal. The quotient $\mathfrak{g}/[\mathfrak{g},\mathfrak{g}]$
is the one-dimensional abelian algebra $\mathbb{R}e_0$, so

$$
\mathfrak{g}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})
$$

is the direct sum of its centre and its derived algebra, two ideals.

*Proof.* The bracket of two elements is pure, so $[\mathfrak{g},\mathfrak{g}]\subseteq\mathrm{Vect}(\mathbb{H})$;
and the pure brackets generate the vector subspace, since $e_1\times e_2=e_3$ with its cyclic images
give a basis. The pure subspace is an ideal because $[\tilde p,\vec q]$ is pure for every $\tilde p$.
The sum is direct because the centre meets the derived algebra at $0$, and both are ideals, so the
bracket is the sum of the two brackets.

### The Isomorphism with $\mathfrak{su}(2)$

**Theorem.** The derived algebra is isomorphic to the real Lie algebra $\mathfrak{su}(2)$ of the
traceless skew-Hermitian $2\times2$ complex matrices, by

$$
e_1\mapsto-\tfrac{i}{2}\sigma_1,\qquad e_2\mapsto-\tfrac{i}{2}\sigma_2,\qquad e_3\mapsto-\tfrac{i}{2}\sigma_3 .
$$

*Proof.* The Pauli matrices satisfy $\sigma_j\sigma_k=\delta_{jk}\mathrm{I}_2+i\sum_l\varepsilon_{jkl}\sigma_l$,
so $[-\tfrac{i}{2}\sigma_j,-\tfrac{i}{2}\sigma_k]=-\tfrac14[\sigma_j,\sigma_k]=\sum_l\varepsilon_{jkl}(-\tfrac{i}{2}\sigma_l)$;
the images reproduce the structure constants of the vector product, and they are traceless and
skew-Hermitian. The map is a Lie isomorphism onto $\mathfrak{su}(2)$.

### The Isomorphism with $\mathfrak{so}(3)$

**Theorem.** The derived algebra is isomorphic to the real Lie algebra $\mathfrak{so}(3)$ of the
skew-symmetric $3\times3$ real matrices, by $\vec p\mapsto C_{\vec p}$, the cross-product matrix
$C_{\vec p}\vec q=\vec p\times\vec q$. Under this map the adjoint representation of
$\mathfrak{g}$ on the derived algebra is

$$
\operatorname{ad}_{\tilde p}\longmapsto C_{\vec p},\qquad
\operatorname{ad}_{\tilde p}=\operatorname{diag}(0,C_{\vec p})\ \text{on}\ \mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H}) .
$$

*Proof.* The cross-product matrix is skew-symmetric because $\vec p\times\vec q\perp\vec p$, and
$C_{\vec p}\vec q=\vec p\times\vec q$ is the defining matrix of the cross product; the
identification $C_{\vec p}\leftrightarrow\vec p$ carries the bracket to the commutator,
$[C_{\vec p},C_{\vec q}]=C_{\vec p\times\vec q}$, since the cross product satisfies the
Jacobi identity. The adjoint vanishes on the centre and acts on the pure part by the cross product.

**Remark (the three presentations).** The three algebras $\mathbb{R}^3$ with the cross product,
$\mathfrak{su}(2)$ and $\mathfrak{so}(3)$ are one and the same real Lie algebra of dimension three,
the compact form of $\mathfrak{sl}(2,\mathbb{C})$; the isomorphism between the last two is
$\vec p\mapsto C_{\vec p}$ through the vector product. This is the block's contribution to the
dictionary of the chapter.

## The Structure Constants

In the basis $(e_0,e_1,e_2,e_3)$ the bracket is

$$
[e_0,e_k]=0,\qquad [e_j,e_k]=\sum_{l=1}^{3}\varepsilon_{jkl}e_l\quad(j,k,l\in\{1,2,3\}),
$$

with $\varepsilon$ the Levi-Civita symbol, and the table is the one of the cross product of
$\mathbb{R}^3$ extended by zero on the scalar direction.

| $[\cdot,\cdot]$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $0$ | $e_3$ | $-e_2$ |
| $e_2$ | $0$ | $-e_3$ | $0$ | $e_1$ |
| $e_3$ | $0$ | $e_2$ | $-e_1$ | $0$ |

## The Ideals, the Simplicity and the Centre

**Theorem.** The ideals of $\mathfrak{g}$ are

$$
0,\qquad \mathbb{R}e_0,\qquad \mathrm{Vect}(\mathbb{H}),\qquad \mathfrak{g} ,
$$

and there are no others. The algebra is not simple and not semisimple; its radical is the centre
$\mathbb{R}e_0$; and the derived algebra $\mathrm{Vect}(\mathbb{H})$ is simple.

*Proof.* An ideal is a subspace stable under the brackets. The centre and the derived algebra are
ideals, and the sum is direct; a nonzero proper ideal $\mathfrak{a}$ that is not the centre meets the
derived algebra, and then its intersection with the derived algebra is an ideal of the derived algebra,
which is $\mathfrak{so}(3)$, simple of dimension three, so the intersection is the whole derived
algebra and $\mathfrak{a}$ contains it; if $\mathfrak{a}$ also contains the centre it is
$\mathfrak{g}$, otherwise $\mathfrak{a}=\mathrm{Vect}(\mathbb{H})$. The radical is the largest
solvable ideal, and the algebra is the sum of the abelian centre and the simple derived algebra, so the
radical is the centre and $\mathfrak{g}$ is reductive and not semisimple.

## The Derived Series, Solvability and Nilpotency

**Proposition.** The derived series stabilises at the derived algebra,
$\mathfrak{g}^{(1)}=[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{H})$,
$\mathfrak{g}^{(2)}=[\mathrm{Vect}(\mathbb{H}),\mathrm{Vect}(\mathbb{H})]=\mathrm{Vect}(\mathbb{H})$,
and the lower central series does the same, so $\mathfrak{g}$ is neither solvable nor nilpotent. Its
derived algebra is perfect, $[\mathrm{Vect}(\mathbb{H}),\mathrm{Vect}(\mathbb{H})]=\mathrm{Vect}(\mathbb{H})$.

*Proof.* The derived algebra is $\mathfrak{so}(3)$, which is perfect, so both series freeze at it; a
solvable or nilpotent algebra would have a vanishing terminal term.

**Remark (the enveloping algebra).** Because $\mathfrak{g}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$
is a direct sum of ideals, the universal enveloping algebra is
$\mathrm{U}(\mathfrak{g})\cong\mathbb{R}[z]\otimes\mathrm{U}(\mathfrak{su}(2))$: the centre
contributes the polynomial ring in one variable and the derived algebra the enveloping algebra of
$\mathfrak{su}(2)$, whose centre is the Casimir of *The Killing Form of the Antisymmetric Plain
Algebra*, below this article in this category.

## Summary

The antisymmetric plain block is the real Lie algebra $\mathfrak{g}=(\mathbb{H},\times)$ of dimension
four, the cross product of the vector parts extended by zero on the scalar direction. Its centre is
the scalar line $\mathbb{R}e_0$ and its derived algebra the vector subspace
$\mathrm{Vect}(\mathbb{H})$, so $\mathfrak{g}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$ is the
direct sum of two ideals, reductive with radical the centre and not semisimple. The derived algebra is
the three-dimensional simple algebra $\mathfrak{so}(3)$, also isomorphic to $\mathfrak{su}(2)$ by the
Pauli matrices and to $\mathbb{R}^3$ with the cross product; the structure constants are the
Levi-Civita symbol extended by zero. The ideals are $0$, the centre, the derived algebra and
$\mathfrak{g}$; the algebra is neither solvable nor nilpotent, its derived algebra being perfect. Over
$\mathbb{C}$ the same structure has $\mathfrak{sl}(2,\mathbb{C})$ in the place of the compact form
$\mathfrak{su}(2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{g}=(\mathbb{H},\times)$ | the real Lie algebra of the block |
| $\mathfrak{z}(\mathfrak{g})=\mathbb{R}e_0$ | the centre |
| $[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{H})$ | the derived algebra |
| $\mathfrak{g}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$ | the direct sum decomposition |
| $[e_j,e_k]=\sum_l\varepsilon_{jkl}e_l$ | the structure constants |
| $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ | the derived algebra, the compact form of $\mathfrak{sl}(2,\mathbb{C})$ |
| $e_k\mapsto-\tfrac{i}{2}\sigma_k$ | the isomorphism with $\mathfrak{su}(2)$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra*, for the bracket and the basis table.
- *The Specificities of the Antisymmetric Plain Algebra*, below this article in this category, for the Jacobi identity and the isolation of the block.
- *The Killing Form of the Antisymmetric Plain Algebra*, below this article in this category, for the invariant form, the radical and the Casimir element.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, below this article in this category, for the adjoint representation, its kernel and its image.
- *Structure of Lie Algebras*, for the general theory of ideals, the radical and the semisimple algebras.
