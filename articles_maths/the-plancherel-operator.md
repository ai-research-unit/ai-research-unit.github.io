
# __The Plancherel Operator__

## Introduction

The Plancherel theorem is an identity of integrals; its operator form is the statement that the transform which produces the integrals is a single unitary operator between two Hilbert spaces. This article develops that operator: the **Plancherel operator** $\mathcal{F}$, defined on $L^2(G)$ and taking values in the direct integral of Hilbert–Schmidt fibres over the unitary dual, its unitarity and its inverse, the way it intertwines the left and the right regular representations with the field of representations, and its decomposable, measurable-field structure. The theorem and the measure are assumed; the object constructed here is the operator.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution and its completion from *The Convolution Algebra $L^1(G)$*; the characters, Pontryagin duality and the abelian transform from *Harmonic Analysis on Groups*; the unitary dual, the operator-valued transform, the direct integral, the Plancherel measure and the group von Neumann algebra from *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*, the latter owning the theorem, the measure and its construction; the regular representations and the completions from *Convolution on a Group* and *The Group Algebra as an Algebra of Operators*; and the Hilbert spaces, direct integrals and measurable fields from *Operator Algebras*. The abelian specialisation is the Fourier operator of *The Fourier Operator*, written in parallel in this Part; the adjoint of a Plancherel-side operator belongs to the `- * Operator Theory` group of this category; the convolution operators are *Convolution on a Group*.

Throughout, $G$ is a second countable unimodular group of type I with left Haar measure $dx$, unitary dual $\operatorname{Irr}(G)$, representation spaces $\mathcal{H}_\pi$ and Plancherel measure $\mu_P$; the fibres are the Hilbert–Schmidt spaces $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ with inner product $\langle A,B\rangle = \operatorname{Tr}(AB^*)$; the transform on $L^1(G)\cap L^2(G)$ is $\hat f(\pi) = \int_G f(x)\pi(x)\,dx$; and the **direct integral** is

$$
\mathcal{H}_P = \int_{\operatorname{Irr}(G)}^{\oplus}\bigl(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*\bigr)\,d\mu_P(\pi) .
$$

The Plancherel measure, its uniqueness and the isomorphism $L(G)\cong\int^\oplus B(\mathcal{H}_\pi)\,d\mu_P$ are those of *The Plancherel Theorem* and *Noncommutative Harmonic Analysis*.

## The Plancherel Operator

**Definition.** On the dense subspace $L^1(G)\cap L^2(G)$ the **Plancherel operator** is

$$
\mathcal{F} : L^2(G) \longrightarrow \mathcal{H}_P, \qquad (\mathcal{F}f)(\pi) = \hat f(\pi) = \int_G f(x)\,\pi(x)\,dx ,
$$

the field of Hilbert–Schmidt operators on the fibres; it is extended to $L^2(G)$ by continuity.

**Theorem (unitarity).** The transform $\mathcal{F}$ is isometric on $L^1(G)\cap L^2(G)$,

$$
\int_{\operatorname{Irr}(G)}\bigl\|\hat f(\pi)\bigr\|_{\mathrm{HS}}^2\,d\mu_P(\pi) = \int_G |f(x)|^2\,dx ,
$$

and it extends to a surjective isometry, hence a unitary operator, $\mathcal{F} : L^2(G)\to\mathcal{H}_P$; consequently $\|\mathcal{F}\| = \|\mathcal{F}^{-1}\| = 1$ and $\mathcal{F}$ is invertible.

**Proof.** The isometry is the Plancherel theorem of *The Plancherel Theorem*; an isometry from a dense subspace of a Hilbert space extends to the whole space with the same norm, and the image is dense because it contains the finite-rank fields supported on compact subsets of the dual, which are total in $\mathcal{H}_P$; a surjective isometry of Hilbert spaces is unitary and has an isometric inverse. $\square$

**Proposition (the fibre is Hilbert–Schmidt).** For $\mu_P$-almost every $\pi$ the operator $\hat f(\pi)$ is Hilbert–Schmidt, the field $\pi\mapsto\hat f(\pi)$ is measurable, and the squared norm of the field is the integral of the squared Hilbert–Schmidt norms; the transform is thus an operator whose values are the trace-class-friendly operators on the representation spaces.

**Proof.** The Hilbert–Schmidt property $\mu_P$-almost everywhere and the measurability are part of the Plancherel theorem's construction of the measure on the coefficient algebra; the norm statement is the isometry above. $\square$

**Remark (the abelian reading).** If $G$ is abelian then every $\mathcal{H}_\pi = \mathbb{C}$, the fibre $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^* = \mathbb{C}$, the direct integral is $L^2(G^\vee,\mu_P)$, and $\mathcal{F}$ is the classical Fourier–Plancherel operator $L^2(G)\to L^2(G^\vee)$; this is the operator studied in *The Fourier Operator*, written in parallel in this Part.

## Intertwining

**Theorem (convolution becomes multiplication).** For every $f \in L^1(G)$ the Plancherel operator intertwines left convolution with the field of its transforms,

