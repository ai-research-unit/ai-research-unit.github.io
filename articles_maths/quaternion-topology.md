
# __Quaternion Topology__

## Introduction

This article collects the topology of the quaternion algebra as a space and of its group of units: the topology of the underlying real four-space, its contractibility, the unit sphere, the homotopy type of the units, the low homotopy groups, and the double cover of the rotation group. It is the quaternion member of the family's topology articles; its counterpart is the biquaternion case, whose ambient space carries a null cone of zero divisors and whose group of units is the non-compact $GL_2(\mathbb{C})$. Here there are no zero divisors, the algebra norm and the Euclidean norm coincide, and the unit sphere is a group.

The article uses *Quaternion Algebra* for the basis and product, *Quaternion Norm and Invertibility* for the quaternion norm, division property and unit group, *Quaternion Exponential and Lie Group Structure* for the polar split of the units and the exponential, and *Quaternion Rotations and Reflections* for the covering of the rotation group. The standard algebraic topology used is cited rather than reproved.

The corpus's default base is a commutative ring; the topology here requires the real numbers, and everything is stated over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$; the quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural} = q_0^2+q_1^2+q_2^2+q_3^2$ and the modulus is $|\tilde q| = \sqrt{N(\tilde q)}$; the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere is $Sp(1) = \{\tilde q : N(\tilde q) = 1\}$.

## The Algebra as a Topological Space

**Theorem.** The linear map

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3\longmapsto(q_0,q_1,q_2,q_3)
$$

is a linear isometry of $(\mathbb{H},|\cdot|)$ onto $\mathbb{R}^4$; the product is bilinear, hence continuous, so $\mathbb{H}$ is a topological algebra over $\mathbb{R}$, and inversion is continuous on the units, so $\mathbb{H}^{\times}$ is a topological group.

*Proof.* The quaternion norm is positive definite with four positive signs, $N(\tilde q) = \sum_k q_k^2$, so $|\tilde q|$ is the Euclidean norm of the coordinate vector and the map is an isometry. Bilinearity gives continuity of the product, and $\tilde q^{-1} = \tilde{q}^{\natural}/N(\tilde q)$ is continuous on the complement of $N = 0$, which is $\mathbb{H}^{\times}$ because the quaternion norm is definite.

**Corollary.** The algebra norm and the Euclidean norm agree on $\mathbb{H}$, so multiplication is continuous for the Euclidean topology and $\mathbb{H}$ is a normed division algebra; this is the property that fails for the biquaternions, whose norm is indefinite.

## Contractibility

**Theorem.** The quaternion algebra is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{H}) = 0$ for all $n\geq1$.

*Proof.* The straight-line homotopy $H(t,\tilde q) = (1-t)\tilde q$ is continuous, begins at the identity and ends at the constant map $0$, so the identity of $\mathbb{H}$ is null-homotopic; a contractible space has all homotopy groups trivial.

**Corollary.** Every vector subspace of $\mathbb{H}$ is contractible as a topological space in its own right, and in particular the scalar subspace $\mathbb{R}_{\mathbb{H}}\cong\mathbb{R}$ and the vector subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ carry no topology beyond that of Euclidean space.

*Proof.* Each is a vector subspace, and the straight-line homotopy above restricts to it.

## The Unit Sphere

**Definition.** The **unit sphere** of $\mathbb{H}$ is $S^3 = \{\tilde q : |\tilde q| = 1\} = Sp(1)$.

**Theorem.** The unit sphere is a closed, compact, connected three-dimensional manifold, homeomorphic to the standard sphere $S^3\subset\mathbb{R}^4$, and it is a topological group under the inherited multiplication, with $S^3\subseteq\mathbb{H}^{\times}$; its smooth and Lie-group structure is that of *Quaternion Exponential and Lie Group Structure*, where it is identified with $Sp(1)\cong SU(2)$.

*Proof.* The unit sphere is the level set of the continuous function $N$ at $1$, hence closed, and it is bounded in $\mathbb{R}^4$, hence compact; it is connected, and the coordinate identification carries it homeomorphically onto the standard sphere, by *Quaternion Norm and Invertibility*. The product of two units is a unit by the multiplicativity $N(p\tilde q) = N(p)N(\tilde q)$, and the operations are continuous, so it is a topological group. Since every unit quaternion is non-zero, $S^3\subseteq\mathbb{H}^{\times}$.

**Remark.** Multiplicativity of the quaternion norm, $N(p\tilde q) = N(p)N(\tilde q)$, is exactly the statement that $S^3$ is closed under the product, so the unit sphere is a subgroup rather than merely a subset; for the biquaternions the corresponding Euclidean sphere is not closed under the product and is not contained in the unit group.

## The Group of Units

**Theorem.** The map $\tilde q\mapsto(|\tilde q|,\tilde q/|\tilde q|)$ is a homeomorphism

$$
\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3,
$$

