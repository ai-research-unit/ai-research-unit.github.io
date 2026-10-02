
# __The Galois Action as an Operator__

## Introduction

A variety $X$ defined over a field $k$ acquires, after the base is extended to a Galois extension $L/k$, a symmetry that $X$ itself does not carry: the Galois group $G = \operatorname{Gal}(L/k)$ acts on the base-changed variety $X_L = X\times_kL$ over $k$, on its points with values in $L$-algebras, on its structure sheaf, and on the cohomology of its sheaves. The action is elementary to write down and surprisingly delicate to use, because it is $k$-linear but **not** $L$-linear: it permutes the coefficients of a function or a cohomology class, so it is a semilinear operator rather than an endomorphism of the layer of *Operators on a Variety*. This article fixes the action, proves its basic properties, and separates the two objects it produces — a genuine action by automorphisms of $X_L$, and a **semilinear** action on the $L$-vector spaces attached to $X_L$.

The article is the second of the `- Operator Theory` group. Its neighbours read the same layer through other operators: *Operators on a Variety* fixes the layer and the conjugation action of an automorphism on it, *The Frobenius Operator* is the Galois action in the arithmetic case of a finite field, where the group has a canonical generator, and *The Galois Action on the Cohomology* reads the action on cohomology classes and their invariants. The descent theory of the base field — the structure that the invariants recover — is the subject of *Real Structures on Varieties and Galois Descent*, a `- * Theory` article of this batch, and the general descent formalism is Part I's *Descent Theory*.

Throughout $k$ is a field, $L/k$ is a Galois extension with group $G$, and $X$ is a variety over $k$; the finite case $[L:k]<\infty$ is the one in which every statement is elementary, and the infinite case is cited from the descent theory as needed. The base change is written $X_L = X\times_k\operatorname{Spec}L$ and its structure sheaf $\mathcal{O}_{X_L}$.

## The Action on the Base Change

**Definition.** For $\sigma\in G$ let
$$
\sigma_X = \operatorname{id}_X\times_k\operatorname{Spec}\sigma \ \in\ \operatorname{Aut}_k(X_L),
$$
the automorphism of $X_L$ over $k$ obtained from the $k$-automorphism $\sigma$ of $L$ on the second factor. The assignment $\sigma\mapsto\sigma_X$ is a group homomorphism
$$
G\longrightarrow\operatorname{Aut}_k(X_L),
$$
that is, a $G$-action on $X_L$ by $k$-automorphisms.

*Proof.* The functor $\operatorname{Spec}$ is contravariant, so the composite $\operatorname{Spec}\sigma\circ\operatorname{Spec}\tau$ is $\operatorname{Spec}(\tau\sigma)$; hence with the natural convention of composition on the second factor the assignment is multiplicative, $\sigma\mapsto\sigma_X$, and $\operatorname{id}_X\times\operatorname{id}=\operatorname{id}$. Each $\operatorname{Spec}\sigma$ is a $k$-automorphism because $\sigma$ fixes $k$, so each $\sigma_X$ lies in $\operatorname{Aut}_k(X_L)$.

**Remark (the action is not that of a $k$-group).** The automorphisms $\sigma_X$ are not defined over $L$: they act on the $L$-coefficients, so they do not lie in $\operatorname{Aut}_L(X_L)$ unless $\sigma_X = \operatorname{id}$, and they act trivially on the first factor $X$. The action is therefore invisible on a variety that is already defined over $L$ in the strong sense that $X_L\cong X\times_k L$ with the $L$-structure forgotten; it records the $k$-structure.

**Example (the case $\mathbb{C}/\mathbb{R}$).** For $k = \mathbb{R}$, $L = \mathbb{C}$ and $G = \{\mathrm{id},\sigma\}$ with $\sigma$ the conjugation of *Galois Theory of ℂ/ℝ*, the action on $X_{\mathbb{C}}$ has order two and is the **real structure** read as an operator. For $X = \mathbb{A}^1_{\mathbb{R}}$ it is the map $\mathbb{A}^1_{\mathbb{C}}\to\mathbb{A}^1_{\mathbb{C}}$, $z\mapsto\bar z$; the fixed points are the real points, and the quotient by it is the real line, as in *Involutions on a Scheme and the Quotient*.

## The Action on Points

