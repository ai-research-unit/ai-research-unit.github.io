
# __Split-Biquaternion Automorphisms and Derivations__

## Introduction

The **split biquaternion algebra** is $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$, an eight-dimensional real algebra isomorphic to $\mathbb{H} \oplus \mathbb{H}$. It carries two structures distinguished by the ground ring: over the split complex algebra $\mathbb{D}$ it is a free $\mathbb{D}$-algebra of rank $4$, and over $\mathbb{R}$ the same set is an eight-dimensional real algebra. This article describes its algebra **automorphisms** and its **derivations**, over each ground structure, and compares them with the biquaternion case. The algebra and its decomposition are used from *Split-Biquaternion Algebra* and *Split-Biquaternion Ideals and Peirce Decomposition*; the split complex unit and the idempotents are those of *Split-Complex Algebra*.

We use the conventions of the split biquaternion algebra: the basis $\{e_0,e_1,e_2,e_3\}$ with $e_k^2 = -e_0$; the central split complex unit $j$ with $j^2 = +1$; the idempotents $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$; the conjugations $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = {}^{*}\bar{\cdot}$, ${}^{\flat} = -{}^{\dagger}$; and the four distinguished subspaces $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{M}_+$, $\mathbb{M}_-$. A general element is $\tilde{Q} = A + jB$ with $A, B \in \mathbb{H}$.

No physics is invoked and no new results are claimed. Everything below is the standard structure theory of a product of two quaternion algebras.

## Standing Facts: the Centre and the Two Halves

Two structural facts govern the whole article.

**The centre.** The centre of $\mathbb{H}_{\mathbb{D}}$ is $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{D} e_0 = \mathrm{span}_{\mathbb{R}}\{e_0, je_0\}$, a real two-dimensional algebra isomorphic to $\mathbb{D}$, with the idempotents $\tilde\Pi_\pm$ as its two nontrivial idempotents. Hence $\mathbb{H}_{\mathbb{D}}$ is **not** central over $\mathbb{R}$: its centre is strictly larger than $\mathbb{R}e_0$.

**The two halves.** The algebra is a product of two copies of the quaternion division algebra, $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$, the isomorphism sending $\tilde{Q}$ to the pair $(\tilde{Q}_+, \tilde{Q}_-)$ of its idempotent components. It is **semisimple but not simple**: the two factors are its minimal two-sided ideals. Every automorphism and every derivation must respect this splitting, up to the one permutation that interchanges the two factors.

## Automorphisms over the Split Complex Numbers

Throughout this section the ground ring is $\mathbb{D}$, and an automorphism is $\mathbb{D}$-linear.

**Definition.** A **$\mathbb{D}$-algebra automorphism** of $\mathbb{H}_{\mathbb{D}}$ is a bijective $\mathbb{D}$-linear map $\sigma$ with $\sigma(xy) = \sigma(x)\sigma(y)$ and $\sigma(1) = 1$. These maps form a group $\mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}})$.

**Theorem.** $\mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) \cong SO(3) \times SO(3)$.

**Proof.** A $\mathbb{D}$-linear automorphism fixes the centre $\mathbb{D}$ pointwise, hence fixes the idempotents $\tilde\Pi_\pm$ and preserves each of the two factors $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$. On each factor it is an $\mathbb{R}$-algebra automorphism of $\mathbb{H}$, and every such automorphism is inner, by the Skolem–Noether theorem for the division algebra $\mathbb{H}$: it is $\iota_{u}(x) = u x u^{-1}$ for some $u \in \mathbb{H}^\times$, depending only on $u$ modulo the central scalars $\mathbb{R}^\times$. Thus the automorphisms of the first factor form $\mathbb{H}^\times / \mathbb{R}^\times \cong S^3/\{\pm 1\} = SO(3)$, and likewise for the second, giving the product.

**Corollary.** As a Lie group, $\mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}})$ has dimension $6$ and is connected and compact.

**Example.** Conjugation by a unit of the first factor, $\sigma(\tilde{Q}_+,\tilde{Q}_-) = (u\tilde{Q}_+ u^{-1}, \tilde{Q}_-)$ with $|u| = 1$, is a $\mathbb{D}$-algebra automorphism; conjugation by a unit of the second factor is the companion. Every $\mathbb{D}$-automorphism is a pair of such conjugations, one per factor.

## Automorphisms over $\mathbb{R}$

Now the ground ring is $\mathbb{R}$, so automorphisms need only be $\mathbb{R}$-linear, and the group is strictly larger.

