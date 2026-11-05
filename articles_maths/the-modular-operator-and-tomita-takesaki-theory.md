# __The Modular Operator and Tomita-Takesaki Theory__

## Introduction

Given a von Neumann algebra $\mathcal{M}$ on a Hilbert space $H$ and a vector $\zeta$ that is cyclic and separating for it, one can define, without any further structure, an antilinear operator $S$ by $S(x\zeta) = x^{*}\zeta$. It is densely defined and closable, and its closure has a polar decomposition $S = J\Delta^{1/2}$ whose two factors are the two objects of the **Tomita–Takesaki theory**: the **modular operator** $\Delta = S^{*}S$, a positive self-adjoint operator, and the **modular conjugation** $J$, an antiunitary involution. Neither is visible from the algebra alone, and both are determined by the pair $(\mathcal{M},\zeta)$.

The theorem says what the two factors do. The modular conjugation is an anti-isomorphism of the algebra onto its commutant, $J\mathcal{M}J = \mathcal{M}'$, and it inverts the modular operator, $J\Delta J = \Delta^{-1}$; the modular operator generates a one-parameter group of automorphisms of the algebra, $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$, and the vector $\zeta$ satisfies the KMS condition for this group. So a single vector produces the commutant, a flow on the algebra, and the analytic condition — the KMS condition — that identifies the flow. This is the deepest structural result about von Neumann algebras, and it is the reason a von Neumann algebra with a cyclic and separating vector is called a **standard form**.

This article fixes the Tomita operator, its polar decomposition, the modular operator, the modular conjugation with the commutant theorem, and the modular group, in the definite case; the group and the KMS condition are developed further in *The Modular Group and the KMS Condition*, and the indefinite version is *The Indefinite Modular Operator* and *Krein–Tomita–Takesaki Theory*.

The Hilbert algebra whose involution produces $S$ is *The Completion of a Hilbert Algebra*; the positivity and the square roots are *Self-Adjoint Elements and the Positive Cone*; the operator algebra is *Von Neumann Algebras and the Hilbert Algebra Completeness*; the states are *The GNS Construction*. Those are cited. The algebra is $\mathcal{M}$, the vector is $\zeta$, and the objects are $S$, $\Delta$, $J$.

## The Tomita Operator

**Definition.** Let $\zeta$ be **cyclic** for $\mathcal{M}$, $\overline{\mathcal{M}\zeta} = H$, and **separating**, $x\zeta = 0\Rightarrow x = 0$. The **Tomita operator** is

$$
S : \mathrm{dom}\,S\to H, \qquad \mathrm{dom}\,S = \mathcal{M}\zeta, \qquad S(x\zeta) = x^{*}\zeta .
$$

**Proposition (well defined, antilinear, involutive, closable).** $S$ is well defined because $\zeta$ is separating, it is antilinear, $S^{2} = \mathrm{id}$ on its domain, and it is closable.

**Proof.** Well-definedness and antilinearity are direct; $S^{2}(x\zeta) = S(x^{*}\zeta) = (x^{*})^{*}\zeta = x\zeta$; for closability, if $x_n\zeta\to0$ and $S(x_n\zeta) = x_n^{*}\zeta\to u$, then for every $y$ and $v$ one gets $\langle u,y\zeta\rangle = \lim\langle x_n^{*}\zeta,y\zeta\rangle = \lim\langle\zeta,x_n y\zeta\rangle = 0$, so $u = 0$ by cyclicity.

**Proposition (the adjoint of $S$).** The adjoint $S^{*}$ is the antilinear operator with $S^{*}(x\zeta) = x^{*}\zeta$ as well; more precisely $S^{*}$ has domain $\mathcal{M}'\zeta$ and $S^{*}(y\zeta) = y^{*}\zeta$ for $y\in\mathcal{M}'$.

**Proof.** $\langle S x\zeta, y\zeta\rangle = \langle x^{*}\zeta,y\zeta\rangle = \langle\zeta,xy\zeta\rangle$ and $\langle x\zeta, S^{*}y\zeta\rangle = \langle x\zeta,y^{*}\zeta\rangle = \langle\zeta,xy^{*}\zeta\rangle$; the two agree for all $x$ exactly when $y$ commutes with $\mathcal{M}$, i.e. for $y\in\mathcal{M}'$.

## The Polar Decomposition

**Theorem (polar decomposition).** The closure $\bar S$ of the Tomita operator has the polar decomposition

$$
\boxed{\;\bar S = J\,\Delta^{1/2}, \qquad \Delta = \bar S^{*}\bar S , \qquad J = \text{the modular conjugation}\;},
$$

with $\Delta$ a positive definite self-adjoint operator and $J$ an antiunitary involution.

