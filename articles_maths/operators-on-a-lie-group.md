
# __Operators on a Lie Group__

## Introduction

A Lie group $G$ is a smooth manifold as well as a group, so its operator layer is richer than that of a topological group: beside the translations and the automorphisms there are the **differential operators**, and among them the ones that commute with the translations. The left-invariant differential operators form an algebra isomorphic to the universal enveloping algebra $U(\mathrm{G})$ of the Lie algebra, and the bi-invariant ones form its centre. On the other side the group carries a convolution product on its functions, and the two pictures meet in the statement that a left-invariant operator is a convolution by a distribution supported at the identity.

This article fixes the operator layer of a Lie group: the smooth operators, the invariant differential operators and their identification with $U(\mathrm{G})$, the bi-invariant operators and the Casimir operator as their first example, and the convolution algebra with the operators it defines. It is the first article of the `- Operator Theory` group of the category; the Casimir operator is *The Casimir Operator of a Lie Group*, the exponential map read as an operator is *The Exponential Map as an Operator*, and the action on functions is *The Regular Representation of a Lie Group*, all below in this group.

The article assumes the definition and the elementary structure of a Lie group from *Lie Groups*, the Lie algebra as the space of left-invariant vector fields with the commutator bracket from *The Lie Algebra and the Exponential Map*, the universal enveloping algebra and the Poincaré--Birkhoff--Witt theorem from *Universal Enveloping Algebras*, and the smooth structure of a manifold with its differential operators from *Smooth Manifolds and Differential Geometry* and *Differential Operators on a Manifold*. From the analysis of groups it assumes the convolution of continuous functions of compact support and the Haar integral of *Locally Compact Groups and Haar Measure*; the specific analysis of $L^1(G)$ and the Fourier theory are *The Convolution Algebra $L^1(G)$* and *Harmonic Analysis on Groups*, cited here and not used. No form, no norm and no distance is introduced beyond the differentiability the definitions require, and no geometry is made.

## The Smooth Operators

### The Operator Layer

**Definition.** A **smooth operator** on $G$ is a smooth map $G \to G$. The smooth operators form a monoid under composition, and its group of units is the group $\operatorname{Diff}(G)$ of diffeomorphisms of $G$ onto itself.

**Proposition.** The left and the right translations $L_g(h) = gh$ and $R_g(h) = hg$ are diffeomorphisms, the inversion $\iota$ is a diffeomorphism, and the inner automorphisms $\Psi_g = L_gR_{g^{-1}}$ are diffeomorphisms and Lie group automorphisms.

*Proof.* These are the statements of *Lie Groups*; the inverse of $L_g$ is $L_{g^{-1}}$, and the smoothness of the group operations makes each map smooth with smooth inverse.

### Operators on Functions

**Definition.** The group acts on the algebra $C^\infty(G)$ of smooth functions by

$$
(L_gf)(x) = f(g^{-1}x), \qquad (R_gf)(x) = f(xg), \qquad (\iota f)(x) = f(x^{-1}) .
$$

Each of $L_g$, $R_g$, $\iota$ is an algebra automorphism of $C^\infty(G)$, and $L_{gh} = L_gL_h$, $R_{gh} = R_gR_h$, $L_gR_h = R_hL_g$.

*Proof.* Pullback along a diffeomorphism is an algebra automorphism; the composition laws are the associativity of the product, and the commutation is $(L_gR_hf)(x) = f(g^{-1}xh) = (R_hL_gf)(x)$.

**Definition.** An operator $D \in \operatorname{End}_\mathbb{C}(C^\infty(G))$ is **left-invariant** when $D L_g = L_g D$ for every $g$, and **right-invariant** when $D R_g = R_g D$ for every $g$; it is **bi-invariant** when it is both. The left-invariant operators form the algebra

$$
D_L(G) = \{D : D L_g = L_g D \ \text{for all } g\},
$$

and the right-invariant operators form $D_R(G)$.

The letters $D_L$ record the side on which the invariance is imposed; the two-sided operators are $D_L(G) \cap D_R(G)$.

## The Invariant Differential Operators

### The First-Order Operators

**Definition.** For $X \in \mathrm{G}$ the **left-invariant vector field** determined by $X$ is the operator on $C^\infty(G)$

$$
\tilde X f = \frac{d}{dt}\Big|_{t=0} f(\exp(-tX)\,x) .
$$

