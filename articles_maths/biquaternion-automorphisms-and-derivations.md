# __Biquaternion Automorphisms and Derivations__

## Introduction

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}.
$$

It carries two structures, distinguished by the ground field. Over $\mathbb{C}$ it is a four-dimensional algebra isomorphic to $M_2(\mathbb{C})$; over $\mathbb{R}$ the same set is an eight-dimensional algebra isomorphic to $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$. This article describes two standard invariants of $\mathbb{B}$: the group of algebra **automorphisms** and the Lie algebra of **derivations**. Both depend on the ground field, so the two views are kept separate and the field is named at each step.

We use the conventions of the article on the biquaternion algebra throughout: the basis $\{e_0, e_1, e_2, e_3\}$ with $e_k^2 = -e_0$; the central scalar imaginary $i$ with $i^2 = -1$; the conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = \bar{\cdot} \circ {}^{*}$, ${}^{\flat} = -{}^{\dagger}$; and the six distinguished subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$. A general element is $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu \in \mathbb{C}$.

No physics is invoked and no new results are claimed. Everything below is standard structure theory of the algebra $M_2(\mathbb{C})$ and of its real form $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$.

## 1. Ideal Structure and Central Simplicity

Before automorphisms and derivations, we record the ideal structure, because both invariants are governed by it.

**Definition.** A **two-sided ideal** of $\mathbb{B}$ is a vector subspace $I \subseteq \mathbb{B}$ with $xy, yx \in I$ for all $x \in \mathbb{B}$, $y \in I$. An algebra is **simple** if its only two-sided ideals are $\{0\}$ and itself.

The ideal lattice of $\mathbb{B}$ is the same over $\mathbb{R}$ and over $\mathbb{C}$, because the conditions $xy, yx \in I$ are field-independent.

**The ideals of $\mathbb{B}$ are only $\{0\}$ and $\mathbb{B}$.** Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$, ideals correspond to ideals. The matrix algebra $M_2(\mathbb{C})$ is simple: a nonzero two-sided ideal contains a nonzero matrix, and multiplying that matrix by matrix units on the left and right produces every matrix unit, hence the whole algebra. Therefore $\mathbb{B}$ has no nonzero proper two-sided ideal.

**The center.** The center of $\mathbb{B}$ is $Z(\mathbb{B}) = \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$, a complex vector space of dimension $1$ in the $\mathbb{C}$-algebra view. In the $\mathbb{R}$-algebra view the same center is the real vector space $\mathbb{C}_{\mathbb{B}} = \mathbb{R} e_0 \oplus \mathbb{R}(i e_0)$, of real dimension $2$ and isomorphic to $\mathbb{C}$ as a real algebra.

**Central simplicity, in the correct ground field.** An algebra is **central** over a field $F$ if its center equals $F \cdot 1$, and **central simple** if in addition it is simple. Therefore:

- Over $\mathbb{C}$, the algebra $\mathbb{B}$ is central simple: it is simple, of dimension $4$, and its center is $\mathbb{C} \cdot e_0 = \mathbb{C}$.
- Over $\mathbb{R}$, the algebra $\mathbb{B}$ is simple but **not central**, because its center $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ is strictly larger than $\mathbb{R} \cdot e_0$. Equivalently, $\mathbb{B}$ is an Azumaya algebra over its center $\mathbb{C}_{\mathbb{B}}$, not over $\mathbb{R}$.

Stating that "$\mathbb{B}$ is central simple" without naming the field $\mathbb{C}$ would be false over $\mathbb{R}$, and the sections below respect this distinction. The algebra is simple but is **not** a division algebra, since it has zero divisors; by Wedderburn–Artin a finite-dimensional simple unital algebra over an algebraically closed field is a full matrix algebra, and here it is $M_2(\mathbb{C})$, of dimension $4 = 2^2$.

## 2. Automorphisms over $\mathbb{C}$

Throughout this section the ground field is $\mathbb{C}$.

