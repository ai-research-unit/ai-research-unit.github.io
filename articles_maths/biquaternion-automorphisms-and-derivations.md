# __Biquaternion Automorphisms and Derivations__

## Introduction

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}.
$$

It carries two structures, distinguished by the ground field. Over $\mathbb{C}$ it is a four-dimensional central simple algebra; over $\mathbb{R}$ the same set is an eight-dimensional algebra, simple but not central. This article describes the group of algebra **automorphisms** of $\mathbb{B}$; the **derivations**, which are its Lie algebra and its infinitesimal symmetries, are in *Biquaternion Lie Algebra*, §*The Derivation Algebra*, and are cited here rather than restated. Both invariants depend on the ground field, so the field is named at each step.

We use the conventions of the article on the biquaternion algebra throughout: the basis $\{e_0, e_1, e_2, e_3\}$ with $e_k^2 = -e_0$; the central scalar imaginary $i$ with $i^2 = -1$; the conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = \bar{\cdot} \circ {}^{*}$, ${}^{\flat} = -{}^{\dagger}$; and the six distinguished subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$. A general element is $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu \in \mathbb{C}$.

No physics is invoked and no new results are claimed. Everything below is standard structure theory of the algebra over each of the two ground fields.

## Standing Facts: Simplicity and the Centre
The automorphism group and the derivation algebra of $\mathbb{B}$ are governed by two structural facts, recorded here and used throughout. Both are proved elsewhere and are cited, not reproved.

**Simplicity.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$: the algebra is **simple**. The proof is in *Biquaternion Ideals and Peirce Decomposition*, §*The Two-Sided Ideals: Simplicity of $\mathbb{B}$*, where the ideal structure of the algebra is developed; the lattice is the same over $\mathbb{R}$ and over $\mathbb{C}$, because the condition $xy,yx\in I$ is field-independent.

**The centre.** The centre of $\mathbb{B}$ is $Z(\mathbb{B})=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, a complex vector space of dimension $1$, the subspace $\mathbb{C}_{\mathbb{B}}$ of *Biquaternion Algebra*. Hence $\mathbb{B}$ is **central simple over $\mathbb{C}$** — simple, of dimension $4$, with centre exactly $\mathbb{C}$ — while over $\mathbb{R}$ the same algebra is simple but **not central**, its centre $\mathbb{C}_{\mathbb{B}}\cong\mathbb{C}$ being strictly larger than $\mathbb{R}e_0$. Stating that "$\mathbb{B}$ is central simple" without naming the field is false over $\mathbb{R}$, and the sections below respect the distinction.

## Automorphisms over $\mathbb{C}$

Throughout this section the ground field is $\mathbb{C}$.

**Definition.** A **$\mathbb{C}$-algebra automorphism** of $\mathbb{B}$ is a bijective $\mathbb{C}$-linear map $\sigma : \mathbb{B} \to \mathbb{B}$ with $\sigma(xy) = \sigma(x)\sigma(y)$ and $\sigma(e_0) = e_0$. These maps form a group under composition, written $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$.

**Inner automorphisms.** For any invertible $g \in \mathbb{B}$ the map $\iota_g(x) = g x g^{-1}$ is a $\mathbb{C}$-algebra automorphism, the **inner automorphism** determined by $g$. Since $\mathbb{C}$ is central, $\iota_g = \iota_{\lambda g}$ for every nonzero $\lambda \in \mathbb{C}$, so $\iota_g$ depends only on the class of $g$ modulo the scalars.

**Theorem (Skolem–Noether).** For any field $k$ and $n \geq 1$, every $k$-algebra automorphism of $M_n(k)$ is inner: for each $\sigma$ there exists $g \in GL_n(k)$ with $\sigma(x) = gxg^{-1}$ for all $x$.

Applied to $\mathbb{B}$, which is central simple over $\mathbb{C}$, the theorem says that **every $\mathbb{C}$-linear automorphism of $\mathbb{B}$ is inner**: each has the form $\iota_g$ for an invertible $g \in \mathbb{B}^{\times}$. Since $\iota_g$ depends only on $g$ modulo the central scalars, there is a surjection

