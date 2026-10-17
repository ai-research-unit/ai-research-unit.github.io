# __The Hermitian Form and the Cone of the Split-Complexoid Algebra__

## Introduction

The sesquilinear product of the split-complex space is the form $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$ on its regular module. The present article reads that form as a **form**: its two slots, its conjugate symmetry, its Gram matrix and its signature; its **positivity**, which is indefinite, and the **cone** that replaces the positive-definite cone of the complex case; the **modules** over the ring, which decompose as pairs of real spaces through the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$, with the classification of the Hermitian forms over them.

The results are the two-dimensional end of the family and they are sharper than in the four-dimensional case. The form $\langle\cdot,\cdot\rangle_{*}$ is conjugate-symmetric, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second, and its realified scalar part is the indefinite form $g(Q_1,Q_2) = q_1q_2-q'_1q'_2$ of signature $(1,1)$. The form is **indefinite**: $\langle 1,1\rangle_{*} = 1$ and $\langle j,j\rangle_{*} = -1$. It therefore defines no positive cone through its Hermitian square, since $Q\bar Q = \langle Q\rangle_{\natural} = q^2-q'^2$ already takes every real value; the cone that survives is the **cone of squares** of the plain product, $\mathcal{C} = \{q_+\ge0, q_-\ge0\} = \{q\ge\lvert q'\rvert\}$, the order cone, closed, convex, pointed, generating and self-dual for $g$, whose boundary meets the null cone in the two positive rays. On $\mathcal{C}$ the reversed Cauchy–Schwarz inequality holds. The Hermitian forms on the modules are classified by a real matrix, hence up to isometry by its rank; every nondegenerate form is isometric to the standard one and is **hyperbolic**, the two idempotent halves supplying a Lagrangian, so the Witt group of the ring is trivial.

**Placement.** The article is the second entry of the split-complex general-plain-sesqualgebra block, after *The Sesquilinear Product of the Split-Complexoid Space*, and it closes the sesquilinear side; the slot reading of the two products and the two pairings with their adjoints are *Relations and Comparison Between the Two Products of the Split-Complexoid Space*, above this article in this category. The product itself, its associator, its one-sided multiplications, its sandwich, its adjoints and its commutator are the first article of the block. The scalar form $g$ and the norm are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space* and *Split-Complex Norm and Invertibility*; the cone of squares, its order and the classes of element are *The Classes of Element of the Split-Complex Algebra*; the null cone and the zero divisors are *Split-Complex Zero Divisors*; and the subspaces with their forms are *Remarkable Subspaces of the Split-Complexoid and the Two Forms*.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$, general element $Q = q+jq'$, conjugate $\bar Q = q-jq'$, idempotents $\Pi_1 = \tfrac12(1+j)$ and $\Pi_2 = \tfrac12(1-j)$, idempotent coordinates $q_+ = q+q'$ and $q_- = q-q'$, real part $\operatorname{Sc}Q = q$. The form is written $\langle\cdot,\cdot\rangle_{*}$ and is the general plain sesquilinear form of the space; the associated symmetric bilinear form is $g$; the conjugation of the coefficient ring is trivial, since the coefficients are real, so only the bar has a sense. A **module** is a left $\mathbb{D}$-module, and the regular module is $\mathbb{D}$ itself.

## The Canonical Hermitian Form

### Definition

**Definition.** The **canonical Hermitian form** of the regular module is

$$
H : \mathbb{D} \times \mathbb{D} \longrightarrow \mathbb{D}, \qquad
\langle Q_1,Q_2\rangle_{*} = Q_1 \star Q_2 = Q_1\bar Q_2 = (q_1q_2-q'_1q'_2) + (q'_1q_2-q_1q'_2)j .
$$

It is the general plain sesquilinear form of the split-complex space, the sesquilinear product of *The Sesquilinear Product of the Split-Complexoid Space* read as a form.

### Conjugate Symmetry and the Two Slots