**Proof.** Each closed antilinear operator has a polar decomposition $\bar S = U|\bar S|$ with $|\bar S| = (\bar S^{*}\bar S)^{1/2}$ and $U$ an antiunitary partial isometry; the operator $|\bar S|$ is the positive square root of the positive self-adjoint $\bar S^{*}\bar S$, which exists by *Self-Adjoint Elements and the Positive Cone*; and $U$ is in fact antiunitary and involutive because $S^{2} = \mathrm{id}$ passes to the closure, forcing $J^{2} = \mathrm{id}$ and $\Delta = J\Delta^{-1}J$.

**Definition.** The operator $\Delta = \bar S^{*}\bar S$ is the **modular operator** of the pair $(\mathcal{M},\zeta)$ and the antiunitary $J$ in the polar decomposition is the **modular conjugation**.

## The Modular Operator

**Proposition (positivity and the relations with $S$).** $\Delta$ is positive definite and self-adjoint, $\Delta^{1/2}$ is its positive square root, and

$$
S = J\Delta^{1/2}, \qquad S^{*} = J\Delta^{-1/2}, \qquad \Delta = S^{*}S, \qquad \Delta^{-1} = SS^{*} .
$$

**Proof.** The polar decomposition and the involutivity $J^{2} = \mathrm{id}$, $S^{2} = \mathrm{id}$.

**Proposition (the action of $\Delta$ on the orbit).** The orbit $\mathcal{M}\zeta$ lies in the domain of $\Delta^{it}$ for every real $t$, and $\Delta^{it}(x\zeta) = \sigma_{-t}(x)\zeta$, where $\sigma_t$ is the modular group of the next section; equivalently $\Delta$ is the conjugate of $\sigma$ under the identification of the orbit with the algebra.

**Proof.** The identity is the definition of the modular group by the polar decomposition; it is the standard rewriting of $S = J\Delta^{1/2}$.

**Remark (the modular operator records the asymmetry of $\zeta$).** $\Delta = \mathrm{id}$ exactly when $\zeta$ is **tracial**, $\omega(xy) = \omega(yx)$ for $\omega$ the vector state; in that case $S$ is antiunitary and the modular conjugation alone carries the theory. The deviation of $\Delta$ from the identity is the extent of the non-traciality of the vector state.

## The Modular Conjugation and the Commutant

**Theorem (Tomita–Takesaki, the conjugation).** With $J$ the modular conjugation of the pair $(\mathcal{M},\zeta)$,

$$
\boxed{\;J\,\mathcal{M}\,J = \mathcal{M}' , \qquad J\,\mathcal{M}'\,J = \mathcal{M} , \qquad J\Delta J = \Delta^{-1} , \qquad J\zeta = \zeta\;} .
$$

**Proof.** The statement $J\mathcal{M}J\subseteq\mathcal{M}'$ is read off the adjoint of $S$: $S^{*}$ has domain $\mathcal{M}'\zeta$ and agrees with $S$ there, and $J = \bar S\Delta^{-1/2}$ on the dense set gives $JxJ$ commuting with $\mathcal{M}$; the reverse inclusion is the same statement applied to $\mathcal{M}'$, or the bicommutant theorem; the inversion of $\Delta$ is $J\Delta J = JS^{*}SJ = S S^{*}$; and $J\zeta = \zeta$ is the fact that $\zeta$ is fixed by the conjugation of its own polar decomposition.

