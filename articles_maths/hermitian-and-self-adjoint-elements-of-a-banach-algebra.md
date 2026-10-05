
# __Hermitian and Self-Adjoint Elements of a Banach Algebra__

## Introduction

The involution of a Banach algebra fixes a real linear subspace, the **self-adjoint** (or **Hermitian**) elements $a^* = a$, and the algebra is the complexification of that real space: every element is uniquely $a = h + ik$ with $h,k$ self-adjoint. The self-adjoint elements carry the order that the involution defines, the positive cone $P = \{b^*b\}$, and the order is the analytic substitute for the comparison of magnitudes; the elements with real spectrum are the self-adjoint ones when the involution is isometric, and the criterion for this is Vidav's: $a$ is self-adjoint exactly when $\lVert e^{ita}\rVert = 1$ for every real $t$. This article develops the Hermitian and self-adjoint elements of an involutive Banach algebra, their products and the Jordan and Lie structures they carry, the positive cone and its order, the characterisation by the exponential, and the way the involution controls the norm.

The article assumes the involutive Banach algebra, the $\mathrm{C}^*$-identity, the isometry of the involution and the contractivity of the $*$-homomorphisms from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the reality of the spectrum and the norm formula for a self-adjoint element from *The Spectrum of a Self-Adjoint Element*; the self-adjoint elements, the positive cone, the order, the square roots and the symmetrised product from *Self-Adjoint Elements and the Positive Cone* and *Involutive Bilinear Algebras*; the states and the positivity they detect from *States and Positive Functionals on an Involutive Algebra*; the Jordan and Lie structures from *Jordan Algebras* and *Lie Algebras*; and the spectrum and the functional calculus from *Topological Algebras and Banach Algebras* and *The Functional Calculus of a Self-Adjoint Element*.

Throughout, $A$ is a unital involutive Banach algebra over $\mathbb{C}$ with involution $a \mapsto a^*$; when a norm statement is made the involution is assumed **isometric**, $\lVert a^*\rVert = \lVert a\rVert$, which holds in every $\mathrm{C}^*$-algebra; $A^+ = \{a : a^* = a\}$ is the real subspace of **self-adjoint** (Hermitian) elements and $A^- = \{a : a^* = -a\}$ the **skew** elements; the **positive cone** is $P = \{b^*b : b \in A\}$, with $a \geq 0$ meaning $a \in P$; the **symmetrised product** and the **commutator** are $h\bullet k = \tfrac12(hk+kh)$ and $[h,k] = hk - kh$; and an element is **unitary** when $u^*u = uu^* = 1$, **normal** when $a^*a = aa^*$, and **positive** when $a \in P$.

## The Self-Adjoint Elements

**Proposition (the real form).** $A^+$ is a real linear subspace of $A$ closed under the involution, $A^-$ is the real subspace $iA^+$, and

$$
A = A^+ \oplus iA^+ , \qquad a = \tfrac12(a + a^*) + \tfrac i2(a - a^*) ,
$$

a direct sum of real vector spaces; the decomposition is unique and $A$ is the complexification of $A^+$.

**Proof.** The fixed set of the real-linear (conjugate-linear) involution is a real vector space; the displayed elements are self-adjoint, they sum to $a$, and a self-adjoint element in $iA^+$ is both self-adjoint and skew, hence zero, giving directness and uniqueness. $\square$

**Proposition (products, squares and commutators).** The product of two self-adjoint elements is self-adjoint exactly when they commute; $h^2$ is positive for every self-adjoint $h$; $A^+$ is closed under the symmetrised product $\bullet$, so it is a real **Jordan algebra**, and $A^-$ is closed under the commutator, so it is a real **Lie algebra**. The involution exchanges the two structures: $(h\bullet k)^* = h\bullet k$ and $[h,k]^* = -[h,k]$ for self-adjoint $h,k$.

**Proof.** $(hk)^* = k^*h^* = kh$, which equals $hk$ exactly when $h,k$ commute; $h^2 = h^*h \in P$; the symmetrised product of two self-adjoint elements is self-adjoint by the same computation with the two terms, and the commutator is skew; the Jordan and Lie identities are the associativity of the product read in the two symmetrisations. $\square$

## The Positive Cone and the Order

**Definition.** The **positive cone** is $P = \{b^*b : b \in A\}$, and the **order** is $a \leq b$ iff $b - a \in P$; an element is **positive** when it lies in $P$.

