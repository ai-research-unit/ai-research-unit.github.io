
# __The Group Algebra as an Involutive Algebra__

## Introduction

The group algebra carries a second operation beside its product: the involution $f\mapsto f^*$, the reflection of a function in the inverse of the group with the modular correction that keeps the norm. With the involution the algebra is read differently: its elements split into Hermitian and skew parts, invertible elements with $f^* = f^{-1}$ are unitary, elements of the form $g^*\!*g$ are positive, and the whole of operator theory on the algebra becomes the theory of a `*`-algebra rather than of a plain Banach algebra. This article fixes the involution and its axioms, describes the classes of elements it distinguishes, and exhibits the $\mathrm{C}^*$-completion in which the involution acquires the $\mathrm{C}^*$-identity — an identity that fails on $L^1(G)$ itself.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its product, its norm and its involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ with the laws $(f*g)^* = g^*\!*f^*$, $(f^*)^* = f$ and $\|f^*\|_1 = \|f\|_1$ from *The Convolution Algebra $L^1(G)$*, which owns the involution and the algebra; the completions $C^*_r(G)$, $C^*(G)$ and $L(G)$ from that article and from *The Group Algebra as an Algebra of Operators*; the characters and the abelian transform from *Harmonic Analysis on Groups*; and the involutive Banach algebras, the `*`-representations, the $\mathrm{C}^*$-algebras, the Gelfand–Naimark theorem and the positive cone from *Operator Algebras* and *Involutive Topological Bilinear Algebras*. The grade involution $\alpha$ of the signed block is a structure of the `- Operator Theory` group and is different from the involution $f^*$; the adjoint of an operator, of which the equality $\lambda(f^*) = \lambda(f)^*$ is the archetype, belongs to the `- * Operator Theory` group, below; the measure algebra has its own involution in *The Involution on the Measure Algebra*, later.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$, and $\mathcal{A} = L^1(G)$ is the group algebra with convolution $(f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy$, $\|fg\|_1\leq\|f\|_1\|g\|_1$, and involution

$$
f^*(x) = \overline{f(x^{-1})}\,\Delta(x)^{-1} .
$$

On a unimodular group $\Delta\equiv1$ and $f^*(x) = \overline{f(x^{-1})}$. The $\mathrm{C}^*$-norm and the completions are

$$
\|f\|_{C^*} = \sup_\pi\|\pi(f)\|_{B(\mathcal{H}_\pi)}, \qquad C^*(G) = \overline{\mathcal{A}}^{\ \|\cdot\|_{C^*}}, \qquad C^*_r(G) = \overline{\lambda(\mathcal{A})}^{\ \|\cdot\|},
$$

the supremum over the continuous unitary representations $\pi$ of $G$.

## The Involution

**Theorem (the involution recalled).** The map $f\mapsto f^*$ is an involutive, isometric, conjugate-linear anti-automorphism of $\mathcal{A}$:

$$
(f^*)^* = f, \qquad (f*g)^* = g^*\!*f^*, \qquad (\lambda f + \mu g)^* = \bar\lambda f^* + \bar\mu g^*, \qquad \|f^*\|_1 = \|f\|_1 .
$$

**Proof.** These are the four axiom verifications of *The Convolution Algebra $L^1(G)$*, §The Involution; the modular factor is exactly what makes the norm isometric under the inversion $x\mapsto x^{-1}$, and it is absent only when $\Delta\equiv1$. $\square$

**Corollary ($L^1(G)$ is an involutive Banach algebra).** With this operation $\mathcal{A}$ is a Banach `*`-algebra; it is commutative exactly when $G$ is abelian and unital exactly when $G$ is discrete, and its involution is the one the harmonic analysis of the category uses throughout.

**Proof.** The algebra laws are those of *The Convolution Algebra $L^1(G)$*; the two structural statements are the commutative and unital criteria there. $\square$

**Remark (two involutions, not one).** The map $f^*$ is an **anti**-automorphism of order two, the structure of the `- * Theory` group. The grade involution $\alpha$ of *The Signed Sandwich on the Group Algebra*, an **auto**morphism of order two, is a different operation on the same algebra; the two coincide on a commutative group algebra and on the sign character they need not. No statement about $f^*$ is a statement about $\alpha$, and the article keeps them apart.

## The Classes of Elements

**Definition.** An element $f \in \mathcal{A}$ is **Hermitian** (or self-adjoint) when $f^* = f$, **skew-Hermitian** when $f^* = -f$, **normal** when $f^*\!*f = f*\!f^*$, **unitary** when $f^*\!*f = f*\!f^* = 1_{\mathcal{A}}$, and **positive**, written $f\geq0$, when $f = g^*\!*g$ for some $g \in \mathcal{A}$; the involution $f\mapsto f^*$ is the **conjugation**, and $\mathrm{Re}\,f = \tfrac12(f + f^*)$, $\mathrm{Im}\,f = \tfrac1{2i}(f - f^*)$ are its real and imaginary parts.

**Theorem (the Hermitian decomposition).** Every $f\in\mathcal{A}$ is uniquely $f = u + iv$ with $u, v$ Hermitian, and the map $f\mapsto (u,v)$ is an $\mathbb{R}$-linear isomorphism $\mathcal{A}\cong \mathcal{A}_h\oplus i\mathcal{A}_h$ of real Banach spaces; the Hermitian elements form a closed real subspace, and

$$
(f*g)^*\!*\!(f*g) = g^*\!*f^*\!*f*\!g .
$$

**Proof.** The decomposition is $u = \mathrm{Re}\,f$, $v = \mathrm{Im}\,f$, and it is unique because $\mathcal{A}_h\cap i\mathcal{A}_h = \{0\}$; the subspace is closed as the kernel of the continuous map $f\mapsto f^*-f$. The displayed identity is the anti-automorphism law applied to the product $f*g$. $\square$

**Proposition (unitaries exist only in the measure algebra).** The unitary group $\mathcal{U} = \{f : f^*\!*f = f*\!f^* = 1\}$ is nonempty if and only if $\mathcal{A}$ has an identity, that is if and only if $G$ is discrete; then the point masses are unitary, $\delta_x^* = \delta_{x^{-1}}$ and $\delta_x^*\!*\delta_x = \delta_e$, and every unitary $f$ satisfies $\|f\|_1\geq1$.

**Proof.** A unitary element is invertible, so its existence forces a unit; for a non-discrete group $\mathcal{A}$ has no identity and no invertible elements. For discrete $G$ the identity is $\delta_e$ and $\delta_x^*\!*\delta_x = \delta_{x^{-1}}*\delta_x = \delta_e$, so the point masses are unitary; a general unitary has $\|f\|_1\|f\|_1 = \|f^*\|_1\|f\|_1\geq\|f^*\!*f\|_1 = \|\delta_e\|_1 = 1$. $\square$

**Theorem (the positive cone).** The set

$$
\mathcal{A}^+ = \Bigl\{\sum_{i=1}^n g_i^*\!*g_i : n\geq0,\ g_i\in\mathcal{A}\Bigr\}
$$

of finite sums of squares is a convex cone under the real scalars, stable under $f\mapsto h^*\!*f*\!h$, and proper, $\mathcal{A}^+\cap(-\mathcal{A}^+)=\{0\}$; the positive functionals on $\mathcal{A}$, those $\omega$ with $\omega(f^*\!*f)\geq0$ for all $f$, are exactly the real-linear functionals that are $\geq0$ on $\mathcal{A}^+$.

**Proof.** The cone is convex by construction and stable under inner multiplication because $h^*\!*(g^*\!*g)*\!h = (g*h)^*\!*(g*h)$; for properness, fix a faithful `*`-representation, for instance the direct sum of the unitary representations: an element of $\mathcal{A}^+\cap(-\mathcal{A}^+)$ has $\pi(f)$ both positive and negative in $B(\mathcal{H}_\pi)$, hence $\pi(f) = 0$, and faithfulness gives $f = 0$. The identification of the positive functionals is the definition read on the generators of the cone and extended by linearity. $\square$

## The $\mathrm{C}^*$-Completion

**Definition.** The **enveloping $\mathrm{C}^*$-norm** of $\mathcal{A}$ is $\|f\|_{C^*} = \sup_\pi\|\pi(f)\|$, the supremum over all continuous unitary representations $\pi$ of $G$ acting through $\pi(f) = \int_G f(x)\pi(x)\,dx$; the **full group $\mathrm{C}^*$-algebra** is the completion $C^*(G) = \overline{\mathcal{A}}^{\|\cdot\|_{C^*}}$.

**Theorem (the identity appears in the completion).** The norm $\|f\|_{C^*}$ is finite for every $f$, with

$$
\|f\|_{C^*} \leq \|f\|_1 ,
$$

and on the completion the involution is isometric and satisfies the $\mathrm{C}^*$-identity

$$
\|f^*\!*f\|_{C^*} = \|f\|_{C^*}^2 \qquad (f\in C^*(G)) ;
$$

the algebra $\mathcal{A}$ is dense in $C^*(G)$ and the inclusion $\mathcal{A}\hookrightarrow C^*(G)$ is injective.

**Proof.** The bound is $\|\pi(f)\|\leq\|f\|_1$ for every representation, so the supremum is finite; the $\mathrm{C}^*$-identity holds in every $B(\mathcal{H}_\pi)$ and passes to the supremum because $f\mapsto\|f\|_{C^*}$ makes the completion a $\mathrm{C}^*$-algebra by construction, and the $\mathrm{C}^*$-algebra axioms include the identity; density is by definition, and injectivity because the regular representation is faithful: $\lambda(f) = 0$ gives $\|f\|_{C^*} = 0$ and then $f = 0$. $\square$

**Corollary (the reduced completion and the quotient).** The **reduced** completion $C^*_r(G) = \overline{\lambda(\mathcal{A})}^{\|\cdot\|}$ is the closure in one representation, the map $C^*(G)\to C^*_r(G)$ extending $\mathrm{id}_{\mathcal{A}}$ is a surjective $\mathrm{C}^*$-homomorphism, and it is injective exactly when $G$ is amenable; the identity $\|f^*\!*f\|_{C^*_r} = \|f\|_{C^*_r}^2$ holds there as well.

**Proof.** The reduced norm is $\sup$ over the single representation $\lambda$, hence dominated by the full norm, giving the quotient; amenability is the standard criterion for the two norms to agree; the identity is inherited from the $\mathrm{C}^*$-algebra $B(L^2(G))$ in which $C^*_r(G)$ is closed. $\square$

## The Failure of the $\mathrm{C}^*$-Identity on $L^1(G)$

**Theorem (the identity holds only for special elements).** On $\mathcal{A}$ itself the $\mathrm{C}^*$-identity can fail: for $G = \mathbb{Z}$ and $f = \delta_0 + i\delta_1 + \delta_2$ one has $\|f\|_1 = 3$, $\|f\|_1^2 = 9$, while

$$
f^*\!*f = 3\delta_0 + \delta_2 + \delta_{-2}, \qquad \|f^*\!*f\|_1 = 5 < 9 .
$$

Hence $\mathcal{A}$ is a Banach `*`-algebra that is not a $\mathrm{C}^*$-algebra, and the $\mathrm{C}^*$-identity is acquired only in the completion $C^*(G)$.

**Proof.** On $\mathbb{Z}$ the involution is $\delta_k^* = \delta_{-k}$ and convolution is the multiplication of the group algebra, so $f^* = \delta_0 - i\delta_{-1} + \delta_{-2}$ and the product is computed coefficient by coefficient: the coefficient of $\delta_n$ in $f^*\!*f$ is $\sum_{k}\overline{a_k}\,a_{k+n}$ for $a = (1, i, 1)$, giving $3$ at $n = 0$, $0$ at $n = \pm1$ and $1$ at $n = \pm2$. The $\ell^1$ norm is therefore $3+0+0+1+1 = 5$, while $\|f\|_1^2 = (1+1+1)^2 = 9$, and the strict inequality is the failure. $\square$

**Remark (what the failure measures).** The quantity $\|f^*\!*f\|_1/\|f\|_1^2$ can be read through the transform: on $\mathbb{Z}$ the Fourier transform of $f^*\!*f$ is $|\hat f|^2$, where $\hat f$ has a zero, and the ratio is the $\ell^1$-to-$\ell^\infty$ inflation of $|\hat f|^2$. The completion replaces the $\ell^1$ norm by the spectral radius $\|\hat f\|_\infty$, which is exactly the norm in which the identity holds. The example shows that the involution alone does not make the group algebra a $\mathrm{C}^*$-algebra; the completion is a genuine construction and not a formality.

## The Abelian Case

**Theorem (the Gelfand transform is a `*`-homomorphism).** Let $G$ be locally compact abelian, so that $\Delta\equiv1$ and $f^*(x) = \overline{f(-x)}$. For every character $\chi\in G^\vee$ the Gelfand transform satisfies

$$
\widehat{f^*}(\chi) = \overline{\hat f(\chi)} , \qquad \widehat{f*g}(\chi) = \hat f(\chi)\,\hat g(\chi),
$$

so the Gelfand transform is a `*`-homomorphism of $L^1(G)$ onto a dense `*`-subalgebra of $C_0(G^\vee)$, and it extends to a `*`-isomorphism $C^*(G)\cong C_0(G^\vee)$.

**Proof.** The convolution theorem is the homomorphism property; the involution identity is the substitution $x\mapsto-x$ in $\hat{f^*}(\chi) = \int\overline{f(-x)}\chi(x)\,dx = \overline{\int f(y)\chi(y)\,dy}$ using $\chi(-y) = \chi(y)^{-1}$ and $|\chi| = 1$. The completion is the $\mathrm{C}^*$-completion of a commutative `*`-algebra, isomorphic to the algebra of continuous functions vanishing at infinity on its spectrum, which is $G^\vee$. $\square$

**Corollary (the Hermitian elements are the real-valued spectrum).** In the abelian case $f$ is Hermitian exactly when $\hat f$ is real-valued, and $f\geq0$ implies $\hat f\geq0$ on $G^\vee$; the converse holds in the completion, where $C^*(G)\cong C_0(G^\vee)$ is a commutative $\mathrm{C}^*$-algebra and $\hat f\geq0$ has a non-negative square root. The positive cone of $\mathcal{A}$ is thus the intersection of the cone of non-negative transforms with the image of the Gelfand transform, and $\mathcal{A}^+\cap(-\mathcal{A}^+) = \{0\}$.

**Proof.** $\widehat{f^*} = \overline{\hat f}$, so $f^* = f$ iff $\hat f$ is real; $f = \sum g_i^*\!*g_i$ gives $\hat f = \sum|\hat g_i|^2\geq0$. In the completion the Gelfand transform is onto $C_0(G^\vee)$ and positive functions have square roots, giving the converse there; for $\mathcal{A}$ itself the square root of $\hat f$ need not be the transform of an integrable function, so the converse can fail and the cone is described as the stated intersection. $\square$

**Remark (what the article does not do).** The adjoint of an operator on $\mathcal{A}$, the equality $\lambda(f^*) = \lambda(f)^*$ and the unitary representations read through the adjoint are the `- * Operator Theory` group of this category; the measure-algebra involution and the adjoint of convolution by a measure are *The Involution on the Measure Algebra*, later; the spectral theory of a single Hermitian element belongs to *Operator Algebras*. The positive definite functions and the GNS construction built from a positive functional are *Positive Definite Functions and the Gelfand–Raikov Theorem*, next.

## Summary

The group algebra $\mathcal{A} = L^1(G)$ is a Banach `*`-algebra for the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, an isometric conjugate-linear anti-automorphism of order two; the grade involution $\alpha$ of the signed block is a distinct order-two structure, an automorphism on the same algebra. The elements split as $f = \mathrm{Re}\,f + i\,\mathrm{Im}\,f$ into Hermitian and skew parts; the Hermitian elements form a closed real subspace, the positive cone $\mathcal{A}^+$ of finite sums of squares is convex and proper and produces the positive functionals, and the unitary elements exist only when $G$ is discrete, where the point masses $\delta_x$ are unitary and every unitary has $\|f\|_1\geq1$. The enveloping $\mathrm{C}^*$-norm $\|f\|_{C^*} = \sup_\pi\|\pi(f)\|$ is bounded by $\|f\|_1$ and satisfies the $\mathrm{C}^*$-identity $\|f^*\!*f\|_{C^*} = \|f\|_{C^*}^2$ after completion to $C^*(G)$, with the reduced completion $C^*_r(G)$ as the quotient met when $G$ is amenable; on $\mathcal{A}$ the identity already fails, as the example $G = \mathbb{Z}$, $f = \delta_0 + i\delta_1 + \delta_2$ with $\|f^*\!*f\|_1 = 5 < 9 = \|f\|_1^2$ shows. In the abelian case the Gelfand transform is a `*`-homomorphism with $\widehat{f^*} = \overline{\hat f}$ and extends to $C^*(G)\cong C_0(G^\vee)$, and Hermitian elements are those with real transform and positive elements those with non-negative transform. The adjoints, the measure algebra and the positive definite functions are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = L^1(G)$, $\|f\|_1$ | The group algebra and its norm |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | The involution; $f^*(x)=\overline{f(x^{-1})}$ when $\Delta\equiv1$ |
| $(f*g)^* = g^*\!*f^*$, $(f^*)^* = f$, $\|f^*\|_1 = \|f\|_1$ | The involution axioms |
| $\mathcal{A}_h$, $\mathrm{Re}\,f$, $\mathrm{Im}\,f$ | Hermitian elements and the real decomposition $f = \mathrm{Re}\,f + i\,\mathrm{Im}\,f$ |
| $\mathcal{U}$ | The unitary group, nonempty iff $G$ is discrete |
| $\mathcal{A}^+$ | The positive cone, the finite sums $\sum_i g_i^*\!*g_i$ |
| $\|f\|_{C^*} = \sup_\pi\|\pi(f)\|$ | The enveloping $\mathrm{C}^*$-norm |
| $C^*(G)$, $C^*_r(G)$ | Full and reduced group $\mathrm{C}^*$-algebras |
| $\|f^*\!*f\|_{C^*} = \|f\|_{C^*}^2$ | The $\mathrm{C}^*$-identity, in the completion |
| $f = \delta_0 + i\delta_1 + \delta_2$, $\|f^*\!*f\|_1 = 5$ | The failure of the identity on $L^1(\mathbb{Z})$ |
| $\widehat{f^*}(\chi) = \overline{\hat f(\chi)}$, $C^*(G)\cong C_0(G^\vee)$ | The abelian `*`-homomorphism |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for Banach `*`-algebras, the involution axioms and the Hermitian and positive elements.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the enveloping $\mathrm{C}^*$-algebra, the $\mathrm{C}^*$-identity and the positive cone.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the group $\mathrm{C}^*$-algebras and the full-to-reduced quotient map.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the involution on $L^1(G)$ with the modular factor and its properties.
- Walter Rudin, *Fourier Analysis on Groups* (Wiley, 1962), for the abelian case and the Gelfand transform as a `*`-isomorphism.
