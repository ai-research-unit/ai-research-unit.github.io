
# __The Involution on the Measure Algebra__

## Introduction

The group algebra $L^1(G)$ is an ideal in the larger convolution algebra $M(G)$ of bounded Radon measures, and $M(G)$ carries an involution of its own: the reflection of a measure by the group inverse followed by conjugation. This involution is isometric and anti-multiplicative on the whole measure algebra, and it restricts on the absolutely continuous measures to the modular-corrected involution of the group algebra; it is therefore the universal source of the involution that the group algebra carries. The adjoint of convolution — the transpose of the operator of convolution by a measure with respect to the Haar pairing — is convolution by the involution, and the unimodular case is where the same identity holds for the right regular representation as well, the two-sided picture being unitary only there. This article fixes the measure algebra, its involution and its restriction, and states the adjoint of convolution; the operator-theoretic form of the adjoint is *The Adjoint of a Convolution Operator*, in the `- * Operator Theory` group.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and its properties from *The Convolution Algebra $L^1(G)$*; the involution, the element classes and the completions from *The Group Algebra as an Involutive Algebra*; the Hermitian forms and the forms of the positive functionals from *Hermitian Forms and the Group Algebra*, immediately preceding; the Radon measures, their total variation, the Riesz representation theorem and the Lebesgue decomposition from *Measure Theory and Integration*; the group von Neumann algebra and the left regular representation from *The Group Algebra as an Algebra of Operators*; and the `*`-representations and the bounded operators on $L^2$ from *Operator Algebras*. The grade involution $\alpha$ of the `- Operator Theory` group is a different order-two structure and is not used; the adjoint of a convolution operator on $L^p$ and its explicit form are *The Adjoint of a Convolution Operator*, in the `- * Operator Theory` group; the Plancherel measure and the unitary representations are the earlier articles of this group.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$, and

$$
M(G) = \bigl\{\mu : \mu \text{ a bounded complex Radon measure on } G\bigr\}, \qquad \|\mu\| = |\mu|(G) ,
$$

with convolution

$$
(\mu*\nu)(E) = \int_G\int_G \mathbf{1}_E(xy)\,d\mu(x)\,d\nu(y) ,
$$

and involution

$$
\mu^*(E) = \overline{\mu(E^{-1})} \qquad (E\subseteq G \text{ Borel}).
$$

The **Haar pairing** is $\langle\mu,f\rangle = \int_G f\,d\mu$ for $\mu\in M(G)$ and $f$ a bounded continuous function.

## The Measure Algebra

**Theorem (the algebra and its ideal).** With the convolution and the total variation norm, $M(G)$ is a unital Banach algebra with identity $\delta_e$ and $\|\mu*\nu\|\leq\|\mu\|\,\|\nu\|$; the map $f\mapsto f\,dx$ is an isometric algebra isomorphism of $L^1(G)$ onto a closed two-sided ideal of $M(G)$, and the Lebesgue decomposition

$$
M(G) = L^1(G)\oplus M_s(G)
$$

expresses every measure uniquely as an absolutely continuous part and a part singular with respect to $dx$.

**Proof.** The convolution inequalities follow from Fubini and the subadditivity of the total variation; associativity is the associativity of the product in $G$; the identity is $\delta_e$. The embedding is isometric by the definition of $L^1(G)$ and is multiplicative, and the ideal property is the translation invariance of $dx$. The Lebesgue decomposition is the Radon–Nikodym theorem for the pair $\mu$ and $dx$. $\square$

**Example (the discrete and compact cases).** For $G$ discrete with counting measure, $M(G) = \ell^1(G)$ is unital and the point masses $\delta_x$ are unitary elements; for $G$ compact, $M(G) = L^1(G)\oplus M_s(G)$ with $M_s(G)$ the discrete measures, and $\delta_e$ is a unit not in $L^1(G)$.

## The Involution

**Theorem (the involution axioms).** The map $\mu\mapsto\mu^*$ is an involution on $M(G)$,

$$
(\mu^*)^* = \mu, \qquad (\lambda\mu + \nu)^* = \bar\lambda\,\mu^* + \nu^*, \qquad (\mu*\nu)^* = \nu^*\!*\mu^*, \qquad \|\mu^*\| = \|\mu\| ,
$$

so that $M(G)$ is a Banach `*`-algebra with isometric involution; the involution is an anti-automorphism of the full measure algebra, with no hypothesis on the group.

