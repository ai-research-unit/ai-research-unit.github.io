# __The Biquaternion Iterated Function Systems__

## Introduction

An iterated function system on a complete metric space is a finite family of contractions, and its attractor is the unique non-empty compact set invariant under the family. In the biquaternion algebra the linear part of an affine map can multiply on the left, on the right, or on both sides, because the algebra is not commutative, so the biquaternion iterated function systems form three nested families and the contraction condition is read from the operator norms of left and right multiplication rather than from the biquaternion norm. The subject is the constructive half of the category: where the quadratic dynamics is not contracting and its fractal is defined as a boundary, an iterated function system is contracting by hypothesis and its fractal is defined as an invariant set, and the two meet in the inverse branches of the square.

The algebra and the four general products are *Introduction to the General Plain Algebra of Biquaternions* and *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; the conjugations and their fixed subspaces are *The Group of Involutions*; the norm comparison is *The Matrix Representation and the Biquaternion Dynamics*; the zero divisors are *The Zero Divisors and the Singular Julia Sets*; the classical theory of the systems, the open set condition and the similarity dimension are *Fractal Geometry* of Part IV.

The article owns the three kinds of affine map, the contraction criterion, the attractor theorem, the similarity case with real quaternionic multipliers, the inverse-branch system of the quadratic map and the degeneracy of the square root at the cone. It does not re-derive the classical theory and does not treat the dimension of the quadratic fractal, which is *The Hausdorff Dimension of the Biquaternion Julia Sets*.

**Standing convention.** The metric is the Euclidean norm $\|\cdot\|_E$ on $\mathbb{B}\cong\mathbb{R}^8$, and $\|L_{\tilde A}\|$, $\|R_{\tilde A}\|$ are the operator norms of left and right multiplication by $\tilde A$. Maps are written $f_i(\tilde Q)=\tilde A_i\tilde Q+\tilde B_i$ unless the two-sided case is meant.

## The Three Kinds of Affine Map

**Definition.** An **affine map** of the algebra is a map of the form

$$
\tilde Q\longmapsto \tilde A\tilde Q+\tilde B \ (\text{left-affine}), \qquad \tilde Q\longmapsto\tilde Q\tilde A+\tilde B\ (\text{right-affine}), \qquad \tilde Q\longmapsto\tilde A\tilde Q\tilde C+\tilde B\ (\text{two-sided}).
$$

The three families are nested; a left-affine map is two-sided with $\tilde C=e_0$, and the two-sided form is the general shape of a map that is affine for the general plain bilinear product.

**Proposition (the two-sided forms span the linear maps).** Every $\mathbb{C}$-linear endomorphism $L$ of $\mathbb{B}$ is a finite sum of two-sided multipliers, $L=\sum_j\tilde A_j(\cdot)\tilde C_j$; the complex-linear maps form a space of complex dimension sixteen and the two-sided forms span it.

**Proof.** The assignment $\tilde A\otimes\tilde C\mapsto\bigl(\tilde Q\mapsto\tilde A\tilde Q\tilde C\bigr)$ extends to an algebra isomorphism $M_2(\mathbb{C})\otimes M_2(\mathbb{C})\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, because $\mathbb{B}\cong M_2(\mathbb{C})$ and $M_2(\mathbb{C})\otimes M_2(\mathbb{C})\cong\operatorname{End}_{\mathbb{C}}\bigl(M_2(\mathbb{C})\bigr)$ (*Modules over the General Plain Algebra of Biquaternions*); both spaces have complex dimension sixteen, so the span is all of them.

**Remark (only the left-affine family is an iterated function system in the classical sense here).** A right-affine map is the mirror of a left-affine one under the natural conjugation, and a two-sided map is a left-affine map composed with the right multiplication; the three families have the same contraction theory, and the article treats the left-affine case and records the differences.

## Contractions in the Euclidean Norm

**Proposition (the Lipschitz constant).** The map $f(\tilde Q)=\tilde A\tilde Q+\tilde B$ is Lipschitz with constant $\|L_{\tilde A}\|$, and $\|L_{\tilde A}\|\le\sqrt2\,\|\tilde A\|_E$. It is a contraction exactly when $\|L_{\tilde A}\|<1$.

**Proof.** $\|f(\tilde P)-f(\tilde Q)\|_E=\|\tilde A(\tilde P-\tilde Q)\|_E\le\|L_{\tilde A}\|\|\tilde P-\tilde Q\|_E$ by definition of the operator norm, and the estimate $\|L_{\tilde A}\|\le\sqrt2\|\tilde A\|_E$ is the norm comparison of *The Matrix Representation and the Biquaternion Dynamics*.

**Theorem (the similarity multipliers).** Let $\tilde A$ be a real quaternion of positive norm, $\tilde A\in\mathbb{H}_{\mathbb{B}}$, $N(\tilde A)=\rho^2$ with $\rho>0$. Then left multiplication by $\tilde A$ is a similarity of the eight-dimensional space with ratio $\rho$,