It is the derivation of $C^\infty(G)$ determined by the left-invariant field of *The Lie Algebra and the Exponential Map*, and the assignment $X \mapsto \tilde X$ is an injective $\mathbb{C}$-linear map $\mathrm{G} \to D_L(G)$ with

$$
[\tilde X, \tilde Y] = \widetilde{[X,Y]} .
$$

*Proof.* The field is left-invariant by construction, the bracket identity is the naturality of the commutator of vector fields, and injectivity follows because $\tilde X$ determines $X$ from the coordinate functions at $e$.

### The Algebra of Left-Invariant Differential Operators

A **differential operator of order at most $k$** on $G$ is a $\mathbb{C}$-linear operator on $C^\infty(G)$ that in every chart is a polynomial of degree at most $k$ in the coordinate derivations; the differential operators form a filtered algebra $D(G)$ whose associated graded algebra is commutative, and the order is the degree of the top symbol. The theory of the algebra is *Differential Operators on a Manifold*, and the next theorem is its Lie-theoretic specialisation.

**Theorem (the universal enveloping algebra).** Evaluation at the identity gives an isomorphism of filtered $\mathbb{C}$-algebras

$$
U(\mathrm{G}) \ \xrightarrow{\ \sim\ }\ D_L(G), \qquad X_1 \cdots X_k \ \longmapsto\ \tilde X_1 \cdots \tilde X_k ,
$$

from the universal enveloping algebra of $\mathrm{G}$ onto the algebra of left-invariant differential operators on $G$. The inverse sends a left-invariant operator $D$ to its value at the identity, read as an element of $U(\mathrm{G})$ by the Poincaré--Birkhoff--Witt identification.

*Proof.* The assignment $X \mapsto \tilde X$ is a Lie algebra homomorphism $\mathrm{G} \to D(G)$ whose image consists of left-invariant operators, so by the universal property it extends to an algebra homomorphism $U(\mathrm{G}) \to D_L(G)$. It is injective because the images of a PBW basis are independent operators: on the coordinate functions $x^1, \ldots, x^n$ of a chart at $e$, the monomials in the $\tilde X_i$ have linearly independent symbols. It is surjective because a left-invariant differential operator is determined by its action at $e$, and that action is a polynomial in the derivations $\tilde X_i$ of bounded degree, hence an element of $U(\mathrm{G})$ by PBW.

**Corollary.** $D_L(G)$ is generated as an algebra by the first-order operators $\tilde X$, $X \in \mathrm{G}$, it is filtered by the order, and its associated graded algebra is the symmetric algebra $S(\mathrm{G})$; in particular $U(\mathrm{G})$ and $D_L(G)$ are isomorphic.

*Proof.* Generation and the filtration are the content of the theorem; the associated graded statement is the Poincaré--Birkhoff--Witt theorem.

## The Bi-Invariant Operators

### The Adjoint Action on the Enveloping Algebra

**Definition.** For $g \in G$ the **adjoint action** on $U(\mathrm{G})$ is the algebra automorphism

$$
\operatorname{Ad}_g : U(\mathrm{G}) \to U(\mathrm{G}), \qquad \operatorname{Ad}_g(X_1 \cdots X_k) = \operatorname{Ad}_gX_1 \cdots \operatorname{Ad}_gX_k ,
$$

extending the adjoint representation of $G$ on $\mathrm{G}$; its derivative at $e$ is the derivation $\operatorname{ad}_X = [X, \cdot]$ extended to $U(\mathrm{G})$.

**Theorem (the centre is the bi-invariant algebra).** The algebra $D_L(G) \cap D_R(G)$ of bi-invariant differential operators is the centre $Z(U(\mathrm{G}))$ of the universal enveloping algebra, under the isomorphism of the preceding section.

*Proof.* A bi-invariant operator is left-invariant, hence of the form $u \in U(\mathrm{G})$; the right invariance is equivalent to $\operatorname{Ad}_g u = u$ for all $g$, and since $\operatorname{Ad}_g$ is the exponential of $\operatorname{ad}$, to $\operatorname{ad}_Y u = 0$ for all $Y \in \mathrm{G}$, that is to the centrality of $u$.

### The Casimir Operator

**Definition.** Let $\mathrm{G}$ be finite-dimensional and semisimple with Killing form $B$, and let $(X_i)$ be a basis of $\mathrm{G}$ with dual basis $(X^i)$ defined by $B(X_i, X^j) = \delta_i^j$. The **Casimir element** is

$$
\Omega = \sum_i X_i X^i \ \in\ Z(U(\mathrm{G})),
$$

