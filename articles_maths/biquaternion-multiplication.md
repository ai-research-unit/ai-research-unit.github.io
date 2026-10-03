# __Biquaternion Multiplication__

## Introduction

This article defines the **product** of two biquaternions and studies the two halves into which it splits. The product of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the complex-linear extension of the quaternion product. It is associative and unital; it is not commutative, and its failure of commutativity is not arbitrary, because the antisymmetric part of the product is the complex cross product of the two vector parts.

The product of two biquaternions is always the sum of its symmetric and its antisymmetric part,

$$
\tilde{P}\tilde{Q} = \tilde{P}\circ\tilde{Q} + \tilde{P}\wedge\tilde{Q} ,
$$

and the two parts are of different kinds. The antisymmetric part is a **pure vector** and makes the algebra a Lie algebra, with the vector subspace as its derived subspace. The symmetric part carries all of the scalar and the mixed scalar–vector terms, and it makes the Hermitian subspace a Jordan algebra. Neither half is a Clifford grade: the split is by order symmetry, not by grade, and the two splits do not coincide.

The article assumes the elements, the basis and the conjugations from *Biquaternion Algebra* and *Different Ways to Consider Biquaternions*, and it defines no form. The graded and Clifford reading of the product is *The Clifford Structure of the Biquaternion Algebra*; the behaviour of the product, the commutator and the symmetrized product on each of the six subspaces is tabulated in *Biquaternion Relations Between Subspaces*; the bracket as a Lie algebra is *Biquaternion Lie Algebra*; the operators $L_{\tilde{P}}$ and $R_{\tilde{P}}$ are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*; and the basis products written out one by one are *Worked Examples in the Biquaternion Algebra*.

Throughout, the product of two elements is written by juxtaposition, $\tilde{P}\tilde{Q}$, and $\tilde{P}=P_0+\mathbf{P}$ separates the complex scalar part $P_0$ from the complex vector part $\mathbf{P}=P_1e_1+P_2e_2+P_3e_3$.

## The Product

### Definition

The **biquaternion product** is the $\mathbb{C}$-bilinear extension of the quaternion product of the units:

$$
e_1e_2 = e_3, \qquad e_2e_3 = e_1, \qquad e_3e_1 = e_2, \qquad e_1^2 = e_2^2 = e_3^2 = -e_0,
$$

with central scalar imaginary $i$, $i^2=-1$. In developed form the product of $\tilde{P}=\sum_\mu P_\mu e_\mu$ and $\tilde{Q}=\sum_\nu Q_\nu e_\nu$ is

$$
\tilde{P}\tilde{Q} = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} P_\mu Q_\nu \, e_\mu e_\nu .
$$

The product is $\mathbb{C}$-bilinear, associative and unital, with unit $e_0$; it is not commutative. The unit relations above are those of *Biquaternion Algebra* and of the quaternion algebra, extended complex-linearly.

### The Scalar–Vector Form

Write $\tilde{P}=P_0+\mathbf{P}$ and $\tilde{Q}=Q_0+\mathbf{Q}$. Expanding the product by the graded pieces of the two factors, the scalar parts contribute scalars, the two mixed products contribute vectors, and the product of the two vector parts is again a sum of a scalar and a vector. The result is

$$
\tilde{P}\tilde{Q} = P_0Q_0 - (\mathbf{P},\mathbf{Q}) + P_0\mathbf{Q} + Q_0\mathbf{P} + \mathbf{P}\times\mathbf{Q} ,
$$

where

$$
(\mathbf{P},\mathbf{Q}) = \sum_{k=1}^{3} P_kQ_k , \qquad
\mathbf{P}\times\mathbf{Q} = (P_2Q_3-P_3Q_2)e_1 + (P_3Q_1-P_1Q_3)e_2 + (P_1Q_2-P_2Q_1)e_3 .
$$

The two pairings are the **complex bilinear dot product** and the **complex bilinear cross product**. They are $\mathbb{C}$-bilinear, and they reduce to the ordinary dot and cross products when the coefficients are real. The formula has the same shape as the quaternion product — a scalar part, a mixed vector part and a cross-product vector part — with the single difference that the coefficients are complex.

### Remark (the Other Products of the Literature)

The word *product* on $\mathbb{B}$ does not always mean the Hamilton product above. The *chiral algebra* of *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation* uses, alongside the Hamilton product, a **Pauli-type** product on the vector parts, $\mathbf{u}_1\cdot\mathbf{u}_2 + i\,\mathbf{u}_1\times\mathbf{u}_2$, whose dot term has the opposite sign to the dot term of this article and whose cross term is the ordinary cross product multiplied by the central $i$ (so a grade-one object where this article has a grade-two one); when that product is used, its conventions must be read from the article that introduces it, not from here. There is also a clash of names: the *outer product* $\odot$ of that chiral algebra is the full product, whereas the **outer product** $\tilde{P}\wedge\tilde{Q}$ of this article is only its antisymmetric part.

