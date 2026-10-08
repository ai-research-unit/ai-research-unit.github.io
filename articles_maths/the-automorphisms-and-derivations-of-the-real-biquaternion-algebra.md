# __The Automorphisms and Derivations of the Real Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}$ is one ring under two scalar systems, and this article treats the symmetries and the infinitesimal symmetries of the **real** reading: the group $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ of its $\mathbb{R}$-algebra automorphisms, and the Lie algebra $\operatorname{Der}_\mathbb{R}(\mathbb{B})$ of its $\mathbb{R}$-linear derivations. The general theory of both invariants, and the complex reading, are *Biquaternion Automorphisms and Derivations*; the present article is the real-reading companion, and its subject is what the smaller scalar field does to the two.

What the smaller field does is not the same to both. The automorphism group **grows**: the complex conjugation is an $\mathbb{R}$-algebra automorphism that is not $\mathbb{C}$-linear and not inner, so the real group contains the complex one as a subgroup of index two, with a second coset of conjugate-linear automorphisms. The derivation space **does not grow**: an $\mathbb{R}$-linear derivation of $\mathbb{B}$ is automatically $\mathbb{C}$-linear, because it must kill the centre and the centre has no nonzero real derivation, so $\operatorname{Der}_\mathbb{R}(\mathbb{B}) = \operatorname{Der}_\mathbb{C}(\mathbb{B})$. One of the two invariants is sensitive to the field and the other is not, and the reason is that automorphisms may be semilinear while derivations may not.

The article assumes *Biquaternion Automorphisms and Derivations* for Skolem–Noether, for the complex group $\operatorname{Aut}_\mathbb{C}(\mathbb{B}) \cong \mathbb{B}^{\times}/\mathbb{C}^{\times} \cong PGL(2,\mathbb{C}) \cong SO(3,\mathbb{C})$ and for the complex derivation space $\operatorname{Der}_\mathbb{C}(\mathbb{B}) \cong \mathbb{B}/\mathbb{C}_{\mathbb{B}}$, and it does not repeat those computations. The change of scalars is *The Change of Scalars from $\mathbb{C}$ to $\mathbb{R}$*; the real subalgebras that the automorphisms move are *The Real Subalgebras of the Biquaternion Algebra*; the conjugations as real-linear maps are *The Four Conjugations Are All $\mathbb{R}$-Linear*; the norm and the invertibility criterion are *Biquaternion Norm and Invertibility*; and the general theory of $\operatorname{Aut}_R(A)$ and $\operatorname{Der}_R(A)$ is *Automorphisms and Derivations of Algebras*.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, unit $e_0$, quaternion units $e_k^2 = -e_0$, central imaginary $i = ie_0$ with $i^2 = -e_0$, and centre $Z(\mathbb{B}) = \mathbb{C}_{\mathbb{B}} = \mathbb{R}\{e_0, i\}$. The quaternion and complex conjugations are ${}^{\natural}$ and $\bar{\cdot}$; the complex conjugation of an element is written $\bar{\tilde Q}$; and an $\mathbb{R}$-algebra automorphism is a bijective $\mathbb{R}$-linear map with $\sigma(\tilde P\tilde Q) = \sigma(\tilde P)\sigma(\tilde Q)$ and $\sigma(e_0) = e_0$.

## Automorphisms as Real-Linear Maps

### Every Automorphism Preserves the Centre

**Proposition.** Let $\sigma$ be an $\mathbb{R}$-algebra automorphism of $\mathbb{B}$. Then $\sigma$ maps the centre onto itself,
$$
\sigma\bigl(Z(\mathbb{B})\bigr) = Z(\mathbb{B}) ,
$$
and the restriction $\sigma|_{\mathbb{C}_{\mathbb{B}}}$ is an $\mathbb{R}$-algebra automorphism of the centre $\mathbb{C}_{\mathbb{B}}$.