**Definition.** A **$\mathbb{C}$-algebra automorphism** of $\mathbb{B}$ is a bijective $\mathbb{C}$-linear map $\sigma : \mathbb{B} \to \mathbb{B}$ with $\sigma(xy) = \sigma(x)\sigma(y)$ and $\sigma(e_0) = e_0$. These maps form a group under composition, written $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$.

**Inner automorphisms.** For any invertible $g \in \mathbb{B}$ the map $\iota_g(x) = g x g^{-1}$ is a $\mathbb{C}$-algebra automorphism, the **inner automorphism** determined by $g$. Since $\mathbb{C}$ is central, $\iota_g = \iota_{\lambda g}$ for every nonzero $\lambda \in \mathbb{C}$, so $\iota_g$ depends only on the class of $g$ modulo the scalars.

**Theorem (Skolem–Noether).** For any field $k$ and $n \geq 1$, every $k$-algebra automorphism of $M_n(k)$ is inner: for each $\sigma$ there exists $g \in GL_n(k)$ with $\sigma(x) = gxg^{-1}$ for all $x$.

Applied to $\mathbb{B} \cong M_2(\mathbb{C})$, the theorem says that **every $\mathbb{C}$-linear automorphism of $\mathbb{B}$ is inner**. Under the identification of invertible biquaternions with $GL_2(\mathbb{C})$, this gives a surjection

$$
GL_2(\mathbb{C}) \longrightarrow \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}), \qquad g \longmapsto \iota_g,
$$

whose kernel is the group of scalar matrices $\mathbb{C}^{*} I$. Hence

$$
\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) \cong GL_2(\mathbb{C}) / \mathbb{C}^{*} = PGL(2,\mathbb{C}).
$$

Because $\mathbb{C}$ is algebraically closed, every scalar is a square and every element of $GL_2(\mathbb{C})$ can be scaled to determinant $1$, so $PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$ and $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$.

**Dimension.** Since $GL_2(\mathbb{C})$ has complex dimension $4$ and $\mathbb{C}^{*}$ has complex dimension $1$, $\dim_{\mathbb{C}} \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = 4 - 1 = 3$. Equivalently, the group has real dimension $6$, and it is connected.

**Example.** For $g = e_1$, with $e_1^{-1} = -e_1$, conjugation fixes $e_1$, $e_0$, $i$ and reverses the signs of $e_2$ and $e_3$: $\iota_{e_1}(e_1) = e_1$, $\iota_{e_1}(e_2) = -e_2$, $\iota_{e_1}(e_3) = -e_3$. Indeed $e_1 e_2 e_1^{-1} = -(e_1 e_2)e_1 = -e_3 e_1 = -e_2$, using $e_1 e_2 = e_3$ and $e_3 e_1 = e_2$.

**Remark.** Quaternion conjugation satisfies $\overline{xy} = \bar{y}\,\bar{x}$ and is an **anti-automorphism**, not an automorphism, so it is not in $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$; complex conjugation is an automorphism but is not $\mathbb{C}$-linear, so it is not in $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ either. It reappears over $\mathbb{R}$ below.

## 3. Automorphisms over $\mathbb{R}$

Now the ground field is $\mathbb{R}$: $\mathbb{B}$ is eight-dimensional, and automorphisms need only be $\mathbb{R}$-linear, not $\mathbb{C}$-linear, which makes the group strictly larger.

**Automorphisms preserve the center.** If $\sigma$ is an $\mathbb{R}$-algebra automorphism and $z$ is central, then $\sigma(z)\sigma(x) = \sigma(zx) = \sigma(xz) = \sigma(x)\sigma(z)$ for every $x$, so $\sigma(z)$ is central. Thus $\sigma$ restricts to an $\mathbb{R}$-algebra automorphism of $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$; since $\mathbb{C}$ as a real algebra has exactly two automorphisms, the identity and $\kappa(z) = z^{*}$, restriction gives a homomorphism $\rho : \mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \to \mathrm{Aut}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}}) = \{\mathrm{id}, \kappa\} \cong \mathbb{Z}/2$.

