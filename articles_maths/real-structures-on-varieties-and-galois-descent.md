
# __Real Structures on Varieties and Galois Descent__

## Introduction

A variety defined over a field $k$ may be presented over a larger field $L$, and the problem of recovering the $k$-structure from the presentation is **descent**. For a Galois extension $L/k$ the extra datum that makes the recovery possible is an action of the Galois group on the $L$-variety whose action on functions is not $L$-linear but only $\sigma$-semilinear, the semilinearity of *The Galois Action as an Operator*; the datum is a **real structure** when the group has two elements, and the descended variety is recovered as the quotient by the action, with the **fixed locus** as the set of points already defined over the base field. This article fixes the involution of a variety, the fixed subscheme and the real points, the quotient by the involution, and the descent theorem that the two produce, and it is the first article of the `- * Theory` group.

The article is the involution-on-the-elements member of the group. Its neighbours are *The Weil Restriction and the Trace Form*, which reads the descent through the restriction of scalars and the trace, *Real Algebraic Varieties*, which studies the real points and the real spectrum, *The Galois Action on the Cohomology*, which reads the involution on the cohomology, and *Involutions on a Scheme and the Quotient*, below in this group, which develops the general involution and the categorical quotient of a scheme; the descent of a single algebra, with its conjugations and real forms, is the written *Real Forms and the Descent of an Algebra* of Part I, and the general descent formalism is Part I's *Descent Theory*. The Galois action itself is *The Galois Action as an Operator*, written above in this category, and its semilinearity is used here without repetition.

Throughout $k$ is a field, $L/k$ is a Galois extension with group $G$, and $X$ is a variety over $k$ or over $L$ as stated. The involution is written $\sigma$ and its linear or semilinear action on the structure sheaf is written $\theta$ when the distinction from the geometric map is needed; the fixed locus is $X^\sigma$. The case $L = \mathbb{C}$, $k = \mathbb{R}$, $G = \{\mathrm{id},\sigma\}$ with $\sigma$ the conjugation of *Galois Theory of ℂ/ℝ* is the model case and is kept in view.

## Real Structures on a Variety

### The Involution of a Variety

**Definition.** A **real structure** on a variety $X$ over a field $k$ is an involution of $X$ over $k$,
$$
\sigma : X\longrightarrow X, \qquad \sigma^2 = \mathrm{id}_X, \qquad \sigma \text{ over } k ,
$$
that is, a $k$-linear action of the group $\mathbb{Z}/2$ on $X$; the pair $(X,\sigma)$ is a **variety with a real structure**. The involution is nontrivial when $\sigma\neq\mathrm{id}_X$, and the structure is **split** when $\sigma$ is the identity.

**Proposition (an involution of the sheaf).** The pullback of $\sigma$ is a $k$-algebra involution of the structure sheaf,
$$
\theta = \sigma^\sharp : \mathcal{O}_X\longrightarrow\sigma_*\mathcal{O}_X, \qquad \theta^2 = \mathrm{id},
$$
and the two determine each other: $\sigma$ is the map whose pullback is $\theta$, by the anti-equivalence of *Schemes*. On an affine chart $X = \operatorname{Spec}A$ the involution is a $k$-algebra involution $\theta : A\to A$ of order two, and the correspondence is bijective.

*Proof.* The pullback of a morphism is a ring map and the pullback of the identity is the identity, so $\theta^2 = (\sigma^2)^\sharp = \mathrm{id}$; the bijection is the contravariance of $\operatorname{Spec}$, since a morphism $X\to X$ over $k$ corresponds to a $k$-algebra map $A\to A$ in the opposite direction.

### The Semilinear Involution over an Extension

**Definition.** Let $L/k$ be Galois and let $X$ be a variety over $L$. A **real structure** on $X$ over $L/k$ is an involution $\sigma$ of the underlying scheme over $k$ whose action on the structure sheaf is semilinear over $L$: for the nontrivial $\sigma\in G$ of order two, the pullback $\theta = \sigma^\sharp$ satisfies
$$
\theta(f+g) = \theta(f)+\theta(g), \qquad \theta(fg) = \theta(f)\theta(g), \qquad \theta(\ell f) = \sigma(\ell)\,\theta(f)
$$
for functions $f,g$ and constants $\ell\in L$. Such a $\theta$ is a **conjugation** of $X$, in the sense of Part I's *Real Forms and the Descent of an Algebra*, and the pair $(X,\theta)$ is a variety with **antilinear involution** when the distinction from the linear case is needed.

