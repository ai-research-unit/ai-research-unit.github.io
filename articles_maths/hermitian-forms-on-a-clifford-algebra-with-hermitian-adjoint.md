
# __Hermitian Forms on a Clifford Algebra with Hermitian Adjoint__

## Introduction

A ring with an anti-involution carries a canonical Hermitian form: for an anti-involution $c$ of a ring $R$, the two-variable map

$$
h_c(x,y) = c(x)\,y
$$

is Hermitian with respect to $c$, and its diagonal $q_c(x) = c(x)x$ is fixed by $c$. The verification is the definition of an anti-involution together with $c^{2} = \mathrm{id}$, and it needs nothing else: no commutativity, no order, no hypothesis on the ring.

Applied to a Clifford algebra this construction gives the **Hermitian forms carried by the algebra itself**. The Clifford algebra has three distinguished anti-involutions available to play the role of $c$: reversion $x^{r}$ and Clifford conjugation $\bar x = \alpha(x^{r})$, which are intrinsic and need no hypothesis on the base, and the dagger $x^{\dagger} = \sigma(\alpha(x^{r}))$, which needs an involution $\sigma$ of the base and is defined in *Involutive Clifford Algebras*. The three forms $h_r$, $h_{\bar\cdot}$ and $h_{\dagger}$ are consequently of two kinds, and the distinction is exact: the intrinsic ones act trivially on the coefficients, so they are $A$-bilinear, while the dagger is only $\sigma$-semilinear on the first argument and gives a genuine sesquilinear form. This is the whole content of the passage from the ordinary to the Hermitian theory.

This article treats the forms on the algebra, their definitions, their linearity, their non-degeneracy, their isometry groups, their Gram matrices, their inertia, and the place of the algebra-valued forms among the Hermitian forms over a ring. The scalar reductions of these forms, the blade form and the trace form, are the subject of *The Blade Form and the Hilbert Structure with Hermitian Adjoint*; the operator built from $h_{\dagger}$ is *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint*; the classical theory of Hermitian forms over a division ring is recalled here only as far as the algebra needs it and belongs to *The Unitary and Symplectic Groups* and to *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the case of the identity involution is *Bilinear Forms*. The general theory of sesquilinear and Hermitian forms over a ring, which the article uses, is in *Involutive Clifford Algebras*.

## The Form Attached to an Anti-Involution

### Definition and the Hermitian Property

**Definition.** Let $R$ be a ring with an anti-involution $c$, that is, an additive map with $c(xy) = c(y)c(x)$ and $c^{2} = \mathrm{id}$. The **Hermitian form attached to $c$** is

$$
h_c : R \times R \longrightarrow R, \qquad h_c(x,y) = c(x)\,y .
$$

**Proposition.** $h_c$ is Hermitian with respect to $c$:

$$
h_c(y,x) = c\bigl(h_c(x,y)\bigr).
$$

**Proof.** By the definition, $h_c(y,x) = c(y)x$, and $c(h_c(x,y)) = c(c(x)y) = c(y)\,c(c(x)) = c(y)x$, using that $c$ is an anti-homomorphism and $c^{2} = \mathrm{id}$.

**Proposition (the diagonal).** The diagonal $q_c(x) = h_c(x,x) = c(x)x$ is fixed by $c$,

$$
c\bigl(q_c(x)\bigr) = q_c(x),
$$

and it satisfies $q_c(ax) = c(a)\,q_c(x)\,a$ for $a \in R$.

**Proof.** $c(c(x)x) = c(x)c(c(x)) = c(x)x$, and $q_c(ax) = c(ax)ax = c(x)c(a)ax$.

**Remark.** The diagonal is the object that becomes a quadratic form when $R$ is commutative and $c$ acts on scalars; in the classical case of a field with $\sigma = \mathrm{id}$ it is the quadratic form that polarises to $h_c$, by

$$
q_c(x+y) - q_c(x) - q_c(y) = h_c(x,y) + h_c(y,x),
$$

which follows by expanding $q_c(x+y)$ and using $h_c(x,y) = c(x)y$ and $h_c(y,x) = c(y)x$.

### Semilinearity and the Two Regimes

**Proposition.** Let $A$ be the centre of $R$, or a commutative ring of coefficients for the Clifford algebra. Then