**Automorphisms preserve the centre.** If $\sigma$ is an $\mathbb{R}$-algebra automorphism and $z$ is central then $\sigma(z)$ is central, so $\sigma$ restricts to an $\mathbb{R}$-algebra automorphism of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cong \mathbb{D}$. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ has exactly two $\mathbb{R}$-algebra automorphisms, the identity and the swap $\tilde\Pi_+ \leftrightarrow \tilde\Pi_-$, restriction gives a homomorphism

$$
\rho : \mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}}) \longrightarrow \mathrm{Aut}_{\mathbb{R}}(\mathbb{D}) \cong \mathbb{Z}/2 .
$$

**The kernel is the $\mathbb{D}$-linear part.** An automorphism lies in $\ker\rho$ exactly when it fixes the centre pointwise, equivalently when it fixes $\tilde\Pi_+$ and $\tilde\Pi_-$ and so preserves each factor. Hence $\ker\rho = \mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) \cong SO(3)\times SO(3)$, the group of the previous section, consisting of the inner automorphisms.

**The swap coset.** The map

$$
c(\tilde{Q}) = \tilde{Q}^{*} , \qquad c(j) = -j ,
$$

is an $\mathbb{R}$-algebra automorphism, because ${}^{*}$ is a ring automorphism of the commutative coefficient algebra $\mathbb{D}$ and fixes the quaternion units $e_k$. It induces the nontrivial element of $\mathbb{Z}/2$ on the centre, it is not $\mathbb{D}$-linear since $c(j) = -j \neq j$, and it is not inner because inner automorphisms fix the centre pointwise. So $\rho$ is surjective and the extension is nontrivial. Since $c^{2} = \mathrm{id}$, the sequence splits:

**Theorem.** $\mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}}) \cong \left(SO(3) \times SO(3)\right) \rtimes \mathbb{Z}/2$, the generator of $\mathbb{Z}/2$ acting by interchanging the two factors of $SO(3)\times SO(3)$.

**Proof.** There is a short exact sequence $1 \to SO(3)\times SO(3) \to \mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}}) \xrightarrow{\rho} \mathbb{Z}/2 \to 1$, split by $c$ because $c^2 = \mathrm{id}$. The action of $c$ on the kernel conjugates an automorphism of the first factor into one of the second and conversely, that is, swaps the factors.

**Concretely**, every real automorphism of $\mathbb{H}_{\mathbb{D}}$ has exactly one of the two forms

$$
\sigma(x_+, x_-) = (u_+ x_+ u_+^{-1},\, u_- x_- u_-^{-1}) \quad\text{or}\quad \sigma(x_+, x_-) = \left(u_+ x_- u_+^{-1},\, u_- x_+ u_-^{-1}\right),
$$

with $u_\pm$ determined up to a real scalar; the first family is the identity coset, the second the coset of $c$.

**Corollary.** $\mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}})$ has real dimension $6$ and exactly two connected components, each a copy of $SO(3)\times SO(3)$.

**Remark.** Quaternion conjugation $\bar{\cdot}$ is an anti-automorphism, not an automorphism, so it is not in either group. The split complex conjugation ${}^{*}$ is an automorphism and appears above. The Hermitian conjugation ${}^{\dagger}$ and the anti-Hermitian conjugation ${}^{\flat}$ are anti-automorphisms and do not appear.

## Derivations

**Definition.** An **$\mathbb{R}$-linear derivation** of $\mathbb{H}_{\mathbb{D}}$ is an $\mathbb{R}$-linear map $D$ with $D(xy) = D(x)y + xD(y)$. The set is a real vector space $\mathrm{Der}(\mathbb{H}_{\mathbb{D}})$, a Lie algebra under $[D_1,D_2] = D_1D_2 - D_2D_1$. A **$\mathbb{D}$-linear derivation** is additionally $\mathbb{D}$-linear; the set is $\mathrm{Der}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}})$.

**Every real derivation is $\mathbb{D}$-linear.** A derivation maps the centre to the centre, since for central $z$ and every $x$, $D(z)x = D(zx) - zD(x) = D(xz) - D(x)z = xD(z)$. A derivation of $\mathbb{D}$ over $\mathbb{R}$ vanishes, because $0 = D(1) = D(j^2) = 2jD(j)$ forces $D(j) = 0$ and $j$ generates $\mathbb{D}$ over $\mathbb{R}$. Hence $D$ vanishes on the centre and, since $j$ is central, $D(jx) = jD(x)$, so $D$ is $\mathbb{D}$-linear. Therefore

$$
\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) = \mathrm{Der}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) .
$$

**Theorem.** $\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) \cong \mathrm{SO}(3) \oplus \mathrm{SO}(3) \cong \mathrm{SO}(4)$, a real Lie algebra of dimension $6$, and every derivation is inner.