**Proposition.** The form is additive in each slot; it is $\mathbb{D}$-linear in the first and $\bar\cdot$-semilinear in the second,

$$
\langle \lambda Q_1, Q_2\rangle_{*} = \lambda\,\langle Q_1,Q_2\rangle_{*}, \qquad \langle Q_1,\lambda Q_2\rangle_{*} = \bar\lambda\,\langle Q_1,Q_2\rangle_{*}, \qquad \lambda \in \mathbb{D},
$$

and it is **conjugate-symmetric**,

$$
\langle Q_2,Q_1\rangle_{*} = \overline{\langle Q_1,Q_2\rangle_{*}} .
$$

**Proof.** The two scalar rules are those of the product, already proved in *The Sesquilinear Product of the Split-Complexoid Space*. For the symmetry, $\langle Q_2,Q_1\rangle_{*} = Q_2\bar Q_1$ and $\overline{\langle Q_1,Q_2\rangle_{*}} = \overline{Q_1\bar Q_2} = \bar Q_1 Q_2$, which is equal to $Q_2\bar Q_1$ by commutativity.

The form is thus Hermitian with respect to the conjugation, in the sense of the ring with involution $(\mathbb{D},\bar\cdot)$. It is not symmetric and not bilinear, and it is not $\mathbb{D}$-bilinear: the second slot is twisted. The scalar product $Q\bar Q = \langle Q\rangle_{\natural}$ of an element with itself is real, as conjugate symmetry forces, and it is the norm.

### The Gram Matrix and the Signature

**Proposition.** In the basis $\{1,j\}$ the Gram matrix of $\langle\cdot\rangle_{*}$ is

$$
G = \begin{pmatrix} \langle 1,1\rangle_{*} & \langle 1,j\rangle_{*} \\ \langle j,1\rangle_{*} & \langle j,j\rangle_{*} \end{pmatrix}
= \begin{pmatrix} 1 & -j \\ j & -1 \end{pmatrix},
$$

conjugate-symmetric, with $G_{ij} = \overline{G_{ji}}$. The realified scalar part has the diagonal Gram matrix

$$
\operatorname{Sc} H = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

of signature $(1,1)$, and the associated symmetric bilinear form is

$$
g(Q_1,Q_2) = \operatorname{Sc} \langle Q_1,Q_2\rangle_{*} = q_1q_2-q'_1q'_2 .
$$

**Proof.** $\langle 1,1\rangle_{*} = 1$, $\langle 1,j\rangle_{*} = \bar j = -j$, $\langle j,1\rangle_{*} = j$ and $\langle j,j\rangle_{*} = j\bar j = -j^2 = -1$; the conjugate symmetry of the matrix is the proposition above read coefficientwise. The scalar part of $Q_1\bar Q_2 = (q_1q_2-q'_1q'_2)+(q'_1q_2-q_1q'_2)j$ is $q_1q_2-q'_1q'_2$, whose matrix in the basis $\{1,j\}$ is diagonal with entries $1$ and $-1$.

So the form has **signature $(1,1)$**: one positive and one negative direction over the reals, the positive direction being the real line and the negative one the split imaginary line. The two directions are orthogonal, since $g(1,j) = 0$. The $\mathbb{D}$-valued Gram matrix $G$ is not the right carrier of the nondegeneracy, since its determinant vanishes, $\det G = -1+j^2 = 0$; the nondegeneracy is read on the real matrix of the next section. The form $g$ is the polarisation of the norm, $\langle Q\rangle_{\natural} = g(Q,Q) = Q\bar Q$, and this article's form theory is the case $n = 1$ of the modules of the section below. The full description of the two forms and the two norms and their signatures is *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*. The sign of the square is what decides the definiteness: the complex structure has $J^2=-\mathrm{id}$ and its canonical Hermitian form is definite, while the split structure has $J^2=+\mathrm{id}$ and its canonical Hermitian form is indefinite, of signature $(1,1)$.

## Positivity and the Cone

### Indefiniteness

