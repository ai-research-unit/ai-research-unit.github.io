
# __Split-Quaternion Automorphisms and Derivations__

## Introduction

The **split-quaternion algebra** is the four-dimensional real algebra

$$
\mathbb{H}_{\mathrm{s}} = \mathrm{Cl}_{1,1},
$$

with basis $1, e_1, e_2, e_3$, the relations $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, $e_3 = e_1 e_2$. This article describes two standard invariants: the group of algebra **automorphisms** and the Lie algebra of **derivations**. Because the algebra is central simple over $\mathbb{R}$, both invariants are as small as the structure permits: every automorphism is inner and every derivation is inner, so there are no outer automorphisms and no exotic derivations.

We use the conventions of the algebra article: the conjugation ${}^{\natural}$, the principal involution $\alpha$ and the reversal $\rho$; the split-quaternion norm $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$; the vector subspace $V = \operatorname{span}\{e_1,e_2,e_3\}$, with bracket algebra $\mathrm{SL}_2(\mathbb{R})$. A general element is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$. No physics is invoked, and everything below is standard structure theory of a central simple real algebra.

## Standing Facts: Simplicity and the Centre

The automorphism group and the derivation algebra are governed by two structural facts.

**Simplicity.** The only two-sided ideals of $\mathbb{H}_{\mathrm{s}}$ are $0$ and $\mathbb{H}_{\mathrm{s}}$.

**The centre.** The centre is $Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1$, a one-dimensional real space. Hence $\mathbb{H}_{\mathrm{s}}$ is **central simple over $\mathbb{R}$**: simple, of real dimension $4$, with centre exactly $\mathbb{R}$. This is the point of departure from the biquaternion algebra $\mathbb{B}$, which over $\mathbb{R}$ is simple but not central, its centre being the two-dimensional subspace $\mathbb{C}_{\mathbb{B}}$. Because the centre here is one-dimensional, an automorphism can only fix it, and a derivation can only vanish on it; there is no conjugate-linear coset and no étale direction to allow extra structure.

## Automorphisms over $\mathbb{R}$

**Definition.** An **$\mathbb{R}$-algebra automorphism** of $\mathbb{H}_{\mathrm{s}}$ is a bijective $\mathbb{R}$-linear map $\sigma : \mathbb{H}_{\mathrm{s}} \to \mathbb{H}_{\mathrm{s}}$ with $\sigma(\tilde q y) = \sigma(\tilde q)\sigma(y)$ and $\sigma(1) = 1$. They form a group under composition, written $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}})$.

**Inner automorphisms.** For an invertible $g \in \mathbb{H}_{\mathrm{s}}$ the map $\iota_g(\tilde q) = g\tilde q g^{-1}$ is an automorphism, the **inner automorphism** determined by $g$. Since the centre is $\mathbb{R}$, the automorphism $\iota_g$ depends only on the class of $g$ modulo nonzero scalars, so $\iota_g = \iota_{\lambda g}$ for $\lambda \in \mathbb{R}^\times$.

**Theorem (Skolem–Noether).** For any field $k$ and $n \geq 1$, every $k$-algebra automorphism of $M_n(k)$ is inner: for each $\sigma$ there exists $g \in GL_n(k)$ with $\sigma(\tilde q) = g\tilde q g^{-1}$ for all $\tilde q$.

**Theorem.** Every $\mathbb{R}$-algebra automorphism of $\mathbb{H}_{\mathrm{s}}$ is inner, and the map

$$
\mathbb{H}_{\mathrm{s}}^\times \longrightarrow \mathrm{Aut}(\mathbb{H}_{\mathrm{s}}), \qquad g \longmapsto \iota_g,
$$

is surjective with kernel the centre $\mathbb{R}^\times$. Hence

$$
\mathrm{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathbb{H}_{\mathrm{s}}^{\times} / \mathbb{R}^\times = \mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1).
$$