**Proof.** A derivation $D$ fixes each central idempotent: from $D(\tilde\Pi_+) = D(\tilde\Pi_+^2) = \tilde\Pi_+D(\tilde\Pi_+) + D(\tilde\Pi_+)\tilde\Pi_+$ and the centrality of $D(\tilde\Pi_+)$ one obtains $D(\tilde\Pi_+) = 0$, and similarly $D(\tilde\Pi_-) = 0$. Hence $D$ kills no element of the form $x_+ \tilde\Pi_+$ into the other factor and, by the Leibniz rule, preserves the splitting; so $D$ acts as a derivation of $\mathbb{H}$ on the first factor and one on the second, and

$$
\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) \cong \mathrm{Der}(\mathbb{H}) \oplus \mathrm{Der}(\mathbb{H}) .
$$

For the division algebra $\mathbb{H}$, every derivation is inner: $\mathrm{Der}(\mathbb{H}) = \mathrm{ad}(\mathbb{H})$ with kernel the centre $\mathbb{R}$, so $\mathrm{Der}(\mathbb{H}) \cong \mathbb{H}/\mathbb{R} \cong \mathrm{SO}(3)$, of dimension $3$. Summing the two factors gives $\mathrm{SO}(3) \oplus \mathrm{SO}(3) \cong \mathrm{SO}(4)$.

**Inner derivations.** For $a \in \mathbb{H}_{\mathbb{D}}$ the map $\mathrm{ad}_a(x) = ax - xa$ is a derivation, and $\mathrm{ad}$ has kernel the centre $Z(\mathbb{H}_{\mathbb{D}}) = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and image all derivations, so

$$
\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) \cong \mathbb{H}_{\mathbb{D}} / \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} ,
$$

an isomorphism of Lie algebras because $[\mathrm{ad}_a,\mathrm{ad}_b] = \mathrm{ad}_{[a,b]}$.

**Derivations and automorphisms.** The two structures are linked by the exponential, $\exp(t\,\mathrm{ad}_a)(x) = e^{ta}xe^{-ta}$, the inner automorphism determined by $e^{ta}$. Hence the Lie algebra of the identity component of $\mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}})$ is the derivation algebra: $\mathrm{Lie}\left(SO(3)\times SO(3)\right) \cong \mathrm{SO}(3)\oplus\mathrm{SO}(3)$.

**An explicit basis.** The derivations $A_k = \tfrac{1}{2}\mathrm{ad}_{e_k}$, $k = 1,2,3$, act on the two factors simultaneously, each as $\mathrm{ad}_{e_k}$, and satisfy $[A_1,A_2] = A_3$ together with its cyclic permutations; the companion derivations $\tfrac{1}{2}\mathrm{ad}_{je_k}$ act with opposite signs on the two factors. Their combinations

$$
D_k^{+} = \tfrac{1}{2}\left(A_k + \tfrac{1}{2}\mathrm{ad}_{je_k}\right) = \tfrac{1}{2}\mathrm{ad}_{e_k \tilde\Pi_+}, \qquad D_k^{-} = \tfrac{1}{2}\left(A_k - \tfrac{1}{2}\mathrm{ad}_{je_k}\right) = \tfrac{1}{2}\mathrm{ad}_{e_k \tilde\Pi_-}
$$

act on the first and on the second factor respectively and vanish on the other, and each triple satisfies $[D_1^{\pm},D_2^{\pm}] = D_3^{\pm}$ together with its cyclic permutations. The six elements $D_k^{\pm}$ are linearly independent and form a real basis of the six-dimensional derivation algebra.

## Worked Examples

**The factor swap.** The map $c(\tilde{Q}) = \tilde{Q}^{*}$ fixes $e_k$ and $je_k$ in the sense $c(e_k) = e_k$, $c(je_k) = -je_k$, and swaps the two halves: $c(x_+,x_-) = (x_-,x_+)$ in components. It satisfies $c^2 = \mathrm{id}$, preserves the product because ${}^{*}$ is an automorphism of $\mathbb{D}$, and is not inner, since the inner automorphisms fix the centre pointwise.

**An inner automorphism.** For $u = e_1$ in the first factor, $\sigma(x_+,x_-) = (e_1 x_+ e_1^{-1}, x_-)$ has $e_1^{-1} = -e_1$, so it fixes $e_1$ and reverses the signs of $e_2$ and $e_3$ in the first factor while leaving the second untouched: $\sigma(e_2,0) = (-e_2,0)$, $\sigma(e_3,0) = (-e_3,0)$.