and the inclusion $S^3\hookrightarrow\mathbb{H}^{\times}$ is a homotopy equivalence; hence the group of units is homotopy equivalent to the sphere $S^3$.

*Proof.* The polar split of *Quaternion Norm and Invertibility* gives the bijection, both directions being continuous; the deformation retraction $r(t,\tilde q) = (1-t)\tilde q+t\,\tilde q/|\tilde q|$ is continuous and retracts $\mathbb{H}^{\times}$ onto $S^3$ along the radial lines.

**Corollary.** The group of units is path-connected and locally path-connected, and it is not compact; it deformation retracts onto the compact subgroup $Sp(1)$, which is its maximal compact subgroup.

*Proof.* $\mathbb{R}_{>0}\times S^3$ is connected and non-compact; the retraction is the corollary to the homeomorphism, and the maximality of $Sp(1)$ is from *Quaternion Exponential and Lie Group Structure*.

## The Homotopy Groups

**Theorem.** The group of units is simply connected and has the homotopy groups of the sphere,

$$
\pi_1(\mathbb{H}^{\times}) = 0, \qquad \pi_2(\mathbb{H}^{\times}) = 0, \qquad \pi_3(\mathbb{H}^{\times})\cong\mathbb{Z},
$$

and more generally $\pi_n(\mathbb{H}^{\times})\cong\pi_n(S^3)$ for every $n$.

*Proof.* By the homotopy equivalence $\mathbb{H}^{\times}\simeq S^3$ the homotopy groups agree with those of $S^3$; the sphere $S^3$ is simply connected, $\pi_2(S^3) = 0$, and the Hopf fibration $S^3\to S^2$ with fibre $S^1$ generates $\pi_3(S^3)\cong\mathbb{Z}$.

**Theorem.** The rotation group of the vector subspace is the projective space,

$$
SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3,
$$

with homotopy groups

$$
\pi_1(SO(3))\cong\mathbb{Z}/2, \qquad \pi_2(SO(3)) = 0, \qquad \pi_3(SO(3))\cong\mathbb{Z}.
$$

*Proof.* The quotient identification is *Quaternion Rotations and Reflections*; the covering $\mathbb{Z}/2\to S^3\to\mathbb{RP}^3$ has connected total space, so its homotopy exact sequence gives $\pi_1(\mathbb{RP}^3)\cong\pi_0(\mathbb{Z}/2)\cong\mathbb{Z}/2$ and isomorphisms $\pi_n(\mathbb{RP}^3)\cong\pi_n(S^3)$ for every $n\geq2$; with $\pi_2(S^3) = 0$ and $\pi_3(S^3)\cong\mathbb{Z}$ this gives the listed groups.

**Corollary.** The fundamental group $\mathbb{Z}/2$ belongs to the rotation group, the quotient, and not to the group of units: the group of units and the unit sphere are simply connected, whereas their adjoint quotient by the centre $\{\pm1\}$ is the rotation group and has fundamental group $\mathbb{Z}/2$.

## The Double Cover of the Rotation Group

**Theorem.** The adjoint map $u\mapsto\operatorname{Ad}_u|_{\operatorname{Im}\mathbb{H}}$ is a surjective group homomorphism

$$
Sp(1)\longrightarrow SO(3)
$$

with kernel $\{\pm1\}$, so the unit sphere is a two-to-one covering group of the rotation group, $SO(3)\cong Sp(1)/\{\pm1\}$; the covering $Sp(1)\to SO(3)$ is the universal cover of $SO(3)$.

*Proof.* The homomorphism property and the kernel follow from *Quaternion Automorphisms and Derivations*; the cover is connected and simply connected, being $S^3$, so it is the universal cover of the connected manifold $SO(3)$.

**Corollary.** The double cover is the topological content of the sign ambiguity of the unit quaternion representing a rotation: $\operatorname{Ad}_u = \operatorname{Ad}_{-u}$, and the two lifts of a closed loop in $SO(3)$ return to opposite points of $Sp(1)$ exactly when the loop is not null-homotopic, in agreement with $\pi_1(SO(3))\cong\mathbb{Z}/2$.

## Comparison with the Biquaternion Case

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the same real dimension eight and is contractible as an ambient space, but its norm is indefinite and it has zero divisors, and this changes the distinguished subsets and the unit group.