**Proof.** The total variation of $\mu^*$ is $|\mu^*|(E) = |\mu|(E^{-1})$, so $|\mu^*|(G) = |\mu|(G)$ and the involution is isometric; the order-two and linearity statements are immediate. For the anti-automorphism, test against $f\in C_{00}(G)$ using the pairing identity $\langle\lambda^*,f\rangle = \overline{\langle\lambda,\tilde f\rangle}$ with $\tilde f(x) = \overline{f(x^{-1})}$. Then

$$
\bigl\langle(\mu*\nu)^*,f\bigr\rangle = \overline{\bigl\langle\mu*\nu,\tilde f\bigr\rangle} = \overline{\int\!\!\int \overline{f(y^{-1}x^{-1})}\,d\mu(x)\,d\nu(y)} = \int\!\!\int f(y^{-1}x^{-1})\,d\overline{\mu(x)}\,d\overline{\nu(y)} ,
$$

and the substitution $u = y^{-1}$, $v = x^{-1}$ turns the last expression into $\int\!\!\int f(uv)\,d\nu^*(u)\,d\mu^*(v) = \langle\nu^*\!*\mu^*,f\rangle$. Since $C_{00}(G)$ separates measures, the identity follows. $\square$

**Corollary (the isometry does not need unimodularity).** The involution of $M(G)$ preserves the norm for every locally compact $G$; the role of the modular function is not here but in the compatibility of the involution with the Haar pairing and with the $L^2$ structure, below.

**Proof.** The computation $|\mu^*|(G) = |\mu|(G)$ above uses only the fact that inversion is a homeomorphism, which holds without any unimodularity. $\square$

## The Involution on the Group Algebra

**Theorem (the restriction reproduces the group-algebra involution).** Under the identification $f\leftrightarrow f\,dx$ the involution of $M(G)$ restricts to the involution of $L^1(G)$,

$$
(f\,dx)^* = f^*\,dx, \qquad f^*(x) = \overline{f(x^{-1})}\,\Delta(x)^{-1} ,
$$

so the involution of the group algebra is exactly the restriction of the measure-algebra involution, and the modular factor is generated by the group inverse together with the change of variable $x\mapsto x^{-1}$.

**Proof.** By definition $(f\,dx)^*(E) = \overline{\int_{E^{-1}}f(x)\,dx}$. Since $E^{-1}$ is the image of $E$ under inversion, the change of variable $x = y^{-1}$ in the integral has Jacobian $\Delta(y)^{-1}$, giving $\overline{\int_{E^{-1}}f(x)dx} = \int_E\overline{f(y^{-1})}\Delta(y)^{-1}dy$, which is the density $f^*$ of $(f\,dx)^*$. $\square$

**Corollary (why $L^1$ has the modular factor).** The four involution axioms of *The Group Algebra as an Involutive Algebra* are the restrictions of the axioms of the theorem above; in particular the modular factor is not an extra convention of the group algebra but the Jacobian of the inversion, and it disappears exactly when $\Delta\equiv1$, that is when $G$ is unimodular.

**Proof.** Restrict the axioms $(\mu*\nu)^* = \nu^*\!*\mu^*$, $(\mu^*)^* = \mu$ and $\|\mu^*\| = \|\mu\|$ to absolutely continuous measures and read the identity $(f*g)\,dx = (f\,dx)*(g\,dx)$. The factor $\Delta(x)^{-1}$ is the Jacobian computed in the theorem. $\square$

## The Adjoint of Convolution

**Theorem (the adjoint of convolution).** Let $\mu\in M(G)$ and let $\lambda(\mu)$ be the operator of left convolution, $\lambda(\mu)\xi = \mu*\xi$, on $L^2(G)$. Then

$$
\lambda(\mu)^* = \lambda(\mu^*) ,
$$

the adjoint with respect to the Haar pairing $\langle\xi,\eta\rangle = \int_G\xi(x)\overline{\eta(x)}\,dx$; consequently $\lambda : M(G)\to B(L^2(G))$ is a `*`-representation for the measure-algebra involution, and its restriction to $L^1(G)$ is the left regular representation with $\lambda(f)^* = \lambda(f^*)$. No hypothesis on $G$ is needed.

**Proof.** For $f\in L^1(G)$ the identity $\lambda(f)^* = \lambda(f^*)$ follows from the unitary representation $\lambda$ by *Unitary Representations and the Adjoint*: $\lambda(f)^* = \int\overline{f(x)}\lambda(x)^{-1}dx$, and the substitution $x\to x^{-1}$ with the inversion identity $dx = \Delta(x)^{-1}dx$ at $x = y^{-1}$ turns this into $\int\overline{f(y^{-1})}\Delta(y)^{-1}\lambda(y)dy = \lambda(f^*)$. The map $\lambda : M(G)\to B(L^2(G))$ is norm-continuous, and $L^1(G)$ is weak-`*` dense in $M(G) = C_0(G)^*$ with convolution and the involution weak-`*` continuous; passing to the limit gives the identity for every $\mu\in M(G)$. $\square$