**Proposition (the cone is closed under sums, positive scalars and inner conjugation).** In a $\mathrm{C}^*$-algebra $P$ is a convex cone, $P + P \subseteq P$, $\lambda P \subseteq P$ for $\lambda \geq 0$, $c^*Pc \subseteq P$ for every $c$, and $P \cap (-P) = \{0\}$, so $\leq$ is a partial order. A positive element $a$ has a unique positive square root $a^{1/2}$, and the absolute value $|a| = (a^*a)^{1/2}$ gives the polar decomposition.

**Proof.** $b^*b + c^*c = (b^*\!:\!c^*)\binom{b}{c}$ is a sum of two squares, and every element of the form $x^*x + y^*y$ is $d^*d$ for $d$ a column with entries $x,y$ in the matrix algebra, which is the standard argument that $P+P \subseteq P$; $\lambda b^*b = (\sqrt\lambda\,b)^*(\sqrt\lambda\,b)$; $c^*(b^*b)c = (bc)^*(bc)$. Properness in a $\mathrm{C}^*$-algebra: if $a \in P\cap(-P)$ then $\sigma(a) \subseteq [0,\infty)\cap(-\infty,0] = \{0\}$ by *The Spectrum of a Self-Adjoint Element*, so $a$ is self-adjoint with spectrum $\{0\}$, hence $a = 0$ by the norm formula $\lVert a\rVert = r(a)$. The square root and the polar decomposition are *Self-Adjoint Elements and the Positive Cone*. $\square$

**Theorem (the states detect the order).** In a $\mathrm{C}^*$-algebra, $a \geq 0$ if and only if $f(a) \geq 0$ for every state $f$; hence $a \leq b$ if and only if $f(a) \leq f(b)$ for every state. The order is the same whether read from the cone or from the states.

**Proof.** A positive element evaluates non-negatively on a positive functional; conversely a self-adjoint element evaluated non-negatively on every state has non-negative spectrum, by the argument of *States and Positive Functionals on an Involutive Algebra*, hence is positive. $\square$

## The Hermitian Characterisation

