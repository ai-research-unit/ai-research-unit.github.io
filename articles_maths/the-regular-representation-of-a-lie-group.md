
# __The Regular Representation of a Lie Group__

## Introduction

A Lie group acts on the space of functions on itself in two ways, by the left and by the right translations, and the two actions commute; the pair of them is the **regular representation** of the group, and its infinitesimal form is the representation of the Lie algebra by the left- and right-invariant vector fields, which extends to the universal enveloping algebra. The left regular representation is the one whose derived representation is injective on the algebra, and the bi-invariant operators — the elements of the centre of the enveloping algebra — are exactly the operators that commute with both actions. The decomposition of the regular representation is the harmonic analysis of the group, and the two-sided action is the model of every operator built from the product.

This article treats the regular representation of a Lie group: the two translation actions and their commutation, the derived representation of the Lie algebra and its extension to the enveloping algebra, the two-sided action and the group algebra, and the compact case with the Peter--Weyl decomposition. It is the fourth article of the `- Operator Theory` group of the category; the invariant differential operators and their identification with the enveloping algebra are from *Operators on a Lie Group*, the exponential map is *The Exponential Map as an Operator*, and the unitary structure and the decomposition are *Unitary Representations of a Lie Group* and *Harmonic Analysis on Groups*, the latter written and cited for the analysis.

The article assumes the Lie group and its smooth structure from *Lie Groups*, the left- and right-invariant vector fields and the exponential from *The Lie Algebra and the Exponential Map*, the universal enveloping algebra from *Universal Enveloping Algebras*, and the Haar integral from *Locally Compact Groups and Haar Measure*. It uses the group algebra $k[G]$ of a topological group only by name, for the comparison with the enveloping algebra; the $L^2$ theory, the irreducible decomposition and the Plancherel measure belong to *Unitary Representations of a Lie Group* and to *Harmonic Analysis on Groups*, and are named here and not developed.

## The Two Translation Actions

### The Actions on Functions

**Definition.** The **left regular representation** and the **right regular representation** of $G$ are the actions on the algebra $C^\infty(G)$ of smooth functions given by

$$
(L_gf)(x) = f(g^{-1}x), \qquad (R_gf)(x) = f(xg) \qquad (g,x\in G) .
$$

The **two-sided action** is the homomorphism $G\times G \to \operatorname{Aut}(C^\infty(G))$, $(g,h)\mapsto L_gR_h$.

**Proposition.** Each of the two actions is an action of $G$ by algebra automorphisms of $C^\infty(G)$, the two actions commute, and the two-sided action has kernel the anti-diagonal copy of the centre of $G$.

*Proof.* Pullback along a diffeomorphism is an algebra automorphism, and $L_{gh} = L_gL_h$, $R_{gh} = R_gR_h$; the commutation is $(L_gR_hf)(x) = f(g^{-1}xh) = (R_hL_gf)(x)$. The kernel is the set of $(g,h)$ with $L_gR_h = \mathrm{id}$, which acts on functions by $f(g^{-1}xh) = f(x)$ for all $f$, hence $g^{-1}xh = x$ for all $x$, so $h = g^{-1}$ and $g$ is central; this is the anti-diagonal copy of the centre.

### The Derived Representation

**Definition.** The **derived representation** of the Lie algebra is the linear map

$$
\mathrm{G} \longrightarrow \operatorname{End}_\mathbb{C}(C^\infty(G)), \qquad X \longmapsto \tilde X ,
$$

sending $X$ to the left-invariant vector field $\tilde X$ of *Operators on a Lie Group*; it is a representation of the Lie algebra by derivations of $C^\infty(G)$, $[\tilde X, \tilde Y] = \widetilde{[X,Y]}$.

**Theorem (the derived representation is the derivative of the regular representation).** For $X \in \mathrm{G}$ and $f \in C^\infty(G)$,

$$
\tilde X f = \frac{d}{dt}\Big|_{t=0} L_{\exp(tX)}f .
$$

Hence the derived representation of the left regular representation is the representation by the left-invariant fields, and the right regular representation has the derived representation $X \mapsto -\tilde X^{R}$, where $\tilde X^{R}$ is the right-invariant field equal to $X$ at the identity.

*Proof.* The value is $\frac{d}{dt}\big|_{t=0} f(\exp(-tX)x)$, which is the definition of the left-invariant field. The right statement is the same computation with $R_{\exp(tX)}$ and the right-trivialisation, the sign being that of the inverse in the flow.

### The Extension to the Enveloping Algebra