**Proof.** Let $A$ be central. For every $\tilde R$,
$$
\sigma(A)\sigma(\tilde R) = \sigma(A\tilde R) = \sigma(\tilde RA) = \sigma(\tilde R)\sigma(A) ,
$$
so $\sigma(A)$ is central; applying the same to $\sigma^{-1}$ gives the reverse inclusion. The restriction is an automorphism because the centre is carried onto itself and $\sigma$ is a homomorphism. $\square$

**Corollary.** The automorphisms of the centre over $\mathbb{R}$ are exactly two, the identity and the complex conjugation $\kappa(A) = \bar A$, so there is a group homomorphism
$$
\rho : \operatorname{Aut}_\mathbb{R}(\mathbb{B}) \longrightarrow \operatorname{Aut}_\mathbb{R}(\mathbb{C}_{\mathbb{B}}) = \{\mathrm{id}, \kappa\} \cong \mathbb{Z}/2 , \qquad \rho(\sigma) = \sigma|_{\mathbb{C}_{\mathbb{B}}} .
$$

**Proof.** The centre is a copy of the field $\mathbb{C}$ as a real algebra, and a field automorphism of $\mathbb{C}$ fixing $\mathbb{R}$ is either the identity or the complex conjugation; both are real-algebra automorphisms. $\square$

### The Kernel Is the Complex Part

**Theorem.** The kernel of $\rho$ is $\operatorname{Aut}_\mathbb{C}(\mathbb{B})$, the group of $\mathbb{C}$-algebra automorphisms.

**Proof.** An automorphism lies in the kernel exactly when it fixes the centre pointwise. A map fixing the centre pointwise commutes with multiplication by the central element $i$; since $i$ generates the centre together with $e_0$, the map is $\mathbb{C}$-linear, $T(i\tilde R) = iT(\tilde R)$. Conversely a $\mathbb{C}$-linear automorphism fixes the scalars, hence fixes the centre pointwise. So $\ker\rho = \operatorname{Aut}_\mathbb{C}(\mathbb{B})$. $\square$

**Corollary.** By Skolem–Noether the kernel is the group of inner automorphisms, $\ker\rho = \{\iota_g : g \in \mathbb{B}^\times\}$, and
$$
\ker\rho \cong \mathbb{B}^\times / \mathbb{C}^\times \cong PGL(2,\mathbb{C}) \cong PSL(2,\mathbb{C}) \cong SO(3,\mathbb{C}) ,
$$
of real dimension six (*Biquaternion Automorphisms and Derivations*, §*Automorphisms over $\mathbb{C}$*).

### The Conjugate-Linear Coset

**Proposition.** The homomorphism $\rho$ is surjective, and $\mathbb{R}$-algebra automorphisms not fixing the centre exist.

**Proof.** The complex conjugation $c(\tilde Q) = \bar{\tilde Q}$ is an $\mathbb{R}$-algebra automorphism, because conjugating a product conjugates its coefficients and the structure constants are real, $c(\tilde P\tilde Q) = c(\tilde P)c(\tilde Q)$; it negates the central element, $c(i) = -i$, so it induces $\kappa$ on the centre, and it is therefore not in the kernel. $\square$

**Proposition.** The automorphism $c$ is not inner: it is not of the form $\iota_g$.

**Proof.** An inner automorphism $\iota_g(\tilde R) = g\tilde Rg^{-1}$ fixes every central element, because $gAg^{-1} = A$ for $A$ central; but $c(i) = -i \neq i$. Hence $c \notin \ker\rho \supseteq \operatorname{Inn}(\mathbb{B})$. $\square$

### The Group and Its Two Components

**Theorem.** The group of $\mathbb{R}$-algebra automorphisms of $\mathbb{B}$ is
$$
\operatorname{Aut}_\mathbb{R}(\mathbb{B}) \;\cong\; \operatorname{Aut}_\mathbb{C}(\mathbb{B}) \rtimes \mathbb{Z}/2 \;\cong\; \bigl(\mathbb{B}^\times/\mathbb{C}^\times\bigr) \rtimes \mathbb{Z}/2 ,
$$
a real Lie group of real dimension six with exactly two components; the nontrivial element of $\mathbb{Z}/2$ acts on $\operatorname{Aut}_\mathbb{C}(\mathbb{B})$ by $\iota_g \mapsto \iota_{\bar g}$, that is, on the level of units, by $g \mapsto \bar g$.