$$
h_c(ax, y) = c(a)\,h_c(x,y), \qquad h_c(x, ay) = h_c(x,y)\,a .
$$

**Proof.** $h_c(ax,y) = c(ax)y = c(x)c(a)y$ and $h_c(x,ay) = c(x)ay$.

**Corollary (the two regimes).** If $c$ acts trivially on the coefficient scalars, then $h_c$ is $A$-**bilinear**; if $c$ acts as a nontrivial involution $\sigma$ on them, then $h_c$ is $\sigma$-**semilinear** in the first argument and $A$-linear in the second. For a Clifford algebra this separates the intrinsic forms from the dagger: reversion and Clifford conjugation fix every coefficient, since they fix the degree-zero part, so $h_r$ and $h_{\bar\cdot}$ are bilinear over the base; the dagger induces $\sigma$ on the coefficients, so $h_{\dagger}$ is genuinely sesquilinear. The passage from the bilinear to the sesquilinear theory is exactly the passage from the identity involution to a general $\sigma$.

**Corollary (the skew companion).** The map $h_c(x,y) - h_c(y,x)$ is $c$-skew, $c(h_c(x,y)-h_c(y,x)) = -(h_c(x,y)-h_c(y,x))$, and when $2$ is invertible in $A$ the form splits into a $c$-Hermitian and a $c$-skew part.

### Non-Degeneracy

**Proposition.** For an anti-involution $c$ the radical of $h_c$ on $R$ is trivial,

$$
\{\, x : h_c(x,y) = 0 \ \text{for all } y \,\} = \{\, x : c(x) = 0 \,\} = 0 ,
$$

because $h_c(x,1) = c(x)$ and $c$ is bijective. In particular every Hermitian form of this shape, and so each of the three forms of a Clifford algebra, is non-degenerate.

**Remark.** Non-degeneracy over $R$ is a weak statement, since the form takes values in the same algebra it is a form on. The forms that carry arithmetic information are its scalar reductions, the trace form and the blade form, whose non-degeneracy is not automatic and is discussed in *The Blade Form and the Hilbert Structure with Hermitian Adjoint*.

## The Three Forms of a Clifford Algebra

### The Table

Let $\sigma$ be an involution of the base $A$, and let $x, y \in \mathrm{Cl}(V,q)$.

| form | definition | anti-involution $c$ | kind | needs |
|---|---|---|---|---|
| Hermitian form | $h_{\dagger}(x,y) = x^{\dagger}y$ | the dagger | $\sigma$-sesquilinear | an involution of $A$ |
| conjugation form | $h_{\bar\cdot}(x,y) = \bar x\,y$ | Clifford conjugation | bilinear | nothing |
| reversion form | $h_{r}(x,y) = x^{r}y$ | reversion | bilinear | nothing |

All three are Hermitian in the sense of their own anti-involution,

$$
h(y,x) = c\bigl(h(x,y)\bigr),
$$

and all three have their diagonal fixed by it. The first two of the table need nothing of the base, which is the sense in which the phrase "the Hermitian forms on the algebra" does not require an involution at all; only the first is genuinely sesquilinear, which is the sense in which the dagger is what adds to the algebra.

**Remark (the dagger is the general member).** When $\sigma = \mathrm{id}$ the dagger is Clifford conjugation and $h_{\dagger} = h_{\bar\cdot}$, so the three collapse to two. When $\sigma \neq \mathrm{id}$ they are distinct, as the involution set on the biquaternion algebra shows: the Klein four-group $\{\mathrm{id}, \bar\cdot, {}^{*}, {}^{\dagger}\}$ of *Involutive Clifford Algebras* gives three distinct anti-involutions and hence three distinct forms.

### The Isometry Groups

**Proposition.** The isometries of $h_c$ on the algebra are

$$
\mathrm{Isom}(h_c) = \{\, s \in \mathrm{Cl}(V,q) : c(s)\,s = 1 \,\},
$$

an identity valid with $c$ the dagger, Clifford conjugation or reversion. In particular

$$
\mathrm{Isom}(h_{\dagger}) = \{\, s : s^{\dagger}s = 1 \,\} = U,
$$