**Theorem (Vidav's characterisation).** Let $A$ be a unital Banach algebra with an isometric involution. An element $a \in A$ is self-adjoint if and only if

$$
\lVert e^{ita}\rVert = 1 \qquad \text{for every } t \in \mathbb{R} .
$$

The self-adjoint elements are therefore exactly the elements all of whose exponentials are isometries, and $a \in A^+$ implies $\sigma(a) \subseteq \mathbb{R}$.

**Proof (sketch).** If $a = a^*$ then $e^{ita}$ is unitary in the C*-algebra generated by $a$, because $(e^{ita})^* = e^{-ita}$, so $\lVert e^{ita}\rVert = 1$ by the $\mathrm{C}^*$-identity. Conversely, if all the exponentials have norm one, the function $t \mapsto \lVert 1 + ita + o(t)\rVert$ controls the numerical range of $a$ and forces it to be real; the numerical range of a Hermitian element is real, and an element with real numerical range is Hermitian, which is Vidav's theorem. $\square$

**Corollary (the norm and the involution).** A unital Banach algebra with an isometric involution, all of whose elements have real numerical range in the Vidav sense, is a $\mathrm{C}^*$-algebra; hence the involution of a $\mathrm{C}^*$-algebra is determined up to the norm, and the $\mathrm{C}^*$-norm is unique.

**Proof.** This is Vidav's theorem: if the set of Hermitian elements complexifies to the whole algebra then the algebra is a $\mathrm{C}^*$-algebra, and the norm is the unique $\mathrm{C}^*$-norm by *Involutive Banach Algebras and the Gelfand–Naimark Theorem*. $\square$

## Examples

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ the self-adjoint elements are the Hermitian matrices, the positive cone is the set of positive semidefinite matrices, and the order is the Loewner order; the unitary elements are the unitary matrices, and $a = h + ik$ is the decomposition of a matrix into its Hermitian and skew-Hermitian parts.

**Example (the function algebra).** For $A = C(X,\mathbb{C})$ the self-adjoint elements are the real-valued continuous functions, $A^+ = C(X,\mathbb{R})$, the positive cone is the cone of non-negative functions, and the order is pointwise; the unitary elements are the functions of modulus one.

**Example (the non-C*-involutive algebra).** Let $A$ be the convolution algebra of a finite group with the involution $f^*(g) = \overline{f(g^{-1})}$. It is an involutive Banach algebra whose involution is isometric for the $\ell^1$-norm, but it is not a $\mathrm{C}^*$-algebra; its Hermitian elements are the class functions only after passing to the reduced $\mathrm{C}^*$-algebra, and the phenomenon shows that the Hermitian elements alone do not determine the topology.

## The Order and the Norm

**Theorem (the order is compatible with the norm).** In a $\mathrm{C}^*$-algebra: if $0 \leq a \leq b$ then $\lVert a\rVert \leq \lVert b\rVert$, so the norm is monotone on the positive cone; the positive cone is closed in the norm; the unit is an **order unit**, $a \leq \lVert a\rVert\cdot1$ for a self-adjoint $a$; and $0 \leq a \leq b$ implies $c^*ac \leq c^*bc$ for every $c$.

**Proof.** If $0 \leq a \leq b$ then $b \leq \lVert b\rVert\cdot1$ because $b$ is self-adjoint with $\lVert b\rVert = r(b)$, so $a \leq \lVert b\rVert\cdot1$ and $\sigma(a) \subseteq [0,\lVert b\rVert]$, giving $\lVert a\rVert = r(a) \leq \lVert b\rVert$; the closedness is the norm continuity of the product; the invariance of the cone is $c^*ac = (ac)^*(ac)$ combined with the order. $\square$

**Proposition (the failure of the lattice property).** The self-adjoint part $A^+$ is a real ordered Banach space with the order unit $1$, but it is a vector lattice exactly when $A$ is commutative; in $M_2(\mathbb{C})$ the projections onto the first coordinate axis and onto the diagonal have no greatest lower bound in $A^+$. The order is therefore an ordered structure, not a lattice.

**Proof.** The commutative case is the lattice $C(X,\mathbb{R})$; the failure is the standard witness in $M_2(\mathbb{C})$, where the two projections do not commute and their set of lower bounds has no greatest element. $\square$

## Summary

In an involutive Banach algebra the self-adjoint elements $A^+ = \{a : a^* = a\}$ form a real subspace whose complexification is the algebra, every element decomposes uniquely as $a = h + ik$ with $h,k$ self-adjoint, and $A^+$ is a Jordan algebra under the symmetrised product while the skew elements form a Lie algebra under the commutator. The positive cone $P = \{b^*b\}$ is a convex cone invariant under inner conjugation and under positive scalars, it is proper in a $\mathrm{C}^*$-algebra, so the associated order is a partial order, and the order is detected by the states: $a \geq 0$ iff every state evaluates non-negatively on $a$. With an isometric involution the self-adjoint elements are exactly those whose exponentials $e^{ita}$ are isometries for all real $t$, Vidav's characterisation, which has real spectrum; and Vidav's theorem recovers the $\mathrm{C}^*$-algebras as the algebras whose Hermitian elements complexify to the whole algebra, giving the uniqueness of the $\mathrm{C}^*$-norm. The spectrum of the self-adjoint elements is *The Spectrum of a Self-Adjoint Element*, and the calculus is *The Functional Calculus of a Self-Adjoint Element*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^+ = \{a : a^* = a\}$ | Self-adjoint (Hermitian) elements, a real subspace |
| $A^-$, $A = A^+\oplus iA^+$ | Skew elements and the decomposition |
| $h\bullet k$, $[h,k]$ | Symmetrised product (Jordan) and commutator (Lie) |
| $P = \{b^*b\}$ | The positive cone |
| $a \leq b$, $b - a \in P$ | The order |
| $a^{1/2}$, $\lvert a\rvert = (a^*a)^{1/2}$ | Square root and absolute value |
| $\lVert e^{ita}\rVert = 1$ | Vidav's characterisation of self-adjointness |
| Unitary, normal | $u^*u = uu^* = 1$; $a^*a = aa^*$ |
| $0 \leq a \leq b \Rightarrow \lVert a\rVert \leq \lVert b\rVert$ | Monotone norm; order unit $1$ |

## Further Reading

- Ivan Vidav, "Eine metrische Kennzeichnung der selbstadjungierten Operatoren", *Mathematische Zeitschrift* 66 (1956), for the characterisation of the Hermitian elements and the exponential criterion.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the Hermitian elements, the numerical range and the uniqueness of the $\mathrm{C}^*$-norm.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the Hermitian and self-adjoint elements of a general involutive Banach algebra.
- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the positive cone, the square roots and the polar decomposition.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the self-adjoint operators and the order they carry.