**The kernel is the $\mathbb{C}$-linear part.** An automorphism lies in $\ker \rho$ exactly when it fixes the center pointwise, and an $\mathbb{R}$-linear map fixing $\mathbb{C}_{\mathbb{B}}$ pointwise is automatically $\mathbb{C}$-linear, since it commutes with multiplication by the central element $i$. Hence $\ker \rho = \mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C})$, the group computed above; these are precisely the inner automorphisms, by Skolem–Noether.

**The conjugation coset.** The map $\rho$ is surjective: $c(\tilde{Q}) = \tilde{Q}^{*}$ is an $\mathbb{R}$-algebra automorphism, since $(xy)^{*} = x^{*}y^{*}$, and it induces $\kappa$ on the center, since $c(i) = -i$. It is not $\mathbb{C}$-linear, and it is not inner, because inner automorphisms fix the center pointwise while $c(i) = -i \neq i$. So the extension is nontrivial.

**The full real automorphism group.** There is a short exact sequence $1 \to PGL(2,\mathbb{C}) \to \mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \xrightarrow{\rho} \mathbb{Z}/2 \to 1$, split by $c$ because $c^{2} = \mathrm{id}$. Hence

$$
\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2,
$$

the generator acting on $PGL(2,\mathbb{C})$ by $\iota_g \mapsto \iota_{g^{*}}$. Concretely, every real automorphism of $\mathbb{B}$ has exactly one of the two forms $\sigma(x) = g x g^{-1}$ or $\sigma(x) = g\, x^{*}\, g^{-1}$, with $g \in GL_2(\mathbb{C})$ determined up to a nonzero complex scalar. The first family is the identity coset of $\mathbb{C}$-linear inner automorphisms; the second is the coset of $c$, consisting of **conjugate-linear** automorphisms.

**Dimension and scope.** As a real Lie group, $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})$ has real dimension $6$ and exactly two connected components, each a copy of $PGL(2,\mathbb{C})$; it is larger than $PGL(2,\mathbb{C})$ and is a real group rather than a complex one. Skolem–Noether describes the identity component $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C})$; the conjugate-linear coset exists because $\mathbb{C}/\mathbb{R}$ has a nontrivial Galois automorphism, and it is not inner.

## 4. Derivations over $\mathbb{C}$

Throughout this section the ground field is $\mathbb{C}$.

**Definition.** A **$\mathbb{C}$-linear derivation** of $\mathbb{B}$ is a $\mathbb{C}$-linear map $D : \mathbb{B} \to \mathbb{B}$ with $D(xy) = D(x)\,y + x\,D(y)$ for all $x, y \in \mathbb{B}$. The set of all such maps is a complex vector space, written $\mathrm{Der}_{\mathbb{C}}(\mathbb{B})$, and it is a Lie algebra under the commutator bracket $[D_1, D_2] = D_1 \circ D_2 - D_2 \circ D_1$.

Every derivation satisfies $D(e_0) = 0$, since $D(e_0) = D(e_0 e_0) = 2D(e_0)$.

**Inner derivations.** For each $a \in \mathbb{B}$ the map $\mathrm{ad}_a(x) = a x - x a = [a, x]$ is a $\mathbb{C}$-linear derivation, the **inner derivation** determined by $a$; the Jacobi identity in the form $[[a,x],y] + [x,[a,y]] = [a,[x,y]]$ is exactly the Leibniz rule for $\mathrm{ad}_a$. The map $\mathrm{ad} : \mathbb{B} \to \mathrm{Der}_{\mathbb{C}}(\mathbb{B})$, $a \mapsto \mathrm{ad}_a$, is $\mathbb{C}$-linear with kernel the center, since $\mathrm{ad}_a = 0$ says exactly that $a$ commutes with everything: $\ker(\mathrm{ad}) = Z(\mathbb{B}) = \mathbb{C}_{\mathbb{B}}$.