**Proof.** The Skolem–Noether theorem for a central simple algebra applies: every automorphism is inner, which gives the surjectivity and the identification of the automorphism group with the quotient. The kernel of $g \mapsto \iota_g$ is the set of units $g$ with $g\tilde q = \tilde q g$ for all $\tilde q$, i.e. the units of the centre, $\mathbb{R}^\times$. The last isomorphism is the adjoint action on $V$ of *Split-Quaternion Rotations and the Lorentz Group*, which identifies $\mathrm{PGL}_2(\mathbb{R})$ with $SO(2,1)$.

**Dimension and components.** Since the unit group has real dimension $4$ and the centre $\mathbb{R}^\times$ has dimension $1$, the group has real dimension $3$. The sign of the split-quaternion norm splits the unit group into the two components $\{N>0\}$ and $\{N<0\}$, and since $N(\lambda g) = \lambda^2 N(g)$ the quotient keeps the sign of the split-quaternion norm, so $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}}) \cong PGL_2(\mathbb{R})$ has **two components**, matching the two components of $SO(2,1)$. The identity component is

$$
\mathrm{Aut}^0(\mathbb{H}_{\mathrm{s}}) \cong PSL_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1),
$$

which is also the image of the norm-one group $U = \{N = 1\}$ under $g \mapsto \iota_g$.

**Invariants.** Every automorphism preserves the split-quaternion norm, $N(\sigma(\tilde q)) = N(\tilde q)$, because $\iota_g$ is inner and $N$ is multiplicative; hence it preserves the group of units, the zero-divisor set, the rank-one idempotents and the subspaces defined by $N$. It also preserves the centre pointwise.

**Example.** For $g = e_3$, with $e_3^{-1} = e_3$ (since $N(e_3) = -1$ and $e_3^{\natural} = -e_3$, so $e_3^{-1} = -e_3/(-1) = e_3$), the inner automorphism acts on the vector subspace by $\iota_{e_3}(e_1) = -e_1$, $\iota_{e_3}(e_2) = -e_2$, $\iota_{e_3}(e_3) = e_3$, the matrix $\operatorname{diag}(-1,-1,1)$ in the basis $e_1,e_2,e_3$. This transformation is in $SO(2,1)$ but not in its identity component: it fixes the spacelike direction $e_3$ and reverses the sheet of the timelike hyperboloid.

## Derivations

**Definition.** An **$\mathbb{R}$-linear derivation** of $\mathbb{H}_{\mathrm{s}}$ is an $\mathbb{R}$-linear map $D : \mathbb{H}_{\mathrm{s}} \to \mathbb{H}_{\mathrm{s}}$ satisfying the Leibniz rule

$$
D(\tilde q y) = D(\tilde q)\,y + \tilde q\,D(y) .
$$

The derivations form a real Lie algebra under the commutator, written $\mathrm{Der}(\mathbb{H}_{\mathrm{s}})$.

**Inner derivations.** For $a \in \mathbb{H}_{\mathrm{s}}$ the map

$$
\mathrm{ad}_a : \tilde q \mapsto [a,\tilde q] = ax - xa
$$

is a derivation, the **inner derivation** by $a$, and $\mathrm{ad}_a$ depends only on the class of $a$ modulo the centre: $\mathrm{ad}_a = \mathrm{ad}_{a + z}$ for $z \in \mathbb{R}$.

**Theorem.** Every derivation of $\mathbb{H}_{\mathrm{s}}$ is inner, and the map

$$
\mathbb{H}_{\mathrm{s}} \longrightarrow \mathrm{Der}(\mathbb{H}_{\mathrm{s}}), \qquad a \longmapsto \mathrm{ad}_a,
$$

has kernel the centre $\mathbb{R}$. Hence

$$
\mathrm{Der}(\mathbb{H}_{\mathrm{s}}) = \mathrm{ad}(\mathbb{H}_{\mathrm{s}}) \cong \mathbb{H}_{\mathrm{s}}/\mathbb{R} \cong V \cong \mathrm{SL}_2(\mathbb{R}),
$$

the vector subspace $V$ **under the commutator bracket**, of real dimension $3$.