## The Symmetric Part

### Definition

The **symmetric part**, also called the **symmetrized product** or the **Jordan product**, of two biquaternions is

$$
\tilde{P}\circ\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the antisymmetric terms of the product cancel and the mixed terms double:

$$
\tilde{P}\circ\tilde{Q} = \bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr) + P_0\mathbf{Q} + Q_0\mathbf{P} .
$$

The symmetrized product is commutative and $\mathbb{C}$-bilinear, and it agrees with the ordinary square on the diagonal:

$$
\tilde{P}\circ\tilde{Q} = \tilde{Q}\circ\tilde{P} , \qquad \tilde{P}\circ\tilde{P} = \tilde{P}^2 .
$$

### It Is the Polarisation of the Square

**Proposition.** The symmetrized product is the polarisation of the square:

$$
\tilde{P}\circ\tilde{Q} = \tfrac{1}{2}\Bigl((\tilde{P}+\tilde{Q})^2 - \tilde{P}^2 - \tilde{Q}^2\Bigr).
$$

**Proof.** Expand $(\tilde{P}+\tilde{Q})^2=\tilde{P}^2+\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}+\tilde{Q}^2$ by bilinearity and divide by two.

The identity is the reason the symmetrized product, not the full product, is the product of the square: $\tilde{P}\circ\tilde{P}=\tilde{P}^2$, and the symmetric part of $\tilde{P}\tilde{Q}$ is exactly the term that a squaring process can see. Directly,

$$
\tilde{P}^2 = \bigl(P_0^2-(\mathbf{P},\mathbf{P})\bigr) + 2P_0\mathbf{P} ,
$$

which is a scalar plus a scalar multiple of $\mathbf{P}$ and contains no cross-product term. Every square-root problem $\xi^2=\tilde{Q}$ is therefore a problem in the symmetric part alone, and the outer product plays no part in *Biquaternion Square Roots of Minus One, Zero and Plus One* and *Biquaternion Square Roots of a General Element*.

### It Is a Jordan Product

**Theorem.** With the product $\circ$, the algebra $\mathbb{B}$ is a commutative Jordan algebra: $\circ$ is commutative and bilinear, and the Jordan identity

$$
(\tilde{P}\circ\tilde{Q})\circ\tilde{P}^2 = \tilde{P}\circ\bigl(\tilde{Q}\circ\tilde{P}^2\bigr)
$$

holds for all $\tilde{P},\tilde{Q}$.

**Proof.** The product of an associative algebra satisfies the Jordan identity for the symmetrized product, by the associativity of the underlying product; commutativity and bilinearity are built into the definition. The general theory is *Jordan Algebras*.

Two consequences follow. First, the Hermitian subspace $\mathbb{M}_+$ is closed under $\circ$: for $\tilde{P},\tilde{Q}\in\mathbb{M}_+$ the product $\tilde{P}\circ\tilde{Q}$ is again Hermitian, so $\mathbb{M}_+$ is a Jordan subalgebra of $\mathbb{B}$. Second, the scalar part of the symmetrized product is the scalar bilinear form read on the pair,