**Every derivation is inner.** For a central simple algebra over a field, and in particular for $M_2(\mathbb{C})$, every derivation is inner; for a matrix algebra this follows from a computation with matrix units. Hence $\mathrm{ad}$ is surjective and induces a $\mathbb{C}$-linear isomorphism

$$
\mathrm{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathbb{B} / \mathbb{C}_{\mathbb{B}}.
$$

**Identification with the traceless part.** Under $\mathbb{B} \cong M_2(\mathbb{C})$ the trace is $\mathrm{Tr}(\tilde{Q}) = 2Q_0$, so $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$ is the **traceless part** of $M_2(\mathbb{C})$, that is, $\mathfrak{sl}(2,\mathbb{C})$, a complex vector space of dimension $3$. Equivalently it is the subspace of vanishing scalar part $\{\tilde{Q} : Q_0 = 0\} = \mathrm{span}_{\mathbb{C}}\{e_1, e_2, e_3\}$, the **complex pure-vector part** of $\mathbb{B}$. The isomorphism is one of Lie algebras, because $[\mathrm{ad}_a, \mathrm{ad}_b] = \mathrm{ad}_{[a,b]}$.

**Dimension.** The derivation space has $\dim_{\mathbb{C}} \mathrm{Der}_{\mathbb{C}}(\mathbb{B}) = 3$, hence real dimension $6$. This matches the automorphism group: $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C})$ also has complex dimension $3$, and $\mathfrak{sl}(2,\mathbb{C})$ is its Lie algebra.

**The bivector reading.** Under the identification $\mathbb{B} \cong \mathrm{Cl}^{+}_{1,3}$, the real span $\mathrm{span}_{\mathbb{R}}\{e_1, e_2, e_3, i e_1, i e_2, i e_3\}$ is the six-dimensional **bivector subspace**, the real form of the complex pure-vector part, and its elements bracket into themselves. Thus the derivation algebra, viewed as a real Lie algebra, is the bivector part of $\mathrm{Cl}^{+}_{1,3}$, equivalently the realification $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ of real dimension $6$, which is the Lie algebra of the Lorentz group. The traceless part, the complex pure-vector part, and the bivector part are three descriptions of one object, with $\dim_{\mathbb{R}} = 2 \dim_{\mathbb{C}}$.

**An explicit basis.** The three derivations $D_1 = \tfrac{1}{2}\mathrm{ad}_{e_1}$, $D_2 = \tfrac{1}{2}\mathrm{ad}_{e_2}$, $D_3 = \tfrac{1}{2}\mathrm{ad}_{e_3}$ are $\mathbb{C}$-linear, so each vanishes on $e_0$ and on $i$, and they act on $e_1, e_2, e_3$ by

$$
D_1(e_2) = e_3, \quad D_1(e_3) = -e_2; \qquad D_2(e_3) = e_1, \quad D_2(e_1) = -e_3; \qquad D_3(e_1) = e_2, \quad D_3(e_2) = -e_1,
$$

with $D_1(e_1) = D_2(e_2) = D_3(e_3) = 0$. They satisfy the standard $\mathfrak{su}(2)$ commutation relations,

$$
[D_1, D_2] = D_3, \qquad [D_2, D_3] = D_1, \qquad [D_3, D_1] = D_2,
$$

so $\{D_1, D_2, D_3\}$ is a complex basis of $\mathrm{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})$. For instance $D_1(e_2) = \tfrac{1}{2}(e_1 e_2 - e_2 e_1) = \tfrac{1}{2}(e_3 + e_3) = e_3$, and $[D_1, D_2] = \tfrac{1}{4}\mathrm{ad}_{[e_1,e_2]} = \tfrac{1}{4}\mathrm{ad}_{2e_3} = D_3$.