**Proof.** Every derivation of $\mathbb{H}_{\mathrm{s}}$ is inner: the standard computation, valid for any central simple $k$-algebra, shows that for a derivation $D$ the element $a = \sum_i D(u_i)v_i$ — where $\sum_i u_i v_i = 1$ is a separating idempotent decomposition — satisfies $D = \mathrm{ad}_a$. The kernel of $\mathrm{ad}$ is the centre: $[a,\tilde q] = 0$ for all $\tilde q$ iff $a \in Z = \mathbb{R}$. The image is $\mathrm{ad}(V) \cong \mathrm{SL}_2(\mathbb{R})$, since the scalar part of $a$ contributes nothing.

**Structure.** The bracket of inner derivations is again inner and satisfies $[\mathrm{ad}_a, \mathrm{ad}_b] = \mathrm{ad}_{[a,b]}$, so the map $a \mapsto \mathrm{ad}_a$ is a Lie algebra homomorphism onto $\mathrm{Der}(\mathbb{H}_{\mathrm{s}})$ with kernel the centre. Under it the bracket of $V$ computed in *Split-Quaternion Scalar and Vector Subspaces*, $[e_1,e_2] = 2e_3$, $[e_2,e_3] = -2e_1$, $[e_3,e_1] = 2e_2$, becomes the bracket of $\mathrm{SL}_2(\mathbb{R})$. In particular $\mathrm{Der}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$, the Lie algebra of the Lorentz group of the vector subspace.

**Every derivation preserves the split-quaternion norm.** Because $\mathrm{Der}$ is spanned by the inner derivations $\mathrm{ad}_a$, and each generates the one-parameter group of automorphisms $t \mapsto \exp(t\,\mathrm{ad}_a) = \mathrm{Ad}_{e^{ta}}$, which preserves $N$, the infinitesimal statement $D(N(\tilde q)) = 0$ holds for every derivation and every $\tilde q$. Every derivation therefore vanishes on the centre and annihilates the split-quaternion norm.

## Outer Automorphisms

**Proposition.** The algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ has **no outer automorphisms**: the group $\mathrm{Out}(\mathbb{H}_{\mathrm{s}}) = \mathrm{Aut}(\mathbb{H}_{\mathrm{s}})/\mathrm{Inn}(\mathbb{H}_{\mathrm{s}})$ is trivial, and every automorphism is inner.

**Proof.** By Skolem–Noether every automorphism is inner, so $\mathrm{Aut} = \mathrm{Inn}$ and the quotient is trivial.

The exceptional phenomena that produce outer automorphisms elsewhere — the outer automorphism of $M_n(\mathbb{D})$ for $n \geq 3$ over a division algebra $\mathbb{D} \neq k$, or the triality of $\mathrm{Cl}_{0,8}$ — do not occur for a $2 \times 2$ matrix algebra over a field. Thus for $\mathbb{H}_{\mathrm{s}}$ the outer automorphism group gives no new symmetry, and the whole automorphism group is the inner one, of two components.

### Anti-Automorphisms

The conjugations ${}^{\natural}$ and $\rho$ are **anti**-automorphisms, satisfying $(\tilde q y)^{\natural} = y^{\natural}\,\tilde{q}^{\natural}$, and are not automorphisms, so they do not appear in $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}})$. Together with the automorphism $\alpha$ they make up the involution group of the algebra, treated in *Split-Quaternion Involution Lattice*. In the Clifford description of *Split-Quaternion Other Algebraic Element Representations*, the two are the reversal and the Clifford conjugation; the existence of anti-automorphisms outside $\mathrm{Aut}$ is the standard asymmetry between an algebra and its opposite, and it is not an outer automorphism phenomenon.

## The Lie Algebra Statement

The three statements fit together as follows. The automorphism group is the Lie group $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$, of dimension $3$ with two components. Its identity component is $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$, with Lie algebra $\mathrm{SO}(2,1)$. The derivation algebra is $\mathrm{Der}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$, and it is exactly the Lie algebra of $\mathrm{Aut}$:

$$
\operatorname{Lie}\bigl(\mathrm{Aut}(\mathbb{H}_{\mathrm{s}})\bigr) \;=\; \mathrm{Der}(\mathbb{H}_{\mathrm{s}}) \;\cong\; \mathrm{SL}_2(\mathbb{R}) \;\cong\; \mathrm{SO}(2,1).
$$

The correspondence is the exponential of the inner derivations, $\exp(t\,\mathrm{ad}_a) = \iota_{e^{ta}}$, which is the usual Lie-theoretic identification of the inner derivations with the Lie algebra of the inner automorphism group. Since $\mathrm{Aut}$ has two components, its Lie algebra is generated by the identity component alone; the two components are distinguished by the determinant, and any automorphism of negative determinant, such as $\iota_{e_3}$ of the example above, lies in the non-identity component.

## Worked Examples

**Example (the elliptic one-parameter group).** Take $a = e_1$, so that $\mathrm{ad}_{e_1}(e_2) = [e_1,e_2] = 2e_3$ and $\mathrm{ad}_{e_1}(e_3) = [e_1,e_3] = -2e_2$, with $\mathrm{ad}_{e_1}(e_1) = 0$. The exponential $t \mapsto \exp(t\,\mathrm{ad}_{e_1})$ is the inner automorphism group generated by $e^{t e_1} = \cos t + \sin t\, e_1$ (a unit of norm $1$), which acts on $V$ as the rotation of the plane $\operatorname{span}\{e_2,e_3\}$ by the doubled angle $2t$, the elliptic subgroup of *Split-Quaternion Rotations and the Lorentz Group*.

**Example (the hyperbolic one-parameter group).** Take $a = e_2$, so that $\mathrm{ad}_{e_2}(e_1) = [e_2,e_1] = -2e_3$ and $\mathrm{ad}_{e_2}(e_3) = [e_2,e_3] = -2e_1$, with $\mathrm{ad}_{e_2}(e_2) = 0$. The exponential is generated by $e^{t e_2/2} = \cosh(t/2) + \sinh(t/2)\, e_2$ (a unit of norm $1$), acting on $V$ as a boost of the plane $\operatorname{span}\{e_1,e_3\}$ of signature $(1,1)$ fixing $e_2$.

**Example (a derivation that is not a scalar multiple of a basis one).** For $a = e_1 + e_2$ the derivation $\mathrm{ad}_a$ has $\mathrm{ad}_a(e_3) = [e_1 + e_2, e_3] = -2e_1 - 2e_2$ and mixes the two involutions' eigenspaces, so it is not proportional to any of $\mathrm{ad}_{e_1}, \mathrm{ad}_{e_2}, \mathrm{ad}_{e_3}$.

**Example (an automorphism of the outer component).** The inner automorphism $\iota_{e_3}$ of the example above has matrix $\operatorname{diag}(-1,-1,1)$ on $V$, of determinant $+1$, in the component of $SO(2,1)$ away from the identity. Its square is the identity.

## The Contrast with the Biquaternion Case

The biquaternion article *Biquaternion Automorphisms and Derivations* separates the automorphisms over $\mathbb{C}$ from those over $\mathbb{R}$, because over $\mathbb{R}$ the centre of $\mathbb{B}$ is the two-dimensional $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ and complex conjugation adds a second, conjugate-linear coset, so that $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$ is strictly larger than $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \cong PGL(2,\mathbb{C})$. For $\mathbb{H}_{\mathrm{s}}$ the centre is one-dimensional over $\mathbb{R}$ and there is no conjugation available, so the group is a single inner group, $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}}) \cong PGL_2(\mathbb{R}) \cong SO(2,1)$, with **no outer automorphisms** and no semilinear coset; the outer automorphism group, which over $\mathbb{R}$ is nontrivial for $\mathbb{B}$, is trivial here. For derivations the two cases agree in shape: all derivations are inner, and the derivation algebra is the vector subspace under the commutator, $\mathrm{SL}_2$ in both, purely real here, realified from $\mathbb{C}$ there. The complexification of $\mathbb{H}_{\mathrm{s}}$ is $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}_{\mathrm{s}} = M_2(\mathbb{C}) \cong \mathbb{B}$, so the two categories describe the same complex algebra over different real forms; the involution and automorphism picture is the part where the real forms differ.