the unitary slice of *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint*, and $\mathrm{Isom}(h_{\bar\cdot}) = \{s : \bar s\,s = 1\} = \mathrm{Pin}(V,q)$ when $\sigma = \mathrm{id}$.

**Proof.** $h_c(sx, sy) = c(sx)(sy) = c(x)c(s)s\,y$. This equals $h_c(x,y) = c(x)y$ for all $x,y$ precisely when $c(s)s = 1$, taking $x = y = 1$ for the necessity. The identification $\{\bar s s = 1\} = \mathrm{Pin}$ is the proposition of *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint*.

**Corollary.** The intrinsic forms have the same isometry group, the Pin group of the quadratic space, and it is compact for a definite real form. The dagger form has the unitary slice, which is generally larger; this is the precise sense in which the Hermitian structure of the algebra is richer than its orthogonal structure.

### The Relation to the Hermitian Sandwich

**Proposition.** The value at the unit of the Hermitian sandwich is the diagonal of $h_{\dagger}$ evaluated at the dagger:

$$
\Theta_x(1) = x\,x^{\dagger} = q_{\dagger}(x^{\dagger}), \qquad q_{\dagger}(u) = u^{\dagger}u .
$$

**Proof.** $(x^{\dagger})^{\dagger} = x$, so $q_{\dagger}(x^{\dagger}) = (x^{\dagger})^{\dagger}x^{\dagger} = x\,x^{\dagger} = \Theta_x(1)$.

**Remark.** The cross-term of the form gives the operator: $h_{\dagger}(u,v) = u^{\dagger}v$, so that $\Theta_x(y) = x\,y\,x^{\dagger} = h_{\dagger}(x^{\dagger}, y)\,x^{\dagger}$ is the form applied to $x^{\dagger}$ and $y$, followed by right multiplication by $x^{\dagger}$. The forms of this article are thus the bilinear data of the operator of the previous one.

## The Gram Matrix and Congruence

### The Matrix of a Sesquilinear Form

Let the module be free of rank $n$ with basis $(e_i)$ on which $c$ acts, and put $H_{ij} = h(e_i,e_j)$. Then $h(x,y) = x^{\dagger}H y$ in the column convention, where ${}^{\dagger}$ is the Hermitian transpose $H^{\dagger} = \sigma(H)^{T}$, the convention of *Involutive Clifford Algebras*. The Hermitian property $h(y,x) = c(h(x,y))$ becomes

$$
H^{\dagger} = H ,
$$

and a change of basis by an invertible matrix $S$ acts by **congruence**,

$$
H \longmapsto S^{\dagger}H\,S ,
$$

not by similarity. This is the algebraic reason why the invariants of a Hermitian form are its inertia and its discriminant, and not its eigenvalues.

### Inertia and the Definite Case

Over $A = \mathbb{R}$ with $\sigma = \mathrm{id}$, a Hermitian form is symmetric bilinear, and Sylvester's law of inertia assigns to it the pair $(p,q)$ of positive and negative squares in a diagonal basis; the form is non-degenerate exactly when $p + q = n$, definite when $pq = 0$, and the isometry group of a definite form is the orthogonal group, compact. Over $A = \mathbb{C}$ with complex conjugation, a Hermitian form satisfies $H^{\dagger} = H$ in the sense $H^{*T} = H$ and Sylvester's law applies with the same conclusion, the isometry group of a definite form being the unitary group. Both statements are the classical ones of *The Unitary and Symplectic Groups*; what the Clifford algebra adds is that the form is carried by the algebra itself, the scalar reductions give the invariants, and the dagger records the signature.

**Remark (the signature of the dagger form).** With $\sigma = \mathrm{id}$ the scalar form $\mathrm{Sc}(x^{\dagger}y) = \mathrm{Sc}(\bar x\,y)$ has Gram matrix diagonal with entries $(-1)^{|I|}\prod_{i\in I}e_i^{2}$ on the blades, the blade form with the parity sign of the dagger inserted; over a positive definite quadratic form the products are $+1$ and the entries are $+1$ on the even blades and $-1$ on the odd ones, while over a negative definite form every entry is $+1$, so its signature is the one of the geometric product rather than the Euclidean one; this is worked out in *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, and it is the reason the blade form uses reversion and not the dagger.

