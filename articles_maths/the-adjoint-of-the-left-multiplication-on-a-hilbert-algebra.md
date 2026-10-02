# __The Adjoint of the Left Multiplication on a Hilbert Algebra__

## Introduction

The adjoint of the left multiplication of a Hilbert algebra is the left multiplication by the involution, $L_x^{*} = L_{x^{\dagger}}$, and everything the adjoint does can be read off from that single identity. This article takes the identity as the starting point and follows it to the operator that carries the whole modular structure. The adjoint is computed at the cyclic vector, where it moves $\xi$ to the involution, $\bar L_x^{*}\xi = \iota(x^{\dagger})$; the closure of the involution, written $S$ and called the **Tomita operator**, is the antilinear operator sending $x\xi$ to $x^{\dagger}\xi$; and the polar decomposition of $S$ produces the **modular operator** $\Delta$ and the **modular conjugation** $J$. So the adjoint of the left multiplication, the involution and the modular operator are three views of one object, and this article is the place where the first view is turned into the third.

Two facts organise the computation. The first is that the adjoint of the left multiplication is again a left multiplication, so the adjoint of a one-sided operator stays on its own side; the passage to the other side is not adjunction but conjugation by $J$, $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$. The second is that the involution on the completion is not a bounded operator: it is the antilinear operator $S$ whose polar decomposition is $S = J\Delta^{1/2}$, so the adjoint of the left multiplication already contains the modular operator, and the deviation of the form from being tracial is exactly the deviation of $S$ from being an isometry.

This article fixes the adjoint of the left multiplication and its action on the cyclic vector, the Tomita operator and its elementary properties, the polar decomposition and the identities it carries, and the self-adjointness and unitarity criteria for the left multiplication.

The involution and the adjoint axiom are *Hermitian Adjoints on a Hilbert Algebra* and *Hilbert Algebras*; the completion is *The Completion of a Hilbert Algebra*; the two representations are *The Left and the Right Regular Representation*; the exchange between the sides and the adjoints of the two multiplications are *The Adjoint of the Left and the Right Multiplication*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the positivity is *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, its completion is $H$, and $\xi = \iota(1)$ is the cyclic vector.

## The Adjoint of the Left Multiplication

**Definition.** For $x\in A$ the **left multiplication** is $L_x(y) = xy$ on $A$, and $\bar L_x$ is its extension to the completion $H$; the **adjoint** $\bar L_x^{*}$ is the Hilbert adjoint on $H$.

**Theorem.** For every $x$ the left multiplication is bounded on the completion and

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} .
$$

**Proof.** On the algebra the identity is the adjoint axiom, $\langle L_xy,z\rangle = \langle xy,z\rangle = \langle y,x^{\dagger}z\rangle = \langle y,L_{x^{\dagger}}z\rangle$; the operator $L_x$ is bounded on $A$ for the form norm, so it extends to $H$ with the same adjoint; both sides of the identity are bounded and agree on the dense subspace $A$, hence on $H$.

**Proposition (the adjoint at the cyclic vector).** With $\xi = \iota(1)$,

$$
\bar L_x\xi = \iota(x) , \qquad \bar L_x^{*}\xi = \iota(x^{\dagger}) ,
$$

so the adjoint is the map of the cyclic vector to the involution, and the deviation of the involution from the identity on $\iota(A)$ is the deviation of $\bar L_x^{*}$ from $\bar L_x$.

**Proof.** $L_x1 = x$ gives the first identity; the second is the theorem applied to $1$.

**Proposition (positivity of the adjoint products).** For every $x$ and every $u\in H$,

$$
\langle\bar L_x\bar L_x^{*}u,u\rangle = \|\bar L_x^{*}u\|^{2}\geq0 , \qquad \langle\bar L_x^{*}\bar L_xu,u\rangle = \|\bar L_xu\|^{2}\geq0 ,
$$

so $\bar L_x\bar L_x^{*}$ and $\bar L_x^{*}\bar L_x$ are positive operators, and the left multiplications form a $\ast$-closed family.

