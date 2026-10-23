# __The Three Conjugations and the Symmetric Biquaternion Fractals__

## Introduction

The biquaternion algebra carries four conjugations, and the quadratic map is equivariant under three of them — the fourth relates the even family to the odd one — so each of the three that fixes the parameter is a symmetry of the corresponding Julia set. This gives a family of symmetric fractals, one for each subgroup of the group of involutions that can occur as a stabiliser, and it organises the pictures of the subject by their symmetry rather than by their coordinates. Two further symmetries are present at every parameter: the central inversion, because the square of an element is unchanged when the element is negated, and the identity, and the two together with the conjugations form the full symmetry group the elementary theory detects.

The four conjugations, their fixed subspaces and the involution group are *The Group of Involutions*; the remarkable subspaces are *Introduction to the Remarkable Subspaces*; the quadratic family and the equivariance theorem are *The Biquaternion Quadratic Map and Its Julia Sets*; the slices are *The Slices of the Biquaternion Julia Sets*; the quaternion and complex fractal pictures are *The Quaternion Quadratic Map and Its Julia Sets* and *The Julia Sets of a Complex Polynomial*.

The article owns the three conjugations used for symmetry (the fourth is excluded, with the reason), the equivariance restated for the group, the classification of the stabiliser and the resulting symmetric families, the extra central inversion, and the identification of the symmetry subspaces with the remarkable subspaces. It does not re-derive the conjugations or the equivariance.

**Standing convention.** ${}^{\natural}$ is quaternion conjugation, $\bar{\cdot}$ complex conjugation, ${}^{*}$ Hermitian conjugation and $\flat$ anti-Hermitian conjugation, so that ${}^{*}={}^{\natural}\bar{\cdot}$, $\flat=-{}^{*}$, and the four maps form the group of involutions $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$. $F_{\tilde Q_3}(\tilde Q_1)=\tilde Q_1^2+\tilde Q_3$.

## The Three Conjugations Used and the One Excluded

**Proposition (the equivariance of the group).** For every $g\in G$ and every parameter,

$$
\boxed{\;g\circ F_{\tilde Q_3}=F_{g(\tilde Q_3)}\circ g\;},
$$

where the left action of $g$ on the parameter is the definition of $g(\tilde Q_3)$. Hence $g(\mathcal K_{\tilde Q_3})=\mathcal K_{g(\tilde Q_3)}$ and $g(J_{\tilde Q_3})=J_{g(\tilde Q_3)}$.

**Proof.** Each of the four maps is a ring endomorphism in the sense of the conjugation articles, so $g(\tilde Q_1^2)=(g\tilde Q_1)^2$, and each preserves the Euclidean norm, hence boundedness. Applying $g$ to $\tilde Q_1^2+\tilde Q_3$ gives the identity. This is the equivariance theorem of *The Biquaternion Quadratic Map and Its Julia Sets*.

**Remark (the fourth conjugation is excluded by a sign).** The natural, the complex and the Hermitian conjugations are anti-automorphisms or automorphisms of the ring; the anti-Hermitian conjugation is an anti-automorphism only up to the central sign,

$$
\boxed{\;(\tilde Q_2\tilde Q_1)^{\flat}=-\tilde Q_1^{\flat}\tilde Q_2^{\flat}\;},
$$

