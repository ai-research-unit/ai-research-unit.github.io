
# __The Left and Right Regular Representation__

## Introduction

A group acts on its own $L^2$ space twice: by the left regular representation $\lambda$ and by the right regular representation $\rho$, and the whole operator theory of the group is the theory of the pair. The two are unitary, they commute, and the von Neumann algebras they generate are each other's commutant; the group algebra acts through the first, the second supplies the commutant, and the anti-linear operator $J\xi(x) = \overline{\xi(x^{-1})}$ exchanges them. This article fixes the pair, computes the commutation and the commutant relation, identifies the underlying Hilbert algebra, and describes the exchange.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$ and its involution from *The Convolution Algebra $L^1(G)$*; the convolution operators from *Convolution on a Group*; the integrated forms, the completions and the group von Neumann algebra $L(G)$ from *The Group Algebra as an Algebra of Operators*; the direct integral and the fibres $\pi\otimes\pi^*$ from *The Plancherel Operator*; the characters and Pontryagin duality from *Harmonic Analysis on Groups*; the unitary dual, the direct-integral decomposition and $L(G)$ from *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*; and the bounded operators, the von Neumann algebras, the double commutant and the standard form from *Operator Algebras*. The general left and right regular representations of a Hilbert algebra are *The Left and the Right Regular Representation*, in the Topology on Algebras slot, and are cited; the modular conjugation is the exchange of *The Modular Operator and Tomita–Takesaki Theory*, also cited. The adjoint of an operator on the group algebra belongs to the `- * Operator Theory` group of this category, and the measure algebra to *The Involution on the Measure Algebra*, later.

Throughout, $G$ is a locally compact Hausdorff group with identity $e$, left Haar measure $dx$ and modular function $\Delta$; $G$ is **unimodular** when $\Delta \equiv 1$; $L^2(G)$ carries the inner product $\langle\xi,\eta\rangle = \int_G\xi(x)\overline{\eta(x)}\,dx$; and

$$
\bigl(\lambda(x)\xi\bigr)(y) = \xi(x^{-1}y), \qquad \bigl(\rho(x)\xi\bigr)(y) = \xi(yx)
$$

are the **left** and the **right regular representation**, with integrated forms $\lambda(f) = \int_G f(x)\lambda(x)\,dx$, $\rho(f) = \int_G f(x)\rho(x)\,dx$ for $f \in L^1(G)$. The generated von Neumann algebras are

$$
\mathcal{M}_L = \lambda(G)'' = L(G), \qquad \mathcal{M}_R = \rho(G)'' ,
$$

and the modular conjugation is $J\xi(x) = \overline{\xi(x^{-1})}$.

## The Two Representations

**Theorem (unitary representations and the commutation).** The maps $\lambda$ and $\rho$ are representations of $G$,

$$
\lambda(x)\lambda(y) = \lambda(xy), \qquad \rho(x)\rho(y) = \rho(yx),
$$

they commute, $\lambda(x)\rho(y) = \rho(y)\lambda(x)$, and they are unitary on $L^2(G)$ for a unimodular group; the pair $(\lambda,\rho)$ is a unitary representation of $G\times G$. For a non-unimodular group $\rho$ is unitary for the inner product weighted by $\Delta$, and the pair is a representation of $G\times G$ with the second factor unitarily equivalent to its twist by the modular function.

**Proof.** The product laws are the associativity of the product on the arguments $y\mapsto x^{-1}y$ and $y\mapsto yx$, and the commutation is that the two translations of $\xi$ by $x$ on the left and $y$ on the right do not interfere. Unitarity of $\lambda$ is the left invariance of $dx$, and of $\rho$ the right invariance, which is $\Delta\equiv1$; the weighted form is the standard correction, recorded in *Locally Compact Groups and Haar Measure*. $\square$

**Proposition (the integrated forms).** For $f, g \in L^1(G)$,

$$
\lambda(f)\lambda(g) = \lambda(f*g), \qquad \rho(f)\rho(g) = \rho(g*f), \qquad \lambda(f)\rho(g) = \rho(g)\lambda(f),
$$

with $\|\lambda(f)\|\leq\|f\|_1$ and $\|\rho(f)\|\leq\|f\|_1$; the commutant relation $L_fR_g = R_gL_f$ of *Convolution on a Group* is the integrated form of the commutation of the representations.

**Proof.** Integrate the group product laws against $f(x)g(y)$; the bounds are the triangle inequality for the operator-valued integral; the identification with the convolutions is the agreement on $L^1(G)\cap L^2(G)$. $\square$

**Remark (the two readings of one algebra).** The left representation $\lambda$ carries the algebra into $\mathcal{M}_L$ and is a representation; the right representation $\rho$ carries it into $\mathcal{M}_R$ and reverses the product. Since $\rho(f)\rho(g) = \rho(g*f)$, the map $f\mapsto\rho(f)$ is an anti-homomorphism, the operator form of the fact that convolution by $f$ on the right is multiplication on the right; both are isometric on $L^1(G)$ and both are bounded on $L^2(G)$ by $\|f\|_1$.

## The Generated von Neumann Algebras