**Derivations and automorphisms.** The two structures are linked by the exponential: $\exp(t\,\mathrm{ad}_a)(x) = e^{ta}\, x\, e^{-ta}$ for $a \in \mathbb{B}$, $t \in \mathbb{R}$. The right-hand side is the inner automorphism determined by $e^{ta}$, so the Lie algebra of the automorphism group is the derivation algebra, $\mathrm{Lie}\,\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = \mathrm{Der}_{\mathbb{C}}(\mathbb{B}) = \mathfrak{sl}(2,\mathbb{C})$.

## 5. Derivations over $\mathbb{R}$

Now the ground field is $\mathbb{R}$. An $\mathbb{R}$-linear derivation is required to satisfy the Leibniz rule but need not be $\mathbb{C}$-linear. At first sight this seems to allow a larger space, but in fact it does not.

**Every real derivation is automatically $\mathbb{C}$-linear.** Let $D$ be an $\mathbb{R}$-linear derivation. As in the automorphism case, $D$ maps the center into itself: if $z$ is central, then for every $x$,

$$
D(z)x = D(zx) - zD(x) = D(xz) - D(x)z = xD(z).
$$

So $D$ restricts to a derivation $\mathbb{C}_{\mathbb{B}} \to \mathbb{C}_{\mathbb{B}}$. But $\mathbb{C}$ has no nonzero $\mathbb{R}$-linear derivations: a derivation of $\mathbb{C}$ is determined by $D(i)$, and $0 = D(-1) = D(i^{2}) = i\,D(i) + D(i)\,i = 2i\,D(i)$ forces $D(i) = 0$, hence $D$ vanishes on the center. Since $i$ is central, the Leibniz rule then gives $D(i x) = D(i)\,x + i\,D(x) = i\,D(x)$, so $D$ is $\mathbb{C}$-linear. Therefore $\mathrm{Der}_{\mathbb{R}}(\mathbb{B}) = \mathrm{Der}_{\mathbb{C}}(\mathbb{B})$.

There is no semilinear analogue for derivations: a derivation cannot conjugate a coefficient.

**Dimension and structure.** Consequently the real derivation space has real dimension $6$, that is, complex dimension $3$, and $\mathrm{Der}_{\mathbb{R}}(\mathbb{B}) = \mathrm{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$, the realification of $\mathfrak{sl}(2,\mathbb{C})$. As a real Lie algebra this is the orthogonal Lie algebra $\mathfrak{so}(1,3)$ of the Lorentz group, equivalently the bivector subspace of $\mathrm{Cl}^{+}_{1,3}$ under the commutator. The derivations $D_1, D_2, D_3$ of the previous section span it over $\mathbb{C}$, and together with $iD_1, iD_2, iD_3$ over $\mathbb{R}$.

**Summary of the asymmetry.** For **automorphisms**, the real group is strictly larger than the complex one, because complex conjugation supplies a second coset. For **derivations**, the real and complex spaces coincide, because the center is étale over $\mathbb{R}$ and admits no nonzero derivation. This is a ground-field distinction and not a convention.

## 6. Worked Examples

**The conjugation involution.** Complex conjugation $c(\tilde{Q}) = \tilde{Q}^{*}$ is an $\mathbb{R}$-algebra automorphism with $c(e_k) = e_k$ ($k = 0,1,2,3$) and $c(i) = -i$; it fixes the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ pointwise, negates the scalar imaginary, satisfies $c^{2} = \mathrm{id}$, preserves the product, and is conjugate-linear over $\mathbb{C}$. It is not inner, because inner automorphisms fix the center pointwise whereas $c(i) = -i$, so it represents the nontrivial coset of $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ in $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})$.

**A rotation derivation.** Take $D = D_3 = \tfrac{1}{2}\mathrm{ad}_{e_3}$, so that $D(e_1) = e_2$ and $D(e_2) = -e_1$. Its exponential acts by

$$
\exp(tD)(e_1) = \cos t\, e_1 + \sin t\, e_2,
$$