## Summary

The split-quaternion algebra is central simple over $\mathbb{R}$, with centre the scalar line $S = \mathbb{R}\cdot1$. Every $\mathbb{R}$-algebra automorphism is inner, by Skolem–Noether, and

$$
\mathrm{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1),
$$

of dimension $3$, with identity component $\mathrm{Aut}^0 \cong \mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ and a unique nontrivial component; every automorphism preserves the split-quaternion norm and the centre. There are no outer automorphisms, $\mathrm{Out}(\mathbb{H}_{\mathrm{s}}) = 1$; the anti-automorphisms ${}^{\natural}$ and $\rho$ are not automorphisms and belong to the involution group instead.

Every derivation is inner, so $\mathrm{Der}(\mathbb{H}_{\mathrm{s}}) = \mathrm{ad}(\mathbb{H}_{\mathrm{s}}) \cong \mathbb{H}_{\mathrm{s}}/\mathbb{R} \cong V \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$, the traceless matrices under the commutator bracket, of real dimension $3$; every derivation vanishes on the centre and annihilates the split-quaternion norm, and the map $a \mapsto \mathrm{ad}_a$ has kernel the centre. The derivation algebra is the Lie algebra of the automorphism group. The contrast with the biquaternion case is exact: there the real automorphism group is strictly larger than the complex one and has a nontrivial outer part, here the group is a single inner group of dimension $3$ with two components; the two systems nevertheless share the same derivation shape, the traceless matrices under the bracket.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\mathrm{Cl}_{1,1}$ | *Split-Quaternion Algebra* |
| $Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1$ | the centre, one-dimensional over $\mathbb{R}$ | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathrm{Aut}(\mathbb{H}_{\mathrm{s}})$ | the algebra automorphisms, $\cong \mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$ | this article |
| $\mathrm{Inn}(\mathbb{H}_{\mathrm{s}})$, $\mathrm{Out}(\mathbb{H}_{\mathrm{s}})$ | inner and outer automorphism groups; $\mathrm{Out} = 1$ | this article |
| $\iota_g(\tilde q) = g\tilde q g^{-1}$ | the inner automorphism by a unit $g$ | this article |
| $\mathrm{Der}(\mathbb{H}_{\mathrm{s}})$ | the derivations, $\cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$ | this article |
| $\mathrm{ad}_a(\tilde q) = [a,\tilde q]$ | the inner derivation by $a$ | this article |
| $V, \mathrm{SL}_2(\mathbb{R})$ | the vector subspace and the traceless matrices | *Split-Quaternion Scalar and Vector Subspaces* |
| $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$ | the split-quaternion norm, invariant under automorphisms and derivations | *Split-Quaternion Norm and Invertibility* |
| $\alpha, \rho, {}^{\natural}$ | the involutions; $\rho, {}^{\natural}$ are anti-automorphisms | *Split-Quaternion Subspaces and the Involutions* |
| $U = \{N=1\}$ | the norm-one group, mapping onto $\mathrm{SO}^{+}(2,1)$ | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the Skolem–Noether theorem and the inner structure of automorphisms and derivations of a simple algebra.
- I. N. Herstein, *Noncommutative Rings*, Carus Mathematical Monographs 15 (Mathematical Association of America, 1968), for derivations of simple rings and the inner derivation theorem.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra*, Graduate Texts in Mathematics 144 (Springer, 1993), for the automorphism group of $M_n(k)$ and its outer-perturbation behaviour for other division algebras.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for automorphism and derivation computations in four-dimensional real algebras.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Graduate Texts in Mathematics 222 (Springer, 2015), for the identification of a Lie algebra with the derivations of its group.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the derivations of the low-dimensional Clifford algebras as the bivector part under the commutator.