$$
\mathrm{Sc}(\tilde{P}\circ\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0-(\mathbf{P},\mathbf{Q}),
$$

since the commutator has no scalar part. It is the scalar bilinear form $B(\tilde{P},\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q})$ of *Association and the Transpose on the Biquaternion Algebra*, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$, the companion of the polarisation $N(\tilde{P},\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ of the norm.

## The Antisymmetric Part

### Definition

The **antisymmetric part** of the product, or **outer product**, is

$$
\tilde{P}\wedge\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the scalar parts cancel and the mixed terms too, leaving the cross product of the vector parts:

$$
\tilde{P}\wedge\tilde{Q} = \mathbf{P}\times\mathbf{Q} .
$$

The outer product is **alternating** and $\mathbb{C}$-bilinear, and it is skew:

$$
\tilde{P}\wedge\tilde{P} = 0 , \qquad \tilde{P}\wedge\tilde{Q} = -\,\tilde{Q}\wedge\tilde{P} .
$$

Its value is a pure vector: the scalar part of $\tilde{P}\wedge\tilde{Q}$ vanishes, for every pair of biquaternions, not only for vector-like ones. The commutator is twice the outer product,

$$
[\tilde{P},\tilde{Q}] := \tilde{P}\tilde{Q}-\tilde{Q}\tilde{P} = 2\,\mathbf{P}\times\mathbf{Q} = 2\,\tilde{P}\wedge\tilde{Q} .
$$

### The Commutativity Criterion

Because the right-hand side of the outer product depends on the vector parts alone, the vanishing of the commutator is a criterion:

$$
\tilde{P}\tilde{Q} = \tilde{Q}\tilde{P} \quad\Longleftrightarrow\quad \mathbf{P}\times\mathbf{Q} = 0 .
$$

The cross product of two complex vectors vanishes exactly when the vectors are **linearly dependent**, so two biquaternions commute if and only if their vector parts are parallel. In particular a central element $\tilde{P}=P_0e_0$ commutes with every biquaternion, since its vector part is zero; the converse holds, so this recovers the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ as the set of elements that commute with all of $\mathbb{B}$.

### It Is a Lie Bracket

The commutator $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ is bilinear, alternating and, by the associativity of the product, satisfies the Jacobi identity; it makes $\mathbb{B}$ a Lie algebra over $\mathbb{C}$. Its image is the kernel of the scalar part, $[\mathbb{B},\mathbb{B}]=\mathrm{Vect}(\mathbb{B})$, the six-dimensional vector subspace, which is therefore the derived subspace; and on pure vectors the bracket is twice the cross product, $[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\times\mathbf{Q}$. The trace functional, the trace-free part, the real form and the adjoint maps are *Biquaternion Lie Algebra*; here only the identity $[\tilde{P},\tilde{Q}]=2\tilde{P}\wedge\tilde{Q}$ with the outer product is recorded.

Under the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ the outer product is the Clifford outer product of the algebra, and it reads back on the vector parts as the cross product; the identity and the naming consequences are in *The Clifford Structure of the Biquaternion Algebra*.

### The Closure of the Two Sectors

The two halves of the product behave differently with respect to the Hermitian split, and the pattern is worth recording here because it is the origin of the Lie and Jordan structures of the algebra.

| $\tilde{P},\tilde{Q}$ | $\tilde{P}\wedge\tilde{Q}$ | $\tilde{P}\circ\tilde{Q}$ |
|---|---|---|
| $\mathbb{M}_+$ (Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |
| $\mathbb{M}_-$ (anti-Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |

That is, the antisymmetric part closes on the anti-Hermitian subspace and carries the Hermitian one into it, so $\mathbb{M}_-$ is a Lie subalgebra; the symmetric part closes on the Hermitian subspace, so $\mathbb{M}_+$ is a Jordan subalgebra. The full subspace-by-subspace table, with the centre, the vector subspace, the quaternion subspace and the anti-quaternion subspace, is *Biquaternion Relations Between Subspaces*.

## The Two Parts Together

### The Split Is by Symmetry, Not by Grade

The product is the sum of its two halves,

$$
\tilde{P}\tilde{Q} = \tilde{P}\circ\tilde{Q} + \tilde{P}\wedge\tilde{Q} ,
$$

and the two halves are read in coordinates as

| part | scalar part | vector part | symmetry |
|---|---|---|---|
| $\tilde{P}\circ\tilde{Q}$ | $P_0Q_0-(\mathbf{P},\mathbf{Q})$ | $P_0\mathbf{Q}+Q_0\mathbf{P}$ | symmetric, $\tilde{P}\circ\tilde{Q}=\tilde{Q}\circ\tilde{P}$ |
| $\tilde{P}\wedge\tilde{Q}$ | $0$ | $\mathbf{P}\times\mathbf{Q}$ | antisymmetric, $\tilde{P}\wedge\tilde{Q}=-\tilde{Q}\wedge\tilde{P}$ |

The antisymmetric part is pure vector and the symmetric part carries the scalar plus the mixed terms. This split is not the Clifford grade split: in the geometric reading the outer product mixes grades, since the complex vector $\mathbf{P}\times\mathbf{Q}$ carries both a grade-one and a grade-two real part. The grade dictionary is *The Clifford Structure of the Biquaternion Algebra*.

### The Operator Reading

The two halves are the balanced and the unbalanced one-sided multiplications. With $L_{\tilde{P}}(\tilde{Q})=\tilde{P}\tilde{Q}$ and $R_{\tilde{P}}(\tilde{Q})=\tilde{Q}\tilde{P}$ the left and right multiplications by $\tilde{P}$,

$$
\tilde{P}\circ\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}+R_{\tilde{P}}\bigr)(\tilde{Q}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}-R_{\tilde{P}}\bigr)(\tilde{Q}) .
$$

The antisymmetric combination $L_{\tilde{P}}-R_{\tilde{P}}$ is the inner derivation $\mathrm{ad}_{\tilde{P}}=L_{\tilde{P}}-R_{\tilde{P}}$ of the algebra, so the outer product is the derivation up to the factor $\tfrac12$, and the symmetric combination $L_{\tilde{P}}+R_{\tilde{P}}$ is twice the symmetrized multiplication by $\tilde{P}$. The operators themselves are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, and their spectra are *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*.

### Worked Example

Take $\tilde{P}=e_0+e_1$ and $\tilde{Q}=e_2$, so that $P_0=1$, $\mathbf{P}=e_1$, $Q_0=0$ and $\mathbf{Q}=e_2$. The dot product vanishes, $(\mathbf{P},\mathbf{Q})=0$, and the cross product is $\mathbf{P}\times\mathbf{Q}=e_1\times e_2=e_3$. Hence

$$
\tilde{P}\circ\tilde{Q} = (1\cdot 0-0)+1\cdot e_2+0\cdot e_1 = e_2 , \qquad \tilde{P}\wedge\tilde{Q} = e_3 , \qquad \tilde{P}\tilde{Q} = e_2+e_3 .
$$

Interchanging the factors changes the sign of the outer product and leaves the symmetric part unchanged,

$$
\tilde{Q}\tilde{P} = e_2-e_3 , \qquad \tilde{Q}\circ\tilde{P} = e_2 , \qquad \tilde{Q}\wedge\tilde{P} = -e_3 ,
$$

so $\tilde{P}\tilde{Q}\neq \tilde{Q}\tilde{P}$ while $\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P} = 2e_2 = 2(\tilde{P}\circ\tilde{Q})$, and the difference is $\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}=2e_3=2(\tilde{P}\wedge\tilde{Q})$, in agreement with the identities above.