$$
\mathbb{B}^{\times} \longrightarrow \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}), \qquad g \longmapsto \iota_g,
$$

whose kernel is the group of nonzero central scalars $\mathbb{C}^{\times} e_0$. Hence

$$
\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \cong \mathbb{B}^{\times} / \mathbb{C}^{\times} .$$

**Dimension.** Since $\mathbb{B}^{\times}$ has complex dimension $4$ and the central scalars have complex dimension $1$, $\dim_{\mathbb{C}} \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = 4 - 1 = 3$. Equivalently, the group has real dimension $6$, and it is connected.

**Corollary (the projective linear group).** Under the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ the units are $GL(2,\mathbb{C})$ and the nonzero central scalars are the scalar matrices, so
$$
\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C}),
$$
the projective general linear group, of complex dimension three. This is the biquaternion form of the classical isomorphism $\operatorname{Aut}(M_n(k))\cong PGL(n,k)$.

**Corollary (the norm).** Every $\mathbb{C}$-linear automorphism preserves the biquaternion norm, and every $\mathbb{R}$-linear automorphism preserves the real norm $r=\sqrt{|N|}$. For an inner automorphism the complex statement is multiplicativity, $N(g\tilde{Q}g^{-1})=N(g)N(\tilde{Q})N(g)^{-1}=N(\tilde{Q})$; complex conjugation reverses the sign of the imaginary part, $N(\tilde{Q}^{*})=N(\tilde{Q})^{*}$, and so preserves $|N|$ without preserving $N$ itself.

**Remark (automorphisms against isometries).** The automorphism group is a proper subgroup of the full isometry group $O(N)$ of the real norm on $\mathbb{B}\cong\mathbb{R}^8$: $PGL(2,\mathbb{C})$ has real dimension $6$, whereas the isometry group of a non-degenerate form of signature $(4,4)$ on $\mathbb{R}^8$ has real dimension $\tfrac{8\cdot7}{2}=28$. The automorphisms are the isometries that also preserve the algebra; the further isometries are not algebra maps.

**Example.** For $g = e_1$, with $e_1^{-1} = -e_1$, conjugation fixes $e_1$, $e_0$, $i$ and reverses the signs of $e_2$ and $e_3$: $\iota_{e_1}(e_1) = e_1$, $\iota_{e_1}(e_2) = -e_2$, $\iota_{e_1}(e_3) = -e_3$. Indeed $e_1 e_2 e_1^{-1} = -(e_1 e_2)e_1 = -e_3 e_1 = -e_2$, using $e_1 e_2 = e_3$ and $e_3 e_1 = e_2$.

**Remark.** Quaternion conjugation satisfies $\overline{xy} = \bar{y}\,\bar{x}$ and is an **anti-automorphism**, not an automorphism, so it is not in $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$; complex conjugation is an automorphism but is not $\mathbb{C}$-linear, so it is not in $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ either. It reappears over $\mathbb{R}$ below.

## Automorphisms over $\mathbb{R}$

Now the ground field is $\mathbb{R}$: $\mathbb{B}$ is eight-dimensional, and automorphisms need only be $\mathbb{R}$-linear, not $\mathbb{C}$-linear, which makes the group strictly larger.

**Automorphisms preserve the center.** If $\sigma$ is an $\mathbb{R}$-algebra automorphism and $z$ is central, then $\sigma(z)\sigma(x) = \sigma(zx) = \sigma(xz) = \sigma(x)\sigma(z)$ for every $x$, so $\sigma(z)$ is central. Thus $\sigma$ restricts to an $\mathbb{R}$-algebra automorphism of $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$; since $\mathbb{C}$ as a real algebra has exactly two automorphisms, the identity and $\kappa(z) = z^{*}$, restriction gives a homomorphism $\rho : \mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \to \mathrm{Aut}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}}) = \{\mathrm{id}, \kappa\} \cong \mathbb{Z}/2$.

