
# __Split-Biquaternion Operator Representation__

## Introduction

A split biquaternion can be read as an operator on the algebra, and the operator of choice in this corpus is the **sandwich** $\tilde{Q} \mapsto \tilde{R}\tilde{Q}\tilde{R}^\dagger$ built from an element and its Hermitian conjugate. This article treats the carrier, the sandwich, its failure to be an automorphism, the sector and form structure it preserves, its kernel, its action on the four distinguished subspaces, its relation to the polar representation, and the doubling of the angle that makes it a covering map. The companion in the biquaternion category is *Biquaternion Operator Representation*, and the group-theoretic consequences are in *Split-Biquaternion Rotations and the Lorentz Group*.

The treatment is purely mathematical. No physics is invoked; the "Lorentz group" appears only as an isometry group of a form. Elements are written $\tilde{Q} = A + jB$ with $A, B \in \mathbb{H}$, the conjugations are $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = {}^{*}\bar{\cdot}$ and ${}^{\flat}$, the split-biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, and the Hermitian form has scalar part $g(\tilde{Q}) = \sum_\mu (q_\mu^2 - q'^2_\mu)$.

## The Carrier and the Sandwich

### The Carrier

The carrier of the representation is the algebra $\mathbb{H}_{\mathbb{D}}$ regarded as a real vector space of dimension $8$, with the real basis

$$
e_0,\quad e_1,\quad e_2,\quad e_3,\quad je_0,\quad je_1,\quad je_2,\quad je_3 .
$$

A representation is a homomorphism from a group to the invertible linear maps of this space. For left multiplication the group is the unit group and the map is faithful; for the sandwich the group is again the unit group, but the map has a kernel.

### The Sandwich

**Definition.** The **sandwich**, or **dagger sandwich**, of a unit $\tilde{R}$ is the real-linear map

$$
\operatorname{H}_{\tilde{R}} : \mathbb{H}_{\mathbb{D}} \to \mathbb{H}_{\mathbb{D}} , \qquad \operatorname{H}_{\tilde{R}}(x) = \tilde{R}\, x\, \tilde{R}^{\dagger} .
$$

The multiplication is well defined for every unit, and $\operatorname{H}_{\tilde{R}}$ depends only on $\tilde{R}$, the two-sided placement of the conjugates being what distinguishes it from left and right multiplication.

### Comparison with Left Multiplication

| | left multiplication $\tilde{R}x$ | the sandwich $\operatorname{H}_{\tilde{R}}(x) = \tilde{R}x\tilde{R}^\dagger$ |
|---|---|---|
| type of map | algebra endomorphism | neither, but a representation of the units |
| image of $e_0$ | $\tilde{R}$ | $\tilde{R}\tilde{R}^\dagger$, not central in general |
| kernel, $\tilde{R}$ of unit norm | $\{e_0\}$ | $\{\pm e_0\}$ (see below) |
| preserves the split-biquaternion norm | $N(\tilde{R}x) = N(\tilde{R})N(x)$ | $N(\operatorname{H}_{\tilde{R}}x) = \left(N_+(\tilde{R})N_-(\tilde{R})\right)N(x)$ |

Left multiplication is the regular representation, recorded for comparison; the sandwich is the map that a two-sided conjugation by the Hermitian conjugate produces, and the last line is its sharpest difference, the scaling of the split-biquaternion norm by the real factor $N_+N_-$ rather than by the split complex factor $N$.

## The Sandwich

### It Is Not an Automorphism

**Proposition.** The sandwich is not multiplicative for a general unit: for $x, y$,

$$
\operatorname{H}_{\tilde{R}}(xy) = \tilde{R}\,xy\,\tilde{R}^\dagger \neq \left(\tilde{R}x\tilde{R}^\dagger\right)\left(\tilde{R}y\tilde{R}^\dagger\right) = \operatorname{H}_{\tilde{R}}(x)\operatorname{H}_{\tilde{R}}(y) ,
$$

because the insertion required between $x$ and $y$ is $\tilde{R}^\dagger \tilde{R}$, which is the unit exactly when $\tilde{R}$ is unitary.

**Proof.** The two sides differ by the factor $\tilde{R}^\dagger\tilde{R}$; the equality for all $x, y$ holds exactly when $\tilde{R}^\dagger\tilde{R} = e_0$.

So the sandwich is a linear representation of the group of units on the algebra, but not one by algebra automorphisms; on the **unitary subgroup** $\{ \tilde{R} : \tilde{R}\tilde{R}^\dagger = e_0 \}$ one has $\tilde{R}^\dagger = \tilde{R}^{-1}$ and the sandwich is the inner automorphism $x \mapsto \tilde{R} x \tilde{R}^{-1}$.

### It Preserves the Two Sectors

**Theorem.** For every unit $\tilde{R}$, the sandwich maps $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$.

**Proof.** Let $x \in \mathbb{M}_+$, so $x^\dagger = x$. Then

$$
\left(\tilde{R} x \tilde{R}^\dagger\right)^\dagger = \tilde{R}^{\dagger\dagger} x^\dagger \tilde{R}^\dagger = \tilde{R} x \tilde{R}^\dagger ,
$$

so the image is Hermitian and lies in $\mathbb{M}_+$. For $x \in \mathbb{M}_-$ one has $x^\dagger = -x$, so the image is anti-Hermitian.

### The Defect Under the Indefinite Form

**Theorem.** For every unit $\tilde{R}$, with $N_\pm(\tilde{R}) = \sum_\mu (q_\mu \pm q'_\mu)^2$ the two real components of the split-biquaternion norm,

$$
N\!\left(\operatorname{H}_{\tilde{R}}(x)\right) = \left(N_+(\tilde{R})\, N_-(\tilde{R})\right) N(x) , \qquad g\!\left(\operatorname{H}_{\tilde{R}}(x)\right) = g(x) \ \text{whenever } \tilde{R} \text{ is unitary} .
$$

**Proof.** The split-biquaternion norm is multiplicative and central, so $N(\tilde{R} x \tilde{R}^\dagger) = N(\tilde{R}) N(x) N(\tilde{R}^\dagger)$; and $N(\tilde{R}^\dagger) = N(\tilde{R})^{*}$ because $\dagger$ fixes $N$ under $\bar{\cdot}$ and conjugates it under ${}^{*}$. In split complex coordinates $N(\tilde{R})N(\tilde{R})^{*} = N_+(\tilde{R})N_-(\tilde{R})$, a real number of either sign. For the Hermitian form, when $\tilde{R}$ is unitary one has $\tilde{R}^\dagger = \tilde{R}^{-1}$, so $\operatorname{H}_{\tilde{R}}$ is the conjugation $x \mapsto \tilde{R}x\tilde{R}^{-1}$, and conjugation by an element preserves the scalar part; hence $g(\operatorname{H}_{\tilde{R}}(x)) = g(x)$.

The **defect** of the sandwich under the indefinite form is therefore the real factor $N_+N_-$ in the split-biquaternion norm, which can vanish — precisely when $\tilde{R}$ is a zero divisor and hence not a unit, so on the unit group it is nonzero — and the Hermitian form $g$ is preserved by every unitary element. The biquaternion sandwich behaves the same way with $|N(\tilde{R})|^2$ in place of $N_+N_-$; the difference is only that there the factor is a sum of squares and here it is a difference.

### The Kernel

**Theorem.** $\operatorname{H}_{\tilde{R}} = \mathrm{id}$ if and only if $\tilde{R}$ is central and unitary, that is $\tilde{R} = Q_0 e_0$ with $q_0^2 - q'^2_0 = 1$. On the unit-norm slice $N(\tilde{R}) = 1$ the kernel reduces to $\{\pm e_0\}$.

**Proof.** If $\operatorname{H}_{\tilde{R}}(x) = x$ for every $x$, taking $x = e_0$ gives $\tilde{R}\tilde{R}^\dagger = e_0$, so $\tilde{R}$ is unitary, and taking $x$ arbitrary gives $\tilde{R}x = x\tilde{R}$, so $\tilde{R}$ is central. A central element is $Q_0 e_0$ with $Q_0 \in \mathbb{D}$, and it is unitary exactly when $Q_0 Q_0^{*} = q_0^2 - q'^2_0 = 1$, the two branches of a hyperbola in the centre. Restricting to $N(\tilde{R}) = Q_0^2 = 1$ gives $Q_0 = \pm 1$.

The kernel of the full sandwich is therefore $\mathbb{R} \times \mathbb{Z}/2$ in the centre — the split complex units of modulus one — in place of the circle $U(1)$ of the biquaternion case. On the unit-norm slice the kernel is the two central signs, and that kernel of order two is the double cover noted below.

## The Action on the Four Subspaces

### The Table

| subspace | preserved by $\operatorname{H}_{\tilde{R}}$? | image |
|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | no | $\tilde{R} Q_0 \tilde{R}^\dagger$, not central in general |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | no | not closed in general |
| $\mathbb{M}_+$ | yes | $\mathbb{M}_+$ |
| $\mathbb{M}_-$ | yes | $\mathbb{M}_-$ |

### The Centre

The centre is not preserved: on the unit element, $\operatorname{H}_{\tilde{R}}(e_0) = \tilde{R}\tilde{R}^\dagger$, which is Hermitian but not central for a general unit $\tilde{R}$. On the unitary subgroup, where the sandwich is an automorphism, it preserves the centre, since an automorphism carries the centre to itself.

### The Two Sectors

The two sectors are the only subspaces of the four that survive, and they survive as a pair: the sandwich preserves each one separately and cannot move one into the other, because the Hermitian character of an element is exactly what the map preserves. This is the operator-theoretic reason that the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is the natural one for the action.

## The Relation to the Polar Representation

The sandwich sees the polar data of an element through the split-biquaternion norm and the two idempotent components, and the dictionary is:

| polar datum of $\tilde{R}$ | what the sandwich sees |
|---|---|
| the two components $\tilde{R}_+, \tilde{R}_-$ | the two left and right multiplications $\tilde{R}_+$ and $\tilde{R}_-^{-1}$ |
| the scale $r = N_+N_-$ | the dilation $N_+N_-$ of the split-biquaternion norm |
| the central factor of modulus one | nothing, since it is central and unitary: the sandwich is unchanged |
| the two unit-sphere parts | the rotation parts of the action |

The sandwich is blind exactly to the central unitary factor, which is the kernel computed above; every other factor of the element appears in the operator. In the biquaternion case the polar representation has the complex phase as its invisible factor; here the phase is replaced by the two branches of the central hyperbola.

## The Doubling of the Angle

**Theorem.** Let $\hat{q} = \cos\theta + \sin\theta\,\hat{\mathbf{u}}$ be a real unit quaternion, with $\hat{\mathbf{u}}$ a unit real vector, and let $\mathbf{v} = v_1 e_1 + v_2 e_2 + v_3 e_3$ be a real vector. Then

$$
\operatorname{H}_{\hat{q}}(\mathbf{v}) = \mathbf{v}\cos 2\theta + \left(\hat{\mathbf{u}} \times \mathbf{v}\right)\sin 2\theta + \hat{\mathbf{u}}\left(\hat{\mathbf{u}}\cdot\mathbf{v}\right)\left(1 - \cos 2\theta\right) ,
$$

which is the rotation of $\mathbf{v}$ about $\hat{\mathbf{u}}$ through the angle $2\theta$.

**Proof.** For a real quaternion $\hat{q}^\dagger = \bar{\hat{q}} = \hat{q}^{-1}$, so $\operatorname{H}_{\hat{q}}(\mathbf{v}) = \hat{q}\mathbf{v}\hat{q}^{-1}$, the standard quaternion rotation formula; the computation in components gives the three terms, and the resulting linear map is orthogonal, fixes $\hat{\mathbf{u}}$, and rotates the plane orthogonal to $\hat{\mathbf{u}}$ by $2\theta$.

The map $\hat{q} \mapsto \operatorname{H}_{\hat{q}}$ therefore rotates by twice the angle carried by the element, which is why it is not faithful on the rotation group: $\hat{q}$ and $-\hat{q}$ give the same operator, and the two elements are the two elements lying over one rotation. Restricted to the real quaternion sphere this gives the double cover

$$
Sp(1) = SU(2) \longrightarrow SO(3) , \qquad \hat{q} \longmapsto \operatorname{H}_{\hat{q}} ,
$$

with kernel $\{\pm e_0\}$, the same computation as in the biquaternion case but now read on a subgroup.

## The Relation to the Biquaternion Dagger Sandwich

In the biquaternion case the dagger sandwich of a unit-norm element is the action of $SL(2,\mathbb{C})$ on the Hermitian matrices, whose image is the proper orthochronous Lorentz group $SO^+(1,3)$; the unit-norm slice is the double cover of the Lorentz group and the kernel on it is $\{\pm e_0\}$. In the split biquaternion case the unit-norm slice $N(\tilde{R}) = 1$ is the six-dimensional group $S^3 \times S^3$ and the sandwich on it is **not** generally an automorphism, since $\tilde{R}^\dagger \neq \tilde{R}^{-1}$ unless $\tilde{R}$ is unitary; the sandwich acts on $\mathbb{M}_-$ by isometries of the Lorentzian form $g$ whenever $\tilde{R}$ is unitary, that is on the unitary group $\{\tilde{R} : \tilde{R}\tilde{R}^\dagger = e_0\} \cong Sp(1) \times \mathbb{R}$, where it is the inner automorphism. Its image fixes the timelike vector $je_0$ and is the compact rotation group $SO(3)$ of the spacelike three-plane, as computed in *Split-Biquaternion Rotations and the Lorentz Group*, so the unitary group realises the elliptic part of $O(3,1)$ and not its hyperbolic part. The doubling of the angle and the double cover are the same in both cases; the difference is which slice of the algebra carries the Lorentz action. This is the operator-theoretic counterpart of the statement, in *Split-Biquaternion Rotations and the Lorentz Group*, that the split biquaternion algebra presents Lorentzian four-planes of both signatures and that the elliptic rotations are realised by the unitary group.

## Summary

The carrier of the operator representation is the eight-dimensional real algebra, and the operator of a unit $\tilde{R}$ is the sandwich $\operatorname{H}_{\tilde{R}}(x) = \tilde{R}x\tilde{R}^\dagger$. It is linear but not multiplicative; it is an algebra automorphism exactly on the unitary subgroup, where it is the conjugation $x \mapsto \tilde{R}x\tilde{R}^{-1}$. It preserves the two sectors $\mathbb{M}_\pm$ and no other of the four distinguished subspaces, and it scales the split-biquaternion norm by the real factor $N_+(\tilde{R})N_-(\tilde{R})$, which is its defect under the indefinite form; the Hermitian form $g$ of signature $(4,4)$ is preserved by every unitary element, and on the unitary subgroup the image is the compact rotation group $SO(3)$ of the Lorentzian form on $\mathbb{M}_-$. The kernel of the full sandwich is the group of central unitary elements, the split complex units of modulus one, an $\mathbb{R} \times \mathbb{Z}/2$ in the centre, and on the unit-norm slice it reduces to $\{\pm e_0\}$. An element acts on its two idempotent components by independent one-sided multiplications by $\tilde{R}_+$ and $\tilde{R}_-^{-1}$, so that the sandwich sees every factor of the polar representation except the central unitary one. On the real unit quaternions the sandwich rotates the vector part by twice the angle carried by the element, giving the double cover $SU(2) \to SO(3)$ with kernel $\{\pm e_0\}$. Compared with the biquaternion dagger sandwich, the unit-norm slice here is the six-dimensional $S^3\times S^3$ rather than $SL(2,\mathbb{C})$, the Lorentz action sitting on the unitary subgroup instead.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\operatorname{H}_{\tilde{R}}(x) = \tilde{R}x\tilde{R}^\dagger$ | The dagger sandwich |
| $\tilde{R}^\dagger = \bar{\tilde{R}}^{*}$ | Hermitian conjugate |
| unitary subgroup | $\{ \tilde{R} : \tilde{R}\tilde{R}^\dagger = e_0 \} \cong Sp(1) \times \mathbb{R}$ |
| $N(\tilde{R}) = \tilde{R}\bar{\tilde{R}}$ | Split-Biquaternion norm, split complex |
| $N_+(\tilde{R})N_-(\tilde{R})$ | Real scaling factor, the defect of the sandwich |
| $g(\tilde{Q}) = \sum_\mu(q_\mu^2 - q'^2_\mu)$ | Scalar part of the Hermitian form, signature $(4,4)$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | The four distinguished subspaces |
| kernel | Central unitary group, the split complex units of modulus one |
| $2\theta$ | Angle of the sandwich of a rotor of angle $\theta$ |

## Further Reading

- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for inner automorphisms and the unitary group of an algebra with conjugation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the two-sided action of the quaternion sphere and the double cover $Sp(1) \to SO(3)$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the sandwich action of versors on the Clifford algebra and the doubling of the angle.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the isometry groups of the forms of signature $(4,4)$, $(3,1)$ and $(2,2)$.