as one checks by summing the series. Equivalently, $e^{t e_3/2} = \cos(t/2) + \sin(t/2) e_3$, and conjugation by this unit quaternion rotates the $e_1$-$e_2$ plane, matching $\exp(t D) = \mathrm{Ad}_{e^{t e_3/2}}$.

Every element of $\mathrm{span}_{\mathbb{C}}\{e_1, e_2, e_3\}$ gives an inner derivation, and $\mathrm{ad}_a$ depends only on $a$ modulo the center $\mathbb{C}_{\mathbb{B}}$; for instance $a = e_1 + i e_2$ gives a derivation that is not a scalar multiple of any $D_k$.

## Summary

The two ground fields give the following table; the field is stated explicitly in every entry.

| Structure | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Algebra | $M_2(\mathbb{C})$, complex dimension $4$ | $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, real dimension $8$ |
| Ideals | $\{0\}$ and $\mathbb{B}$ only | $\{0\}$ and $\mathbb{B}$ only |
| Center | $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$, dimension $1$ over $\mathbb{C}$ | $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$, dimension $2$ over $\mathbb{R}$ |
| Central simple? | yes, central simple over $\mathbb{C}$ | no: simple, but center $\mathbb{C} \neq \mathbb{R}$ |
| Automorphism group | $PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$, complex dimension $3$ ($6$ over $\mathbb{R}$), connected | $PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$, real dimension $6$, two components |
| Derivation space (the Lie algebra of the automorphism group) | $\mathrm{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})$, complex dimension $3$ ($6$ over $\mathbb{R}$); traceless part, complex pure-vector part, bivectors | $\mathrm{Der}_{\mathbb{R}}(\mathbb{B}) = \mathrm{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}} \cong \mathfrak{so}(1,3)$, real dimension $6$ |

In summary: over $\mathbb{C}$ the algebra is central simple, every automorphism is inner, and $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$; over $\mathbb{R}$ complex conjugation adds a second, conjugate-linear coset, so $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$ is strictly larger; and over either field the derivations are the inner derivations $x \mapsto [a,x]$ with $a$ traceless, forming $\mathfrak{sl}(2,\mathbb{C})$, of dimension $3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$, identified with the bivector part of $\mathrm{Cl}^{+}_{1,3}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; $M_2(\mathbb{C})$ over $\mathbb{C}$, real dimension $8$ over $\mathbb{R}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of $\mathbb{B}$; the scalar subspace |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, vanishing scalar part |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | Real-quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})$ | Algebra automorphisms over $\mathbb{C}$: $PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$ |
| $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B})$ | Algebra automorphisms over $\mathbb{R}$: $PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$ |
| $\mathrm{Der}_{\mathbb{C}}(\mathbb{B})$ | Derivations over $\mathbb{C}$, $\cong \mathfrak{sl}(2,\mathbb{C})$ |
| $\mathrm{Der}_{\mathbb{R}}(\mathbb{B})$ | Derivations over $\mathbb{R}$, $\cong \mathfrak{sl}(2,\mathbb{C})$ as a real Lie algebra, $\cong \mathfrak{so}(1,3)$ |
| $\mathrm{ad}_a(x) = [a,x]$ | Inner derivation by $a$ |
| $D_k = \tfrac{1}{2}\mathrm{ad}_{e_k}$ | Basis of $\mathrm{Der}_{\mathbb{C}}(\mathbb{B})$, $[D_1,D_2] = D_3$ etc. |
| $\mathrm{Cl}_{1,3}^{+}$ | Even Clifford algebra; isomorphic to $\mathbb{B}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88, Springer, 1982.
- I. N. Herstein, *Noncommutative Rings*, Carus Mathematical Monographs 15, Mathematical Association of America, 1968.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra*, Graduate Texts in Mathematics 144, Springer, 1993.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294, Springer, 1991.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129, Springer, 1991.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition, Cambridge University Press, 2001.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition, Graduate Texts in Mathematics 222, Springer, 2015.