**Theorem.** The form $\langle\cdot,\cdot\rangle_{*}$ is **indefinite**: it is neither positive semidefinite nor negative semidefinite, and it has isotropic vectors other than $0$.

**Proof.** $\langle 1,1\rangle_{*} = 1 > 0$ and $\langle j,j\rangle_{*} = -1 < 0$, so the scalar part takes both signs; that already excludes both semidefiniteness. The isotropic set is non-zero since $\langle 1+j,1+j\rangle_{*} = \langle 1+j\rangle_{\natural} = 0$.

The indefinite form is the two-dimensional member of the family in which no definite form exists. For the complex field the canonical form $A\bar C$ is already positive definite, and every nonzero element has positive square length; on $\mathbb{D}$ the two sign directions are present in every basis pair $\{1,j\}$, and the isotropic set is a pair of lines rather than the origin alone.

### The Hermitian Square Gives No Cone

**Proposition.** The Hermitian square of the form, the map $Q \mapsto Q\bar Q = \langle Q\rangle_{\natural}$, has image all of $\mathbb{R}_{\mathbb{D}}$:

$$
\{Q\bar Q : Q \in \mathbb{D}\} = \mathbb{R}.
$$

**Proof.** $Q\bar Q = q^2-q'^2$ is real for every $Q$, and it is an arbitrary real number: for a given $t\in\mathbb{R}$ the element

$$
Q = \frac{t+1}{2} + j\,\frac{1-t}{2}
$$

satisfies $Q\bar Q = \frac{(t+1)^2-(1-t)^2}{4} = t$. So the image is all of $\mathbb{R}$.

So the sesquilinear side of the ring produces **no positive cone**. The positive cone of a Hermitian form is the image of the form on the diagonal, and here that image is the whole real line rather than a half-line or a cone; the reason is indefiniteness, and it is the sharpest contrast with the complex case, where the image of $A\bar A$ is the ray $\mathbb{R}_{\ge0}$. On $\mathbb{D}$ the indefinite form has no positive cone at all, and the cone of the ring is carried by the *plain* product instead.

### The Cone of Squares

**Definition.** The **cone of squares** of $\mathbb{D}$ is the image of the squaring map of the plain product,

$$
\mathcal{C} = \{Q^2 : Q \in \mathbb{D}\} = \{Q : q_+ \ge 0,\; q_- \ge 0\} = \{Q = q+jq' : q \ge \lvert q'\rvert\},
$$

the set on which both idempotent coordinates are non-negative.

**Theorem.** The cone $\mathcal{C}$ is a **symmetric cone**: it is closed, convex, salient (pointed), generating, and self-dual with respect to the scalar form $g$,

$$
\mathcal{C}^{*} = \{Q_2 : g(Q_1,Q_2) \ge 0 \ \text{for all } Q_1 \in \mathcal{C}\} = \mathcal{C}.
$$

**Proof.** The identification of the image with the coordinate description is the criterion of square roots of *The Classes of Element of the Split-Complex Algebra*. Closure and convexity: the idempotent coordinates of a non-negative combination of elements of $\mathcal{C}$ are non-negative. Salience: if $Q_1$ and $-Q_1$ both lie in $\mathcal{C}$ then $q_{1+} \ge 0$, $q_{1-} \ge 0$ and $-q_{1+} \ge 0$, $-q_{1-} \ge 0$, so $Q_1 = 0$. Generating: $Q_1 = q_{1+}\Pi_1 + q_{1-}\Pi_2$ is the difference of the two elements $\max(q_{1+},0)\Pi_1 + \max(q_{1-},0)\Pi_2$ and $\max(-q_{1+},0)\Pi_1+\max(-q_{1-},0)\Pi_2$ of $\mathcal{C}$, so $\mathcal{C}-\mathcal{C} = \mathbb{D}$. Self-duality: in idempotent coordinates $g(Q_1,Q_2) = \tfrac12(q_{1+}q_{2-} + q_{1-}q_{2+})$, so $g(\Pi_1,Q_2) = \tfrac12 q_{2-}$ and $g(\Pi_2,Q_2) = \tfrac12 q_{2+}$; if $Q_2 \notin \mathcal{C}$ then one of $q_{2+}, q_{2-}$ is negative, and taking $Q_1 = \Pi_2$ (if $q_{2+} < 0$) or $Q_1 = \Pi_1$ (if $q_{2-} < 0$) gives $g(Q_1,Q_2) < 0$ with $Q_1 \in \mathcal{C}$, so $Q_2 \notin \mathcal{C}^{*}$; conversely $q_{1+},q_{1-},q_{2+},q_{2-} \ge 0$ give $g(Q_1,Q_2)\ge0$, so $\mathcal{C}\subset\mathcal{C}^{*}$. Hence $\mathcal{C}^{*} = \mathcal{C}$.