**Proposition (the linear case is the case of a trivial twist).** When $L = k$ the semilinearity is the $k$-linearity and the two definitions of an involution agree; when $L\neq k$ the semilinear involution is not a morphism over $L$ and not an $L$-linear involution of the sheaf.

*Proof.* For $L=k$ one has $\sigma=\mathrm{id}$ on the constants and the third identity is the second. For $L\neq k$ the nontrivial $\sigma$ moves the constants, so $\theta$ does not commute with the $L$-scalars and is not an $\mathcal{O}_X$-algebra map over $L$.

**Example (the conjugation of $\mathbb{C}$ over $\mathbb{R}$).** For $L = \mathbb{C}$, $k = \mathbb{R}$ and $\sigma$ the conjugation of *Galois Theory of ℂ/ℝ*, a real structure on a complex variety is an involution with $\theta(\ell f) = \bar{\ell}\,\theta(f)$. On $X = \mathbb{A}^1_{\mathbb{C}} = \operatorname{Spec}\mathbb{C}[x]$ the conjugation fixes $x$ and conjugates the coefficients, $\theta(x) = x$ and $\theta(\ell) = \bar\ell$, so $\theta(\ell x^n) = \bar\ell x^n$; the same formula $\theta([x_0:x_1]) = [\bar x_0:\bar x_1]$ defines the conjugation of $\mathbb{P}^1_{\mathbb{C}}$. The real structures of the two examples are the model of the article.

## The Fixed Locus and the Real Points

### The Fixed Subscheme

**Definition.** The **fixed locus** of an involution $\sigma$ of $X$ is the equaliser of $\sigma$ and the identity, that is, the fibre product of the graph $(\mathrm{id},\sigma) : X\to X\times_kX$ with the diagonal $\Delta : X\to X\times_kX$; it is a closed subscheme $X^\sigma\subseteq X$, and it is characterised as the largest closed subscheme on which $\sigma$ acts as the identity.

**Theorem (the fixed locus on an affine chart).** Let $X = \operatorname{Spec}A$ and let $\theta$ be the involution of $A$ that defines $\sigma$. Then
$$
X^\sigma = \operatorname{Spec}\bigl(A\big/\mathrm{I}_\theta\bigr), \qquad \mathrm{I}_\theta = \bigl(\,\theta(a)-a\ :\ a\in A\,\bigr),
$$
the ideal generated by the elements moved by $\theta$. In particular the fixed locus is cut out by the vanishing of the differences $\theta(a)-a$, and it is a closed subvariety of $X$.

*Proof.* The equaliser of two morphisms of affine schemes is computed by the coequaliser of the two corresponding algebra maps. The graph of $(\mathrm{id},\sigma)$ corresponds to $A\otimes_kA\to A$, $a\otimes b\mapsto a\,\theta(b)$, and the diagonal to the product $a\otimes b\mapsto ab$; their coequaliser is $A$ modulo the ideal generated by the differences $m(x)-c(x)$ as $x$ ranges over $A\otimes_kA$. On the generators $x = 1\otimes b$ these differences are $b - \theta(b)$, and on $x = a\otimes1$ they are $a - a = 0$, so the ideal is $\mathrm{I}_\theta$ as displayed.

**Remark (the fixed locus is not the quotient).** The fixed locus $X^\sigma$ is not the quotient $X/\sigma$ of the subalgebra of invariants, and the elementary example shows why. For $A = k[x]$ with $\theta(x) = -x$ in characteristic not two the fixed locus is $\operatorname{Spec}k[x]/(2x) = \operatorname{Spec}k$, a single point, while the invariants $A^\theta = k[x^2]$ give the quotient $\operatorname{Spec}k[x^2]$, a line. The two differ, and the involution is fixed-point-free away from the origin; keeping them apart is the convention of this group.