**A derivation.** Take $D = D_3^{+} = \tfrac{1}{2}\mathrm{ad}_{e_3 \tilde\Pi_+}$, acting on the first factor alone. Its exponential acts by $\exp(tD)(e_1,0) = (\cos t\,e_1 + \sin t\,e_2, 0)$, matching $A(e^{te_3/2},0)$; the second factor is fixed, because $\mathrm{ad}_{e_3\tilde\Pi_+}$ acts as zero there.

**A derivation that mixes nothing.** Any $a = a_+ \tilde\Pi_+ + a_- \tilde\Pi_-$ gives the pair $\mathrm{ad}_a = (\mathrm{ad}_{a_+}, \mathrm{ad}_{a_-})$, and $\mathrm{ad}_a$ depends only on $a$ modulo the centre: adding a central element changes neither component.

## Summary

The split biquaternion algebra is the product $\mathbb{H} \oplus \mathbb{H}$ of two quaternion division algebras, with centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cong \mathbb{D}$ and two minimal two-sided ideals. Over the split complex algebra every automorphism is $\mathbb{D}$-linear and consists of an inner automorphism of each factor, so $\mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) \cong SO(3) \times SO(3)$, connected, of dimension $6$. Over $\mathbb{R}$ an automorphism may also interchange the two factors, and the split complex conjugation $c(\tilde{Q}) = \tilde{Q}^{*}$ realises that swap, an outer automorphism; hence $\mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}}) \cong (SO(3)\times SO(3)) \rtimes \mathbb{Z}/2$, of dimension $6$ with two connected components. Every real derivation is automatically $\mathbb{D}$-linear, because the centre $\mathbb{D}$ admits no nonzero derivation; every derivation preserves the splitting and is inner, so $\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) \cong \mathbb{H}_{\mathbb{D}}/\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cong \mathrm{SO}(3)\oplus\mathrm{SO}(3) \cong \mathrm{SO}(4)$, of dimension $6$, the Lie algebra of the identity component of the automorphism group. The contrast with the biquaternion case is exact: there the algebra is simple and central over $\mathbb{C}$, every automorphism is inner, $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$ and $\mathrm{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$, with derivation algebra $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}} \cong \mathrm{SO}(1,3)$; here the semisimple product structure replaces the simple algebra, the compact group $SO(3)\times SO(3)$ replaces the projective Lorentz group, and the derivation algebra $\mathrm{SO}(4)$ replaces $\mathrm{SO}(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H} \cong \mathbb{H}\oplus\mathbb{H}$ | Split biquaternion algebra; product of two quaternion algebras |
| $e_0,e_1,e_2,e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $j$ | Central split complex unit, $j^2 = +1$ |
| $\tilde\Pi_\pm = \tfrac{1}{2}(1\pm j)$ | Central idempotents, the two factors |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \mathrm{span}_{\mathbb{R}}\{e_0, je_0\}$ | Centre of the algebra |
| $\tilde{Q} \mapsto (\tilde{Q}_+,\tilde{Q}_-)$ | Isomorphism to $\mathbb{H}\oplus\mathbb{H}$ |
| $\bar\cdot, {}^{*}, {}^{\dagger}, {}^{\flat}$ | Quaternion, split complex, Hermitian, anti-Hermitian conjugations |
| $\mathrm{Aut}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) \cong SO(3)\times SO(3)$ | $\mathbb{D}$-linear automorphisms |
| $\mathrm{Aut}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}}) \cong (SO(3)\times SO(3))\rtimes\mathbb{Z}/2$ | Real automorphisms |
| $c(\tilde{Q}) = \tilde{Q}^{*}$ | Factor swap, the outer real automorphism |
| $\mathrm{Der}(\mathbb{H}_{\mathbb{D}}) = \mathrm{Der}_{\mathbb{D}}(\mathbb{H}_{\mathbb{D}}) \cong \mathrm{SO}(3)\oplus\mathrm{SO}(3)\cong\mathrm{SO}(4)$ | Derivation algebra |
| $\mathrm{ad}_a(x) = ax - xa$ | Inner derivation |
| $D_k^{\pm} = \tfrac{1}{2}\mathrm{ad}_{e_k \tilde\Pi_\pm}$ | Derivation basis: $D_k^{+}$ acts on the first factor, $D_k^{-}$ on the second, $[D_1^{\pm},D_2^{\pm}]=D_3^{\pm}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for Skolem–Noether and the automorphisms and derivations of a product of simple algebras.
- I. N. Herstein, *Noncommutative Rings*, Carus Mathematical Monographs 15 (Mathematical Association of America, 1968), for inner automorphisms and derivations of central simple algebras.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the automorphism group and derivation algebra of the quaternion algebra.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for derivations of associative algebras and the isomorphism $\mathrm{SO}(4)\cong\mathrm{SO}(3)\oplus\mathrm{SO}(3)$.