The coordinates $q_+$ and $q_-$ diagonalise the cone and the form together, which is why the computations are one-dimensional. The cone of squares of the plain product is the order cone on $\mathbb{D}$: it defines the partial order $Q_1 \preceq Q_2 \iff Q_2-Q_1 \in \mathcal{C}$, and the squares are its non-negative elements, $Q^2 \in \mathcal{C}$ for every $Q$. No element acts as the order unit or the identity of the order beyond $1$, which is interior to the cone since $1_+ = 1_- = 1 > 0$.

### The Relation to the Null Cone and the Zero Divisors

**Theorem.** The isotropic cone of $\langle\cdot,\cdot\rangle_{*}$ is the null cone, and it is the union of the two boundaries of the double cone of non-negativity:

$$
\{Q : \langle Q,Q\rangle_{*} = 0\} = \mathcal{N} = \partial\mathcal{C} \cup \partial(-\mathcal{C}) = \mathbb{R}\Pi_1 \cup \mathbb{R}\Pi_2,
$$

where $\partial\mathcal{C} = \mathbb{R}_{\ge0}\Pi_1\cup\mathbb{R}_{\ge0}\Pi_2$. The zero divisors are $\mathcal{N}\setminus\{0\}$.

**Proof.** $\langle Q,Q\rangle_{*} = Q\bar Q = \langle Q\rangle_{\natural} = q^2-q'^2$, which vanishes iff $(q-q')(q+q') = 0$, i.e. $Q \in \mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$; the identification of the null cone with the zero divisors is *Split-Complex Zero Divisors*. The half-line description is read from the signs of $q_+$ and $q_-$.

So the isotropic set of $\langle\cdot,\cdot\rangle_{*}$ is the null cone, a cross of two lines of real dimension $1$, and the zero divisors are its nonzero points. The cone $\mathcal{C}$ meets it in the two non-negative rays, which are the boundary of the order cone, and the points of the null cone are exactly the elements across which the sign of $\langle\cdot,\cdot\rangle_{\natural}$ changes. The form $\langle\cdot,\cdot\rangle_{*}$ is indefinite, the real line being its positive direction and the split imaginary line its negative one; the norm $\langle\cdot\rangle_{\natural}$, its sign and the distribution of the invertible elements are *Split-Complex Norm and Invertibility*.

### The Reversed Cauchy–Schwarz Inequality

**Theorem (reversed Cauchy–Schwarz).** For $Q_1, Q_2$ in the closed cone $\mathcal{C}$, with $g$ the scalar form,

$$
g(Q_1,Q_2)^2 \;\ge\; g(Q_1,Q_1)\,g(Q_2,Q_2),
$$

with equality if and only if $Q_1$ and $Q_2$ are proportional. On the interior of the cone all three quantities are positive, and the inequality is the reverse of the definite one.

**Proof.** In idempotent coordinates $g(Q_1,Q_2) = \tfrac12(q_{1+}q_{2-} + q_{1-}q_{2+})$ and $g(Q_1,Q_1) = q_{1+}q_{1-} = \langle Q_1\rangle_{\natural}$ and $g(Q_2,Q_2) = q_{2+}q_{2-}$, so

$$
g(Q_1,Q_2)^2 - g(Q_1,Q_1)\,g(Q_2,Q_2)
= \tfrac14\big((q_{1+}q_{2-} + q_{1-}q_{2+})^2 - 4\,q_{1+}q_{1-}\,q_{2+}q_{2-}\big)
= \tfrac14\,(q_{1+}q_{2-} - q_{1-}q_{2+})^2 \;\ge\; 0 .
$$

The middle expression is the arithmetic–geometric mean difference of the two non-negative numbers $\alpha = q_{1+}q_{2-}$ and $\beta = q_{1-}q_{2+}$. Equality holds exactly when $\alpha = \beta$, that is when $q_{1+}q_{2-} = q_{1-}q_{2+}$, which says that the pairs $(q_{1+},q_{1-})$ and $(q_{2+},q_{2-})$ are proportional and hence that $Q_1$ and $Q_2$ are proportional.

**Remark.** The inequality is the reverse of the Cauchy–Schwarz inequality of a definite form, and it holds on the cone because both idempotent coordinates are non-negative there, so the two products $\alpha$ and $\beta$ have the same sign. The reversed direction is the form-level statement of the indefiniteness: on a definite form the inequality points the other way, and its reversal is exactly the arrival of the isotropic cone, here the pair of lines $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$.

## The Modules over the Ring

### The Decomposition of a Module

**Theorem.** Every left $\mathbb{D}$-module $M$ decomposes as a pair of real vector spaces,

$$
M = M_+ \oplus M_-, \qquad M_+ = \Pi_1 M, \quad M_- = \Pi_2 M,
$$

on which $\mathbb{D}$ acts through the two characters $Q \mapsto q_+$ and $Q \mapsto q_-$; and the free module of rank $n$ is $\mathbb{D}^n = \mathbb{R}^n \oplus \mathbb{R}^n$.

**Proof.** The idempotents $\Pi_1,\Pi_2$ are central, orthogonal and complete, so $M = \Pi_1 M\oplus\Pi_2 M$; on $\Pi_1 M$ the element $Q = q_+\Pi_1+q_-\Pi_2$ acts as the real scalar $q_+$ and on $\Pi_2 M$ as $q_-$; the assignment is the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ read on the module, and it is additive because the two idempotents commute with every scalar.

So the module category of $\mathbb{D}$ is the product of two copies of the category of real vector spaces: every module is the pair $(M_+,M_-)$ of the two eigenspaces of the idempotents, every module is projective, and a finitely generated module is free of rank $n$ exactly when $\dim M_+ = \dim M_- = n$.

### The Classification of the Hermitian Forms

**Theorem.** A Hermitian form $\langle\cdot,\cdot\rangle_{*}$ on the free module $\mathbb{D}^n$ is determined by one real $n\times n$ matrix $P$: on the vectors $X = X_+\Pi_1 + X_-\Pi_2$ and $Y = Y_+\Pi_1+Y_-\Pi_2$, with $X_+,X_-,Y_+,Y_-\in\mathbb{R}^n$,

$$
{\langle X,Y\rangle_{*}}_+ = X_+^{\mathrm T} P\,Y_-, \qquad {\langle X,Y\rangle_{*}}_- = X_-^{\mathrm T} P^{\mathrm T} Y_+ .
$$

Two such forms are isometric if and only if their matrices have the same rank; the invertible change of basis $(X_+,X_-)\mapsto(U_+X_+,U_-X_-)$ acts by $P \mapsto U_+^{\mathrm T} P U_-$, and the normal form is $\operatorname{diag}(I_r,0)$. In particular, a nondegenerate Hermitian form on $\mathbb{D}^n$ is one with $P$ invertible, and all of them are isometric to the standard form with $P = I$;

$$
{\langle X,Y\rangle_{*}}_+ = X_+^{\mathrm T}Y_-, \qquad {\langle X,Y\rangle_{*}}_- = X_-^{\mathrm T}Y_+ .
$$

**Proof.** Write the Gram coefficients $G_{ij} = P_{ij}\Pi_1 + P_{ji}\Pi_2$ with real $P_{ij}$; then the conjugate symmetry $G_{ij} = \overline{G_{ji}}$ holds automatically, and the display is the coefficientwise computation of $\langle X,Y\rangle_{*} = \sum_{ij}G_{ij}X_i\bar Y_j$ using $X_i\bar Y_j = X_{i,+}Y_{j,-}\Pi_1 + X_{i,-}Y_{j,+}\Pi_2$. A $\mathbb{D}$-linear automorphism is a pair $(U_+,U_-)$ of invertible real matrices, and it preserves $\langle\cdot,\cdot\rangle_{*}$ exactly when $U_+^{\mathrm T}PU_- = P$. Since left and right multiplication by invertible matrices reduces any $P$ to $\operatorname{diag}(I_r,0)$ with $r = \operatorname{rank}P$, the isometry class is the rank. Nondegeneracy is $P$ invertible, by the same display.

So the classification is by a single integer, the rank. The $\mathbb{D}$-valued Gram matrix of the regular module is the case $n = 1$, $P = 1$; the canonical form of the first section is the standard nondegenerate form of rank one.

### The Hyperbolic Witt Group

**Theorem.** Every nondegenerate Hermitian form over $(\mathbb{D},\bar\cdot)$ is **hyperbolic**: it has a Lagrangian, a submodule of half the $\mathbb{R}$-dimension equal to its own orthogonal complement. Consequently the Witt group of the Hermitian forms over $(\mathbb{D},\bar\cdot)$, the **hyperbolic Witt group** of the ring, is trivial.

**Proof.** It suffices to show the standard form of the second theorem hyperbolic, since every nondegenerate form is isometric to it. On $\mathbb{D}^n$ with the two components $\langle X,Y\rangle_{*+}$ and $\langle X,Y\rangle_{*-}$ as displayed, take

$$
L = \mathbb{R}^n\Pi_1 = \{(X_+,0)\} ;
$$

then $\langle\cdot,\cdot\rangle_{*}$ vanishes identically on $L$, since ${\langle X,Y\rangle_{*}}_+ = X_+^{\mathrm T}\cdot 0 = 0$ and ${\langle X,Y\rangle_{*}}_- = 0^{\mathrm T}\cdot Y_+ = 0$ for $X,Y\in L$, and the orthogonal complement is $L$ itself, since $\langle X,Y\rangle_{*} = 0$ for all $X\in L$ forces $Y_- = 0$. The submodule $L$ has real dimension $n$, half the real dimension $2n$ of $\mathbb{D}^n$, so it is a Lagrangian. A form with a Lagrangian is metabolic, hence represents the zero class in the Witt group, and every nondegenerate form does so.

So the Witt group of the sesquilinear forms over the split-complex ring is the **trivial group** $\{0\}$. This is the algebraic expression of the indefiniteness: a definite form is never metabolic, so a Witt group generated by a definite form is infinite cyclic as over the reals, while the split-complex ring has no definite form and its only nondegenerate class is the hyperbolic one, which is zero. The same two idempotent halves that make every form hyperbolic make every module self-dual and cancel the Witt group.

## Summary

The canonical Hermitian form of the split-complex regular module is $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second, conjugate-symmetric. Its Gram matrix in the basis $\{1,j\}$ is $\left(\begin{smallmatrix}1&-j\\j&-1\end{smallmatrix}\right)$, whose scalar part is diagonal of signature $(1,1)$; the associated symmetric bilinear form is $g(Q_1,Q_2) = q_1q_2-q'_1q'_2$, the polarisation of the norm.

The form is **indefinite**, and its diagonal image $Q\bar Q = \langle Q\rangle_{\natural} = q^2-q'^2$ is all of $\mathbb{R}$, so the sesquilinear side supplies no positive cone: this is the sharp contrast with the complex ray. The cone of the ring is the **cone of squares** of the plain product, $\mathcal{C} = \{q_+\ge0, q_-\ge0\} = \{q\ge\lvert q'\rvert\}$, a symmetric cone — closed, convex, salient, generating and self-dual for $g$ — carrying the order of $\mathbb{D}$; its boundary is the two positive rays of the null cone, and the isotropic cone of $\langle\cdot,\cdot\rangle_{*}$ is that null cone, the zero divisors with the origin. On $\mathcal{C}$ the reversed Cauchy–Schwarz inequality $g(Q_1,Q_2)^2 \ge g(Q_1,Q_1)g(Q_2,Q_2)$ holds, with equality exactly for proportional pairs.