**Proof.** The sequence
$$
1 \longrightarrow \operatorname{Aut}_\mathbb{C}(\mathbb{B}) \longrightarrow \operatorname{Aut}_\mathbb{R}(\mathbb{B}) \xrightarrow{\ \rho\ } \mathbb{Z}/2 \longrightarrow 1
$$
is exact, and it splits because $c^2 = \mathrm{id}$; hence the semidirect product, with the action induced by conjugation by $c$. Writing an element with $\rho(\sigma) = \kappa$ as $\sigma = \iota_g \circ c$ gives $\sigma(\tilde R) = g\bar{\tilde R}g^{-1}$, so every real automorphism has exactly one of the two forms
$$
\sigma(\tilde R) = g\,\tilde R\,g^{-1} \qquad\text{or}\qquad \sigma(\tilde R) = g\,\bar{\tilde R}\,g^{-1}, \qquad g \in \mathbb{B}^\times ,
$$
with $g$ determined modulo the nonzero complex scalars; the first family is the identity component, the second is the coset of $c$. The first family is the identity component and the second is its translate by the complex conjugation, so there are exactly two components. The action of $c$ on a unit is $c$ itself, and $c \iota_g c^{-1} = \iota_{\bar g}$ on the complex part. $\square$

**Remark (the second family is conjugate-linear).** The automorphisms $g\bar{\tilde R}g^{-1}$ are $\mathbb{C}$-antilinear: they satisfy $\sigma(\lambda \tilde R) = \bar\lambda\,\sigma(\tilde R)$ for $\lambda \in \mathbb{C}$, because $\bar{\cdot}$ is antilinear and $\iota_g$ is linear. They are the automorphisms that the real reading has and the complex reading does not, and they are exactly the elements outside the identity component.

**Remark (the outer automorphism group).** Since the kernel of $\rho$ is the whole identity component and its image is $\mathbb{Z}/2$, the outer automorphism group is
$$
\operatorname{Out}_\mathbb{R}(\mathbb{B}) = \operatorname{Aut}_\mathbb{R}(\mathbb{B}) / \operatorname{Inn}(\mathbb{B}) \cong \mathbb{Z}/2 ,
$$
generated by the class of the complex conjugation.

## Why the Automorphism Group Grows

The enlargement is the Galois theory of $\mathbb{C}/\mathbb{R}$ read on the algebra. The nontrivial automorphism $\kappa$ of the field of scalars is not available over $\mathbb{C}$, where there is no smaller field to conjugate down to; over $\mathbb{R}$ it extends to the algebra as the complex conjugation $c$, and $c$ is not inner because it moves the centre. The two cosets of the previous section are therefore the two Galois twists of the algebra:

- the identity coset, of automorphisms that fix the scalars, that is, the $\mathbb{C}$-linear automorphisms;
- the conjugate coset, of automorphisms that negate the scalars, that is, the $\mathbb{C}$-antilinear automorphisms.

**Proposition (fixed fields and fixed subspaces).** The complex conjugation $c$ fixes the quaternion subspace $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\}$ pointwise and negates the central imaginary, $c(\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}}$ and $c(i) = -i$.

**Proof.** On the coefficients, $c(Q_\mu) = \bar Q_\mu$; for a real coefficient $\bar Q_\mu = Q_\mu$, so $c$ fixes every real combination of the $e_\mu$, which is $\mathbb{H}_{\mathbb{B}}$, and $c(i) = c(ie_0) = \bar i\, e_0 = -i$. $\square$