$$
\|\tilde A\tilde Q\|_E=\rho\,\|\tilde Q\|_E \quad \text{for every } \tilde Q ,
$$

so $f(\tilde Q)=\tilde A\tilde Q+\tilde B$ is a similarity with ratio $\rho$ and is a contraction exactly when $\rho<1$.

**Proof.** Write $\tilde A=\rho U$ with $U$ a real unit quaternion. Left multiplication by a unit real quaternion is a rotation of the four-dimensional real space $\mathbb{H}$, because it preserves the quaternion norm and the identity; writing $\tilde Q=\tilde P+i\tilde R$ with $\tilde P,\tilde R\in\mathbb{H}$, one has $\tilde A\tilde Q=\tilde A\tilde P+i\tilde A\tilde R$ and $\|\tilde A\tilde Q\|_E^2=\rho^2(\|\tilde P\|^2+\|\tilde R\|^2)=\rho^2\|\tilde Q\|_E^2$. The last clause is the Lipschitz criterion with the constant $\rho$.

**Remark (the central multipliers).** For a central multiplier $\tilde A=\lambda e_0$ the similarity ratio is $|\lambda|$, the smallest possible among the multipliers of a given biquaternion norm, because $\|\lambda e_0\|_E=|\lambda|$ and the operator norm is $|\lambda|$. **For a real quaternionic multiplier the ratio is the square root of the biquaternion norm; for a general multiplier the ratio lies between the two extremes and there is no formula in terms of $N$ alone**, because the algebra is not a division algebra.

**Remark (the zero divisors are not contractions of the algebra).** If $\tilde A$ is a zero divisor then left multiplication by $\tilde A$ is a singular operator, but its operator norm can still be less than one; the map is then a contraction with an image contained in a proper subspace. **A zero-divisor multiplier is a legitimate contraction whose image avoids a direction, and the attractor it produces is contained in the image subspace**; no invertibility of the multiplier is needed for the existence of the attractor.

## The Attractor and the Similarity Dimension

**Theorem (the attractor).** Let $f_1,\dots,f_m$ be contractions of $\mathbb{B}$ with constants $r_i<1$. There is a unique non-empty compact set $K\subset\mathbb{B}$ with

$$
K=\bigcup_{i=1}^m f_i(K),
$$

the **attractor** of the system, and for every non-empty compact $E$ the iterates of $E$ under the Hutchinson operator converge to $K$ in the Hausdorff metric.

**Proof.** The Hutchinson operator $E\mapsto\bigcup_if_i(E)$ is a contraction of the complete metric space of non-empty compact sets with the Hausdorff metric, with constant $\max_ir_i<1$, by the classical theorem (*Fractal Geometry*); the metric space is complete and the fixed point is the attractor.

**Theorem (the similarity dimension).** If in addition every $f_i$ is a similarity of ratio $r_i$ and the open set condition holds, then the Hausdorff dimension of the attractor is the unique $s$ with

$$
\sum_{i=1}^m r_i^s=1 ,
$$

and the Hausdorff measure in dimension $s$ of the attractor is positive and finite.

**Proof.** The classical theorem of Moran and Hutchinson (*Fractal Geometry*); by the similarity multipliers theorem the ratios are the numbers $\rho_i$ for real quaternionic multipliers and $|\lambda_i|$ for central ones.

**Corollary (the real quaternionic system).** For multipliers $\tilde A_i=\rho_iU_i$ with $U_i$ real unit quaternions, $\rho_i\in(0,1)$, and translations $\tilde B_i$, the system is a family of similarities of ratios $\rho_i$; if the open set condition holds the attractor has Hausdorff dimension $s$ with $\sum_i\rho_i^s=1$, irrespective of the units $U_i$ and the translations.

**Remark (the units rotate and do not change the dimension).** The units $U_i$ are the freedom of the system: the ratios fix the dimension, the units and the translations fix the geometry. **In the biquaternion algebra the units form the group of real unit quaternions, a three-dimensional rotation group, so the geometric freedom is exactly the rotational freedom of the classical three-dimensional systems times the choice of the translation.** This is the sense in which the biquaternion systems of similarities are the real three-dimensional systems with a complex phase.

## The Inverse Branches of the Quadratic Map

**Proposition (the square root and its branches).** For $\tilde W\in\mathbb{B}$ the equation $\tilde Q^2=\tilde W$ is solved by the square-root formula of the algebra: writing the root as $\tilde Q=Q_0e_0+\mathbf Q$, its scalar part is $P_0=\pm\sqrt{x}$ for the two solutions $x_\pm=\tfrac12(Q_0\pm\sqrt{n})$ of the reduced quadratic in $x=P_0^2$, and there are generically four roots, falling to two in the degenerate cases and to none for a non-zero nilpotent $\tilde W$ (*Biquaternion Square Roots of a General Element*). On the regular part of the square map the roots are therefore the values of finitely many local branches.