### The Real Points

**Definition.** For $X$ over $L$ with a real structure and for a field $R$ between $k$ and $L$, the **$R$-points of the fixed locus** are
$$
X^\sigma(R) = \operatorname{Hom}_k(\operatorname{Spec}R, X^\sigma),
$$
the points of $X$ with values in $R$ fixed by the involution. When $R = k$ they are the **real points** of $X$. For $L = \mathbb{C}$ and $k = \mathbb{R}$ they are the **real points of the complex variety**, $X^\sigma(\mathbb{R}) = X(\mathbb{C})^\sigma$, the points of $X$ with complex coordinates on which the conjugation acts trivially.

**Theorem (the fixed points of the geometric action).** Let $X$ be a variety over $L$ with a real structure, and let $G = \{\mathrm{id},\sigma\}$. Then the real points are the fixed points of the action on the $L$-points,
$$
X^\sigma(k) = X(L)^{G},
$$
and they are the $k$-points of the descended variety of the next section.

*Proof.* A point $P : \operatorname{Spec}L\to X$ lies in the fixed locus precisely when $\sigma\circ P = P$, which is the defining condition of $X(L)^G$; the identification with the $k$-points is the fixed-point theorem of *The Galois Action as an Operator*, and the descent is the quotient construction below.

### The Fixed Locus of the Conjugation

**Theorem (the real form of the affine space).** For $L = \mathbb{C}$, $k = \mathbb{R}$ and the conjugation of the coefficients on $A = \mathbb{C}[x_1,\ldots,x_n] = \mathbb{R}[x_1,\ldots,x_n]\otimes_{\mathbb{R}}\mathbb{C}$, the fixed locus is
$$
(\mathbb{A}^n_{\mathbb{C}})^\sigma = \operatorname{Spec}\bigl(\mathbb{C}[x_1,\ldots,x_n]^\theta\bigr) = \operatorname{Spec}\mathbb{R}[x_1,\ldots,x_n] = \mathbb{A}^n_{\mathbb{R}} .
$$

*Proof.* The ideal $\mathrm{I}_\theta$ is generated by $\theta(\ell)-\ell = \bar\ell-\ell$ for $\ell\in\mathbb{C}$, which contains $i-(-i) = 2i$ and therefore the whole of the imaginary axis; killing it leaves $\mathbb{R}[x_1,\ldots,x_n]$. Equivalently, a polynomial of $\mathbb{C}[x_1,\ldots,x_n]$ is fixed by the coefficient conjugation exactly when its coefficients are real.

**Corollary (projectivisation commutes with the fixed locus).** For the conjugation of $\mathbb{P}^n_{\mathbb{C}}$ the fixed locus is $\mathbb{P}^n_{\mathbb{R}}$, and more generally the fixed locus of a graded involution of a graded ring is the projective spectrum of the invariant part.

*Proof.* A homogeneous polynomial has real coefficients after the conjugation exactly when all its coefficients are real, and the Proj construction of *Schemes* takes the invariant subring of the graded ring to the fixed locus in the same way as $\operatorname{Spec}$ takes invariants; the two computations agree on the standard affine charts $x_i\neq0$.

## The Quotient by the Involution

**Definition.** Let $X$ be a variety with a real structure and let $G = \{\mathrm{id},\sigma\}$. A **quotient** of $X$ by $\sigma$ is a variety $X/\sigma$ over $k$ with a morphism $\pi : X\to X/\sigma$ over $k$ such that $\pi\circ\sigma = \pi$ and such that every morphism $\psi : X\to Y$ over $k$ with $\psi\circ\sigma = \psi$ factors uniquely as $\psi = \phi\circ\pi$. When such a quotient exists it is unique, and it is the **categorical quotient**.

**Theorem (the quotient of an affine variety).** Let $X = \operatorname{Spec}A$ and let $\theta$ be the involution of $A$. Then the **invariant ring** $A^\theta = \{a\in A : \theta(a) = a\}$ is a finitely generated $k$-algebra when $A$ is finitely generated over $k$, the morphism
$$
\pi : X\longrightarrow\operatorname{Spec}A^\theta
$$
induced by the inclusion $A^\theta\hookrightarrow A$ is a quotient by $\sigma$, and $\pi_*\mathcal{O}_X^\sigma = \mathcal{O}_{\operatorname{Spec}A^\theta}$.