## Summary

The biquaternion product is the complex-linear extension of the quaternion product; it is associative and unital, and not commutative. It always splits into a symmetric and an antisymmetric part,

$$
\tilde{P}\tilde{Q} = \tilde{P}\circ\tilde{Q} + \tilde{P}\wedge\tilde{Q} , \qquad \tilde{P}\circ\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}) .
$$

The **antisymmetric part** is the complex cross product of the vector parts, $\tilde{P}\wedge\tilde{Q}=\mathbf{P}\times\mathbf{Q}$; it is alternating, pure vector, and vanishes exactly when the vector parts are linearly dependent, which is the commutativity criterion. Twice the outer product is the commutator, $[\tilde{P},\tilde{Q}]=2\tilde{P}\wedge\tilde{Q}$; the commutator makes $\mathbb{B}$ a Lie algebra with derived subspace the vector subspace $\mathrm{Vect}(\mathbb{B})$, and under the Clifford identification the outer product is the Clifford outer product of the algebra.

The **symmetric part** is $\mathbb{C}$-bilinear and commutative, it agrees with the square on the diagonal, $\tilde{P}\circ\tilde{P}=\tilde{P}^2$, and it is the polarisation of the square, $\tilde{P}\circ\tilde{Q}=\tfrac{1}{2}((\tilde{P}+\tilde{Q})^2-\tilde{P}^2-\tilde{Q}^2)$. It makes $\mathbb{B}$ a Jordan algebra; its scalar part is the scalar bilinear form $\mathrm{Sc}(\tilde{P}\circ\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q})=P_0Q_0-(\mathbf{P},\mathbf{Q})$; it contains all the powers and hence all the square-root problems; and it closes on the Hermitian subspace, which is a Jordan subalgebra. The antisymmetric part closes on the anti-Hermitian subspace, which is a Lie subalgebra.

Read on the operators, the symmetric part is the balanced multiplication $\tfrac{1}{2}(L_{\tilde{P}}+R_{\tilde{P}})$ and the antisymmetric part the derivation $\tfrac{1}{2}(L_{\tilde{P}}-R_{\tilde{P}})=\tfrac{1}{2}\mathrm{ad}_{\tilde{P}}$. The split is by order symmetry, not by Clifford grade.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{P}\tilde{Q}$ | the biquaternion product |
| $\tilde{P}=P_0+\mathbf{P}$ | scalar part plus vector part |
| $(\mathbf{P},\mathbf{Q})$ | the complex bilinear dot product, $\sum_k P_kQ_k$ |
| $\mathbf{P}\times\mathbf{Q}$ | the complex bilinear cross product |
| $\tilde{P}\circ\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | the symmetric or symmetrized (Jordan) product |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | the antisymmetric part, or outer product |
| $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ | the commutator, $2\,\tilde{P}\wedge\tilde{Q}$ |
| $L_{\tilde{P}}$, $R_{\tilde{P}}$ | left and right multiplications by $\tilde{P}$ |
| $\mathrm{ad}_{\tilde{P}}$ | the inner derivation $L_{\tilde{P}}-R_{\tilde{P}}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the derived subspace $[\mathbb{B},\mathbb{B}]$ |
| $\mathrm{Sc}$ | the scalar part of an element |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product that is extended here.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the outer product as the antisymmetric part of a Clifford product.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the cross-product form of the outer product and the grade correspondence.