$$
\mathcal{F}\,\lambda(f)\,\mathcal{F}^{-1} = \int_{\operatorname{Irr}(G)}^{\oplus} \hat f(\pi)\,d\mu_P(\pi) ,
$$

the field acting on the fibre $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ by left multiplication, $A\mapsto\hat f(\pi)A$; the operator $\lambda(f)$ is thereby unitarily equivalent to a decomposable operator with the fibres $\hat f(\pi)$.

**Proof.** The convolution theorem gives $(\mathcal{F}\lambda(f)h)(\pi) = \widehat{f*h}(\pi) = \hat f(\pi)\hat h(\pi) = \hat f(\pi)(\mathcal{F}h)(\pi)$, which is the displayed identity on the dense subspace and hence everywhere. $\square$

**Theorem (the regular representations become the fields).** Under $\mathcal{F}$,

$$
\mathcal{F}\,\lambda(x)\,\mathcal{F}^{-1} = \int_{\operatorname{Irr}(G)}^{\oplus} \pi(x)\otimes 1\,d\mu_P(\pi), \qquad
\mathcal{F}\,\rho(x)\,\mathcal{F}^{-1} = \int_{\operatorname{Irr}(G)}^{\oplus} 1\otimes\pi^*(x)\,d\mu_P(\pi),
$$

where the first factor acts on $\mathcal{H}_\pi$ and the second on $\mathcal{H}_\pi^*$; the two fields generate the decomposable algebra $\int^\oplus B(\mathcal{H}_\pi)\,d\mu_P(\pi)$.

**Proof.** The left regular representation corresponds to the field $\pi\otimes\pi^*$, and left convolution is the first leg, so $\lambda(x)$ acts on the first factor of the fibre while $\rho(x)$, commuting with it, acts on the second through the contragredient; the generation statement is the multiplicity-one decomposition of the regular representation, from *Noncommutative Harmonic Analysis*. $\square$

**Corollary (the group von Neumann algebra as a decomposable algebra).** The Plancherel operator carries $L(G) = \lambda(G)''$ onto the algebra of decomposable fields $\int^\oplus B(\mathcal{H}_\pi)\,d\mu_P(\pi)$, and the centre onto the diagonalisable fields $L^\infty(\operatorname{Irr}(G),\mu_P)$; the Plancherel measure is the spectral measure of the trace.

**Proof.** A von Neumann algebra is carried to its commutant-equivalent by a unitary equivalence; the identification $L(G)\cong\int^\oplus B(\mathcal{H}_\pi)\,d\mu_P$ and the description of the centre are those of *The Plancherel Theorem*, §Construction and Normalisation. $\square$

## The Inverse and the Inversion Formula

**Definition.** The **inverse Plancherel operator** is $\mathcal{F}^{-1}$, which on the field $\hat h$ is given by

$$
(\mathcal{F}^{-1}\hat h)(x) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}\bigl(\hat h(\pi)\,\pi(x)^{-1}\bigr)\,d\mu_P(\pi) ,
$$

the integral converging in $L^2(G)$ and defining the inverse transform.

**Theorem (inversion).** For $f \in L^1(G)\cap L^2(G)$ with $\pi\mapsto\operatorname{Tr}(\hat f(\pi)\pi(x)^{-1})$ integrable against $\mu_P$ for almost every $x$,

$$
f(x) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}\bigl(\hat f(\pi)\,\pi(x)^{-1}\bigr)\,d\mu_P(\pi)
$$

for almost every $x$; equivalently $\mathcal{F}^{-1}\mathcal{F} = \mathrm{id}$ and $\mathcal{F}\mathcal{F}^{-1} = \mathrm{id}$.

**Proof.** The formula is the inversion theorem of *The Plancherel Theorem*; it identifies the right-hand side with $f$ and hence with $\mathcal{F}^{-1}(\mathcal{F}f)$, which gives the two identities by the unitarity of $\mathcal{F}$. $\square$

**Proposition (the definite form as a fibre trace).** The operator trace of the transform recovers the value at the identity,

$$
f(e) = \int_{\operatorname{Irr}(G)}\operatorname{Tr}\bigl(\hat f(\pi)\bigr)\,d\mu_P(\pi) ,
$$

for $f$ in the coefficient algebra for which the integral converges absolutely, the trace being the ordinary trace on the finite-rank operators; in operator language the Plancherel isomorphism sends the evaluation functional at $e$ to the fibre-wise operator trace.

**Proof.** This is the definite form of the Plancherel theorem; the operator reading is the statement that $\operatorname{Tr}$ is the trace of the $B(\mathcal{H}_\pi)$ fibre, so that the identity is the disintegration of the trace $\tau$ of $L(G)$ along $\mu_P$. $\square$

## Decomposability and the Measurable Field

**Theorem (the operator is decomposable).** The Plancherel operator is a **decomposable** operator of the direct integral: it is measurable in the field sense, its inverse is decomposable, and for every $f \in L^1(G)$ the operator $\mathcal{F}\lambda(f)\mathcal{F}^{-1}$ has constant fibre $\hat f(\pi)$ on the diagonal of the field algebra. The fibres are the multiplication operators $\hat f(\pi)$, and their essential supremum against $\mu_P$ is the norm of the operator in the algebra.