*Proof.* The invariants of a finitely generated algebra under a finite group action form a finitely generated algebra, by Noether's theorem as in Part I's *Invariant Theory*; the map $\pi$ is invariant because $\theta|_{A^\theta} = \mathrm{id}$, and the universal property is the universal property of the invariants: a $\theta$-invariant map $\psi^\flat : A\to B$ lands in $B^\sigma$ only if its image is fixed, and it factors uniquely through $A^\theta$ by the universal property of the subalgebra. The identification of the pushforward is the definition of the structure sheaf of $\operatorname{Spec}A^\theta$.

**Theorem (the general quotient, stated).** Let a finite group $G$ act on a variety $X$ over $k$ by $k$-automorphisms. Then the quotient $X/G$ exists as a variety when $X$ is quasi-projective, the morphism $\pi : X\to X/G$ is finite and surjective, and the structure sheaf of the quotient is the sheaf of invariants $\mathcal{O}_{X/G} = (\pi_*\mathcal{O}_X)^G$. The quotient by an involution is the case $G = \mathbb{Z}/2$.

*Proof.* The construction on an affine chart is the theorem above, the finite generation of the invariants making $\operatorname{Spec}A^G$ a variety; the local constructions glue because a quotient is unique and the invariant sheaf is defined globally. The theorem for a general finite group on an arbitrary scheme, with the categorical quotient and the fixed subscheme, is developed below in this group in *Involutions on a Scheme and the Quotient*; the case of the involution is what this article uses.

**Theorem (the fixed locus inside the quotient).** The canonical map $X^\sigma\to X\to X/\sigma$ identifies $X^\sigma$ with a closed subscheme of $X/\sigma$, and it is an isomorphism precisely when the fixed locus is all of $X$, that is, when $\sigma = \mathrm{id}$.

*Proof.* The map $X^\sigma\to X/\sigma$ is the restriction of the quotient map to the fixed locus, and it is a closed immersion because $X^\sigma\subseteq X$ is closed and the quotient map is finite; it cannot be onto unless every point is fixed, in which case $\sigma = \mathrm{id}$ by the anti-equivalence above.

## Galois Descent

### Descent Data

**Definition.** Let $L/k$ be a Galois extension with group $G$ and let $X$ be a variety over $L$. A **descent datum** on $X$ is an action of $G$ on $X$ over $k$ whose action $\theta_\sigma = \sigma^\sharp$ on the structure sheaf is semilinear over $L$ for each $\sigma\in G$:
$$
\theta_\sigma(\ell f) = \sigma(\ell)\,\theta_\sigma(f), \qquad \theta_{\sigma\tau} = \theta_\sigma\circ\theta_\tau .
$$
The datum is **effective** if there is a variety $X_0$ over $k$ with an isomorphism $X\cong X_0\times_kL$ over $L$ under which the action becomes the action on the second factor of *The Galois Action as an Operator*.

**Proposition (the datum of the previous sections).** A real structure over $L/k$ is a descent datum for the group $G = \mathbb{Z}/2$: it is the datum of the single involution $\theta$ with the semilinearity displayed above.

*Proof.* The two-element group has one nontrivial element, and the multiplicativity $\theta_{\sigma\tau} = \theta_\sigma\theta_\tau$ is $\theta^2 = \mathrm{id}$ together with $\theta_{\mathrm{id}} = \mathrm{id}$; the semilinearity is the definition of the real structure.

### The Descent Theorem

**Theorem (Galois descent for affine varieties).** Let $L/k$ be a finite Galois extension with group $G$. Then the functor
$$
X_0\longmapsto X_0\times_kL
$$
from affine $k$-varieties to affine $L$-varieties with a descent datum is an equivalence of categories, with quasi-inverse
$$
X\longmapsto X^G = \operatorname{Spec}\bigl(\Gamma(X,\mathcal{O}_X)^G\bigr),
$$
the spectrum of the invariant ring of the action on the global functions.

