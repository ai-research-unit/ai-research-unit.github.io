# __The K-Regular Sector__

## Introduction

This is the non-zero half of the Krein partition of the biquaternion algebra: the set on which the Krein norm does not vanish. It is the complement of the null set,

$$
\mathbb{B}^{\natural*}=\mathbb{B}\setminus\mathcal K
=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}\neq0\},
$$

and it splits into the positive region and the negative region. Its partner is *The K-Degenerate Sector*, for $\mathcal K$. The two articles carry the partition of *K-Regularity and Degeneracy in the Biquaternion Algebra*; the spectral condition is not used as a subdivision, and §*Why There Is No Spectral Split* of that article gives the four reasons.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$, and the coefficient signs are $\varepsilon=(1,-1,-1,-1)$. The forms are

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}},\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$

so that $\langle\tilde Q\rangle_{\natural*}=|Q_t|^2-\lVert\vec Q\rVert_E^2$ is the **Krein norm** and $\lVert\tilde Q\rVert_E^2=\langle\tilde Q\rangle_{*}$ is the Euclidean norm. The **algebraic norm** is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$; it is complex-valued and multiplicative, and it decides invertibility. The null set is $\mathcal K=\{\langle\tilde Q\rangle_{\natural*}=0\}$; the algebraic null cone is $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$, and its punctured part is the zero-divisor set $\mathcal Z$. The product is the plain product, with unit $e_t$.

## Definition and Characterisation

**Definition.** The **Krein-regular sector** is

$$
\mathbb{B}^{\natural*}=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}\neq0\}
=\{\tilde Q:|Q_t|\neq\lVert\vec Q\rVert_E\},
$$

the union of the **positive region** $\mathbb{B}^{\natural*}_+=\{\langle\tilde Q\rangle_{\natural*}>0\}$ and the **negative region** $\mathbb{B}^{\natural*}_-=\{\langle\tilde Q\rangle_{\natural*}<0\}$.

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\mathbb{B}^{\natural*}$;

(ii) $|Q_t|\neq\lVert\vec Q\rVert_E$;

(iii) the complex line $\mathbb{C}\tilde Q$ is non-degenerate for the Krein form;

(iv) the real plane $\operatorname{span}_{\mathbb{R}}\{\tilde Q,i\tilde Q\}$ is non-degenerate for the realified form;

(v) the restriction of the Krein form to the line $\mathbb{C}\tilde Q$ is definite.

*Proof.* (i) $\iff$ (ii) is the coordinate form of the norm. (ii) $\iff$ (iii) is the line criterion of *K-Regularity and Degeneracy in the Biquaternion Algebra*, §*Krein Orthogonality and the Complement*: a line is degenerate exactly when its radical is non-zero, and for a Hermitian form on a complex line the radical is the line itself exactly when the form vanishes at a non-zero point. (iii) $\iff$ (iv) is the realification: the real plane is the real space of the complex line, and the real form is the real part of the Hermitian one, so a radical over $\mathbb{C}$ and a radical over $\mathbb{R}$ coincide. (iii) $\iff$ (v): on the line the form is $\lambda\mapsto|\lambda|^2\langle\tilde Q\rangle_{\natural*}$, which is non-degenerate exactly when $\langle\tilde Q\rangle_{\natural*}\neq0$, and then it is definite with the sign of that value.

**Proposition (the sign is the sign of the line).** The line $\mathbb{C}\tilde Q$ is positive definite exactly in the positive region and negative definite exactly in the negative region. The line carries the sign of the norm, and no other sign occurs.

**Corollary (what the positive region excludes).** Every positive element has $Q_t\neq0$ and is non-zero; every negative element has $\vec Q\neq0$.

*Proof.* $|Q_t|>\lVert\vec Q\rVert_E\ge0$ gives $Q_t\neq0$; $|Q_t|<\lVert\vec Q\rVert_E$ gives $\vec Q\neq0$. The origin has value $0$ and lies in neither region.

**Remark (the sector is the set of non-isotropic elements).** An element is isotropic when its line is totally isotropic, that is, when the form vanishes identically on the line; the sector is exactly the complement of that set. The word regular is used in the metric sense of the main article, not in the ring-theoretic sense of a non-zero-divisor.

## The Two Signs

**Theorem (the positive region).** The map

