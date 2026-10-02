
# __Involutive Topological Division Rings__

## Introduction

A topological division ring is a topological ring in which every nonzero element is invertible and inversion is continuous; a division ring read in the form group is the ring whose additive group is the underlying group of every operator, and its involutions are the continuous anti-automorphisms of order two. On a division ring the involution has no zero divisors to fight, so the self-adjoint elements — the elements the involution fixes — and the skew elements give an additive decomposition of the whole ring, the norm form $x\sigma(x)$ is anisotropic, and the fixed set is a closed division subring. What the topology adds is the closedness of the self-adjoint and the skew sets, the continuity of the averaging map and of the norm form, and the fact that the fixed division subring is again a topological division ring. This article treats involutive topological division rings: it fixes the structure, proves that the self-adjoint and skew sets are closed and give a topological direct sum when $2$ is invertible, identifies the fixed division subring and the kind of the involution, computes the norm form and its anisotropy, and reads the whole thing on the valued and the locally compact division rings.

The article assumes the topological ring, the topological division ring, the continuity of inversion, the linear topologies and the completion from *Topological Rings and Fields*; the involution, its fixed and skew sets and the averaging map from *Involutive Rings* and *Involutive Topological Rings and Fields*; the closed equalizer and the dense-fixed-set argument from *Involutive Topological Rings and Fields*; the absolute value, the valuation and the non-Archimedean division ring from *Absolute Values, Valuations and Completions* and *Operators on a Non-Archimedean Field*; the isometric involution and the norm form from *Involutive Valued Fields* and *Involutions of a Non-Archimedean Field*; and the fixed division subring of a local field from *Involutive Local Fields*. The adjoint of an operator is the subject of the `- * Operator Theory` group and is not used here, and the central simple algebras with involution, the Hermitian forms and the classification of the involutions of the first and second kind are *The Book of Involutions*, named at the boundary and not developed.

Throughout, $D$ is a topological division ring, Hausdorff, with centre $Z(D)$; $\sigma$ is a **continuous involution**, an anti-automorphism of order two that is a homeomorphism; the **self-adjoint** elements are $D^\sigma = \{x : \sigma(x) = x\}$, the **skew** elements are $\mathrm{Skew}(D) = \{x : \sigma(x) = -x\}$, the **inverted** elements (with respect to the involution and the inversion) are $I(D,\sigma) = \{x : \sigma(x) = x^{-1}\}$, the norm form is $N(x) = x\,\sigma(x)$, and the **kind** of the involution is first when it fixes $Z(D)$ pointwise and second otherwise.

## The Self-Adjoint and the Skew Elements

**Definition.** The **self-adjoint set** is $D^\sigma = \{x : \sigma(x) = x\}$ and the **skew set** is $\mathrm{Skew}(D) = \{x : \sigma(x) = -x\}$; an element is self-adjoint, or symmetric, if it lies in the first, and skew, or antisymmetric, if it lies in the second.

**Theorem (closedness and the additive decomposition).** Both $D^\sigma$ and $\mathrm{Skew}(D)$ are closed in $D$, being the equalizers of the continuous maps $\sigma$ and $\mathrm{id}$, respectively $\sigma$ and $-\mathrm{id}$; they are additive subgroups. When $2 = 1+1$ is invertible in $D$ the averaging elements $\tfrac12(x+\sigma(x))$ and $\tfrac12(x-\sigma(x))$ are continuous in $x$ and

$$
D = D^\sigma \oplus \mathrm{Skew}(D)
$$

is a topological direct sum of additive topological groups; the projections are $\tfrac12(\mathrm{id}\pm\sigma)$. When $2$ is not invertible the two sets meet in the elements of order two of the characteristic, and the decomposition is not available.