**Definition.** For a $k$-algebra $R$, the $R$-points of $X$ form the set $X(R) = \operatorname{Hom}_k(\operatorname{Spec}R,X)$. An $L$-point is a morphism $P : \operatorname{Spec}L\to X$ over $k$, and the group $G$ acts on $X(L)$ by
$$
(\sigma\cdot P) = P\circ\operatorname{Spec}\sigma .
$$

**Proposition (a left action).** The assignment above is a left action of $G$ on the set $X(L)$: $e\cdot P = P$ and $\sigma\cdot(\tau\cdot P) = (\sigma\tau)\cdot P$ for all $\sigma,\tau\in G$.

*Proof.* The identity is $\operatorname{Spec}(\mathrm{id}) = \mathrm{id}$, and the composition law is
$$
\sigma\cdot(\tau\cdot P) = P\circ\operatorname{Spec}\tau\circ\operatorname{Spec}\sigma = P\circ\operatorname{Spec}(\sigma\tau) = (\sigma\tau)\cdot P ,
$$
using the contravariance of $\operatorname{Spec}$ exactly as for the action on $X_L$. The same computation for a general test object $T$ shows that $G$ acts on the functor of points $T\mapsto X_L(T)$.

**Theorem (the fixed points are the $k$-points).** For a finite Galois extension $L/k$ the fixed points of the action on the $L$-points are the $k$-points,
$$
X(L)^G = X(k).
$$

*Proof.* A $k$-point is an $L$-point that is already defined over $k$, and $\operatorname{Spec}\sigma$ fixes every $k$-morphism, so $X(k)\subseteq X(L)^G$. Conversely let $X = \operatorname{Spec}A$ be affine and let $P$ correspond to the $k$-algebra homomorphism $\varphi : A\to L$. That $P$ is fixed by $\sigma$ says $\sigma\circ\varphi = \varphi$, that is $\varphi(a) = \sigma(\varphi(a))$ for all $a$ and all $\sigma$, so $\varphi$ takes values in $L^G = k$ and is a $k$-homomorphism $A\to k$, which is a $k$-point. The general case follows by covering $X$ with affine charts, the condition being local.

**Corollary.** For $X$ of finite type over $k$ and $L = \bar k$ the separable closure, the action of $G = \operatorname{Gal}(\bar k/k)$ on the geometric points $X(\bar k)$ has fixed set $X(k)$; in particular the $k$-points are recovered from the geometric points by taking invariants, which is the elementary case of Galois descent.

## The Action on Functions and on the Structure Sheaf

**Definition.** For an open $U\subseteq X_L$ and a function $f\in\mathcal{O}_{X_L}(U)$, the **translate** of $f$ by $\sigma$ is the function on $\sigma_X^{-1}(U)$ defined by
$$
(\sigma\cdot f)(x) = \sigma\bigl(f(\sigma_X^{-1}x)\bigr) .
$$

**Proposition (the action is $k$-linear and $\sigma$-semilinear).** The translate is well defined, and for all $f,g$ and $\ell$ in the constant sheaf $L$,
$$
\sigma\cdot(f+g) = \sigma\cdot f + \sigma\cdot g, \qquad
\sigma\cdot(fg) = (\sigma\cdot f)(\sigma\cdot g), \qquad
\sigma\cdot(\ell f) = \sigma(\ell)\,(\sigma\cdot f).
$$
Hence $\sigma$ acts by a $k$-algebra automorphism of $\mathcal{O}_{X_L}$ that is $\sigma$-semilinear over the constant field $L$: it is linear over $k$ and twists the $L$-scalars by $\sigma$.

*Proof.* Composition and the field automorphism $\sigma$ preserve sums and products, which gives the first two identities, and they give the third because $\sigma$ is additive and $\sigma(\ell)\in L$ is a constant. On an affine chart $X_L = \operatorname{Spec}(A\otimes_kL)$ the translate of $\sum_ia_i\otimes\ell_i$ is $\sum_ia_i\otimes\sigma(\ell_i)$: the action fixes $A\otimes 1$ and applies $\sigma$ to the second factor.

**Theorem (the invariant functions are the functions on $X$).** Let $X = \operatorname{Spec}A$ be affine and $L/k$ finite Galois. Then the ring of invariants of the action on the coordinate ring is
$$
(A\otimes_kL)^G = A\otimes_kL^G = A ,
$$
the image of the pullback $A\to A\otimes_kL$, $a\mapsto a\otimes1$. Consequently $\Gamma(X_L,\mathcal{O}_{X_L})^G = \Gamma(X,\mathcal{O}_X)$.

