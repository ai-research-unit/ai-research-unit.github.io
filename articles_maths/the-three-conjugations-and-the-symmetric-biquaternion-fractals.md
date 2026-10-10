# __The Three Conjugations and the Symmetric Biquaternion Fractals__

## Introduction

The biquaternion algebra carries four conjugations, and the quadratic map is equivariant under three of them — the fourth relates the even family to the odd one — so each of the three that fixes the parameter is a symmetry of the corresponding Julia set. This gives a family of symmetric fractals, one for each subgroup of the group of involutions that can occur as a stabiliser, and it organises the pictures of the subject by their symmetry rather than by their coordinates. Two further symmetries are present at every parameter: the central inversion, because the square of an element is unchanged when the element is negated, and the identity, and the two together with the conjugations form the full symmetry group the elementary theory detects.

The four conjugations, their fixed subspaces and the involution group are *The Group of Involutions*; the remarkable subspaces are *Introduction to the Remarkable Subspaces*; the quadratic family and the equivariance theorem are *The Biquaternion Quadratic Map and Its Julia Sets*; the slices are *The Slices of the Biquaternion Julia Sets*; the quaternion and complex fractal pictures are *The Quaternion Quadratic Map and Its Julia Sets* and *The Julia Sets of a Complex Polynomial*.

The article owns the three conjugations used for symmetry (the fourth is excluded, with the reason), the equivariance restated for the group, the classification of the stabiliser and the resulting symmetric families, the extra central inversion, and the identification of the symmetry subspaces with the remarkable subspaces. It does not re-derive the conjugations or the equivariance.

**Standing convention.** ${}^{\natural}$ is quaternion conjugation, $\bar{\cdot}$ complex conjugation, ${}^{*}$ Hermitian conjugation and $\flat$ anti-Hermitian conjugation, so that ${}^{*}={}^{\natural}\bar{\cdot}$, $\flat=-{}^{*}$, and the four maps form the group of involutions $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$. $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$.

## The Three Conjugations Used and the One Excluded

**Proposition (the equivariance of the group).** For every $g\in G$ and every parameter,

$$
g\circ F_{\tilde C}=F_{g(\tilde C)}\circ g ,
$$

where the left action of $g$ on the parameter is the definition of $g(\tilde C)$. Hence $g(\mathcal K_{\tilde C})=\mathcal K_{g(\tilde C)}$ and $g(J_{\tilde C})=J_{g(\tilde C)}$.

**Proof.** Each of the four maps is a ring endomorphism in the sense of the conjugation articles, so $g(\tilde Q^2)=(g\tilde Q)^2$, and each preserves the Euclidean norm, hence boundedness. Applying $g$ to $\tilde Q^2+\tilde C$ gives the identity. This is the equivariance theorem of *The Biquaternion Quadratic Map and Its Julia Sets*.

**Remark (the fourth conjugation is excluded by a sign).** The natural, the complex and the Hermitian conjugations are anti-automorphisms or automorphisms of the ring; the anti-Hermitian conjugation is an anti-automorphism only up to the central sign,

$$
(\tilde P\tilde Q)^{\flat}=-\tilde Q^{\flat}\tilde P^{\flat} ,
$$