**Proof.** The sets are equalizers of continuous maps, hence closed; they are additive because σ and −id are additive; the identities $\sigma(\tfrac12(x+\sigma(x)))=\tfrac12(\sigma(x)+x)$ and $\sigma(\tfrac12(x-\sigma(x)))=\tfrac12(\sigma(x)-x)=-\tfrac12(x-\sigma(x))$ show that the two averages lie in $D^\sigma$ and in the skew set, and their sum is $x$; the projections are continuous because σ and the scalar $\tfrac12$ are. When $2 = 0$ the two equations $\sigma(x)=x$ and $\sigma(x)=-x$ coincide, so the intersection is the whole kernel of $\sigma-\mathrm{id}$ read twice and the decomposition fails.

**Proposition (the self-adjoint set is not a subring in general).** The product of two self-adjoint elements need not be self-adjoint: $\sigma(xy) = \sigma(y)\sigma(x) = yx$, which equals $xy$ only when $x$ and $y$ commute. Hence $D^\sigma$ is a subring exactly when its elements commute, in which case it is a division subring; in general it is a closed additive subgroup, and the skew set spans an ideal-like subspace with $D^\sigma\,\mathrm{Skew}\subseteq\mathrm{Skew}$ and $\mathrm{Skew}\,D^\sigma\subseteq\mathrm{Skew}$.

**Proof.** The computation gives the criterion; if $D^\sigma$ is a subring its nonzero elements are invertible in $D$ and their inverses are self-adjoint because $\sigma(x^{-1}) = \sigma(x)^{-1} = x^{-1}$, so it is a division subring. The inclusions are $\sigma(xy) = \sigma(y)\sigma(x) = \pm yx$ according to the signs of $x$ and $y$.

## The Fixed Division Subring

**Theorem (the fixed set of a continuous involution is a closed division subring).** Let $\sigma$ be a continuous involution of $D$. Then $D^\sigma$ is a division subring of $D$, closed, and a topological division ring for the subspace topology with the restricted inversion; the fixed set of the centre is $Z(D)^\sigma = Z(D)\cap D^\sigma$, a subfield of the centre, and the involution is of the first kind exactly when $Z(D)^\sigma = Z(D)$ and of the second kind exactly when $Z(D)^\sigma$ has index two in $Z(D)$.

**Proof.** $D^\sigma$ contains $1$, is closed under subtraction, and is closed under multiplication and inversion by the computation of the previous proposition; it is closed as an equalizer. Inversion in $D^\sigma$ is the restriction of the continuous inversion of $D$, hence continuous, and the subspace topology makes it a topological division ring. The centre statement is that an automorphism of $D$ that fixes $D^\sigma$ pointwise acts on $Z(D)$ and its fixed set there is $Z(D)\cap D^\sigma$; an order-two automorphism of a field has fixed subfield of index at most two.

**Corollary (when the self-adjoint set is a subfield).** If $D$ is commutative then $D^\sigma$ is a subfield of $D$, closed, and equal to the fixed field of the field involution; for a commutative $D$ the involution is the identity on $D^\sigma$ and every element is $a + b$ with $a\in D^\sigma$ and $b$ skew, the decomposition of the previous section.

**Proof.** A commutative $D$ is a field; $\sigma$ is then an automorphism of order two and $D^\sigma$ is its fixed field, closed by the theorem and a subfield because the product of self-adjoint elements is self-adjoint in the commutative case.

**Remark (the two kinds and generation).** For an involution of the first kind the self-adjoint elements together with the skew elements generate $D$ additively; for an involution of the second kind the centre is a quadratic extension $Z(D)/Z(D)^\sigma$ and $D$ is generated over $D^\sigma$ by the skew elements of the centre. Whether the self-adjoint elements generate $D$ as a division ring is a genuine hypothesis, satisfied for the classical division rings and the valued ones; the article states it as such and does not claim it in general.

## The Norm Form and Anisotropy

**Theorem (the norm form).** For every $x\in D$ the norm form $N(x) = x\sigma(x)$ is self-adjoint,

$$
\sigma(N(x)) = N(x) ,
$$

and $N(x) = 0$ if and only if $x = 0$; hence $N$ is anisotropic. The norm form of $\sigma(x)$ is the $\sigma$-image of the norm form, $N(\sigma(x)) = \sigma(N(x))$, and the norm-one set