**Proof.** The count is the corollary on the number of roots of *Biquaternion Square Roots of a General Element*: four roots when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n\neq0$, two in the degenerate cases, and none for a rootless element, the example being a non-zero nilpotent of the algebra; the square map is the polynomial $M\mapsto M^2$ in the matrix model (*Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*).

**Remark (the Julia set as the attractor of the branches).** Off the critical set the inverse branches $f_j$ of $\tilde Q\mapsto\tilde Q^2$ — four local branches on the regular part — map small disks into small disks and, where the branches are contractions, generate an iterated function system whose attractor is the local piece of the Julia set; the inverse branch of the quadratic map is the classical *graph-directed* or *multi-valued* system. **The biquaternion Julia set is the attractor of the inverse branches on the regular part, and on the cone branches collapse and the system loses maps**, which is the constructive form of the obstruction of *The Zero Divisors and the Singular Julia Sets*.

**Remark (the cone as the collapse of the system).** When a branch reaches the critical set, preimages coincide and the system has fewer maps there; the Hausdorff dimension of the attractor then drops by the dimension of the collapsed branch, and no open set condition can be restored on the cone because the images are not separated.

## Symmetries of the Systems

**Proposition (the conjugations act on the systems).** Let $g$ be one of the conjugations ${}^{\natural},\bar{\cdot},{}^{*}$. If every generator and every translation of a system satisfies $g(\tilde A_i)=\tilde A_i$ and $g(\tilde B_i)=\tilde B_i$, then $g$ maps the attractor to itself. If $g$ maps the data of a system to the data of another system, then $g$ maps the attractor of the first to the attractor of the second.

**Proof.** $g$ is an isometry of the Euclidean norm and satisfies $g(\tilde P\tilde Q)=g(\tilde P)g(\tilde Q)$ for $\tilde A\tilde Q$ with $\tilde A$ fixed; applying $g$ to $K=\bigcup f_i(K)$ gives the first statement, and the second is the same computation with the images of the generators and translations.

**Remark (the symmetric systems).** A system with real quaternionic generators and translations is invariant under the quaternion conjugation, and a system with central real generators is invariant under the whole group $G$; **the symmetries of the attractor are read from the symmetries of the generator list, exactly as for the quadratic fractal, and the classification of the previous article applies.**

## Summary

The affine maps of the biquaternion algebra are of three kinds, left-affine, right-affine and two-sided, the last being the general shape and all three having the same contraction theory; the Lipschitz constant of a left-affine map is the operator norm of left multiplication, bounded by $\sqrt2$ times the Euclidean norm of the multiplier. For a real quaternionic multiplier of norm $\rho$ the map is a similarity of ratio $\rho$, for a central multiplier the ratio is the modulus, and a zero-divisor multiplier may still be a contraction with an image in a proper subspace. The attractor exists by Hutchinson's theorem, and in the similarity case with the open set condition its Hausdorff dimension solves $\sum r_i^s=1$; the units of the multipliers rotate the pieces without changing the dimension, so the geometry of a biquaternion similarity system is the geometry of a real three-dimensional system with a complex phase. The inverse branches of the quadratic map form the natural system on the regular part, whose attractor is the local Julia set and which loses branches at the zero-divisor cone; the symmetries of the systems are read from the symmetries of the generator list.

## Summary of Notation

| symbol | meaning |
|---|---|
| $f_i(\tilde Q)=\tilde A_i\tilde Q+\tilde B_i$ | a left-affine generator |
| $\|L_{\tilde A}\|$, $\|R_{\tilde A}\|$ | operator norms of left and right multiplication |
| $\rho_i$, $U_i$ | the norm and the unit of a real quaternionic multiplier |
| $K=\bigcup_if_i(K)$ | the attractor |
| $s$, $\sum r_i^s=1$ | the similarity dimension |
| $f_j$ | the inverse branches of the square |
| $g\in\{{}^{\natural},\bar{\cdot},{}^{*}\}$ | a conjugation acting on a system |

## Further Reading

- *Fractal Geometry* (`articles_maths/fractal-geometry.md`) and *Iterated Function Systems in the Complex Plane* (`articles_maths/iterated-function-systems-in-the-complex-plane.md`), for the attractor theorem, the open set condition and the similarity dimension used here.
- *The Matrix Representation and the Biquaternion Dynamics* (`articles_maths/the-matrix-representation-and-the-biquaternion-dynamics.md`), for the norm comparison that gives the Lipschitz bound.
- *Biquaternion Square Roots of a General Element* (`articles_maths/biquaternion-square-roots-of-a-general-element.md`), for the square root and its branches.
- *The Zero Divisors and the Singular Julia Sets* (`articles_maths/the-zero-divisors-and-the-singular-julia-sets.md`), for the cone on which the branches collapse.
- *The Hausdorff Dimension of the Biquaternion Julia Sets* (`articles_maths/the-hausdorff-dimension-of-the-biquaternion-julia-sets.md`), for the dimension of the quadratic fractal as against the systems.