so that $(\tilde Q_1^2)^{\flat}=-(\tilde Q_1^{\flat})^2$ and $\flat\circ F_{\tilde Q_3}=F^{-}_{\flat(\tilde Q_3)}\circ\flat$, where $F^{-}_{\tilde Q_3'}(\tilde Q_1)=-\tilde Q_1^2+\tilde Q_3'$ is the *odd* quadratic family. **The anti-Hermitian conjugation relates the even family to the odd family, not to itself, and is therefore not a symmetry of the even fractal.** The three conjugations ${}^{\natural},\bar{\cdot},{}^{*}$ are the ones the article uses.

## The Stabiliser and the Symmetry Group

**Definition.** The **symmetry group** of the parameter $\tilde Q_3$ is $G_{\tilde Q_3}=\{g\in G : g(\tilde Q_3)=\tilde Q_3\}$, and the **even symmetry group** is

$$
\Gamma_{\tilde Q_3}=G_{\tilde Q_3}\times\{\pm\mathrm{id}\} ,
$$

where $\mathrm{id}$ acts as the identity and $-\mathrm{id}$ as $\tilde Q_1\mapsto-\tilde Q_1$.

**Theorem (the stabiliser).** $G_{\tilde Q_3}$ is one of the following.

1. $G$, when $\tilde Q_3=Ce_t$ with $C$ real.
2. $\{\mathrm{id},{}^{\natural}\}$, when $\tilde Q_3=Ce_t$ with $C$ non-real.
3. $\{\mathrm{id},\bar{\cdot}\}$, when $\tilde Q_3$ is a non-central element fixed by complex conjugation, that is $\tilde Q_3\in\mathbb{H}_{\mathbb{B}}$ with $\tilde Q_3\notin\mathbb{C}e_t$.
4. $\{\mathrm{id},{}^{*}\}$, when $\tilde Q_3$ is a non-central element fixed by Hermitian conjugation, that is $\tilde Q_3\in\mathbb{M}_+$ with $\tilde Q_3\notin\mathbb{C}e_t$.
5. $\{\mathrm{id}\}$, otherwise.

**Proof.** The fixed subspace of ${}^{\natural}$ is the centre, of $\bar{\cdot}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and of ${}^{*}$ the Hermitian sector $\mathbb{M}_+$ (*The Group of Involutions*, *Introduction to the Remarkable Subspaces*). An element fixed by a set of involutions lies in the intersection of their fixed subspaces; the intersections are $\mathbb{C}e_t\cap\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_+=\mathbb{R}e_t$, $\mathbb{C}e_t$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{B}$, for the five cases, and the real central elements are exactly the real multiples of $e_t$.

**Theorem (the even symmetry).** For every parameter, $\mathcal K_{\tilde Q_3}$ and $J_{\tilde Q_3}$ are invariant under $\tilde Q_1\mapsto-\tilde Q_1$, and the full symmetry group of the two sets contains $\Gamma_{\tilde Q_3}$.

**Proof.** $F_{\tilde Q_3}(-\tilde Q_1)=(-\tilde Q_1)^2+\tilde Q_3=\tilde Q_1^2+\tilde Q_3=F_{\tilde Q_3}(\tilde Q_1)$, because the square is an even map; hence $-\tilde Q_1$ and $\tilde Q_1$ have the same orbit after the first term, and one orbit is bounded exactly when the other is. The invariance under $G_{\tilde Q_3}$ is the equivariance theorem restricted to the stabiliser. The two families of maps commute: $-\mathrm{id}$ is $(-\mathrm{id})\mathrm{id}$-linear and composes with the conjugations to the conjugations.

## The Symmetric Families

**Theorem (the four symmetric fractals and the generic one).** The symmetry group $\Gamma_{\tilde Q_3}$ is one of

$$
\boxed{\;G\times\{\pm\mathrm{id}\}\ (\text{order }8), \quad \{\mathrm{id},{}^{\natural}\}\times\{\pm\mathrm{id}\}\ (\text{order }4), \quad \{\mathrm{id},\bar{\cdot}\}\times\{\pm\mathrm{id}\}, \quad \{\mathrm{id},{}^{*}\}\times\{\pm\mathrm{id}\}, \quad \{\pm\mathrm{id}\}\ (\text{order }2)\;},
$$

according as the parameter is a real central element, a non-real central element, a non-central real quaternion, a non-central Hermitian element, or a general element. The corresponding fractals are the **fully symmetric**, the **centrally symmetric**, the **quaternion-symmetric**, the **Hermitian-symmetric** and the **generic** biquaternion Julia sets.

**Proof.** Immediate from the two theorems above; the orders are those of the products.

**Remark (the names are the fixed subspaces).** The five families are named by the symmetry subspace that contains the parameter, and each family is symmetric about the remarkable subspaces of the algebra: the real central fractals about the centre, the quaternion subspace, the Hermitian sector and the vector part; the central fractals about the centre; the quaternion-symmetric fractals about the quaternion subspace; the Hermitian-symmetric ones about the Hermitian sector. **The symmetry axes of the biquaternion fractals are the remarkable subspaces**, and the classification above is the statement that the parameter lies on the intersection of the axes it preserves.

## The Central Slice and the Mirror

**Proposition (the complex conjugation acts as the mirror on the central slice).** For a central parameter $\tilde Q_3=Ce_t$, the restriction of $\bar{\cdot}$ to the centre is the complex conjugation $C\mapsto\bar C$, and

$$ \boxed{\;\bar{\cdot}\bigl(J_{Ce_t}\cap\mathbb{C}e_t\bigr)=J_{\bar C e_t}\cap\mathbb{C}e_t\;}. $$

So the Julia set of the complex quadratic map and that of its conjugate parameter are mirror images in the central slice, and they coincide exactly when $C$ is real.

**Proof.** The restriction of the equivariance to the centre, where the dynamics is the complex quadratic map and $\bar{\cdot}$ acts as the coefficientwise conjugation.

**Remark (why the central fractal is not mirror-symmetric for non-real C).** For non-real $C$ the group $G_C$ contains only ${}^{\natural}$, and the mirror $C\mapsto\bar C$ is not in it, so the central slice of $J_{Ce_t}$ is the complex Julia set $J_C$ and not its mirror $J_{\bar C}$; the two are distinct unless $J_C$ happens to be symmetric. **The complex Julia set of a non-real parameter appears in the biquaternion theory exactly as itself, without its mirror, and the mirror is a second slice at the conjugate parameter.** This is the precise content of the failure of the mirror symmetry.

## The Central Inversion and the Antipodal Structure

**Remark (the antipodal quotient).** The even symmetry $\tilde Q_1\mapsto-\tilde Q_1$ is present for every parameter and is not a symmetry of the algebra but of the map; the quotient by it is the natural projective picture of the subject. **Every biquaternion Julia set is antipodally symmetric, and a fundamental domain for the inversion is one half of the space; a picture of the whole slice always shows two copies.** The symmetry is a symmetry of the map at every parameter and is not a statement about the parameter: $J_{\tilde Q_3}$ and $J_{-\tilde Q_3}$ are different sets in general, and only the map is invariant under the inversion, not the family.

**Remark (the quaternion slice as the visible symmetry).** In the quaternion slice $\mathbb{H}_{\mathbb{B}}$ the symmetry under ${}^{\natural}$ and $\bar{\cdot}$ is the classical conjugacy symmetry of the quaternion Julia sets, and the symmetry under $\tilde Q_1\mapsto-\tilde Q_1$ is the antipodal one; the two generate a group of order four acting on the three-dimensional picture. **The quaternion pictures of the subject are the pictures of the quaternion-symmetric family, and their symmetry is a slice of the full group and not the full group.**

## Summary

The quadratic map is equivariant under three of the four conjugations, and the fourth is excluded because it is an anti-automorphism only up to sign and relates the even family to the odd one. The conjugations that fix the parameter form the stabiliser, a subgroup of the Klein group, and with the central inversion — present at every parameter because the square is even — they generate the symmetry group of the Julia set. The stabiliser is the full group for a real central parameter, the subgroup $\{\mathrm{id},{}^{\natural}\}$ for a non-real central parameter, $\{\mathrm{id},\bar{\cdot}\}$ for a non-central real quaternion, $\{\mathrm{id},{}^{*}\}$ for a non-central Hermitian element, and the trivial group otherwise; the five cases are the five symmetric families, with the symmetry axes the remarkable subspaces. On the central slice, complex conjugation acts as the mirror carrying $J_C$ to $J_{\bar C}$, so a non-real central parameter shows its Julia set without its mirror. Every biquaternion Julia set is antipodally symmetric, and the quaternion picture is a slice of these symmetries.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{\natural},\bar{\cdot},{}^{*},\flat$ | quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the group of involutions |
| $G_{\tilde Q_3}$ | the stabiliser of the parameter |
| $\Gamma_{\tilde Q_3}=G_{\tilde Q_3}\times\{\pm\mathrm{id}\}$ | the even symmetry group |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_+,\mathbb{M}_-$ | the remarkable subspaces |
| $F_{\tilde Q_3}(\tilde Q_1)=\tilde Q_1^2+\tilde Q_3$ | the quadratic family |
| $J_{\tilde Q_3}$, $\mathcal K_{\tilde Q_3}$ | the Julia set and the filled Julia set |

## Further Reading

- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, the group they form and their fixed subspaces.
- [The Biquaternion Quadratic Map and Its Julia Sets](the-biquaternion-quadratic-map-and-its-julia-sets.html), for the equivariance theorem and the central-parameter reduction.
- [The Slices of the Biquaternion Julia Sets](the-slices-of-the-biquaternion-julia-sets.html), for the central, real and quaternion slices whose symmetries are read here.
- [The Quaternion Quadratic Map and Its Julia Sets](the-quaternion-quadratic-map-and-its-julia-sets.html), for the quaternion pictures and their classical symmetries.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable subspaces that are the symmetry axes.