**Corollary (the standard form).** The quadruple $(\mathcal{M}, \mathcal{M}', H, J)$ is a **standard form**: the algebra acts, the commutant is its conjugate, the conjugation is an anti-isomorphism between them, the vector $\zeta$ is cyclic and separating for both, and the positive cone $\mathcal{M}_{+}\zeta$ is self-dual.

**Proof.** Cyclicity for $\mathcal{M}'$ follows from the theorem and cyclicity for $\mathcal{M}$; the other statements are the theorem and the definition of the modular conjugation.

**Remark (why the commutant is automatic).** The commutant of a von Neumann algebra is one of the most delicate objects of the theory, and Tomita's theorem computes it from a single vector. This is the practical content of the theorem, and it is the reason it is used everywhere the commutant is needed.

## The Modular Group

**Theorem (Tomita–Takesaki, the flow).** With $\Delta$ the modular operator of the pair $(\mathcal{M},\zeta)$, the family

$$
\boxed{\;\sigma_t = \mathrm{Ad}\,\Delta^{it} : \mathcal{M}\to\mathcal{M}, \qquad \sigma_t(x) = \Delta^{it}x\Delta^{-it}\;},
$$

is a one-parameter group of automorphisms of $\mathcal{M}$, strongly continuous in the strong topology, and the vector $\zeta$ satisfies the KMS condition for it: for all $x, y\in\mathcal{M}$ the function $F(t) = \langle\sigma_t(y)x\zeta,\zeta\rangle$ extends holomorphically to the strip $0<\mathrm{Im}\,z<1$ with boundary values

$$
F(t) = \omega(x\sigma_t(y)), \qquad F(t+i) = \omega(\sigma_t(y)x), \qquad \omega = \text{the vector state of } \zeta .
$$

**Proof.** $\Delta^{it}$ is unitary for every real $t$, hence conjugation by it is an automorphism; the group law is that of $t\mapsto\Delta^{it}$; the strong continuity is the strong continuity of a unitary group generated by a self-adjoint operator; the KMS statement is the analytic continuation of $\Delta = S^{*}S$, the two boundary values corresponding to the two faces $S$ and $S^{*}$ of the Tomita operator.

**Definition.** $\sigma$ is the **modular group** or **modular automorphism group** of the pair $(\mathcal{M},\zeta)$.

**Remark (the flow is invisible in the algebra alone).** The modular group is determined by the vector and not only by the algebra: conjugating the representation by a modular group changes the vector but not the algebra, and the modular groups of different vectors are the flows computed from different modular operators. This is taken up in *The Modular Group and the KMS Condition*.

## Worked Cases

### Tracial Vectors

If $\zeta$ is a trace vector, $\omega(xy) = \omega(yx)$, then $\Delta = \mathrm{id}$, the modular group is trivial, the modular conjugation is the map $x\zeta\mapsto x^{*}\zeta$ extended, and the standard form is symmetric between the algebra and its commutant.

### The Unit Vector of $M_n(\mathbb{C})$

For $\mathcal{M} = M_n(\mathbb{C})$ acting on $H = M_n(\mathbb{C})$ by left multiplication with the Hilbert–Schmidt form and $\zeta = 1$, the modular operator is the identity (the trace is tracial), the modular conjugation is $J(x) = x^{*}$, and $J\mathcal{M}J = \mathcal{M}'$ is the algebra of right multiplications.

### The Abelian Case

For $\mathcal{M} = L^{\infty}(X)$ acting on $H = L^{2}(X)$ with $\zeta$ the constant function one, the modular operator is the identity, the modular conjugation is complex conjugation of functions, the algebra is its own commutant and the theory degenerates to the statement that the commutant of an abelian algebra is itself.

## Summary

For a von Neumann algebra $\mathcal{M}$ with a **cyclic and separating** vector $\zeta$, the **Tomita operator** $S(x\zeta) = x^{*}\zeta$ is a densely defined closable antilinear involution, and its closure has the polar decomposition $\bar S = J\Delta^{1/2}$. The factor $\Delta = \bar S^{*}\bar S$ is the **modular operator**: positive definite and self-adjoint, with $\Delta^{-1} = SS^{*}$. The factor $J$ is the **modular conjugation**: antiunitary, involutive, fixing $\zeta$, inverting the modular operator, and carrying the algebra to its commutant, $J\mathcal{M}J = \mathcal{M}'$. Together they turn $(\mathcal{M},H,\zeta)$ into a **standard form** in which the commutant is computed from one vector. The **modular group** $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ is a strongly continuous one-parameter group of automorphisms of $\mathcal{M}$, and the vector state of $\zeta$ satisfies the **KMS condition** with respect to it; $\Delta$ is the identity exactly when the vector state is tracial, and the modular group and the KMS condition are the subject of *The Modular Group and the KMS Condition*. The Hilbert algebra that produces $S$ is *The Completion of a Hilbert Algebra*, the positivity and square roots are *Self-Adjoint Elements and the Positive Cone*, the indefinite counterparts are *The Indefinite Modular Operator* and *Krein–Tomita–Takesaki Theory*, and the operator algebra is *Von Neumann Algebras and the Hilbert Algebra Completeness*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$, $S(x\zeta) = x^{*}\zeta$ | Tomita operator, antilinear and involutive |
| $S^{*}$, $S^{*}(y\zeta) = y^{*}\zeta$ | Adjoint, defined on $\mathcal{M}'\zeta$ |
| $\bar S = J\Delta^{1/2}$ | Polar decomposition |
| $\Delta = \bar S^{*}\bar S$ | Modular operator, positive definite self-adjoint |
| $J$ | Modular conjugation, antiunitary, $J^{2} = \mathrm{id}$, $J\zeta = \zeta$ |
| $J\mathcal{M}J = \mathcal{M}'$ | The commutant theorem |
| $J\Delta J = \Delta^{-1}$ | Inversion of the modular operator |
| $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ | Modular group |
| $\Delta = \mathrm{id}$ | Tracial vector state |

## Further Reading

- Minoru Tomita, "On canonical forms of von Neumann algebras" (1967), for the original construction.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular theory in its algebraic form.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the Tomita–Takesaki theorem and the standard form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the polar decomposition of the Tomita operator and the modular group.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the standard form and the self-dual cone.