and the **Casimir operator** of $G$ is the bi-invariant differential operator it defines.

**Theorem.** The Casimir element is independent of the basis, it lies in the centre $Z(U(\mathrm{G}))$, and in an irreducible representation of $G$ it acts as a scalar. Its definition, its eigenvalues and its role in the representation theory are *The Casimir Operator of a Lie Group*, below in this group.

*Proof.* A change of basis replaces the pair of dual bases by a contragredient pair, and the sum is invariant; centrality is the invariance of the form under the adjoint action, $B(\operatorname{ad}_Z X, Y) + B(X, \operatorname{ad}_Z Y) = 0$; the scalar statement is Schur's lemma, developed in the companion article.

## The Convolution Algebra

### Convolution on the Group

The Haar integral of *Locally Compact Groups and Haar Measure* gives $G$ a left-invariant measure $dx$, unique up to a positive scalar. For functions $f, h$ in $C_c^\infty(G)$ the **convolution** is

$$
(f * h)(x) = \int_G f(y)\,h(y^{-1}x)\,dy ,
$$

and its general theory — associativity, continuity, approximate identities — belongs to *Convolution on a Topological Group* and *The Convolution Algebra $L^1(G)$*. The Lie-theoretic content is that convolution by a function is a smoothing operator:

**Proposition.** For $f, h \in C_c^\infty(G)$ the convolution $f * h$ lies in $C_c^\infty(G)$, and for each fixed $f$ the operator $\lambda(f) : h \mapsto f * h$ is continuous on $C^\infty(G)$ and commutes with every left translation.

*Proof.* The integrand is smooth in $x$ and the integral is over the compact support of $f$, so differentiation under the integral sign gives smoothness; the support of $f * h$ is contained in $\operatorname{supp} f \cdot \operatorname{supp} h$, which is compact. Linearity and continuity are evident, and

$$
L_g(f*h)(x) = \int_G f(y)h(y^{-1}g^{-1}x)\,dy = (f * L_g h)(x),
$$

using the left invariance of the Haar measure, so $\lambda(f)L_g = L_g\lambda(f)$.

### The Convolution Algebra

**Theorem.** The space $C_c^\infty(G)$ is an associative algebra under convolution, with an approximate identity given by a sequence of non-negative functions of integral one whose supports shrink to $e$. The assignment

$$
\lambda : C_c^\infty(G) \longrightarrow \operatorname{End}_\mathbb{C}(C^\infty(G)), \qquad \lambda(f)h = f * h ,
$$

is an algebra homomorphism whose image is contained in the operators commuting with the left translations.

*Proof.* Associativity is Fubini together with the change of variable $z = y^{-1}x$; the approximate identity statement is that of *Convolution on a Topological Group*; the homomorphism property is $\lambda(f)\lambda(h) = \lambda(f*h)$, again Fubini; the commutation is the proposition above.

### The Distributions Supported at the Identity

**Definition.** A **distribution** on $G$ is an element of the topological dual of $C_c^\infty(G)$; it is **supported at $e$** when it annihilates the functions vanishing on a neighbourhood of $e$. The distributions supported at $e$ form the algebra $\mathcal{D}_e(G)$ under convolution, with

$$
\langle u * v, f\rangle = \langle u \otimes v, (x,y) \mapsto f(xy)\rangle .
$$

**Theorem (the operators are the distributions).** The algebra $\mathcal{D}_e(G)$ of distributions supported at the identity is isomorphic to $U(\mathrm{G})$, and a left-invariant operator $D$ is the convolution by the distribution $u \in \mathcal{D}_e(G)$ that corresponds to it,

$$
D f = u * f \qquad (f \in C_c^\infty(G)) .
$$

*Proof.* Evaluation at $e$ is a bijection from the distributions supported at $e$ onto the formal polynomials in the coordinate derivations at $e$, that is onto $U(\mathrm{G})$; convolution of two such distributions is composition of the corresponding operators, because the two-sided action of $G$ on itself makes the convolution reproduce the higher derivatives. Composing with the isomorphism of the first theorem identifies the distributions with the left-invariant operators, and the identity $Df = u * f$ on test functions extends to $C^\infty(G)$.

**Corollary.** The convolution algebra $C_c^\infty(G)$ is represented on $C^\infty(G)$ by the operators $\lambda(f)$, and the map $u \mapsto (f \mapsto u * f)$ is an algebra isomorphism from $U(\mathrm{G})$ onto the left-invariant operators.

## The Examples

### The Additive Group of a Vector Space