**Theorem (the commutant relation).** On a unimodular group the two algebras generated by the two representations are each other's commutant,

$$
\mathcal{M}_L' = \mathcal{M}_R, \qquad \mathcal{M}_R' = \mathcal{M}_L ,
$$

so that $\mathcal{M}_L = \lambda(G)'' = \rho(G)'$ and $\mathcal{M}_R = \rho(G)'' = \lambda(G)'$. The von Neumann algebra generated by both representations is $\mathcal{M}_L\vee\mathcal{M}_R$, and its centre is $\mathcal{M}_L\cap\mathcal{M}_R$.

**Proof.** The left and the right translations commute, so $\mathcal{M}_R\subseteq\mathcal{M}_L'$ and $\mathcal{M}_L\subseteq\mathcal{M}_R'$; the reverse inclusions are the standard commutant theorem for the regular representation of a unimodular group, quoted from *The Group Algebra as an Algebra of Operators* and *Noncommutative Harmonic Analysis*. The centre of a von Neumann algebra generated by two mutually commutant pieces is their intersection. $\square$

**Corollary (the algebra and its mirror).** The left picture alone determines the right picture and conversely: there is no way to give the left regular representation without giving, on the same space, the right one. The algebra $\mathcal{M}_L$ is the group von Neumann algebra, its commutant is the algebra of the right translations, and the double commutant theorem gives $\mathcal{M}_L'' = \mathcal{M}_L$ and $\mathcal{M}_R'' = \mathcal{M}_R$.

**Proof.** The identities are the theorem; the double commutant statement is von Neumann's theorem applied to each. $\square$

**Proposition (the discrete and compact readings).** If $G$ is discrete the vector $\delta_e \in L^2(G)$ is cyclic and separating for $\mathcal{M}_L$, and the vector state $\omega(T) = \langle T\delta_e,\delta_e\rangle$ is the trace; if $G$ is compact, $\mathcal{M}_L$ contains the rank-one projection onto the constants and the constants are the $\rho$-fixed vectors.

**Proof.** For discrete $G$ the translates $\lambda(G)\delta_e$ span $L^2(G)$ (cyclicity) and no nonzero $T\in\mathcal{M}_L$ annihilates $\delta_e$ (separating); the trace statement is *The Group Algebra as an Algebra of Operators*. For compact $G$ the constants are the one-dimensional trivial subrepresentation, fixed by $\rho$, and the associated projection lies in $\mathcal{M}_L$ by the commutant relation. $\square$

## The Hilbert Algebra Behind the Pair

**Definition.** The **Haar pairing** on the group algebra is $\langle f,h\rangle = \int_G f(x)\overline{h(x)}\,dx$, defined on $L^1(G)\cap L^2(G)$; it is the restriction of the $L^2(G)$ inner product to the dense intersection.

**Proposition (the group algebra is a Hilbert algebra).** With the Haar pairing and the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, the algebra $L^1(G)\cap L^2(G)$ (more precisely its completion inside $L^2(G)$) is a **Hilbert algebra** in the sense of *Hilbert Algebras*; its left regular representation is $\lambda$ and its right regular representation is $\rho$, and the commutation $\lambda(f)\rho(g) = \rho(g)\lambda(f)$ is the associativity axiom of the Hilbert algebra.

**Proof.** The involution and the pairing satisfy $\langle f*h,k\rangle = \langle h,f^* * k\rangle$, which is the adjoint axiom of a Hilbert algebra: it is the computation $\iint f(y)h(y^{-1}x)\overline{k(x)}\,dy\,dx = \int h(z)\overline{(f^**k)(z)}\,dz$ using the substitution $x = yz$ and the definition of $f^*$; associativity of convolution gives the remaining axiom. The identification of the two regular representations is by construction. $\square$

**Remark (the general theory is a sibling).** The general left and right regular representations of a Hilbert algebra, their adjoint compatibility $L_{x^\dagger} = L_x^*$, $R_{x^\dagger} = R_x^*$ and the production of the algebra and commutant are *The Left and the Right Regular Representation*, in the Topology on Algebras slot; the present article supplies the group instance and does not repeat that theory. The adjoint of the operators $\lambda(f)$, $\rho(f)$ is not taken here; the equality $\lambda(f^*) = \lambda(f)^*$ belongs to the `- * Operator Theory` group.

## The Modular Conjugation

**Definition.** The **modular conjugation** of $L^2(G)$ is the anti-linear isometry

$$
J : L^2(G)\to L^2(G), \qquad (J\xi)(x) = \overline{\xi(x^{-1})},
$$

which is defined for every locally compact group and is an involution, $J^2 = \mathrm{id}$, with $J$ isometric.

**Theorem (the exchange of the two pictures).** On a unimodular group $J$ conjugates the left regular representation into the right,

$$
J\,\lambda(x)\,J = \rho(x), \qquad J\,\rho(x)\,J = \lambda(x) \qquad (x \in G),
$$

and consequently $J\,\mathcal{M}_L\,J = \mathcal{M}_R$ and $J\,\mathcal{M}_R\,J = \mathcal{M}_L$; the conjugation exchanges the algebra and its commutant and is the group instance of the modular conjugation of the standard form.