**Proof.** The two displays are the definition of the Hilbert adjoint.

**Proposition (the adjoint is determined by the form).** If an antilinear map $\Phi$ of $A$ satisfies $L_{\Phi(x)} = L_x^{*}$ for every $x$ then $\Phi = \dagger$; the adjoint axiom therefore determines the involution and conversely.

**Proof.** Evaluating at $1$ gives $\Phi(x) = \Phi(x)\cdot 1 = L_{\Phi(x)}1 = L_x^{*}1 = x^{\dagger}$ by the previous proposition.

## The Tomita Operator

**Definition.** The **Tomita operator** of the Hilbert algebra is the antilinear map

$$
S : A\xi\longrightarrow A\xi , \qquad S(x\xi) = x^{\dagger}\xi ,
$$

with domain the dense subspace $A\xi$; its closure, when needed, is written $\bar S$.

**Proposition (elementary properties).** $S$ is antilinear, $S^{2} = \mathrm{id}$ on its domain, $S$ is isometric exactly when the form is tracial, and $S$ satisfies

$$
L_x^{*} = S\,R_x\,S \qquad \text{and} \qquad S\,L_x\,S = R_{x^{\dagger}} .
$$

**Proof.** Antilinearity is that of the involution; $S^{2}(x\xi) = S(x^{\dagger}\xi) = x\xi$; the identities are computed on $A\xi$: $SR_xS(y\xi) = SR_x(y^{\dagger}\xi) = S(y^{\dagger}x\xi) = (y^{\dagger}x)^{\dagger}\xi = x^{\dagger}y\xi = L_{x^{\dagger}}(y\xi)$, which is $L_x^{*}$ by the theorem, and $SL_xS(y\xi) = S(xy^{\dagger}\xi) = (xy^{\dagger})^{\dagger}\xi = yx^{\dagger}\xi = R_{x^{\dagger}}(y\xi)$.

**Corollary (the adjoint is a conjugation of the other side).** The adjoint of the left multiplication by $x$ is the right multiplication by $x$ conjugated by the Tomita operator, and the Tomita operator exchanges the two sides.

**Proof.** The first identity of the proposition.

**Remark (why the adjoint carries the modular operator).** The identity $L_x^{*} = SR_xS$ shows that the adjoint of a one-sided operator is obtained by conjugating the *other* one-sided operator with $S$, an operator that is not bounded unless the form is tracial. So the adjoint of the left multiplication, read through the cyclic vector, is exactly the involution, and read on the completion it is the modular operator in disguise; the two readings are reconciled by the polar decomposition of the next section.

## The Polar Decomposition

**Theorem (Tomita–Takesaki).** The closure of $S$ has a polar decomposition

$$
\bar S = J\,\Delta^{1/2} ,
$$

where $J$ is an antiunitary involution, $J^{2} = \mathrm{id}$, and $\Delta = \bar S^{*}\bar S$ is a positive self-adjoint operator, generally unbounded; equivalently $\bar S = J\Delta^{1/2}$, $\bar S^{*} = J\Delta^{-1/2}$ and $\Delta = \bar S^{*}\bar S$.

**Proof.** The operator $\bar S$ is closed and densely defined, so it has a polar decomposition $\bar S = U|\bar S|$ with $|\bar S| = (\bar S^{*}\bar S)^{1/2} = \Delta^{1/2}$ and $U$ a partial isometry with kernel $\ker\bar S$ and range $\overline{\mathrm{ran}\,\bar S}$; the involutivity $S^{2} = 1$ forces $\ker\bar S = \{0\}$, because $\bar Sy = 0$ with $0\in\mathrm{dom}\,\bar S$ gives $y = \bar S^{2}y = \bar S0 = 0$; hence $\overline{\mathrm{ran}\,|\bar S|} = (\ker|\bar S|)^{\perp} = H$ and $U$ is an antiunitary operator with $U^{2} = \mathrm{id}$, written $J$.

**Proposition (the identities carried by the decomposition).** With $S = J\Delta^{1/2}$ one has