Let $G = \mathbb{R}^n$ with the additive structure. The left-invariant vector fields are the constant coefficient derivations $\partial_1, \ldots, \partial_n$, the universal enveloping algebra is the polynomial algebra $\mathbb{C}[\partial_1, \ldots, \partial_n]$, and the left-invariant differential operators are the constant coefficient operators. Convolution is the ordinary convolution of functions, and the distributions supported at the origin are the finite linear combinations of the delta distribution and its derivatives.

### A Torus

Let $G = T^n = \mathbb{R}^n/\mathbb{Z}^n$. The left-invariant differential operators are the constant coefficient operators in the coordinate derivations, and on the character $e^{2\pi i\,m\cdot x}$, $m \in \mathbb{Z}^n$, the operator $P(\partial)$ acts by the scalar $P(2\pi i m)$. Convolution acts on the Fourier coefficients by multiplication, which is the convolution theorem of *Harmonic Analysis on Groups*.

### A Compact Matrix Group

Let $G$ be a compact connected Lie group, such as $SU(2)$ or $SO(3)$. The bi-invariant operators are the polynomials in the Casimir element, and by *Harmonic Analysis on Groups* the Peter--Weyl theorem decomposes $C^\infty(G)$ into finite-dimensional irreducible components on each of which the Casimir operator acts by a scalar; the operator layer of $G$ is therefore diagonalised by the representation theory, which is the content of *The Casimir Operator of a Lie Group* and of *Unitary Representations of a Lie Group*.

## Summary

A Lie group carries the monoid of its smooth self-maps, whose units are the diffeomorphisms, and it acts on its smooth functions by the translations $L_g$, $R_g$ and the inversion. A differential operator is left-invariant when it commutes with every $L_g$ and right-invariant when it commutes with every $R_g$; the left-invariant ones form an algebra isomorphic to the universal enveloping algebra $U(\mathrm{G})$ by evaluation at the identity, with the correspondence $X \mapsto \tilde X$ on the first order and the Poincaré--Birkhoff--Witt monomials giving independent operators. The bi-invariant operators are exactly the centre $Z(U(\mathrm{G}))$, and the first member of that centre is the Casimir element of a semisimple algebra, which acts as a scalar on each irreducible representation. On the group side the Haar integral makes $C_c^\infty(G)$ an associative algebra under convolution, and convolution by a function is a smoothing operator commuting with the left translations, so the assignment $f \mapsto \lambda(f)$ is a representation of the convolution algebra. The distributions supported at the identity form the same algebra of operators, and they are the same object as the left-invariant differential operators: a left-invariant operator is the convolution by a distribution supported at $e$, and the algebra of these distributions is $U(\mathrm{G})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$, $\mathrm{G} = \operatorname{Lie}(G)$ | a Lie group, its identity and its Lie algebra |
| $\operatorname{Diff}(G)$ | the group of diffeomorphisms of $G$ |
| $L_g$, $R_g$, $\Psi_g = L_gR_{g^{-1}}$ | left translation, right translation and inner automorphism |
| $C^\infty(G)$ | the algebra of smooth functions, with the action $L_gf(x) = f(g^{-1}x)$ |
| $D_L(G)$, $D_R(G)$ | the left- and right-invariant operators |
| $\tilde X$ | the left-invariant vector field determined by $X$ |
| $U(\mathrm{G}) \cong D_L(G)$ | the isomorphism of the enveloping algebra with the left-invariant operators |
| $Z(U(\mathrm{G})) = D_L(G) \cap D_R(G)$ | the centre, the bi-invariant operators |
| $\Omega = \sum_i X_i X^i$ | the Casimir element of a semisimple algebra |
| $(f*h)(x) = \int_G f(y)h(y^{-1}x)\,dy$ | the convolution of functions |
| $\lambda(f)h = f*h$ | the convolution operator |
| $\mathcal{D}_e(G) \cong U(\mathrm{G})$ | the distributions supported at the identity |

## Further Reading

- Sigurdur Helgason, *Groups and Geometric Analysis* (American Mathematical Society, 2000), for the invariant differential operators, the enveloping algebra and the convolution algebra of a Lie group.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the bi-invariant operators, the Casimir element and their eigenvalues.
- John M. Lee, *Introduction to Smooth Manifolds* (Springer, second edition, 2013), for the differential operators on a manifold and the left-invariant vector fields.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the convolution algebra, the approximate identities and the representation on functions.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the distributions supported at the identity and their identification with the enveloping algebra.