*Proof.* Write $A\otimes_kL$ as a free $A$-module with basis a $k$-basis of $L$; the action is by the matrix of $\sigma$ on the second factor, applied entrywise, and the invariant subspace of $L$ under $G$ is $k$ by the fundamental theorem of Galois theory (*Fields*). Hence the invariant submodule is the $A$-span of $1\otimes L^G = A\otimes1$. The sheaf statement follows by glueing over an affine cover.

**Remark (why the action is not in the operator layer of *Operators on a Variety*).** The operator layer of $X_L$ is $\mathcal{E}nd(\mathcal{O}_{X_L}) = \mathcal{O}_{X_L}$, whose operators are the multiplications by functions, and these are $L$-linear. The Galois translate is $k$-linear and not $L$-linear, so it is not a section of the operator layer; it is an automorphism of the $k$-structure of that layer. This is the precise sense in which the Galois action is an operator that does not belong to the operators of the previous article, and it is the reason the semilinearity of the next section is not an accident of notation.

## The Action on Cohomology

**Proposition (the semilinear action on cohomology).** Let $\mathcal{F}$ be a quasi-coherent sheaf on $X_L$ carrying a compatible action of $G$, that is, isomorphisms $\alpha_\sigma : \sigma_X^*\mathcal{F}\to\mathcal{F}$ with $\alpha_{\sigma\tau} = \alpha_\sigma\circ\sigma_X^*\alpha_\tau$. Then each $\sigma$ induces a $\sigma$-semilinear map
$$
\sigma^* : H^i(X_L,\mathcal{F})\longrightarrow H^i(X_L,\mathcal{F}), \qquad
\sigma^*(\ell\,v) = \sigma(\ell)\,\sigma^*(v),
$$
and the assignment is multiplicative, $(\sigma\tau)^* = \sigma^*\tau^*$ in the sense of the cocycle condition above. In particular $H^i(X_L,\mathcal{O}_{X_L})$ is a **semilinear $G$-module** over $L$.

*Proof.* The automorphism $\sigma_X$ induces an isomorphism $\mathcal{F}\to(\sigma_X)_*\mathcal{F}$, hence a map $H^i(X_L,\mathcal{F})\to H^i(X_L,(\sigma_X)_*\mathcal{F})\cong H^i(X_L,\mathcal{F})$ by the functoriality of cohomology of *Coherent Sheaves*. On an affine chart the cohomology is computed from the Čech complex of the $L$-coefficients, and $\sigma$ acts on the coefficients by $\sigma$, which gives the semilinearity. The multiplicativity is the functoriality $(\sigma_X\tau_X)^* = \tau_X^*\sigma_X^*$ composed with the cocycle.

**Theorem (the invariants of the structure sheaf).** For a finite Galois extension $L/k$ the invariants of the semilinear action on the cohomology of the structure sheaf are the cohomology of $X$:
$$
H^i(X_L,\mathcal{O}_{X_L})^G \cong H^i(X,\mathcal{O}_X)\otimes_kL^G \cong H^i(X,\mathcal{O}_X)
$$
whenever $X$ is separated, so that the cohomology is computed by the Čech complex of an affine cover with $G$-stable indexing.

*Proof.* For an affine cover $\mathfrak{U}$ of $X$ the cover $\mathfrak{U}_L$ of $X_L$ has $G$-stable Čech complex $C^\bullet(\mathfrak{U}_L,\mathcal{O}_{X_L}) = C^\bullet(\mathfrak{U},\mathcal{O}_X)\otimes_kL$ with the action on the second factor, and taking invariants commutes with cohomology of a complex of $A$-modules by the freeness in the previous theorem. The identified cohomology is the Čech cohomology of $X$, which agrees with the sheaf cohomology on a separated scheme.

The comparison in the infinite case — the **Hochschild–Serre spectral sequence** relating the invariants of $H^i(X_{\bar k},\mathcal{O})$ to the cohomology of $X$ and the group cohomology of $G$ — is stated, with the Galois representations it defines, in *The Galois Action on the Cohomology*, below in this batch.

## The Galois Action and the Operator Layer