*Proof.* On coordinate rings the statement is the descent of a module with a semilinear action, Part I's *Descent Theory* and the algebra case of *Real Forms and the Descent of an Algebra*: for an $L$-algebra $A$ with a semilinear $G$-action the invariants $A^G$ are a $k$-algebra with $A^G\otimes_kL\cong A$, and the two functors are inverse. The sheaf-theoretic form for a general variety, with the invariant sheaf in place of the invariant ring, is the descent of the projected *Equivariant Sheaves and Descent*, in the category *Sheaves and Cohomology*; the quasi-projective case follows by glueing the affine statement over a $G$-stable affine cover, which exists because $G$ is finite.

**Corollary (the quotient is the descended variety).** For a variety $X$ over $L$ with a real structure over $L/k$, the quotient $X/G$ of the previous section is the descended variety $X_0$: its base change is $X$,
$$
(X/G)\times_kL\ \cong\ X ,
$$
and the real points of $X/G$ are the fixed points of the involution, $(X/G)(k) = X(L)^G = X^\sigma(k)$.

*Proof.* The invariants of the semilinear action are a $k$-algebra whose base change is $A$ by the descent theorem; the quotient is the spectrum of the invariants by the definition of the categorical quotient, and the identification of the points is the fixed-point theorem already used.

### Fixed Locus, Quotient and Descent

**Remark (three objects of the involution).** The involution of a variety produces three objects that must not be conflated. The **fixed locus** $X^\sigma$ is the closed subscheme of points already defined over $k$; the **quotient** $X/\sigma$ is the descended variety, whose base change is $X$; and the **invariants** $\Gamma(X,\mathcal{O}_X)^\sigma$ are the global functions on the quotient. The fixed locus maps to the quotient as a closed subscheme, and the two agree exactly when the involution is trivial; in the semilinear case over $\mathbb{C}/\mathbb{R}$ the quotient is the real form and the fixed locus is the set of its real points.

**Remark (the split and the twisted structures).** A real structure is **split** when $X\cong X_0\times_kL$ with the trivial action up to isomorphism, and **twisted** otherwise; the descent theorem says that the twisted structures are classified by the descent data, which for an affine algebra is the set of conjugations, the same classification as Part I's *Real Forms and the Descent of an Algebra*. The real points of a twisted structure may be empty even when the complex variety is nonempty, and the conics below show it.

## Examples

### Affine and Projective Space

**Example ($\mathbb{A}^n$ and $\mathbb{P}^n$).** For the conjugation of $\mathbb{C}[x_1,\ldots,x_n]$ and of its graded form, the descended varieties are $\mathbb{A}^n_{\mathbb{R}}$ and $\mathbb{P}^n_{\mathbb{R}}$, with real points $\mathbb{R}^n$ and $\mathbb{P}^n(\mathbb{R})$; the quotient of the affine space is the affine space, and the fixed locus is the whole real form.

**Example (the roots of unity and the finite subgroups).** The conjugation of $\mathbb{C}$ acts on the group $\mu_n$ of $n$-th roots of unity by $\zeta\mapsto\zeta^{-1}$; the fixed points are the roots with $\zeta = \pm1$, the descended group is $\mu_2$ over $\mathbb{R}$, and the quotient $\mu_n/\sigma$ is a variety with two real points. This is the finite-group model of the fixed locus of a real structure.

### Conics

**Example (a conic with a real point).** The affine conic $C : y^2 = x^2-1$ over $\mathbb{R}$, or its projective closure, has two real points at infinity and the real points of the affine piece consist of the two branches $y = \pm\sqrt{x^2-1}$; the complex conic is isomorphic to $\mathbb{P}^1_{\mathbb{C}}$ and its real structure is the one descended from the conjugation, the split case. The two points at infinity are exchanged by nothing and fixed individually, being the real solutions of $x^2=y^2$ at $z=0$.

**Example (the anisotropic conic).** The projective conic $C : x^2+y^2+z^2 = 0$ over $\mathbb{R}$ has no real point: for real $x,y,z$ the form is a sum of squares and vanishes only at $x=y=z=0$, which is not a point of the projective plane. Its complex conic is again $\mathbb{P}^1_{\mathbb{C}}$, so the real structure is a twisted form of the projective line with empty real locus, the anisotropic form. The two examples have the same complexification and different real points, which is the content of the classification of the real forms of a conic; the classification by the genus of the real locus is the subject of *Real Structures on a Curve*, below in this group.

