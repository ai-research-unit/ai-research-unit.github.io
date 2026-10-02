# __The Indefinite Modular Operator__

## Introduction

For a von Neumann algebra on a Hilbert space with a cyclic and separating vector $\xi$, the Tomita operator $S$ is defined by $S(x\xi) = x^{\dagger}\xi$; it is antilinear, densely defined and closable, and its polar decomposition $S = \jmath\Delta^{1/2}$ produces the two objects of the whole theory: the **modular operator** $\Delta = S^{*}S$, self-adjoint and positive, and the **modular conjugation** $\jmath$, antilinear and involutive. The entire construction rests on the definiteness of the inner product, through the closure of $S$ and through the positivity of $\Delta$.

On a Krein space the same formula defines the same antilinear operator, but its properties change. The adjoint in the polar decomposition is now the indefinite one, so what is obtained is a **$J$-modular operator** $\Delta$ that is positive for the definite form of the fundamental symmetry $J$ and self-adjoint for the indefinite one, and a **$J$-modular conjugation** $\jmath$ that is $J$-unitary and commutes with $J$. The two objects therefore carry $J$ with them: the modular data of an indefinite algebra is $J$-twisted, and the classical theory is the case $J = \mathrm{id}$.

What must be added is a condition: on a Krein space the Tomita operator need not be closable, so the polar decomposition need not exist. The hypotheses that make it exist are that $\xi$ be **$J$-cyclic** for the algebra and **$J$-separating** for it, together with the availability of a self-dual cone carried by $\xi$; then $S$ has a closure and the closure factorises. This article fixes the operator $S$, the $J$-cyclic and $J$-separating hypotheses, the polar decomposition into the $J$-modular operator and the $J$-modular conjugation, and the properties that the two inherit.

The Krein space, the form and the operator $J$ are *Krein Spaces* and *The Fundamental Symmetry*; the algebra is *Krein–von Neumann Algebras*; the indefinite representation that produces the algebra is *The Indefinite GNS Construction*; the theorem that uses the modular data is *Krein–Tomita–Takesaki Theory*; the definite construction is *The Modular Operator and Tomita-Takesaki Theory*. Those are cited. The Krein space is $K$ with form $[\cdot,\cdot]$ and fundamental symmetry $J$, the algebra is $\mathcal{M}$, and the vector is $\xi$.

## The Tomita Operator for a Krein Space

**Definition.** Let $\mathcal{M}$ be a Krein–von Neumann algebra on $K$ and $\xi\in K$. The **Tomita operator** is the antilinear operator

$$
S : \mathcal{M}\xi\to K, \qquad S(x\xi) = x^{\dagger}\xi ,
$$

with domain the linear span of the orbit $\mathcal{M}\xi$.

**Proposition (well-definedness and involution).** $S$ is well defined: if $x\xi = 0$ then $x^{\dagger}\xi = 0$ exactly when $\xi$ is separating for $\mathcal{M}$. On its domain $S$ is an involution, $S^{2} = \mathrm{id}$, and hence bijective onto its image.

**Proof.** If $S$ were ambiguous there would be $x$ with $x\xi = 0$ and $x^{\dagger}\xi\neq0$; the separating hypothesis excludes this, and then $S^{2}(x\xi) = S(x^{\dagger}\xi) = (x^{\dagger})^{\dagger}\xi = x\xi$.

**Definition.** The vector $\xi$ is **$J$-cyclic** for $\mathcal{M}$ when the orbit $\mathcal{M}\xi$ is dense in $K$, and **$J$-separating** when $x\xi = 0$ with $x\in\mathcal{M}$ forces $x = 0$. Cyclicity is density of the domain of $S$ and separatingness is well-definedness of $S$; note that separatingness cannot be read off the orbit, since $\mathcal{M}$ is closed under $\dagger$ and so $\mathcal{M}^{\dagger}\xi = \mathcal{M}\xi$.

**Proposition (what changes in the indefinite case).** For a Hilbert space the operator $S$ is closed (indeed $S^{**} = S$), and this is the Cauchy–Schwarz inequality in disguise. For a Krein space $S$ need not be closed, and it need not be the case that $S^{**} = S$; the graph of $S$ may fail to be a graph of a closed operator.

**Proof.** In the definite case $S$ is an isometry of the norm, $\|x\xi\| = \|x^{\dagger}\xi\|$, and that identity is exactly the Cauchy–Schwarz inequality applied to the positive definite form, so the closed graph argument goes through. In the indefinite case the identity becomes $[x\xi,x\xi] = [x^{\dagger}\xi,x^{\dagger}\xi]$, which holds but bounds neither side, since the form is indefinite; the closed graph argument has nothing to stand on and $S$ need not be closed.

**Remark (the missing inequality).** The whole difference is a single missing inequality: an indefinite form does not bound the norm of a vector by the norm of its image under $S$. All the extra hypotheses of the next section are devices that supply a substitute bound.