**Proposition (the Galois action acts on the layer by conjugation).** Each $\sigma_X$ is an automorphism of $X_L$ over $k$, so by *Operators on a Variety* it acts on the operator layer $\mathcal{O}_{X_L}$ by
$$
\mathrm{Ad}_{\sigma_X}(m_f) = m_{\sigma\cdot f},
$$
and on the vector fields by pushforward. The fixed part of this action is generated by the operators defined over $k$: the invariant functions are $\Gamma(X,\mathcal{O}_X)$ and the invariant global vector fields are those of $X$.

*Proof.* The formula is the defining conjugation of the automorphism action, applied to the translation computed in the previous section. The fixed part is the theorem on invariant functions, and the fixed vector fields are the derivations that commute with the action, which are exactly those of the descended variety.

**Remark (the two actions on the cohomology must be told apart).** On a variety over a finite field the action of the Galois group and the action of the Frobenius generate the arithmetic operators; they commute, and their composition gives the same semilinear structure. The Frobenius is treated next, in *The Frobenius Operator*.

## Summary

For a Galois extension $L/k$ with group $G$, the base change $X_L = X\times_kL$ carries a left action of $G$ by the $k$-automorphisms $\sigma_X = \operatorname{id}_X\times_k\operatorname{Spec}\sigma$, which is the operator of the article. On the points it reads $\sigma\cdot P = P\circ\operatorname{Spec}\sigma$, a left action whose fixed set on $X(L)$ is the set of $k$-points, $X(L)^G = X(k)$; on functions it reads $(\sigma\cdot f)(x) = \sigma(f(\sigma_X^{-1}x))$, a $k$-algebra automorphism of the structure sheaf that is $\sigma$-semilinear over the constant field $L$, with invariant ring $\Gamma(X_L,\mathcal{O}_{X_L})^G = \Gamma(X,\mathcal{O}_X)$; and on the cohomology of a $G$-equivariant quasi-coherent sheaf it gives a semilinear $G$-action whose invariants on the structure sheaf recover $H^i(X,\mathcal{O}_X)$. The action is by automorphisms of $X_L$, hence acts by conjugation on the operator layer, but it is not itself an operator of that layer, since it is $k$-linear and not $L$-linear; the semilinearity is the structural feature that the later descent articles read.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $L$, $G=\operatorname{Gal}(L/k)$ | base field; Galois extension; Galois group |
| $X$, $X_L=X\times_kL$ | variety over $k$ and its base change |
| $\sigma_X=\operatorname{id}_X\times_k\operatorname{Spec}\sigma$ | the automorphism of $X_L$ induced by $\sigma$ |
| $X(L)$, $\sigma\cdot P=P\circ\operatorname{Spec}\sigma$ | $L$-points and the left action on them |
| $X(L)^G=X(k)$ | fixed points of the action are the $k$-points |
| $(\sigma\cdot f)(x)=\sigma(f(\sigma_X^{-1}x))$ | translate of a function; $\sigma$-semilinear over $L$ |
| $(A\otimes_kL)^G=A$ | invariants of the coordinate ring |
| $\alpha_\sigma:\sigma_X^*\mathcal{F}\to\mathcal{F}$ | descent datum making a sheaf $G$-equivariant |
| $\sigma^*$ on $H^i$ | the semilinear action on cohomology |
| $H^i(X_L,\mathcal{O})^G\cong H^i(X,\mathcal{O})$ | invariants of the cohomology of the structure sheaf |
| $\mathrm{Ad}_{\sigma_X}(m_f)=m_{\sigma\cdot f}$ | the action on the operator layer |
| $H^i(X_{\bar k},\mathcal{O})$ | geometric cohomology; the invariants are read in *The Galois Action on the Cohomology* |

## Further Reading

- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the Galois action on objects over a field and the descent of structures.
- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique* (Séminaire Bourbaki, 1959–1962), for descent along a Galois cover and the effective descent of sheaves.
- James S. Milne, *Lectures on Étale Cohomology* (v4.02, 2013), for the Galois action on cohomology and the Hochschild–Serre spectral sequence.
- Emil Artin, *Galois Theory* (Dover, 1998), for the fundamental theorem and the action of the Galois group on the extension.
- Michael Artin, *Algebra* (Pearson, second edition, 2011), for the elementary theory of group actions on fields and rings.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, third edition, 2013), for fields of definition of a variety and the action of the Galois group on its points.