| Feature | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|
| Underlying space | $\mathbb{R}^4$, contractible | $\mathbb{R}^8$, contractible |
| Norm | definite, $N(\tilde q) = \sum_k q_k^2$, $N = \lvert\cdot\rvert^2$ | indefinite, complex valued |
| Zero divisors / null set | none: $\tilde q\neq0\Rightarrow N(\tilde q) > 0$ | the null cone $\mathcal{N} = \{N = 0\}$, real dimension $6$ |
| Euclidean unit sphere | $S^3 = Sp(1)$, a group, $S^3\subseteq\mathbb{H}^{\times}$ | $S^7_E$, not a group, $S^7_E\not\subseteq\mathbb{B}^{\times}$ |
| Group of units | $\mathbb{R}_{>0}\times S^3\simeq S^3$ | $GL_2(\mathbb{C})\simeq U(2)\simeq S^1\times S^3$ |
| Polar representation | global on $\mathbb{H}^{\times}$ | only off the null cone |
| Homotopy groups of the units | $\pi_1 = 0$, $\pi_3\cong\mathbb{Z}$ | $\pi_1\cong\mathbb{Z}$, $\pi_3\cong\mathbb{Z}$ |
| Rotation group from the adjoint action | $SO(3)$, $\pi_1\cong\mathbb{Z}/2$ | $PSL(2,\mathbb{C})$, non-compact |

The essential difference is the definiteness of the quaternion norm. For $\mathbb{H}$ the polar decomposition $\tilde q = |\tilde q|\,u$ is defined for every non-zero quaternion, so the group of units is a global product and the sphere $S^3$ is a deformation retract; there is no boundary or exceptional set in the polar representation. For $\mathbb{B}$ the same construction is available only where $N\neq0$, the null cone being the obstruction, and the unit group is the non-compact $GL_2(\mathbb{C})$, whose maximal compact subgroup $U(2)$ deforms to $S^1\times S^3$ and contributes the free factor $\mathbb{Z}$ to $\pi_1$. The biquaternion account is in *Biquaternion Topology*.

## Summary

The quaternion algebra is the Euclidean space $\mathbb{R}^4$ with the product as a continuous bilinear map, so it is a topological algebra and a normed division algebra; the algebra norm and the Euclidean norm coincide, and the space is contractible with all homotopy groups trivial. The unit sphere $S^3 = Sp(1)$ is a compact connected topological group contained in the unit group, because the quaternion norm is multiplicative; its Lie-group structure and its identification with $SU(2)$ are in *Quaternion Exponential and Lie Group Structure*.

The group of units is homeomorphic to $\mathbb{R}_{>0}\times S^3$ and deformation retracts onto $S^3$, so it is homotopy equivalent to the sphere: $\pi_1 = 0$, $\pi_2 = 0$, $\pi_3\cong\mathbb{Z}$. Its adjoint quotient by the centre is the rotation group $SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3$, which has $\pi_1\cong\mathbb{Z}/2$, $\pi_2 = 0$, $\pi_3\cong\mathbb{Z}$; the fundamental group $\mathbb{Z}/2$ therefore belongs to the quotient and not to the units.

The adjoint map $Sp(1)\to SO(3)$ is the universal two-to-one cover, with kernel $\{\pm1\}$, which is the topological content of the sign ambiguity in the unit-quaternion parametrisation of a rotation. The biquaternion case differs through the indefiniteness of its norm: its null cone obstructs the polar representation, its Euclidean unit sphere is not a group and is not contained in the units, and its unit group $GL_2(\mathbb{C})$ has $\pi_1\cong\mathbb{Z}$. For the quaternion division algebra the polar representation is global and has no boundary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}\cong\mathbb{R}^4$ | Quaternion algebra as a topological space; contractible |
| $\lvert \tilde q\rvert = \sqrt{N(\tilde q)}$ | Modulus, equal to the Euclidean norm |
| $N(\tilde q) = \tilde q\tilde{q}^{\natural} = \sum_k q_k^2$ | Definite norm, four positive signs |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar and vector subspaces, $\cong\mathbb{R}$ and $\cong\mathbb{R}^3$ |
| $S^3 = Sp(1) = \{\lvert \tilde q\rvert = 1\}$ | Unit sphere; compact group, $S^3\subseteq\mathbb{H}^{\times}$ |
| $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$ | Group of units; $\simeq S^3$ |
| $\pi_1(\mathbb{H}^{\times}) = 0$, $\pi_3(\mathbb{H}^{\times})\cong\mathbb{Z}$ | Homotopy groups of the units |
| $\operatorname{Ad}_u(\tilde q) = u\tilde q u^{-1}$ | Adjoint action; quotient map to $SO(3)$ |
| $SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3$ | Rotation group; $\pi_1\cong\mathbb{Z}/2$ |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra; indefinite norm, null cone |
| $\mathcal{N} = \{N = 0\}$ | Null cone of $\mathbb{B}$, absent here |
| $GL_2(\mathbb{C})\simeq U(2)\simeq S^1\times S^3$ | Biquaternion group of units |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for homotopy groups, covering spaces and the fundamental group of projective space.
- Dale Husemoller, *Fibre Bundles* (Springer, 3rd ed. 1994), for the Hopf fibration and the homotopy of spheres.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the covering $SU(2)\to SO(3)$ and the topology of the classical groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for the homotopy groups of the compact classical groups.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the unit sphere and the group of units of a quaternion algebra.
- Norman Steenrod, *The Topology of Fibre Bundles* (Princeton University Press, 1951), for fibre bundles, covering spaces and the homotopy groups of spheres.