$$
\Phi_+:\mathbb{C}^{\times}\times\mathbb{B}^6_1\longrightarrow\mathbb{B}^{\natural*}_+,
\qquad
\Phi_+(Q_t,W)=Q_t(e_t+W),
$$

with $\mathbb{B}^6_1=\{W\in\mathbb{C}^3:\lVert W\rVert_E<1\}$ the open unit ball, is a bijection. The positive region is therefore connected, of real dimension $8$, and homotopy equivalent to $S^1$.

*Proof.* On the region $Q_t\neq0$, and $W=\vec Q/Q_t$ has $\lVert W\rVert_E=|Q_t|^{-1}\lVert\vec Q\rVert_E<1$; conversely $\langle Q_t(e_t+W)\rangle_{\natural*}=|Q_t|^2(1-\lVert W\rVert_E^2)>0$. The inverse is $\tilde Q\mapsto(Q_t,\vec Q/Q_t)$. A product of a circle and a ball is homotopy equivalent to the circle.

**Theorem (the negative region).** The map

$$
\Phi_-:\mathbb{R}_{>0}\times D^2\times S^5\longrightarrow\mathbb{B}^{\natural*}_-,
\qquad
\Phi_-(r,w,W)=r(we_t+W),
$$

with $D^2=\{w\in\mathbb{C}:|w|<1\}$ the open unit disk and $S^5=\{W\in\mathbb{C}^3:\lVert W\rVert_E=1\}$, is a bijection. The negative region is therefore connected, of real dimension $8$, and homotopy equivalent to $S^5$.

*Proof.* For $\tilde Q$ negative put $r=\lVert\vec Q\rVert_E>0$, $W=\vec Q/r$ and $w=Q_t/r$; then $|w|=|Q_t|/r<1$. Conversely $\langle r(we_t+W)\rangle_{\natural*}=r^2(|w|^2-1)<0$. The inverse is $\tilde Q\mapsto(\lVert\vec Q\rVert_E,Q_t/\lVert\vec Q\rVert_E,\vec Q/\lVert\vec Q\rVert_E)$. The factors $\mathbb{R}_{>0}$ and $D^2$ are contractible.

**Corollary (the topologies differ).** The two regions are both of real dimension $8$, and they are not homeomorphic: their homotopy types are $S^1$ and $S^5$. They are the two components of the regular set, and the regular set is not connected.

**Theorem (homogeneity).** For $c>0$ the level set $\{\langle\tilde Q\rangle_{\natural*}=c\}$ is a single orbit of $\mathrm{U}(1,3)$, isomorphic to $\mathrm{U}(1,3)/\mathrm{U}(3)$; for $c<0$ it is a single orbit, isomorphic to $\mathrm{U}(1,3)/\mathrm{U}(1,2)$.

*Proof.* Two vectors of equal non-zero value are carried one to the other by an isometry of the form, by Witt's theorem. The stabiliser of a positive vector is the unitary group of its orthogonal complement, which is negative definite of complex dimension three, hence $\mathrm{U}(3)$; the stabiliser of a negative vector is the unitary group of a complement of signature $(1,2)$, hence $\mathrm{U}(1,2)$. The dimensions agree: $\dim_{\mathbb{R}}\mathrm{U}(1,3)=16$, $\dim_{\mathbb{R}}\mathrm{U}(3)=\dim_{\mathbb{R}}\mathrm{U}(1,2)=9$, and $16-9=7$ is the real dimension of a level set.

**Corollary (the sector is not one orbit).** The regular sector is a union of level sets and therefore of infinitely many orbits; the invariant that separates them is the value of the norm, and it is the only continuous invariant of the sector under the isometry group.

## Geometry

**Theorem (open and dense).** The sector $\mathbb{B}^{\natural*}$ is open and dense in $\mathbb{B}$, of real dimension $8$. Its complement $\mathcal K$ is closed, of empty interior and of real codimension one, and it is the common boundary

$$
\partial\mathbb{B}^{\natural*}_+=\partial\mathbb{B}^{\natural*}_-=\mathcal K .
$$