## The Polar Decomposition and the $J$-Modular Pair

**Definition.** The vector $\xi$ is **modular** for the pair $(\mathcal{M},J)$ when it is $J$-cyclic and $J$-separating and the Tomita operator $S$ has a closure $\bar S$ that factorises as

$$
\bar S = \jmath\,\Delta^{1/2},
$$

with $\jmath$ an antilinear isometry of the definite form of $J$ and $\Delta$ a positive definite self-adjoint operator of that form. The operator $\Delta$ is the **$J$-modular operator** and $\jmath$ the **$J$-modular conjugation** attached to $\xi$.

**Proposition (the $J$-modular operator).** When the polar decomposition exists the $J$-modular operator is

$$
\Delta = \bar S^{\dagger}\bar S
$$

with $\dagger$ the indefinite adjoint, it is positive for the definite form $\langle\cdot,\cdot\rangle = [J\cdot,\cdot]$, self-adjoint for the indefinite form, and it commutes with $J$; its domain is the set of $u$ with $\bar Su\in\mathrm{dom}\,\bar S^{\dagger}$.

**Proof.** The polar decomposition of a closed operator gives $\bar S^{\dagger}\bar S = \Delta^{1/2}\jmath^{\dagger}\jmath\Delta^{1/2} = \Delta^{1/2}\Delta^{1/2} = \Delta$, using $\jmath^{\dagger}\jmath = \mathrm{id}$ for a $J$-unitary antilinear isometry; positivity for the definite form is the assignment of $\Delta^{1/2}$ as the positive factor; the commutation with $J$ is the commutation of the factorisation with the fundamental symmetry, which holds because $S$ is defined by the involution and the involution is $J$-compatible in a Krein algebra.

**Proposition (the $J$-modular conjugation).** With the notation of the polar decomposition, $\jmath$ is antilinear, $J$-unitary, involutive, $\jmath^{2} = \mathrm{id}$, and it commutes with the fundamental symmetry,

$$
\jmath J = J\jmath , \qquad [\jmath u,\jmath v] = \overline{[u,v]} .
$$

**Proof.** The involution $S^{2} = \mathrm{id}$ passes to the closure as $\jmath\Delta^{1/2}\jmath\Delta^{1/2} = \mathrm{id}$, and the uniqueness of the polar decomposition, together with the positivity of $\Delta$, forces $\jmath^{2} = \mathrm{id}$; the $J$-unitarity is the isometry statement of the definition, and the commutation with $J$ is the $J$-compatibility of the involution underlying $S$.

**Theorem (the modular flow is the flow of the pair).** The one-parameter family

$$
\sigma_t(x) = \Delta^{it}\,x\,\Delta^{-it}, \qquad x\in\mathcal{M},
$$

is a one-parameter group of $J$-automorphisms of $\mathcal{M}$: each $\sigma_t$ is an algebra automorphism of $\mathcal{M}$, each $\sigma_t$ is compatible with the indefinite adjoint, $\sigma_t(x^{\dagger}) = \sigma_t(x)^{\dagger}$, and $\sigma_{s+t} = \sigma_s\sigma_t$.

**Proof.** $\Delta^{it}$ is a group of definite-unitary operators commuting with $J$, and a $J$-commuting definite-unitary $U$ induces the automorphism $x\mapsto UxU^{-1} = UxU^{\dagger}$ of $\mathcal{M}$, which is compatible with the indefinite adjoint because $U^{\dagger} = JU^{*}J = U^{-1}$; the group law is that of $t\mapsto\Delta^{it}$.

## The Role of the $J$-Cyclic and $J$-Separating Conditions

**Proposition (cyclic gives density, separating gives well-definedness).** $J$-cyclicity makes $\mathcal{M}\xi$ dense and hence makes $S$ densely defined; $J$-separating makes $S$ well defined and injective. Both are needed, and neither can be dropped.

**Proof.** Density of the domain is cyclicity, well-definedness is separatingness by the first proposition of the article; a cyclic but not separating vector makes $S$ ambiguous, and a separating but not cyclic one leaves $S$ defined only on a non-dense domain, so that it has no closure to speak of.

**Proposition (the self-dual cone supplies closability).** If in addition $\xi$ carries a **self-dual cone** $C$ — a closed convex cone with $C = C^{\natural} = \{u : [u,v]\geq0 \text{ for all } v\in C\}$ — then the Tomita operator $S$ is closable, and the polar decomposition of its closure exists.

**Proof.** The self-dual cone is exactly the structure that replaces the Cauchy–Schwarz-type inequality missing in the indefinite case; it provides a positive definite form with respect to which $S$ is represented by a bounded operator and hence closable. This is the theory of *Krein–Tomita–Takesaki Theory*.