**Remark (the automorphisms and the real subalgebras).** The group $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ acts on the set of real subalgebras, and the second coset changes the orbits that the identity component alone would produce. The complex conjugation $c$ fixes the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{R}\{e_0, i\}$ setwise and fixes $\mathbb{H}_{\mathbb{B}}$ pointwise, so it fixes setwise every copy of $\mathbb{C}$ that lies in $\mathbb{H}_{\mathbb{B}}$; a copy that is neither the centre nor contained in $\mathbb{H}_{\mathbb{B}}$ is carried to a different one. Indeed $c$ acts on the roots of $-e_0$ by $\xi \mapsto \bar\xi$, and for a pure root $\xi$ the conjugated root $\bar\xi$ spans the same real line $\mathbb{R}\xi$ exactly when the coefficients of $\xi$ are real, that is, exactly when the copy lies in $\mathbb{H}_{\mathbb{B}}$; the remaining non-central copies, spanned by roots with non-real coefficients, are moved. (The central copy $\mathbb{R}\{e_0,i\}$ is fixed setwise rather than pointwise, since $c(i) = -i$.) The second coset accordingly permutes the conjugates $g\mathbb{H}_{\mathbb{B}}g^{-1}$ of the quaternion subspace by the Galois twist $g \mapsto \bar g$. The real subalgebras and their orbits are *The Real Subalgebras of the Biquaternion Algebra*.

## Derivations

### Definitions

**Definition.** An $\mathbb{R}$-**linear derivation** of $\mathbb{B}$ is an $\mathbb{R}$-linear map $D : \mathbb{B} \to \mathbb{B}$ satisfying the Leibniz rule
$$
D(\tilde P\tilde Q) = D(\tilde P)\,\tilde Q + \tilde P\,D(\tilde Q) \qquad \text{for all } \tilde P, \tilde Q \in \mathbb{B}.
$$
The set of them is a real vector space $\operatorname{Der}_\mathbb{R}(\mathbb{B})$ and a real Lie algebra under $[D_1,D_2] = D_1D_2 - D_2D_1$.

**Proposition.** Every derivation kills the identity: $D(e_0) = 0$.

**Proof.** $D(e_0) = D(e_0e_0) = D(e_0)e_0 + e_0D(e_0) = 2D(e_0)$, so $D(e_0) = 0$. $\square$

### Every Real Derivation Is Complex-Linear

**Theorem.** Every $\mathbb{R}$-linear derivation of $\mathbb{B}$ is $\mathbb{C}$-linear, and consequently
$$
\operatorname{Der}_\mathbb{R}(\mathbb{B}) = \operatorname{Der}_\mathbb{C}(\mathbb{B}) .
$$

**Proof.** Let $D$ be an $\mathbb{R}$-linear derivation. First, $D$ maps the centre into itself: if $A$ is central then
$$
D(A)\tilde R = D(A\tilde R) - A\,D(\tilde R) = D(\tilde R A) - D(\tilde R)\,A = \tilde R\,D(A)
$$
for every $\tilde R$, so $D(A)$ is central. So $D$ restricts to a derivation $\mathbb{C}_{\mathbb{B}} \to \mathbb{C}_{\mathbb{B}}$, and the centre is a copy of $\mathbb{C}$ as a real algebra; but $\mathbb{C}$ has no nonzero $\mathbb{R}$-linear derivation, because $0 = D(-e_0) = D(i^2) = iD(i) + D(i)i = 2i\,D(i)$ forces $D(i) = 0$. Hence $D$ kills the centre. Now the Leibniz rule gives, for every $\tilde R$,
$$
D(i\tilde R) = D(i)\,\tilde R + i\,D(\tilde R) = i\,D(\tilde R) ,
$$
so $D$ commutes with multiplication by the scalar $i$; since $\mathbb{C}$ is generated over $\mathbb{R}$ by $i$, the derivation is $\mathbb{C}$-linear. The reverse inclusion is immediate. $\square$

**Remark (there are no conjugate-linear derivations).** The proof uses only the Leibniz rule and the centrality of $i$; there is no room for a derivation to conjugate a coefficient, because the Leibniz rule already forces the derivation to take $i$ to $0$ and hence to commute with $i$. This is the structural asymmetry with the automorphisms: an $\mathbb{R}$-algebra automorphism may send the central element $i$ to $\pm i$ and be semilinear, but a derivation may not.