## Hermitian Forms over a General Involution Ring

The construction $h_c(x,y) = c(x)y$ is the special case of a Hermitian form over a ring with involution in which the module is the ring itself and the form is the unit form $h(x,y)=c(x)y$. The general theory, with $\varepsilon$-Hermitian forms, their Witt group, hyperbolic planes, the discriminant and the Wall group, is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. Two facts of that theory are used here and are recalled: the extension theorem for Hermitian forms over a division ring with involution, by which an isometry of a subspace extends when the orthogonal complement is non-degenerate, and the cancellation theorem, which hold with the usual exceptions in characteristic two. Both are quoted, not proved.

## Summary

For an anti-involution $c$ of a ring $R$ the map $h_c(x,y) = c(x)y$ is **Hermitian with respect to $c$**, its diagonal $q_c(x) = c(x)x$ is fixed by $c$, and its radical on $R$ is trivial, so the form never degenerates on the algebra itself. A Clifford algebra carries three such forms: the **Hermitian form** $h_{\dagger}(x,y) = x^{\dagger}y$ of the dagger, which is $\sigma$-semilinear in the first argument and needs an involution of the base; and the two **intrinsic** forms $h_{\bar\cdot}(x,y) = \bar x\,y$ and $h_r(x,y) = x^{r}y$, which fix the coefficients and are therefore bilinear, and which need nothing of the base. All three satisfy $h(y,x) = c(h(x,y))$ in the sense of their own $c$, and all three have $c$-fixed diagonals.

The isometry group of $h_c$ is $\{s : c(s)s = 1\}$; for the dagger this is the unitary slice $U$, and for Clifford conjugation with $\sigma = \mathrm{id}$ it is the Pin group, so the intrinsic forms see the orthogonal geometry and the dagger sees the unitary one, which is the precise sense in which the involutive base adds to the algebra. The Gram matrix of a sesquilinear form satisfies $H^{\dagger} = H$ with $H^{\dagger} = \sigma(H)^{T}$ and transforms by congruence $H \mapsto S^{\dagger}HS$ under a change of basis, so the invariants are inertia and discriminant rather than spectrum; over $\mathbb{R}$ and $\mathbb{C}$ Sylvester's law gives the signature, and the scalar reduction of the dagger form has the signature of the geometric product, $(-1)^{|I|}\prod_{i\in I}e_i^{2}$ on the blades, which over a positive definite form reads $+1$ on the even blades and $-1$ on the odd ones. The value at the unit of the Hermitian sandwich is the diagonal of $h_{\dagger}$ at the dagger, $\Theta_x(1) = q_{\dagger}(x^{\dagger})$, which is how the forms of this article are the bilinear data of the operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c$ | Anti-involution, $c(xy)=c(y)c(x)$, $c^{2}=\mathrm{id}$ |
| $h_c(x,y) = c(x)y$ | Hermitian form attached to $c$ |
| $q_c(x) = c(x)x$ | Its diagonal, fixed by $c$ |
| $h_{\dagger}(x,y) = x^{\dagger}y$ | Hermitian form of the dagger, $\sigma$-sesquilinear |
| $h_{\bar\cdot}(x,y) = \bar x\,y$ | Conjugation form, bilinear |
| $h_r(x,y) = x^{r}y$ | Reversion form, bilinear |
| $H_{ij} = h(e_i,e_j)$ | Gram matrix, $H^{\dagger}=H$ |
| $H^{\dagger} = \sigma(H)^{T}$ | Hermitian transpose |
| $H \mapsto S^{\dagger}HS$ | Congruence under a change of basis |
| $\mathrm{Isom}(h_c) = \{s : c(s)s=1\}$ | Isometry group of the form |
| $U = \{s : s^{\dagger}s=1\}$ | Unitary slice, $\mathrm{Isom}(h_{\dagger})$ |
| $(p,q)$ | Inertia of a scalar Hermitian form |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for Hermitian forms over rings with involution, their Gram matrices and congruence.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution and the Hermitian forms carried by the algebra.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the classification of Hermitian forms over division rings and the extension theorem.
- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 3rd ed. 1971), for the unitary group and the classical groups over a ring with involution.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the passage between bilinear and sesquilinear forms and the behaviour in characteristic two.