$$
U(D,\sigma) = \{x\in D^\times : N(x) = 1\}
$$

is a closed subgroup of $D^\times$.

**Proof.** $\sigma(x\sigma(x)) = \sigma(\sigma(x))\sigma(x) = x\sigma(x)$, so the value is self-adjoint; in a division ring a product of nonzero elements is nonzero, so $N(x) = 0$ only for $x = 0$; and $N(\sigma(x)) = \sigma(x)\sigma(\sigma(x)) = \sigma(x)x = \sigma(N(x))$. For the subgroup: if $N(u) = 1$ then $\sigma(u)u = \sigma(u\sigma(u)) = \sigma(N(u)) = 1$, so $\sigma(u) = u^{-1}$ and $N(u^{-1}) = u^{-1}\sigma(u)^{-1} = u^{-1}u = 1$; and if $N(u) = N(v) = 1$ then $N(uv) = uv\,\sigma(v)\sigma(u) = u\,(v\sigma(v))\,\sigma(u) = u\,\sigma(u) = 1$, the middle factor telescoping. Closedness is the continuity of $N$ on $D^\times$.

**Corollary (multiplicativity in the commutative case only).** If $D$ is a field the norm form is multiplicative, $N(xy) = N(x)N(y)$, and $U(D,\sigma)$ is the kernel of $N$ on the units; in the noncommutative case $N$ is multiplicative on the elements whose norm is central, and the norm-one condition $N(u) = 1$ implies $\sigma(u) = u^{-1}$, so $U(D,\sigma)$ is contained in the inverted set $I(D,\sigma)$.

**Proof.** In the commutative case $\sigma(xy) = \sigma(y)\sigma(x) = \sigma(x)\sigma(y)$; in general $N(uv) = u\,N(v)\,\sigma(u)$, which is $N(u)N(v)$ when $N(v)$ is central, and the implication $N(u)=1\Rightarrow\sigma(u)=u^{-1}$ is the computation of the theorem.

## The Topological Reading

**Theorem (continuity and closedness).** A continuous involution of a topological division ring is a homeomorphism, the self-adjoint and the skew sets are closed, the averaging maps are continuous when $2$ is invertible, and the fixed division subring $D^\sigma$ is a closed topological division ring; the completion $\widehat{D}$ is an involutive topological division ring when $D$ is a valued division ring with an isometric involution, and $\widehat{D}^{\widehat\sigma} = \widehat{D^\sigma}$ then.

**Proof.** Continuity of σ and σ² = id give that σ is a homeomorphism; the closedness and averaging are the earlier statements; the completion is *The Involution and the Completion of a Ring* and the fixed set of the completion is the completion of the fixed set for the isometric involution by the same article, and a valued division ring has a compatible valuation making the completion a division ring.

**Corollary (the locally compact case).** A locally compact non-discrete division ring is either $\mathbb{R}$, $\mathbb{C}$, the quaternions $\mathbb{H}$ or a finite-dimensional division algebra over a local field; a continuous involution of it has compact self-adjoint and norm-one sets, and the fixed division subring is closed and locally compact.

**Proof.** The classification of locally compact division rings is the standard one; the self-adjoint and norm-one sets are closed and bounded, hence compact in a locally compact ring, and the fixed division subring is closed and locally compact.

## Examples

**Example (the quaternions $\mathbb{H}$).** With the quaternion conjugation $\tilde q^{\natural}$, the involution is an anti-automorphism of order two of the first kind, fixing the centre $\mathbb{R}$; the self-adjoint elements are the reals, the skew elements are the pure quaternions $q_1e_1 + q_2e_2 + q_3e_3$, and $N(\tilde q) = \tilde q\tilde q^{\natural} = |\tilde q|^2$ is the square of the norm. The decomposition $\mathbb{H} = \mathbb{R}\oplus\mathbb{R}^3$ is topological, and the norm-one set is the compact sphere.