## Summary

A **real structure** on a variety is an involution: $k$-linear on a $k$-variety, or semilinear with respect to a nontrivial element of a Galois group on an $L$-variety. The **fixed locus** $X^\sigma$ is the equaliser of the involution and the identity, a closed subscheme; on an affine chart $X=\operatorname{Spec}A$ it is $\operatorname{Spec}(A/(\theta(a)-a))$, and it is not the quotient by the invariants. Its points with values in a field $R$ are the points fixed by the involution, and for $L=\mathbb{C}$, $k=\mathbb{R}$ its $\mathbb{R}$-points $X^\sigma(\mathbb{R}) = X(\mathbb{C})^\sigma$ are the real points of the complex variety. The **quotient** $X/\sigma$ is the categorical quotient, realised on an affine chart as $\operatorname{Spec}A^\theta$ with $A^\theta$ the invariant ring, finitely generated by the theorem of *Invariant Theory*, and it is a finite surjective quotient in the quasi-projective case.

**Galois descent** is the corresponding statement for a finite Galois extension $L/k$ with group $G$: the functor $X_0\mapsto X_0\times_kL$ is an equivalence from $k$-varieties to $L$-varieties with an effective descent datum — an action of $G$ that is semilinear on the structure sheaf — with quasi-inverse the spectrum of the invariants, $X\mapsto X^G$. The real structure over $L/k$ is the case $G=\mathbb{Z}/2$, and the quotient is the descended variety, with real points the fixed points of the involution. Three objects are kept apart throughout: the fixed locus, the quotient, and the invariants. They agree exactly when the involution is trivial, and the example $x\mapsto-x$ on the affine line shows the general difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\sigma^2=\mathrm{id}_X$ | a real structure: an involution of $X$ over $k$ |
| $\theta=\sigma^\sharp$, $\theta(\ell f)=\sigma(\ell)\theta(f)$ | the (semi)linear involution on the structure sheaf |
| $X^\sigma$ | the fixed locus: the equaliser of $\sigma$ and the identity |
| $\operatorname{I}_\theta=(\theta(a)-a)$ | the ideal cutting out the fixed locus on an affine chart |
| $X^\sigma(R)$ | the $R$-points fixed by the involution; real points for $R=k$ |
| $X^\sigma(k)=X(L)^G$ | the real points are the fixed points of the Galois action |
| $A^\theta=\{a:\theta(a)=a\}$ | the invariant ring; coordinate ring of the quotient |
| $X/\sigma=\operatorname{Spec}A^\theta$ (affine) | the quotient; the descended variety |
| $\mathcal{O}_{X/G}=(\pi_*\mathcal{O}_X)^G$ | the invariant sheaf; structure sheaf of the quotient |
| $\theta_\sigma$, $\theta_{\sigma\tau}=\theta_\sigma\theta_\tau$ | a descent datum for the Galois group $G$ |
| $X_0\mapsto X_0\times_kL$, $X\mapsto X^G$ | the equivalence of Galois descent |
| $(X/G)\times_kL\cong X$ | the quotient is the descended variety |
| split, twisted, anisotropic | the real structure is trivial, or not; no real points |

## Further Reading

- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for descent along a Galois extension and the classification of forms.
- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique* (Séminaire Bourbaki, 1959–1962), for effective descent of varieties and schemes.
- Michael Artin, *Algebra* (Pearson, second edition, 2011), for the fixed field of an involution and the elementary descent of a structure.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, third edition, 2013), for real structures on a variety, the real points and the descent of the base field.
- Jean-Pierre Serre, *Cohomological invariants in Galois cohomology* (University Lecture Series 28, American Mathematical Society, 2003), for the classification of the twisted forms by cohomology.
- Claude Chevalley, *Introduction to the Theory of Algebraic Functions of One Variable* (American Mathematical Society, 1951), for the descent of a function field and the real points of a curve.