**Remark (where the unimodularity does appear).** The measure-algebra involution itself needs no hypothesis; the identity $\lambda(\mu)^* = \lambda(\mu^*)$ needs none either, because the left regular representation is unitary for every $G$. The unimodular case is distinguished by the fact that the **right** regular representation is also unitary on $L^2(G)$ for the left Haar measure, so that right convolution is a `*`-representation as well, $\rho(\mu)^* = \rho(\mu^*)$; when $G$ is not unimodular, $\rho(x)$ is unitary only for the weighted inner product $\langle\xi,\eta\rangle_\Delta = \int\xi\overline{\eta}\,\Delta$, and the right-handed adjoint identity must be read there. The exact operator form of the adjoint, on $L^p$ and for the two-sided case, is *The Adjoint of a Convolution Operator*, in the `- * Operator Theory` group.

**Remark (what the article does not do).** The operator-theoretic adjoint of a convolution operator, its explicit form on $L^p$, the case of a two-sided measure and the involutive algebra structure it gives are *The Adjoint of a Convolution Operator*, in the `- * Operator Theory` group below, where the theory is developed on the operator level; the adjoint of a representation operator is *Unitary Representations and the Adjoint*, there. The grade involution of the signed block is not the measure involution: the first is an automorphism, the second an anti-automorphism, and the two are distinguished as in *The Group Algebra as an Involutive Algebra*.

## Summary

The bounded Radon measures on $G$ form a unital Banach algebra $M(G)$ under convolution, with identity $\delta_e$ and $\|\mu*\nu\|\leq\|\mu\|\|\nu\|$, in which $L^1(G)$ sits as a closed two-sided ideal, $M(G) = L^1(G)\oplus M_s(G)$ by Lebesgue decomposition. The involution $\mu^*(E) = \overline{\mu(E^{-1})}$ is isometric and satisfies the anti-automorphism $(\mu*\nu)^* = \nu^*\!*\mu^*$ on the whole of $M(G)$, with no hypothesis on the group: the isometry uses only that inversion is a homeomorphism. Restricted to the absolutely continuous measures the involution gives $(f\,dx)^* = f^*\,dx$ with $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, so the modular factor of the group-algebra involution is the Jacobian of the inversion and vanishes exactly in the unimodular case. The operator of left convolution by $\mu$ on $L^2(G)$ has adjoint $\lambda(\mu)^* = \lambda(\mu^*)$ for every $G$, so $\lambda$ is a `*`-representation of the measure algebra and the left regular representation satisfies $\lambda(f)^* = \lambda(f^*)$; the unimodular case is the one in which the right regular representation is also unitary on $L^2(G)$ and right convolution is a `*`-representation with the same involution. The operator-theoretic adjoint is the neighbouring `- * Operator Theory` article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M(G)$, $\|\mu\| = |\mu|(G)$ | The measure algebra and the total variation norm |
| $(\mu*\nu)(E) = \int\!\!\int\mathbf{1}_E(xy)\,d\mu\,d\nu$ | Convolution of measures |
| $\delta_e$ | The identity of $M(G)$ |
| $M(G) = L^1(G)\oplus M_s(G)$ | The Lebesgue decomposition |
| $\mu^*(E) = \overline{\mu(E^{-1})}$ | The involution on $M(G)$ |
| $(\mu*\nu)^* = \nu^*\!*\mu^*$ | The anti-automorphism, no unimodularity needed |
| $\|\mu^*\| = \|\mu\|$ | Isometry of the involution |
| $(f\,dx)^* = f^*\,dx$ | Restriction to $L^1(G)$ |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | The modular factor as the Jacobian of inversion |
| $\lambda(\mu)^* = \lambda(\mu^*)$ | The adjoint of convolution, unimodular case |

## Further Reading

- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the measure algebra, its convolution, its involution and the Lebesgue decomposition.
- Walter Rudin, *Fourier Analysis on Groups* (Wiley, 1962), for the measure algebra of an abelian group and the involution on it.
- Hans Reiter and Jan D. Stegeman, *Classical Harmonic Analysis and Locally Compact Groups* (Oxford University Press, second edition, 2000), for the modular function, the unimodular case and the modular twisting of the adjoint.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the `*`-representation of the measure algebra on $L^2(G)$ and the group von Neumann algebra.
- Sterling K. Berberian, *Baer ${}^*$-Rings* (Springer, 1972), for involutions on algebras of measures and the anti-automorphism axioms.