**The kernel is the $\mathbb{C}$-linear part.** An automorphism lies in $\ker \rho$ exactly when it fixes the center pointwise, and an $\mathbb{R}$-linear map fixing $\mathbb{C}_{\mathbb{B}}$ pointwise is automatically $\mathbb{C}$-linear, since it commutes with multiplication by the central element $i$. Hence $\ker \rho = \mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$, the group computed above; these are precisely the inner automorphisms, by Skolem–Noether.

**The conjugation coset.** The map $\rho$ is surjective: $c(\tilde{Q}) = \tilde{Q}^{*}$ is an $\mathbb{R}$-algebra automorphism, since $(xy)^{*} = x^{*}y^{*}$, and it induces $\kappa$ on the center, since $c(i) = -i$. It is not $\mathbb{C}$-linear, and it is not inner, because inner automorphisms fix the center pointwise while $c(i) = -i \neq i$. So the extension is nontrivial.

**The full real automorphism group.** There is a short exact sequence $1 \to \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \to \mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \xrightarrow{\rho} \mathbb{Z}/2 \to 1$, split by $c$ because $c^{2} = \mathrm{id}$. Hence

$$
\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \rtimes \mathbb{Z}/2,
$$

the generator acting on $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ by $\iota_g \mapsto \iota_{g^{*}}$. Concretely, every real automorphism of $\mathbb{B}$ has exactly one of the two forms $\sigma(x) = g x g^{-1}$ or $\sigma(x) = g\, x^{*}\, g^{-1}$, with $g \in \mathbb{B}^{\times}$ determined up to a nonzero complex scalar. The first family is the identity coset of $\mathbb{C}$-linear inner automorphisms; the second is the coset of $c$, consisting of **conjugate-linear** automorphisms.

**Dimension and scope.** As a real Lie group, $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})$ has real dimension $6$ and exactly two connected components, each a copy of $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$; it is larger and is a real group rather than a complex one. Skolem–Noether describes the identity component $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$; the conjugate-linear coset exists because $\mathbb{C}/\mathbb{R}$ has a nontrivial Galois automorphism, and it is not inner.

## Summary

The two ground fields give the following table; the field is stated explicitly in every entry.

| Structure | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Algebra | simple $\mathbb{C}$-algebra, complex dimension $4$ | simple $\mathbb{R}$-algebra, real dimension $8$ |
| Ideals | $\{0\}$ and $\mathbb{B}$ only | $\{0\}$ and $\mathbb{B}$ only |
| Center | $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$, dimension $1$ over $\mathbb{C}$ | $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$, dimension $2$ over $\mathbb{R}$ |
| Central simple? | yes, central simple over $\mathbb{C}$ | no: simple, but center $\mathbb{C} \neq \mathbb{R}$ |
| Automorphism group | $\mathbb{B}^{\times}/\mathbb{C}^{\times}$, complex dimension $3$ ($6$ over $\mathbb{R}$), connected | $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \rtimes \mathbb{Z}/2$, real dimension $6$, two components |

In summary: over $\mathbb{C}$ the algebra is central simple, every automorphism is inner, and $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \cong \mathbb{B}^{\times}/\mathbb{C}^{\times}$; over $\mathbb{R}$ complex conjugation adds a second, conjugate-linear coset, so $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \rtimes \mathbb{Z}/2$ is strictly larger. The derivations, the Lie algebra of this group, are the inner derivations $x \mapsto [a,x]$ with $a$ traceless; they are in *Biquaternion Lie Algebra*, §*The Derivation Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; complex dimension $4$, real dimension $8$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of $\mathbb{B}$; the scalar subspace |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, vanishing scalar part |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | Real-quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ | Algebra automorphisms over $\mathbb{C}$, $\cong \mathbb{B}^{\times}/\mathbb{C}^{\times}$ |
| $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})$ | Algebra automorphisms over $\mathbb{R}$, $\cong \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \rtimes \mathbb{Z}/2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88, Springer, 1982.
- I. N. Herstein, *Noncommutative Rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra*, Graduate Texts in Mathematics 144, Springer, 1993.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294, Springer, 1991.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129, Springer, 1991.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition, Cambridge University Press, 2001.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition, Graduate Texts in Mathematics 222, Springer, 2015.