The modules over the ring decompose as pairs of real vector spaces through $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$; the Hermitian forms on $\mathbb{D}^n$ are determined by a real matrix $P$, classified up to isometry by its rank, with a unique nondegenerate form in each rank, isometric to the standard one. Every nondegenerate form is hyperbolic — the two idempotent halves supply the Lagrangian $\mathbb{R}^n\Pi_1$ — so the hyperbolic Witt group of the ring is trivial, against the nontrivial group of the complex case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ | Split-complex algebra |
| $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$ | Canonical Hermitian form on the regular module |
| $\langle Q_2,Q_1\rangle_{*} = \overline{\langle Q_1,Q_2\rangle_{*}}$ | Conjugate symmetry |
| $g(Q_1,Q_2) = \operatorname{Sc}\langle Q_1,Q_2\rangle_{*} = q_1q_2-q'_1q'_2$ | Scalar form, polarisation of the norm |
| $\left(\begin{smallmatrix}1&-j\\j&-1\end{smallmatrix}\right)$ | Gram matrix of $\langle\cdot\rangle_{*}$; scalar part of signature $(1,1)$ |
| $\mathcal{N} = \{Q : \langle Q\rangle_{\natural} = 0\}$ | Isotropic cone of $\langle\cdot,\cdot\rangle_{*}$, the null cone |
| $\langle Q\rangle_{\natural} = Q\bar Q = q^2-q'^2$ | Hermitian square; its image is all of $\mathbb{R}$ |
| $\mathcal{C} = \{q_+\ge0, q_-\ge0\} = \{q\ge\lvert q'\rvert\}$ | Cone of squares, the order cone, a symmetric cone |
| $\mathcal{C}^{*} = \mathcal{C}$ | Self-duality with respect to $g$ |
| $g(Q_1,Q_2)^2 \ge g(Q_1,Q_1)g(Q_2,Q_2)$ on $\mathcal{C}$ | Reversed Cauchy–Schwarz inequality |
| $\mathbb{D}^n = \mathbb{R}^n\oplus\mathbb{R}^n$ | Decomposition of a free module |
| ${\langle X,Y\rangle_{*}}_+ = X_+^{\mathrm T}P\,Y_-$, ${\langle X,Y\rangle_{*}}_- = X_-^{\mathrm T}P^{\mathrm T}Y_+$ | Hermitian form of matrix $P$; isometry by rank $P$ |
| $\mathbb{R}^n\Pi_1$ | Lagrangian of the standard form; hyperbolic forms |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Grundlehren der mathematischen Wissenschaften 294, 1991), for Hermitian forms over a ring with involution, their classification and their Witt group.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, Grundlehren der mathematischen Wissenschaften 270, 1985), for signatures, isotropic cones and the Witt group of a form.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Cauchy–Schwarz and reversed Cauchy–Schwarz inequalities and the geometry of indefinite forms.
- John B. Conway, *A Course in Functional Analysis* (Springer, Graduate Texts in Mathematics 96, 2nd ed. 1990), for indefinite inner product spaces, their isotropic cones and their cones of positivity.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for modules over a product of fields, their decompositions and their endomorphism rings.