$$
\Delta = \bar S^{*}\bar S , \qquad J\Delta J = \Delta^{-1} , \qquad J\,\Delta^{it}\,J = \Delta^{-it} ,
$$

and the modular group $t\mapsto\Delta^{it}$ is a one-parameter group of unitaries.

**Proof.** The first identity is the definition of $|\bar S|$; from $\bar S^{2} = 1$ and $\bar S = J\Delta^{1/2}$ one gets $\mathrm{id} = J\Delta^{1/2}J\Delta^{1/2}$, whence $J\Delta^{1/2}J = \Delta^{-1/2}$ and $J\Delta J = \Delta^{-1}$; the third identity follows by functional calculus.

**Corollary (the adjoint of the left multiplication recovered).** The adjoint of the left multiplication satisfies

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} = S\,\bar R_x\,S = J\Delta^{1/2}\,\bar R_x\,J\Delta^{1/2} , \qquad \jmath\,\bar L_x\,\jmath = \bar R_{x^{\dagger}} ,
$$

the first identity being the conjugation by the Tomita operator and the second its bounded version, valid without the modular operator.

**Proof.** Substituting $S = J\Delta^{1/2}$ into $S\bar R_xS = \bar L_{x^{\dagger}}$ gives the displayed product; the second identity is *The Adjoint of the Left and the Right Multiplication*, and it needs no domain condition because $\jmath$ is antiunitary and the right multiplication is bounded.

**Remark (the deviation from a tracial form).** The form is tracial exactly when $\Delta = \mathrm{id}$, in which case $S = J$ is a bounded antiunitary involution and the adjoint of the left multiplication is bounded on $A$; the modular operator is therefore the quantitative description of the failure of the involution to be a bounded adjoint operation, and it is obtained from the adjoint of the left multiplication and nothing else.

## Self-Adjointness and Unitarity

**Theorem (the criteria).** For $x\in A$:

1. $\bar L_x$ is self-adjoint exactly when $x = x^{\dagger}$;
2. $\bar L_x$ is normal exactly when $xx^{\dagger} = x^{\dagger}x$;
3. $\bar L_x$ is unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is a unitary element of the algebra;
4. $\bar L_x$ is positive exactly when $x$ lies in the positive cone of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** Self-adjointness is $\bar L_x = \bar L_{x^{\dagger}}$ with the left representation faithful; normality is $\bar L_x\bar L_x^{*} = \bar L_{xx^{\dagger}}$ against $\bar L_x^{*}\bar L_x = \bar L_{x^{\dagger}x}$; unitarity adds the two equations of the normal case with the value $\mathrm{id}$; positivity is $\langle L_xy,y\rangle = \langle xy,y\rangle\geq0$ for all $y$, which is the definition of the positive cone.

**Corollary (unitary left multiplications form a group).** The unitary elements of $A$ form a group and the map $x\mapsto\bar L_x$ is a homomorphism of that group into the unitary group of $H$, with inverse $x\mapsto x^{\dagger}$.

**Proof.** $(xy)^{\dagger}(xy) = y^{\dagger}x^{\dagger}xy = 1$ for unitary $x,y$; multiplicativity of the left representation.

**Proposition (the modular flow on the left multiplications).** The modular group acts by

$$
\Delta^{it}\,\bar L_x\,\Delta^{-it} = \bar L_{\sigma_t(x)} , \qquad \sigma_t(x) = \Delta^{it}x\Delta^{-it} ,
$$

so the modular automorphism of the algebra is the conjugation of the left multiplication by the modular operator.

**Proof.** The modular group is implemented by unitaries of the standard form; the conjugation of a left multiplication is the left multiplication by the conjugated element, by *The Modular Operator and Tomita-Takesaki Theory*.