*Proof.* The norm is a real polynomial, so its non-zero set is open and its zero set is closed. Off the origin the gradient in the real coordinates $(\operatorname{Re}Q_t,\operatorname{Im}Q_t,\operatorname{Re}\vec Q,\operatorname{Im}\vec Q)$ is $2(\operatorname{Re}Q_t,\operatorname{Im}Q_t,-\operatorname{Re}\vec Q,-\operatorname{Im}\vec Q)\neq0$, so the zero set is a hypersurface. The origin is the only critical point, and near it $e_t$ and $\vec e_x$ give values of both signs, so every null point is a boundary point of both regions.

**Remark (cones without apex).** Both regions are stable under every non-zero complex scalar, $\langle\lambda\tilde Q\rangle_{\natural*}=|\lambda|^2\langle\tilde Q\rangle_{\natural*}$, and neither contains the origin: each is a cone with its apex deleted. The apex lies in the closure of both.

**Remark (neither region is convex).** The positive elements $e_t$ and $-e_t$ have the zero element as midpoint, and the negative elements $\vec e_x$ and $-\vec e_x$ do the same. Convexity fails in the strongest way in both regions.

**Remark (the Krein cone).** The closure of the positive region is the Krein cone $P_K=\{|Q_t|\ge\lVert\vec Q\rVert_E\}$, closed and star-shaped with respect to the origin, neither convex nor pointed; it is *K-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Krein Cone*, and its boundary structure is *The Krein Level Sets and the Hyperbolic Structure*.

## Multiplication and Inversion

**Theorem (the sector is not closed under multiplication).** The product of two regular elements can be positive, negative or null.

*Proof.* Four witnesses.

- **Positive times positive, negative product.** $\tilde Q=e_t+\tfrac12\vec e_x$ is positive, with value $\tfrac34$, and
$$
\tilde Q^2=\tfrac34e_t+\vec e_x,\qquad
\langle\tilde Q^2\rangle_{\natural*}=\tfrac{9}{16}-1=-\tfrac{7}{16}.
$$
- **Negative times negative, positive product.** $\vec e_x$ and $-\vec e_x$ are both negative, with value $-1$, and their product is $e_t$, of value $1$.
- **Regular times regular, null product.** $\vec e_x$ and $\vec e_x+i\vec e_y$ are negative, with values $-1$ and $-2$, and
$$
\vec e_x(\vec e_x+i\vec e_y)=\vec e_x^2+i\vec e_x\vec e_y=-e_t+i\vec e_z,\qquad
\langle\cdot\rangle_{\natural*}=1-1=0.
$$
- **Null times null, positive product.** $e_t+\vec e_x$ and $e_t-\vec e_x$ are null, and their product is $2e_t$, of value $4$.

**Theorem (inversion preserves the sign).** Let $\tilde Q$ be a unit, with algebraic norm $\langle\tilde Q\rangle_{\natural}\neq0$. Then

$$
\langle\tilde Q^{-1}\rangle_{\natural*}=\frac{\langle\tilde Q\rangle_{\natural*}}{\lvert\langle\tilde Q\rangle_{\natural}\rvert^2}.
$$

*Proof.* $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}=(Q_t-\vec Q)/\langle\tilde Q\rangle_{\natural}$, so the scalar part of the inverse is $Q_t/\langle\tilde Q\rangle_{\natural}$ and its vector part is $-\vec Q/\langle\tilde Q\rangle_{\natural}$. Hence
$$
\langle\tilde Q^{-1}\rangle_{\natural*}=\frac{|Q_t|^2-\lVert\vec Q\rVert_E^2}{\lvert\langle\tilde Q\rangle_{\natural}\rvert^2}.
$$

**Corollary (the sector is inversion-stable).** The regular sector is stable under inversion wherever inversion is defined, and each sign region is stable as well: inversion preserves the sign and rescales the value by a positive factor. The positive region is a **symmetric subset of the unit group** — closed under inversion, not closed under multiplication. The negative region contains zero divisors, on which inversion is undefined, and on its units it is inversion-stable.

**Remark (the group actions).** The sector is stable under $\mathbb{C}^{\times}$ and under the Krein isometry group $\mathrm{U}(1,3)$, which preserves the value. It is not stable under the unit group acting by similarity: the conjugation of §*Why There Is No Spectral Split* moves an element of the negative region to another value.

## Relation to the Algebraic Partition

**Theorem (positive implies unit).** If $\langle\tilde Q\rangle_{\natural*}>0$ then $\tilde Q$ is a unit of the plain product.