so that $(\tilde Q^2)^{\flat}=-(\tilde Q^{\flat})^2$ and $\flat\circ F_{\tilde C}=F^{-}_{\flat(\tilde C)}\circ\flat$, where $F^{-}_{\tilde C'}(\tilde Q)=-\tilde Q^2+\tilde C'$ is the *odd* quadratic family. **The anti-Hermitian conjugation relates the even family to the odd family, not to itself, and is therefore not a symmetry of the even fractal.** The three conjugations ${}^{\natural},\bar{\cdot},{}^{*}$ are the ones the article uses.

## The Stabiliser and the Symmetry Group

**Definition.** The **symmetry group** of the parameter $\tilde C$ is $G_{\tilde C}=\{g\in G : g(\tilde C)=\tilde C\}$, and the **even symmetry group** is

$$
\Gamma_{\tilde C}=G_{\tilde C}\times\{\pm\mathrm{id}\} ,
$$

where $\mathrm{id}$ acts as the identity and $-\mathrm{id}$ as $\tilde Q\mapsto-\tilde Q$.

**Theorem (the stabiliser).** $G_{\tilde C}$ is one of the following.

1. $G$, when $\tilde C=Ce_0$ with $C$ real.
2. $\{\mathrm{id},{}^{\natural}\}$, when $\tilde C=Ce_0$ with $C$ non-real.
3. $\{\mathrm{id},\bar{\cdot}\}$, when $\tilde C$ is a non-central element fixed by complex conjugation, that is $\tilde C\in\mathbb{H}_{\mathbb{B}}$ with $\tilde C\notin\mathbb{C}e_0$.
4. $\{\mathrm{id},{}^{*}\}$, when $\tilde C$ is a non-central element fixed by Hermitian conjugation, that is $\tilde C\in\mathbb{M}_+$ with $\tilde C\notin\mathbb{C}e_0$.
5. $\{\mathrm{id}\}$, otherwise.

**Proof.** The fixed subspace of ${}^{\natural}$ is the centre, of $\bar{\cdot}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and of ${}^{*}$ the Hermitian sector $\mathbb{M}_+$ (*The Group of Involutions*, *Introduction to the Remarkable Subspaces*). An element fixed by a set of involutions lies in the intersection of their fixed subspaces; the intersections are $\mathbb{C}e_0\cap\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_+=\mathbb{R}e_0$, $\mathbb{C}e_0$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{B}$, for the five cases, and the real central elements are exactly the real multiples of $e_0$.

**Theorem (the even symmetry).** For every parameter, $\mathcal K_{\tilde C}$ and $J_{\tilde C}$ are invariant under $\tilde Q\mapsto-\tilde Q$, and the full symmetry group of the two sets contains $\Gamma_{\tilde C}$.

**Proof.** $F_{\tilde C}(-\tilde Q)=(-\tilde Q)^2+\tilde C=\tilde Q^2+\tilde C=F_{\tilde C}(\tilde Q)$, because the square is an even map; hence $-\tilde Q$ and $\tilde Q$ have the same orbit after the first term, and one orbit is bounded exactly when the other is. The invariance under $G_{\tilde C}$ is the equivariance theorem restricted to the stabiliser. The two families of maps commute: $-\mathrm{id}$ is $(-\mathrm{id})\mathrm{id}$-linear and composes with the conjugations to the conjugations.

## The Symmetric Families

**Theorem (the four symmetric fractals and the generic one).** The symmetry group $\Gamma_{\tilde C}$ is one of

$$
G\times\{\pm\mathrm{id}\}\ (\text{order }8), \quad \{\mathrm{id},{}^{\natural}\}\times\{\pm\mathrm{id}\}\ (\text{order }4), \quad \{\mathrm{id},\bar{\cdot}\}\times\{\pm\mathrm{id}\}, \quad \{\mathrm{id},{}^{*}\}\times\{\pm\mathrm{id}\}, \quad \{\pm\mathrm{id}\}\ (\text{order }2),
$$

according as the parameter is a real central element, a non-real central element, a non-central real quaternion, a non-central Hermitian element, or a general element. The corresponding fractals are the **fully symmetric**, the **centrally symmetric**, the **quaternion-symmetric**, the **Hermitian-symmetric** and the **generic** biquaternion Julia sets.

**Proof.** Immediate from the two theorems above; the orders are those of the products.

**Remark (the names are the fixed subspaces).** The five families are named by the symmetry subspace that contains the parameter, and each family is symmetric about the remarkable subspaces of the algebra: the real central fractals about the centre, the quaternion subspace, the Hermitian sector and the vector part; the central fractals about the centre; the quaternion-symmetric fractals about the quaternion subspace; the Hermitian-symmetric ones about the Hermitian sector. **The symmetry axes of the biquaternion fractals are the remarkable subspaces**, and the classification above is the statement that the parameter lies on the intersection of the axes it preserves.

## The Central Slice and the Mirror

**Proposition (the complex conjugation acts as the mirror on the central slice).** For a central parameter $\tilde C=Ce_0$, the restriction of $\bar{\cdot}$ to the centre is the complex conjugation $C\mapsto\bar C$, and

$$
\bar{\cdot}\bigl(J_{Ce_0}\cap\mathbb{C}e_0\bigr)=J_{\bar C e_0}\cap\mathbb{C}e_0 .
$$

So the Julia set of the complex quadratic map and that of its conjugate parameter are mirror images in the central slice, and they coincide exactly when $C$ is real.

**Proof.** The restriction of the equivariance to the centre, where the dynamics is the complex quadratic map and $\bar{\cdot}$ acts as the coefficientwise conjugation.

**Remark (why the central fractal is not mirror-symmetric for non-real C).** For non-real $C$ the group $G_C$ contains only ${}^{\natural}$, and the mirror $C\mapsto\bar C$ is not in it, so the central slice of $J_{Ce_0}$ is the complex Julia set $J_C$ and not its mirror $J_{\bar C}$; the two are distinct unless $J_C$ happens to be symmetric. **The complex Julia set of a non-real parameter appears in the biquaternion theory exactly as itself, without its mirror, and the mirror is a second slice at the conjugate parameter.** This is the precise content of the failure of the mirror symmetry.

## The Central Inversion and the Antipodal Structure

**Remark (the antipodal quotient).** The even symmetry $\tilde Q\mapsto-\tilde Q$ is present for every parameter and is not a symmetry of the algebra but of the map; the quotient by it is the natural projective picture of the subject. **Every biquaternion Julia set is antipodally symmetric, and a fundamental domain for the inversion is one half of the space; a picture of the whole slice always shows two copies.** The symmetry is a symmetry of the map at every parameter and is not a statement about the parameter: $J_{\tilde C}$ and $J_{-\tilde C}$ are different sets in general, and only the map is invariant under the inversion, not the family.

**Remark (the quaternion slice as the visible symmetry).** In the quaternion slice $\mathbb{H}_{\mathbb{B}}$ the symmetry under ${}^{\natural}$ and $\bar{\cdot}$ is the classical conjugacy symmetry of the quaternion Julia sets, and the symmetry under $\tilde Q\mapsto-\tilde Q$ is the antipodal one; the two generate a group of order four acting on the three-dimensional picture. **The quaternion pictures of the subject are the pictures of the quaternion-symmetric family, and their symmetry is a slice of the full group and not the full group.**

## Summary

The quadratic map is equivariant under three of the four conjugations, and the fourth is excluded because it is an anti-automorphism only up to sign and relates the even family to the odd one. The conjugations that fix the parameter form the stabiliser, a subgroup of the Klein group, and with the central inversion — present at every parameter because the square is even — they generate the symmetry group of the Julia set. The stabiliser is the full group for a real central parameter, the subgroup $\{\mathrm{id},{}^{\natural}\}$ for a non-real central parameter, $\{\mathrm{id},\bar{\cdot}\}$ for a non-central real quaternion, $\{\mathrm{id},{}^{*}\}$ for a non-central Hermitian element, and the trivial group otherwise; the five cases are the five symmetric families, with the symmetry axes the remarkable subspaces. On the central slice, complex conjugation acts as the mirror carrying $J_C$ to $J_{\bar C}$, so a non-real central parameter shows its Julia set without its mirror. Every biquaternion Julia set is antipodally symmetric, and the quaternion picture is a slice of these symmetries.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{\natural},\bar{\cdot},{}^{*},\flat$ | quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the group of involutions |
| $G_{\tilde C}$ | the stabiliser of the parameter |
| $\Gamma_{\tilde C}=G_{\tilde C}\times\{\pm\mathrm{id}\}$ | the even symmetry group |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable subspaces |
| $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ | the quadratic family |
| $J_{\tilde C}$, $\mathcal K_{\tilde C}$ | the Julia set and the filled Julia set |

## Further Reading

- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations, the group they form and their fixed subspaces.
- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the equivariance theorem and the central-parameter reduction.
- *The Slices of the Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-biquaternion-julia-sets.md`), for the central, real and quaternion slices whose symmetries are read here.
- *The Quaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-quaternion-quadratic-map-and-its-julia-sets.md`), for the quaternion pictures and their classical symmetries.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces that are the symmetry axes.