**Theorem.** The derived representation extends to an algebra homomorphism

$$
U(\mathrm{G}) \longrightarrow \operatorname{End}_\mathbb{C}(C^\infty(G)), \qquad X_1 \cdots X_k \longmapsto \tilde X_1 \cdots \tilde X_k ,
$$

whose image is the algebra $D_L(G)$ of left-invariant differential operators; it is injective, and its image on the right-invariant side is the opposite algebra $D_R(G)$.

*Proof.* This is the universal property of the enveloping algebra applied to the Lie algebra homomorphism $X \mapsto \tilde X$, together with the isomorphism $U(\mathrm{G}) \cong D_L(G)$ of *Operators on a Lie Group*. The right-invariant side is the same statement with the opposite multiplication, since the right-invariant fields compose in the reverse order.

**Corollary (the derived representations commute).** For all $u, v \in U(\mathrm{G})$ and the corresponding left- and right-invariant operators $\tilde u \in D_L(G)$, $\tilde v \in D_R(G)$, one has $\tilde u\tilde v = \tilde v\tilde u$.

*Proof.* The left and right translations of the group commute and generate the two actions, so their differential operators commute; equivalently, the two-sided action differentiates to two commuting representations of the algebra and of its opposite.

## The Two-Sided Action and the Group Algebra

### The Two-Sided Action on Functions

**Definition.** The **two-sided action** of $U(\mathrm{G})\otimes U(\mathrm{G})$ on $C^\infty(G)$ is the extension of $(X,Y)\mapsto \tilde X - \tilde Y^{R}$, sending $u\otimes v$ to the operator $\tilde u\,\tilde v^{R}$; it is an algebra homomorphism from $U(\mathrm{G})\otimes U(\mathrm{G})$ to $\operatorname{End}_\mathbb{C}(C^\infty(G))$.

**Theorem (the bi-invariant operators are the invariants).** An operator $D \in \operatorname{End}_\mathbb{C}(C^\infty(G))$ commutes with every left and every right translation if and only if it lies in the image of the centre $Z(U(\mathrm{G}))$,

$$
D_L(G)\cap D_R(G) = \tilde Z(U(\mathrm{G})) .
$$

*Proof.* This is the identification of the bi-invariant differential operators with the centre of the enveloping algebra from *Operators on a Lie Group*, restated as the statement that the operators fixed by the two-sided action are the elements of the centre. An operator commuting with all translations is in particular left-invariant and right-invariant, hence bi-invariant; the converse is the centrality.

### The Comparison with the Group Algebra

**Proposition.** The group algebra $k[G]$ acts on functions by convolution, $f\mapsto f*h$ for $h\in k[G]$, and this action commutes with the left translations; the enveloping algebra acts on functions by the left-invariant differential operators $\tilde u$, and the two actions are related by the fact that the distribution supported at $e$ corresponding to $u$ is the limit of the group algebra elements approaching the identity. The enveloping algebra is not a subalgebra of the group algebra: it is the algebra of the distributions supported at the identity, by *Operators on a Lie Group*.

*Proof.* The convolution action and its commutation with the left translations are the convolution theorem of *Operators on a Lie Group*; the distribution realisation of the enveloping algebra is the same theorem, read for the distributions supported at the identity rather than for the smooth functions.

## The Compact Case

### The Peter--Weyl Decomposition

**Theorem (Peter--Weyl).** Let $G$ be compact. The left regular representation on $L^2(G)$ decomposes as the Hilbert direct sum

$$
L^2(G) = \bigoplus_{\pi\in\widehat{G}} V_\pi\otimes V_\pi^{*},
$$

over the set $\widehat{G}$ of equivalence classes of irreducible unitary representations, each occurring with multiplicity its dimension; the matrix coefficients $\pi\mapsto \langle \pi(g)v,w\rangle$ span a dense subspace. The decomposition is stated and proved in *Unitary Representations of a Lie Group* and in *Harmonic Analysis on Groups*; the operator-theoretic content is that the regular representation is the direct integral of the irreducible unitary representations.

*Proof (statement).* The proof is by the spectral theorem for the compact self-adjoint convolution operators, which is the analysis of *Harmonic Analysis on Groups*; the operator layer uses only the decomposition, and the Casimir operator of *The Casimir Operator of a Lie Group* acts on each summand by the scalar attached to $\pi$.