*Proof.* Positivity gives $|Q_t|>\lVert\vec Q\rVert_E$, hence $Q_t\neq0$. If $\tilde Q$ were a zero divisor, then $\langle\tilde Q\rangle_{\natural}=0$, so $Q_t^2=-\sum_kQ_k^2$ and
$$
|Q_t|^2=\Bigl|\sum_kQ_k^2\Bigr|\le\sum_k|Q_k|^2=\lVert\vec Q\rVert_E^2,
$$
in contradiction with positivity. A non-zero element that is not a zero divisor is a unit.

**Theorem (the zero divisors of the sector).** The zero divisors of the regular sector are exactly the zero divisors that are not doubly null,

$$
\mathcal Z\cap\mathbb{B}^{\natural*}=\mathcal Z\setminus\mathcal K_{\mathrm d},
$$

and they all lie in the negative region.

*Proof.* By *K-Regularity and Degeneracy in the Biquaternion Algebra*, §*The degeneracy case: the null set*, an algebraic-null element has non-positive Krein norm, with equality exactly on the doubly null Peirce lines. So a zero divisor has negative or zero Krein norm; it is in the regular sector exactly when the value is negative, and then it is not doubly null. Conversely a zero divisor that is not doubly null has negative value and lies in the sector.

**The sector against the algebraic partition.**

| | unit | zero divisor |
|---|---|---|
| **positive region** | every element: $e_t$ has $(1,1)$ | none |
| **negative region** | $e_t+2\vec e_x$ has $(-3,5)$ | $\vec e_x+i\vec e_y$ has $(-2,0)$ |

The pair is $(\langle\tilde Q\rangle_{\natural*},\langle\tilde Q\rangle_{\natural})$.

**Corollary (the sector meets every algebraic class except the origin).** The regular sector contains positive units, negative units and negative zero divisors. The origin, which is neither a unit nor a zero divisor, is the only algebraic class it misses, and the origin lies in the degenerate sector.

**Remark (the sector is not the unit group).** The unit group is the union of the positive region and the negative units; it is strictly larger than the positive region and strictly smaller than the sector. The difference is the negative zero divisors, on which the two partitions disagree.

## Comparison with the Degenerate Sector

| | regular sector | degenerate sector |
|---|---|---|
| condition | $\langle\tilde Q\rangle_{\natural*}\neq0$ | $\langle\tilde Q\rangle_{\natural*}=0$ |
| real dimension | $8$ | $7$ |
| components | two, $\mathbb{B}^{\natural*}_+$ and $\mathbb{B}^{\natural*}_-$ | one |
| smoothness | open submanifold | smooth off the origin, apex at the origin |
| homotopy type | $S^1\uplus S^5$ | $S^1\times S^5$ up to homotopy |
| line $\mathbb{C}\tilde Q$ | non-degenerate, definite | totally isotropic |
| algebraic classes | units and zero divisors | units and zero divisors |
| closed under products | no | no |
| closed under inversion | on the units | on the isotropic units |

**The two sectors exhaust the algebra.** $\mathbb{B}=\mathbb{B}^{\natural*}\uplus\mathcal K$, and the partition is by the value alone. The comparison of the algebraic classes inside each sector is the content of the two articles: here the classes are separated by the sign, there by the algebraic norm.

## Consequences

**Left multiplication.** If $\tilde Q$ is positive it is a unit, and $L_{\tilde Q}$ is a bijection of complex rank $4$. If $\tilde Q$ is negative, $L_{\tilde Q}$ has rank $4$ when $\tilde Q$ is a unit and rank $2$ when it is a zero divisor, by *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Annihilators*. The rank therefore follows the algebraic norm and not the Krein sign.

**The sandwich.** The operator $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ is singular exactly on the algebraic null cone, by *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Sandwich*. On the positive region it is invertible throughout; on the negative region it is invertible exactly on the negative units and singular on the negative zero divisors.

**The polar decomposition.** The modulus–unit decomposition $\tilde Q=\Rho\tilde U$ requires $\Rho^2=\langle\tilde Q\rangle_{\natural}$ with $\Rho\neq0$, so it exists exactly on the unit group. It therefore exists throughout the positive region, and on the negative region exactly off the zero divisors. The decomposition itself is *The Polar Decomposition of a N-Regular Biquaternion*.

**The adjoint.** The Krein adjoint is defined for every element, because the form is non-degenerate, so the sector imposes no restriction on it; the operator theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*.