**Example ($\mathbb{C}$ with the conjugation).** The field of complex numbers is a topological division ring with the conjugation, an involution of the second kind because its centre is $\mathbb{C}$ and the involution acts nontrivially on it; the self-adjoint elements are the reals, a closed subfield of index two, and $N(Z) = Z\bar Z = |Z|^2$.

**Example (a local field with the identity).** A local field with the identity involution has $D^\sigma = D$, skew set zero and norm form the square; this is the degenerate case.

**Example (a valued division ring).** For a division ring with a valuation and an isometric involution, the valuation ring $\mathcal{O}_D$ is stable, the self-adjoint elements of $\mathcal{O}_D$ form a closed additive subgroup, and the norm form satisfies $v(N(x)) = 2v(x)$; this is the valued companion of the field case of *Involutions of a Non-Archimedean Field*.

**Example (the function field).** The division ring $k(t)$ with the involution $t\mapsto -t$ is of the second kind when $k$ carries a nontrivial involution and the involution acts on the constants, and of the first kind when $k$ has trivial involution; the self-adjoint elements form the fixed subfield $k(t^2)$ in the first case, closed for the $t$-adic topology.

## Summary

An involutive topological division ring is a topological division ring with a continuous involution; the self-adjoint set $D^\sigma$ and the skew set $\mathrm{Skew}(D)$ are closed additive subgroups, equalizers of the continuous maps $\sigma$ with $\mathrm{id}$ and with $-\mathrm{id}$, and when $2$ is invertible they give the topological direct sum $D = D^\sigma\oplus\mathrm{Skew}(D)$ through the continuous averaging projections, while the product of self-adjoint elements is self-adjoint only when its factors commute, so $D^\sigma$ is a division subring exactly when its elements commute and it is a closed additive subgroup in general. The fixed set is a closed division subring, a topological division ring in the subspace topology, and the involution is of the first kind when it fixes the centre pointwise and of the second kind when the fixed field of the centre has index two in the centre. The norm form $N(x) = x\sigma(x)$ is self-adjoint and anisotropic, so its zero set is zero, and the norm-one set is closed and is contained in the unitary group of the Hermitian form $B(x,y) = x\sigma(y)$, with multiplicativity holding in the commutative case only.

Topologically, a continuous involution is a homeomorphism, the self-adjoint and skew sets and the fixed division subring are closed, and the completion preserves the involution with $\widehat{D}^{\widehat\sigma} = \widehat{D^\sigma}$ in the isometric valued case; on a locally compact division ring the self-adjoint elements and the norm-one set are compact. The adjoints built from the involution — the involution on the bounded operators, the adjoints under the residue pairing and under a Hermitian valuation, and the adjoints of the sandwich, of the reflection and of the left multiplication — are the `- * Operator Theory` group of this category and are not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D$, $Z(D)$ | Topological division ring and its centre |
| $\sigma$ | Continuous involution (anti-automorphism of order two) |
| $D^\sigma = \{x : \sigma(x) = x\}$ | Self-adjoint elements, a closed division subring |
| $\mathrm{Skew}(D) = \{x : \sigma(x) = -x\}$ | Skew elements, closed |
| $D = D^\sigma\oplus\mathrm{Skew}(D)$ | Topological direct sum when $2$ is invertible |
| $N(x) = x\sigma(x)$ | Norm form, self-adjoint and anisotropic |
| $U(D,\sigma)$ | Norm-one set, closed in $D^\times$ |
| $I(D,\sigma) = \{x : \sigma(x) = x^{-1}\}$ | Inverted set, the unitary elements |
| First kind, second kind | $\sigma$ fixes $Z(D)$ pointwise, or not |
| $\widehat{D}^{\widehat\sigma} = \widehat{D^\sigma}$ | The completion in the isometric valued case |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew elements, the decomposition and the structure of rings with involution.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for division rings with involution and the first and second kinds.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the classification of involutions of division rings and the unitary groups.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for topological division rings, inversion, the valued division rings and the completion.
- P. M. Cohn, *Skew Field Constructions*, London Mathematical Society Lecture Note Series 27 (Cambridge University Press, 1977), for the structure of division rings and the role of the centre.