### The Structure of the Real Derivation Algebra

**Corollary.** The real derivation space is
$$
\operatorname{Der}_\mathbb{R}(\mathbb{B}) = \operatorname{Der}_\mathbb{C}(\mathbb{B}) \cong \mathbb{B}/\mathbb{C}_{\mathbb{B}} ,
$$
the quotient of $\mathbb{B}$ by its centre, that is, the traceless part $\operatorname{span}_\mathbb{C}\{e_1,e_2,e_3\}$ of complex dimension three (real dimension six); it is an inner derivation algebra, $\operatorname{ad}_{\tilde A}(\tilde R) = [\tilde A,\tilde R]$ with $\tilde A$ traceless, of real dimension six.

**Proof.** By the theorem the real derivations are the complex ones, and by *Biquaternion Automorphisms and Derivations*, §*Derivations over $\mathbb{C}$*, the complex derivations are exactly the inner derivations $\operatorname{ad}_{\tilde A}$ with $\tilde A$ traceless, forming a complex vector space of dimension three, hence a real vector space of dimension six. $\square$

**Remark (the real basis and the Lie algebra).** Over $\mathbb{R}$ the derivation algebra is spanned by the six real linear combinations of the complex basis $D_1,D_2,D_3$ and its multiple by $i$, that is, by $\{D_1,D_2,D_3,iD_1,iD_2,iD_3\}$; as a real Lie algebra it is $\mathfrak{so}(1,3)$, the Lie algebra of the Lorentz group, equivalently the bivector part of the even Clifford algebra $\mathrm{Cl}^+_{1,3}$ (*Biquaternion Automorphisms and Derivations*, §*Derivations over $\mathbb{R}$*).

## The Lie Correspondence over the Real Field

**Theorem.** The Lie algebra of the real Lie group $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ is $\operatorname{Der}_\mathbb{R}(\mathbb{B})$.

**Proof.** The identity component of $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ is $\operatorname{Aut}_\mathbb{C}(\mathbb{B})$, whose Lie algebra is $\operatorname{Der}_\mathbb{C}(\mathbb{B})$ by the exponential formula $\exp(t\,\mathrm{ad}_{\tilde A})\,\tilde R = e^{t\tilde A}\,\tilde R\, e^{-t\tilde A}$ (*Biquaternion Automorphisms and Derivations*, §*Derivations over $\mathbb{C}$*). Since the Lie algebra of a Lie group depends only on its identity component, and $\operatorname{Der}_\mathbb{R}(\mathbb{B}) = \operatorname{Der}_\mathbb{C}(\mathbb{B})$ by the theorem above, the Lie algebra of the full real group is the real derivation space. $\square$

**Corollary.** The tangent space at the identity of $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ has real dimension six, which is the dimension of the group; the second component, the conjugate coset, contributes no tangent directions at the identity.

**Remark (the two invariants against each other).** Over $\mathbb{R}$ the automorphism group is strictly larger than over $\mathbb{C}$, by the conjugate coset, while the derivation space is the same; over $\mathbb{C}$ the automorphism group is a single component and every automorphism is inner, and the derivation space is its Lie algebra. The comparison is therefore: adding the scalars of a Galois-twisted coset to an automorphism group is possible, since an automorphism may be semilinear; adding the corresponding twist to a derivation algebra is not, since a derivation is linear by its Leibniz rule. The general statement is *Automorphisms and Derivations of Algebras*, and the complex case is *Biquaternion Automorphisms and Derivations*.

## Summary