**Theorem (the Casimir on the regular representation).** On a compact semisimple group the Casimir operator of *The Casimir Operator of a Lie Group* is the Laplacian of a bi-invariant metric, its eigenspaces are the irreducible summands of the Peter--Weyl decomposition, and its eigenvalue on the summand of highest weight $\lambda$ is the quadratic invariant $\langle\lambda,\lambda+2\varrho\rangle$.

*Proof.* The Casimir is central, hence bi-invariant, hence acts on each irreducible summand by a scalar by Schur's lemma; the scalar is computed in *The Casimir Operator of a Lie Group*, and the identification with the Laplacian of a bi-invariant metric is the same article. The analytic consequences — the heat kernel, the Weyl character formula and the asymptotics — are the subject of *Harmonic Analysis on Groups*.

## Examples

### The Additive Group

Let $G = \mathbb{R}^n$. The left and right translations coincide with the translations of the vector space, $L_gf(x) = f(x-g) = R_{-g}f(x)$, the derived representation is $X\mapsto X\cdot\nabla$, and the enveloping algebra is the algebra of constant coefficient differential operators; the Fourier transform diagonalises the regular representation, and the decomposition is the direct integral over $\mathbb{R}^n$ of the characters, the Plancherel theorem of *Harmonic Analysis on Groups*.

### A Compact Group

Let $G = SU(2)$. The irreducible unitary representations are the symmetric powers of the defining representation, the regular representation is the Hilbert sum of the $\pi_n$ with multiplicity $n+1$, and the Casimir operator acts by the scalar $-\frac14 n(n+2)$ in a standard normalisation; the analysis is the classical theory of the spherical harmonics on the three-sphere, and the operators of the group are the bi-invariant differential operators in the Casimir element.

### A Nilpotent Group

Let $G$ be the Heisenberg group with its three-dimensional nilpotent algebra. The regular representation is not of finite type, its decomposition is by the unitary characters of the centre, and the derived representation of the algebra is faithful; the correspondence between the orbits of the coadjoint action and the irreducible unitary representations is *Unitary Representations and the Orbit Method*, below in the category.

## Summary

The left and right regular representations of a Lie group are the actions on smooth functions by $L_gf(x) = f(g^{-1}x)$ and $R_gf(x) = f(xg)$; they are actions by algebra automorphisms, they commute, and the kernel of the two-sided action is the anti-diagonal copy of the centre. The derived representation of the Lie algebra is by the left-invariant fields, $X \mapsto \tilde X$, it is the derivative of the left regular representation, and it extends to an injective algebra homomorphism $U(\mathrm{G}) \to D_L(G)$ from the universal enveloping algebra onto the left-invariant differential operators; the right-invariant operators are the same statement with the opposite multiplication, and they commute with the left-invariant ones. The operators commuting with both actions are exactly the image of the centre $Z(U(\mathrm{G}))$, that is the bi-invariant operators; the group algebra acts by convolution and commutes with the left translations, while the enveloping algebra is realised as the distributions supported at the identity. On a compact group the Peter--Weyl theorem decomposes the regular representation into the irreducible unitary representations with multiplicity their dimension, and the Casimir operator, which is the Laplacian of a bi-invariant metric, acts on each summand by its quadratic invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_gf(x) = f(g^{-1}x)$ | the left regular representation |
| $R_gf(x) = f(xg)$ | the right regular representation |
| $L_gR_h$ | the two-sided action, with kernel the anti-diagonal centre |
| $\tilde X$ | the left-invariant field, the derived representation of $X$ |
| $U(\mathrm{G}) \to D_L(G)$ | the extension to the enveloping algebra, injective |
| $\tilde v^{R}$ | the right-invariant operator attached to $v$ |
| $\tilde u\tilde v^{R} = \tilde v^{R}\tilde u$ | commutation of the two derived representations |
| $\tilde Z(U(\mathrm{G}))$ | the operators commuting with both actions |
| $k[G]$ | the group algebra, acting by convolution |
| $\bigoplus_\pi V_\pi\otimes V_\pi^{*}$ | the Peter--Weyl decomposition for compact $G$ |
| $\langle\lambda,\lambda+2\varrho\rangle$ | the Casimir eigenvalue on a summand |

## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the regular representation, the convolution algebra and the Peter--Weyl theorem.
- Sigurdur Helgason, *Groups and Geometric Analysis* (American Mathematical Society, 2000), for the derived representation, the invariant operators and the decomposition.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the regular representation, the Casimir operator and the Plancherel theory.
- Jean Dieudonné, *Treatise on Analysis*, Volume 5 (Academic Press, 1977), for the regular representation of a Lie group and its derived representation.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the two-sided action, the enveloping algebra and the distributions.