**Proof.** A unitary equivalence onto a direct integral carries the measurable-field structure of the algebra to that of the fibres; the fibre of $\mathcal{F}\lambda(f)\mathcal{F}^{-1}$ is $\hat f(\pi)$ by the intertwining theorem, and the norm of a decomposable operator's image in the algebra of the field is the essential supremum of the fibre norms. $\square$

**Corollary (the type I condition in operator form).** The existence of the operator $\mathcal{F}$ with all fibres $B(\mathcal{H}_\pi)$ and diagonal action is exactly the type I property of $G$; for a group that is not of type I the operator exists only as a direct integral over a non-atomic space of factors and is not indexed by the unitary dual. The operator realisation of the dichotomy is that of *The Plancherel Theorem*, §Non-Unimodular and Non-Type-I Cases.

**Proof.** The equivalence of the type I property, the direct-integral decomposition of the regular representation and the existence of $\mu_P$ is the dichotomy of *The Plancherel Theorem*; the operator statement is its restatement in terms of the field algebra. $\square$

**Remark (what the article does not do).** The article has taken no adjoint: unitarity is stated as isometry and surjectivity, and the inverse is $\mathcal{F}^{-1}$, not $\mathcal{F}^*$; the equality $\mathcal{F}^* = \mathcal{F}^{-1}$ and the adjoints of the operators on the Plancherel side belong to the `- * Operator Theory` group of this category. The construction of the measure, the definite and inversion forms are *The Plancherel Theorem*, cited; the abelian operator is *The Fourier Operator*, written in parallel.

## Summary

The Plancherel operator is the transform $\mathcal{F}f(\pi) = \int_G f(x)\pi(x)dx$, taking $L^2(G)$ to the direct integral $\mathcal{H}_P = \int^\oplus(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)d\mu_P(\pi)$ of Hilbert–Schmidt fibres; it is a unitary operator, isometric on $L^1(G)\cap L^2(G)$ by the Plancherel identity $\int\|\hat f(\pi)\|_{\mathrm{HS}}^2d\mu_P = \int|f|^2dx$ and surjective because the finite-rank fields are total. Conjugation by $\mathcal{F}$ turns left convolution into the field of pointwise multiplications $\hat f(\pi)$, and turns the left and right regular representations into the two legs $\pi\otimes1$ and $1\otimes\pi^*$ of the field algebra, so that $L(G)$ becomes the decomposable algebra $\int^\oplus B(\mathcal{H}_\pi)d\mu_P$ with centre $L^\infty(\operatorname{Irr}(G),\mu_P)$. The inverse is the inversion formula $\mathcal{F}^{-1}\hat h(x) = \int\operatorname{Tr}(\hat h(\pi)\pi(x)^{-1})d\mu_P$, and the definite form $f(e) = \int\operatorname{Tr}\hat f(\pi)d\mu_P$ is the fibre-wise trace. The operator is decomposable, its fibres are the multiplication operators, and the type I property of $G$ is exactly the condition that the field algebra be indexed by $\operatorname{Irr}(G)$ with the constant multiplicity $d_\pi$. No adjoint is taken, and the measure, the theorem and the abelian specialisation are cited from *The Plancherel Theorem* and *The Fourier Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{F}$ | The Plancherel operator, $(\mathcal{F}f)(\pi) = \hat f(\pi)$ |
| $\mathcal{H}_P = \int^\oplus(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)d\mu_P$ | The direct-integral Hilbert space of fibres |
| $\langle A,B\rangle = \operatorname{Tr}(AB^*)$ | Hilbert–Schmidt inner product on a fibre |
| $\hat f(\pi) = \int_G f(x)\pi(x)\,dx$ | The operator-valued transform |
| $\int\|\hat f(\pi)\|_{\mathrm{HS}}^2\,d\mu_P = \int\lvert f\rvert^2\,dx$ | Plancherel isometry |
| $\mathcal{F}\lambda(f)\mathcal{F}^{-1} = \int^\oplus\hat f(\pi)$ | Convolution becomes multiplication |
| $\pi\otimes 1$, $1\otimes\pi^*$ | Fibres of the left and right regular representations |
| $\mathcal{F}^{-1}\hat h(x) = \int\operatorname{Tr}(\hat h(\pi)\pi(x)^{-1})\,d\mu_P$ | Inverse (inversion formula) |
| $f(e) = \int\operatorname{Tr}(\hat f(\pi))\,d\mu_P$ | Definite form as a fibre trace |
| $L(G)\cong\int^\oplus B(\mathcal{H}_\pi)\,d\mu_P$ | The group von Neumann algebra as a decomposable algebra |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the abstract Plancherel theorem, the direct-integral decomposition and measurable fields of operators.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for decomposable operators, the algebra of a direct integral and the centre of $L(G)$.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the unitary Plancherel transform and the inversion formula.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the standard form of a von Neumann algebra and the disintegration of the trace.
- Walter Rudin, *Fourier Analysis on Groups* (Wiley, 1962), for the abelian case of the Plancherel operator and its inverse.