**Proof.** Compute $(J\lambda(x)J\xi)(y)$: one has $(J\xi)(z) = \overline{\xi(z^{-1})}$, hence $(\lambda(x)J\xi)(z) = \overline{\xi(z^{-1}x)}$, and evaluating at $z = y^{-1}$ and conjugating gives $\xi(yx) = (\rho(x)\xi)(y)$. The second identity is the first with $x$ replaced by $x^{-1}$; the exchange of the algebras follows from the exchange of the generators. $\square$

**Corollary (the exchange is the operator form of inversion).** For $f \in L^1(G)$,

$$
J\,\lambda(f)\,J = \rho(\overline{f}), \qquad J\,\rho(f)\,J = \lambda(\overline{f}),
$$

where $\overline{f}(x) = \overline{f(x)}$; on a unimodular group $\overline{f} = f^*\circ\iota$, that is $\overline{f(x)} = f^*(x^{-1})$, so the conjugation intertwines the two representations through the involution read under inversion.

**Proof.** Integrate the group identity $J\lambda(x)J = \rho(x)$ against $f(x)\,dx$, using that $J$ is anti-linear and isometric: $J\lambda(f)J = \int\overline{f(x)}\rho(x)\,dx = \rho(\overline{f})$. The second identity is the first with the roles exchanged. On a unimodular group $\overline{f(x)} = f^*(x^{-1})$ by the definition of $f^*$; the reading of $f^*$ as the adjoint of $\lambda(f)$ is left to the `- * Operator Theory` group. $\square$

**Remark (the non-unimodular case).** For a non-unimodular group the modular conjugation is not of this simple form: the Tomita–Takesaki modular operator $\nabla$ enters, the left and right representations are related by the modular flow, and the standard form is the one of the modular theory of *Operator Algebras*; the article records only that the pair $(\mathcal{M}_L,\mathcal{M}_R)$ is the general standard-form pair, with the group's modular function supplying the modular operator.

## Summary

The left and the right regular representations $\lambda(x)\xi(y) = \xi(x^{-1}y)$ and $\rho(x)\xi(y) = \xi(yx)$ are representations of $G$ on $L^2(G)$ that commute and combine into a representation of $G\times G$; on a unimodular group both are unitary, and in general the second is unitary for the inner product weighted by the modular function. Their integrated forms satisfy $\lambda(f)\lambda(g) = \lambda(f*g)$, $\rho(f)\rho(g) = \rho(g*f)$ and $\lambda(f)\rho(g) = \rho(g)\lambda(f)$, the second being an anti-homomorphism; the generated von Neumann algebras $\mathcal{M}_L = \lambda(G)'' = L(G)$ and $\mathcal{M}_R = \rho(G)''$ are each other's commutant on a unimodular group, so the left picture determines the right, and the algebra generated by both has centre $\mathcal{M}_L\cap\mathcal{M}_R$. The Haar pairing and the involution make $L^1(G)\cap L^2(G)$ a Hilbert algebra whose left and right regular representations are precisely $\lambda$ and $\rho$, which is the group instance of the general theory of *The Left and the Right Regular Representation*. The modular conjugation $J\xi(x) = \overline{\xi(x^{-1})}$ is an anti-linear involution exchanging the two pictures, $J\lambda(x)J = \rho(x)$, and it exchanges the algebra and its commutant; for a non-unimodular group it is replaced by the modular conjugation of the Tomita–Takesaki theory. No adjoint of an operator on the group algebra is taken; the equality $\lambda(f^*) = \lambda(f)^*$ and the measure algebra are the `- *` groups of this category and *The Involution on the Measure Algebra*, later.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda(x)$, $\rho(x)$ | Left and right regular representations on $L^2(G)$ |
| $\lambda(f)$, $\rho(f)$ | Integrated forms, $f\in L^1(G)$ |
| $\lambda(x)\rho(y) = \rho(y)\lambda(x)$ | The two representations commute |
| $\mathcal{M}_L = \lambda(G)'' = L(G)$ | The von Neumann algebra of the left translations |
| $\mathcal{M}_R = \rho(G)''$ | The von Neumann algebra of the right translations |
| $\mathcal{M}_L' = \mathcal{M}_R$, $\mathcal{M}_R' = \mathcal{M}_L$ | The commutant relation, unimodular $G$ |
| $\langle f,h\rangle = \int_G f\overline{h}\,dx$ | The Haar pairing |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | The involution of the Hilbert algebra |
| $J\xi(x) = \overline{\xi(x^{-1})}$ | Modular conjugation, $J^2 = \mathrm{id}$ |
| $J\lambda(x)J = \rho(x)$ | The exchange of the two pictures |
| $\pi\otimes\pi^*$ | The Plancherel fibre of the regular representation |

## Further Reading

- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the commutant of the regular representation, the standard form and the Hilbert algebra of a group.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the Tomita–Takesaki modular theory and the modular conjugation.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the left and right regular representations and the commutant theorem.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the regular representations of a locally compact group.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the modular function of a non-unimodular group and the modular flow it defines.