The real automorphism group of $\mathbb{B}$ is obtained from the complex one by adjoining the complex conjugation, which is $\mathbb{R}$-linear, conjugate-linear over $\mathbb{C}$, and not inner because it moves the centre. The restriction to the centre gives an exact sequence
$$
1 \longrightarrow \operatorname{Aut}_\mathbb{C}(\mathbb{B}) \longrightarrow \operatorname{Aut}_\mathbb{R}(\mathbb{B}) \xrightarrow{\ \rho\ } \mathbb{Z}/2 \longrightarrow 1 ,
$$
split by $c$, so that
$$
\boxed{\ \operatorname{Aut}_\mathbb{R}(\mathbb{B}) \cong \operatorname{Aut}_\mathbb{C}(\mathbb{B}) \rtimes \mathbb{Z}/2 \cong \bigl(\mathbb{B}^\times/\mathbb{C}^\times\bigr)\rtimes\mathbb{Z}/2 , \quad \operatorname{Der}_\mathbb{R}(\mathbb{B}) = \operatorname{Der}_\mathbb{C}(\mathbb{B}) . }
$$

Every real automorphism has exactly one of the forms $\tilde R \mapsto g\tilde Rg^{-1}$ and $\tilde R \mapsto g\bar{\tilde R}g^{-1}$, the group is a real Lie group of real dimension six with two components, and its outer automorphism group is $\mathbb{Z}/2$, generated by the class of the complex conjugation. Every real derivation is automatically $\mathbb{C}$-linear, because it kills the centre and the centre has no nonzero real derivation, so the real derivation space coincides with the complex one, $\operatorname{Der}_\mathbb{R}(\mathbb{B}) \cong \mathbb{B}/\mathbb{C}_{\mathbb{B}}$, of real dimension six, with the real Lie algebra $\mathfrak{so}(1,3)$; it is the Lie algebra of the real automorphism group, read on its identity component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Aut}_\mathbb{R}(\mathbb{B})$ | $\mathbb{R}$-algebra automorphisms; real dimension $6$, two components |
| $\operatorname{Aut}_\mathbb{C}(\mathbb{B})$ | $\mathbb{C}$-algebra automorphisms, $= \ker\rho$, the identity component |
| $\rho : \operatorname{Aut}_\mathbb{R}(\mathbb{B}) \to \{\mathrm{id},\kappa\}$ | restriction of an automorphism to the centre |
| $\kappa$ | the complex conjugation of the centre $\mathbb{C}_{\mathbb{B}}$ |
| $c(\tilde Q) = \bar{\tilde Q}$ | the complex conjugation of $\mathbb{B}$, the nontrivial coset |
| $\iota_g(\tilde R) = g\tilde Rg^{-1}$ | the inner automorphism determined by the unit $g$ |
| $\mathbb{B}^\times/\mathbb{C}^\times \cong PGL(2,\mathbb{C})$ | the complex automorphism group |
| $\operatorname{Der}_\mathbb{R}(\mathbb{B})$ | $\mathbb{R}$-linear derivations, $= \operatorname{Der}_\mathbb{C}(\mathbb{B})$ |
| $\operatorname{ad}_{\tilde A}(\tilde R) = [\tilde A,\tilde R]$ | the inner derivation by $\tilde A$ |
| $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$ | the traceless part, $\cong \operatorname{Der}_\mathbb{C}(\mathbb{B})$, complex dimension $3$ |

## Further Reading

- *Biquaternion Automorphisms and Derivations* (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for Skolem–Noether, the complex groups and the complex derivation algebra.
- *Automorphisms and Derivations of Algebras* (`articles_maths/automorphisms-and-derivations-of-algebras.md`), for the general theory over a commutative ring.
- *The Change of Scalars from $\mathbb{C}$ to $\mathbb{R}$* (`articles_maths/the-change-of-scalars-from-c-to-r.md`), for the field-of-scalars viewpoint on the automorphism group.
- *The Four Conjugations Are All $\mathbb{R}$-Linear* (`articles_maths/the-four-conjugations-are-all-r-linear.md`), for the conjugations as real-linear operators.
- *The Real Subalgebras of the Biquaternion Algebra* (`articles_maths/the-real-subalgebras-of-the-biquaternion-algebra.md`), for the action of the automorphism group on the copies of $\mathbb{C}$ and $\mathbb{H}$.
- Nathan Jacobson, *Lie Algebras*, Dover reprint (1979), for the derivations of an associative algebra and the inner derivations.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for Skolem–Noether and the automorphisms of a central simple algebra.