**Remark (three data, not two).** In the definite case the modular data is attached to the pair (algebra, cyclic and separating vector). In the indefinite case it is attached to the triple (algebra, $J$-cyclic and $J$-separating vector, self-dual cone), and the fundamental symmetry $J$ is carried along by each of the two objects produced. This is the precise sense in which the modular operator is *indefinite*: not that its spectrum is complex, but that it is positive for $J$ and self-adjoint for the form whose sign $J$ reverses.

## Worked Cases

### The Trivial Algebra on $\mathbb{C}^{1,1}$

Let $K = \mathbb{C}^{1,1}$, $\mathcal{M}$ the diagonal $2\times2$ matrices, $J = \mathrm{diag}(1,-1)$ and $\xi = e_1+e_2$. Then $\xi$ is $J$-cyclic, the orbit of $x = \mathrm{diag}(a,b)$ being the point $(a,b)$ and the orbit of $\mathcal{M}$ all of $K$, and it is $J$-separating, since $x\xi = 0$ means $a = b = 0$. Here $x^{\dagger} = \mathrm{diag}(\bar a,\bar b)$, so the Tomita operator is **termwise complex conjugation**,
$$
S(a e_1 + b e_2) = \bar a\,e_1 + \bar b\,e_2 ,
$$
an antilinear involution with $S^{2} = \mathrm{id}$; it satisfies $[Su,Sv] = \overline{[u,v]}$ and $\jmath J = J\jmath$ with $\jmath = S$, so it is the $J$-modular conjugation, and the polar decomposition $S = \jmath\Delta^{1/2}$ has $\Delta = \mathrm{id}$.

### A Pontryagin Space

On $\ell^{2}\oplus-\mathbb{C}$ with the algebra of diagonal operators and $\xi$ with all coordinates nonzero, the vector is $J$-cyclic and $J$-separating as soon as the self-dual cone is chosen; the $J$-modular operator is then diagonal, positive definite for $\langle\cdot,\cdot\rangle$ and self-adjoint for the form, and its $t$-th power generates the modular flow by rotating the phases of the coordinates. The choice of the cone, not the choice of $\xi$, is the extra datum.

### The Definite Case

For $J = \mathrm{id}$ the theory collapses to *The Modular Operator and Tomita-Takesaki Theory*: a cyclic and separating vector suffices, the self-dual cone is automatic (the positive cone of the Hilbert space), the $J$-modular operator is the modular operator and the $J$-modular conjugation is the modular conjugation.

## Summary

The **Tomita operator** of a Krein–von Neumann algebra $\mathcal{M}$ and a vector $\xi$ is the antilinear map $S(x\xi) = x^{\dagger}\xi$; it is well defined exactly when $\xi$ is **$J$-separating** and densely defined exactly when $\xi$ is **$J$-cyclic**, and it is involutive. In the definite case $S$ is closed and its polar decomposition gives the modular operator and the modular conjugation; in the indefinite case $S$ need not be closed, and the decomposition exists only under the additional hypothesis of a **self-dual cone**, and then reads $\bar S = \jmath\Delta^{1/2}$. The factor $\Delta$ is the **$J$-modular operator**: positive definite for the form of $J$, self-adjoint for the indefinite form, commuting with $J$, equal to $\bar S^{\dagger}\bar S$. The factor $\jmath$ is the **$J$-modular conjugation**: antilinear, $J$-unitary, involutive, commuting with $J$. The family $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$ is a one-parameter group of $J$-automorphisms of $\mathcal{M}$, and it is the modular flow whose properties — the invariance of the algebra, the identification of the commutant and the $J$-KMS condition — are the **Krein–Tomita–Takesaki theory**. The algebra is *Krein–von Neumann Algebras*, the form and $J$ are *Krein Spaces* and *The Fundamental Symmetry*, and the definite case is *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$, $S(x\xi) = x^{\dagger}\xi$ | Tomita operator, antilinear, involutive |
| $\xi$ $J$-cyclic / $J$-separating | Density of $\mathcal{M}\xi$ / well-definedness of $S$ |
| $C = C^{\natural}$ | Self-dual cone, the closability hypothesis |
| $\bar S = \jmath\Delta^{1/2}$ | Polar decomposition |
| $\Delta = \bar S^{\dagger}\bar S$ | $J$-modular operator |
| $\jmath$ | $J$-modular conjugation, $\jmath^{2} = \mathrm{id}$, $\jmath J = J\jmath$ |
| $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$ | Modular flow, a group of $J$-automorphisms |
| $J = \mathrm{id}$ | The definite case |

## Further Reading

- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the classical Tomita operator and its polar decomposition.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular operator and the modular conjugation.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the self-dual cones of a Krein space.
- Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory* (Akademie-Verlag, 1990), for the indefinite adjoint and the closability of the Tomita operator.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the operators commuting with a fundamental symmetry.