**Remark (what the adjoint alone cannot see).** The adjoint of the left multiplication sees the involution, hence the real form, and it sees the modular operator through $S$; it does not see the *boundedness* of the involution, which is a property of the form and is decided by whether $\Delta = \mathrm{id}$. The unbounded aspects of the modular operator, its domain and its spectral theory, are deferred with the modular operator itself to *The Modular Operator and Tomita-Takesaki Theory* and to the analysis of *Analysis on Linear Spaces* (Part III).

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ with the standard form, $L_g^{*} = L_{g^{-1}}$, the Tomita operator is $S(g\xi) = g^{-1}\xi$, and the form is tracial, so $\Delta = \mathrm{id}$ and $S = J$ is a bounded antiunitary involution with $J\bar L_gJ = \bar R_{g^{-1}}$.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\bar L_a^{*} = \bar L_{a^{*}}$ with $a^{*}$ the conjugate transpose, the Tomita operator is $S(a\xi) = a^{*}\xi$ extended, the polar decomposition is $S = J$ with $\Delta = \mathrm{id}$, and every left multiplication is normal.

### A Non-Tracial Case

For the group von Neumann algebra of an infinite non-abelian group with a non-tracial vector state, the Tomita operator is unbounded, $\Delta\neq\mathrm{id}$, and the adjoint of the left multiplication is the $\Delta$-twisted right multiplication; this is the case in which the three descriptions — involution, adjoint, modular operator — visibly differ.

## Summary

The adjoint of the **left multiplication** of a Hilbert algebra is the left multiplication by the involution, $\bar L_x^{*} = \bar L_{x^{\dagger}}$, and it is computed at the cyclic vector by $\bar L_x^{*}\xi = \iota(x^{\dagger})$; the adjoint axiom is exactly this identity, so the form determines the involution and conversely. The **Tomita operator** $S(x\xi) = x^{\dagger}\xi$ is the closure of the involution, it is antilinear with $S^{2} = \mathrm{id}$ on its domain, it exchanges the sides through $SL_xS = R_{x^{\dagger}}$, and it converts an adjoint into a conjugation of the other side, $L_x^{*} = SR_xS$. Its **polar decomposition** $\bar S = J\Delta^{1/2}$ produces the modular conjugation $J$, the modular operator $\Delta = \bar S^{*}\bar S$, the inversion $J\Delta J = \Delta^{-1}$ and the modular group, so the adjoint of the left multiplication already carries the modular structure and the deviation of the form from being tracial is exactly $\Delta\neq\mathrm{id}$. The **criteria** are: $\bar L_x$ self-adjoint exactly when $x = x^{\dagger}$, normal exactly when $xx^{\dagger} = x^{\dagger}x$, unitary exactly when $x$ is a unitary element, positive exactly when $x$ is in the positive cone; the modular group acts by $\Delta^{it}\bar L_x\Delta^{-it} = \bar L_{\sigma_t(x)}$. The involution and the adjoint axiom are *Hermitian Adjoints on a Hilbert Algebra*, the two-sided adjoint identities are *The Adjoint of the Left and the Right Multiplication*, the modular objects are *The Modular Operator and Tomita-Takesaki Theory*, and the unbounded spectral theory is deferred to Part III with *Analysis on Linear Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_x(y) = xy$, $\bar L_x$ | Left multiplication and its extension to $H$ |
| $\bar L_x^{*} = \bar L_{x^{\dagger}}$ | The adjoint |
| $\bar L_x^{*}\xi = \iota(x^{\dagger})$ | The adjoint at the cyclic vector |
| $S(x\xi) = x^{\dagger}\xi$ | The Tomita operator |
| $S^{2} = \mathrm{id}$, $SL_xS = R_{x^{\dagger}}$ | Involutivity and the exchange of sides |
| $L_x^{*} = SR_xS$ | Adjoint as a conjugation of the right multiplication |
| $\bar S = J\Delta^{1/2}$ | Polar decomposition |
| $\Delta = \bar S^{*}\bar S$, $J\Delta J = \Delta^{-1}$ | Modular operator and conjugation |
| $x = x^{\dagger}$, $xx^{\dagger} = x^{\dagger}x$, $x^{\dagger}x = 1$ | Self-adjoint, normal, unitary criteria |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hilbert algebras, the left multiplication and its adjoint.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the Tomita operator of a Hilbert algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the polar decomposition of the Tomita operator.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular operator from the involution.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the modular group.