**The level sets.** The sector is the union of the level sets $\{\langle\tilde Q\rangle_{\natural*}=c\}$ over $c\neq0$, each a homogeneous space, the positive ones of type $\mathrm{U}(1,3)/\mathrm{U}(3)$ and the negative ones of type $\mathrm{U}(1,3)/\mathrm{U}(1,2)$. Their topology is *The Krein Level Sets and the Hyperbolic Structure*, and the positive family is the complex hyperbolic ball.

## Summary

| question | answer |
|---|---|
| definition | $\mathbb{B}^{\natural*}=\{\langle\tilde Q\rangle_{\natural*}\neq0\}=\{|Q_t|\neq\lVert\vec Q\rVert_E\}$ |
| descriptions | complement of $\mathcal K$; non-isotropic line; non-degenerate real plane; definite restriction to the line |
| components | positive region, homotopy $S^1$; negative region, homotopy $S^5$ |
| parametrisations | $Q_t(e_t+W)$ with $Q_t\neq0$, $\lVert W\rVert_E<1$; $r(we_t+W)$ with $r>0$, $w\in D^2$, $W\in S^5$ |
| homogeneity | level sets are the orbits $\mathrm{U}(1,3)/\mathrm{U}(3)$ and $\mathrm{U}(1,3)/\mathrm{U}(1,2)$ |
| multiplication | not closed: positive times positive can be negative, negative times negative positive, regular times regular null |
| inversion | preserves the sign, with $\langle\tilde Q^{-1}\rangle_{\natural*}=\langle\tilde Q\rangle_{\natural*}/\lvert\langle\tilde Q\rangle_{\natural}\rvert^2$ |
| algebraic classes | positive units, negative units, negative zero divisors; no positive zero divisor |
| operators | left multiplication and the sandwich follow the algebraic norm; the polar decomposition exists exactly on the units |

The sector is the metric interior and exterior of the null set, taken together. It carries two signs, two topologies and three algebraic classes, and it is the whole of the algebra on which the Krein norm is a genuine measure: the positive region is the inside of the cone, the negative region the outside, and the null set between them is the degenerate sector.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}^{\natural*}$ | the Krein-regular sector, the complement of $\mathcal K$ |
| $\mathbb{B}^{\natural*}_+$ | the positive region, $\langle\tilde Q\rangle_{\natural*}>0$ |
| $\mathbb{B}^{\natural*}_-$ | the negative region, $\langle\tilde Q\rangle_{\natural*}<0$ |
| $\mathcal K$ | the null set, $\langle\tilde Q\rangle_{\natural*}=0$ |
| $\mathcal K_{\mathrm d}$ | the doubly null set, $\mathcal K\cap\mathcal N$ |
| $\mathcal Z$ | the zero-divisor set, $\mathcal N\setminus\{0\}$ |
| $\langle\tilde Q\rangle_{\natural*}=|Q_t|^2-\lVert\vec Q\rVert_E^2$ | the Krein norm |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the algebraic norm, which decides invertibility |
| $\lVert W\rVert_E^2=\sum_k|W_k|^2$ | the Euclidean norm on the vector part |
| $\mathbb{B}^6_1$ | the open unit ball of $\mathbb{C}^3$ |
| $D^2$, $S^5$ | the open unit disk and the unit sphere of $\mathbb{C}^3$ |
| $P_K$ | the Krein cone, the closure of the positive region |
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the sandwich |

## Further Reading

- [The K-Degenerate Sector](the-krein-norm-degenerate-sector.html), for the null set, the doubly null Peirce lines and the isotropic units.
- [K-Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the partition, the Krein cone, the two partitions of the algebra, and the four reasons why no spectral split is available.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form, its Gram matrix and its inertia.
- [K-Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the line criterion and the two partitions of the algebra.
- [The Fundamental Symmetry of the Form](the-fundamental-symmetry-of-the-form.html), for the fundamental symmetry and the bridge.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, their topology and the complex hyperbolic ball.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the group $\mathrm{U}(1,3)$ and its action.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the multiplicative norm, the unit group and the zero-divisor cone.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the sandwich, the rank of left multiplication and the polar decomposition.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ and its failure at the algebraic null cone.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction of the form to the six remarkable subspaces.
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the Krein adjoint and the operator theory of the form.
