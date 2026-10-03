
# __Split-Biquaternion Null Quadric and Projective Geometry__

## Introduction

The split biquaternion algebra carries a split complex valued norm, a real Euclidean form as its real part, and a Hermitian form of signature $(4,4)$; the projectivisation of the last is a smooth quadric of Kleinian type in $\mathbb{P}^7$, and the zero divisor set of the algebra projects to a pair of maximal linear subspaces of that quadric. This article treats the zero divisor locus and its rank-one description, the Segre structure and its degeneration, the projective null quadric of the Hermitian form, and the relations to the projective geometry of the biquaternions and to the Lorentzian geometry. The algebra and the forms are used from *Split-Biquaternion Algebra*, *Split-Biquaternion Norm and Invertibility* and *Split-Biquaternion Rotations and the Lorentz Group*, where the split-biquaternion norm, its polarisation and the real forms with their signatures are established; the geometric picture of a single algebra is in *Split-Biquaternion Geometry*.

The treatment is purely mathematical. No physics is invoked; the projective and quadric language is that of *Quadratic Forms and Polarisation* and of *Pseudo-Riemannian and Lorentzian Geometry*, cited rather than reproduced.

## The Null Cone of the Split-Biquaternion Norm

**Theorem.** The split-biquaternion norm $N$ is **anisotropic**: $N(\tilde{Q}) = 0$ if and only if $\tilde{Q} = 0$. Consequently the null cone of $N$ is the single point $\{0\}$.

This is established in *Split-Biquaternion Norm and Invertibility*; the reason is that $\mathrm{Re}\,N(\tilde{Q}) = R(\tilde{Q})$ is a sum of squares of the eight real coordinates, vanishing only at the origin.

The set of elements that are not units is nevertheless large, and it is cut out by $N$ taking a zero divisor value rather than the value zero. This is the essential difference from the biquaternion case, where the zero divisors are exactly the null cone of an isotropic form over $\mathbb{C}$; here the split-biquaternion norm is anisotropic and the non-invertible elements are described by the vanishing of one split complex component.

## The Rank-One Description and the Zero Divisor Locus

**Definition.** An element $\tilde{Q} \neq 0$ is a **zero divisor** if there is a nonzero $\tilde{R}$ with $\tilde{Q}\tilde{R} = 0$ or $\tilde{R}\tilde{Q} = 0$. The **zero divisor locus** is the set $Z \subset \mathbb{H}_{\mathbb{D}}$ of zero divisors together with $0$.

**Theorem.** $\tilde{Q}$ is a zero divisor if and only if $N(\tilde{Q})$ is a zero divisor of $\mathbb{D}$, equivalently if and only if one of the two idempotent components vanishes:

$$
Z = \mathbb{H} \tilde\Pi_+ \cup \mathbb{H} \tilde\Pi_- = \{\tilde{Q}_+ = 0\} \cup \{\tilde{Q}_- = 0\} .
$$

Each of the two sets is a four-dimensional real subspace, and they meet only at the origin.

**Proof.** The split-biquaternion norm is multiplicative and the inverse formula $\tilde{Q}^{-1} = \tilde{Q}^{\natural}N(\tilde{Q})^{-1}$ holds, so $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})$ is a unit of $\mathbb{D}$; the non-units are the elements whose split-biquaternion norm is $0$ or a nonzero zero divisor of $\mathbb{D}$. Since $N(\tilde{Q}) = N_+(\tilde{Q})\tilde\Pi_+ + N_-(\tilde{Q})\tilde\Pi_-$ with $N_\pm(\tilde{Q}) = \sum_\mu (q_\mu\pm q'_\mu)^2$, the split-biquaternion norm is a zero divisor of $\mathbb{D}$ exactly when one of $N_\pm$ vanishes, and a sum of squares vanishes exactly when all its terms do, that is when $\tilde{Q}_\pm = 0$.

**Definition.** An element is of **rank one** if it generates a minimal left ideal, that is if the left ideal $\mathbb{H}_{\mathbb{D}}\tilde{Q}$ is one of the two minimal left ideals.

**Theorem.** The nonzero zero divisors are exactly the elements of rank one. Explicitly, every nonzero zero divisor is $\tilde{Q} = u \tilde\Pi_+$ or $\tilde{Q} = u \tilde\Pi_-$ with $u \in \mathbb{H} \setminus \{0\}$, and the two families are the two minimal left ideals.

**Proof.** $\mathbb{H}_{\mathbb{D}} \tilde\Pi_+ = \mathbb{H} \tilde\Pi_+$ is minimal, since its annihilator contains $\tilde\Pi_-$; and $\mathbb{H}_{\mathbb{D}}\tilde{Q}$ is minimal exactly when $\tilde{Q}$ is a zero divisor, because writing $\tilde{Q} = (\tilde{Q}_+,\tilde{Q}_-)$ the ideal is the pair of ideals $(\mathbb{H}\tilde{Q}_+,\mathbb{H}\tilde{Q}_-)$, which is minimal precisely when one component vanishes, each factor $\mathbb{H}$ being a division algebra so that a single nonzero component generates all of it.

The rank-one description here is thus a **single-quaternion** parametrisation, $\tilde{Q} = u \tilde\Pi_\pm$, in which only one quaternion parameter occurs — the degenerate counterpart of the outer product $uv^{T}$ of the biquaternion case, in which two independent spinor parameters occur. The reason is structural: $\mathbb{H}$ is a division algebra, so no nonzero element of a single factor is a zero divisor, and the rank-one elements are exactly those killed by one of the two central idempotents.

## The Projective Null Quadric

**Definition.** The **projective null quadric** of the algebra is the projectivisation of the null cone of the Hermitian form $g$:

$$
Q(g) = \left\{ [\tilde{Q}] \in \mathbb{P}(\mathbb{H}_{\mathbb{D}}) : g(\tilde{Q}) = 0 \right\} \subset \mathbb{P}^7 , \qquad g(\tilde{Q}) = \sum_\mu (q_\mu^2 - q'^2_\mu) .
$$

**Theorem.** $Q(g)$ is a smooth non-degenerate quadric of dimension $6$ and of Kleinian signature $(4,4)$. It contains two families of maximal isotropic projective three-spaces, and through each point of $Q(g)$ there passes exactly one member of each family. The two zero divisor ideals project to two skew maximal isotropic three-spaces, and these two lie in the same family.

**Proof.** The null cone of $g$ is a smooth irreducible hypersurface away from the origin because the gradient of $g$ is nonzero there; projectivising gives a smooth quadric of dimension $6$. The maximal totally isotropic subspaces of a non-degenerate form of signature $(4,4)$ have dimension $4$, so their projectivisations are three-spaces; the two families and the incidence properties are the standard description of the maximal isotropic subspaces of a neutral form. The ideals are totally isotropic of dimension $4$ by *Split-Biquaternion Geometry*, so each projects to a maximal isotropic three-space.

The zero divisor locus thus has a projective description: it is not a hypersurface but the union of two skew linear three-spaces on the quadric, and the quadric is the unique smooth quadric of signature $(4,4)$ up to projective equivalence.

## The Segre Embedding and Its Degeneration

In the biquaternion case the norm is the determinant and the nonzero null elements are the rank-one matrices $uv^{T}$; projectivising gives the **Segre embedding** $\mathbb{P}^1\times\mathbb{P}^1 \to \mathbb{P}^3$, whose image is the null quadric $Q^2$, and the two rulings are the two families of spinor lines. The split biquaternion case does not admit this description, and the reason is exact.

**Theorem.** There is no Segre embedding whose image is the projective zero divisor locus. Instead, the projectivised zero divisor locus splits as a disjoint union of two projective three-spaces,

$$
\mathbb{P}(Z) = \mathbb{P}(\mathbb{H}\tilde\Pi_+) \sqcup \mathbb{P}(\mathbb{H}\tilde\Pi_-) = \mathbb{P}^3 \sqcup \mathbb{P}^3 ,
$$

with no incidence between them; the analogue of the rank-one outer product is the single-factor parametrisation $\tilde{Q} = u \tilde\Pi_\pm$, and the analogue of the tensor product of two spinor spaces is absent.

**Proof.** The rank-one elements are parametrised by a single nonzero quaternion $u$, up to a real scalar, giving $\mathbb{P}(\mathbb{H}\tilde\Pi_\pm) \cong \mathbb{P}^3$; two such projective points never coincide because the two ideals meet only at the origin, and no projectively invariant two-parameter factorisation exists, because $\mathbb{H}$ is a division algebra and its projective line $\mathbb{P}^1(\mathbb{H}) \cong S^4$ is not the $\mathbb{P}^1$ of the biquaternion spinors.

The Segre-type object that does appear is the biquaternion one transported through the idempotent decomposition: the biquaternion quadric $Q^2 = \mathbb{P}^1\times\mathbb{P}^1$ corresponds, under the Peirce decomposition, to a pair of quaternionic rank-one conditions, each of which is vacuous because $\mathbb{H}$ is a division algebra. In this sense the Segre structure does not degenerate into a different Segre structure; it vanishes, and the smooth quadric $Q(g)$ of the previous section is the genuinely new object.

## The Relation to the Biquaternion Case

The biquaternion norm is $\sum Q_\mu^2$ with $Q_\mu \in \mathbb{C}$; over $\mathbb{C}$ it is the determinant of $M_2(\mathbb{C})$, its null cone is the zero divisor set, and its projectivisation is the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$. The realification $\mathrm{Re}\,N$ has split signature $(4,4)$ and the Lorentzian slice is $\mathbb{M}_+$ or $\mathbb{M}_-$ up to sign. The split biquaternion norm is $\sum Q_\mu^2$ with $Q_\mu \in \mathbb{D}$; its real part is now positive definite rather than split, and the indefinite structure lives entirely in the Hermitian form $g$ and in the imaginary part $I$. The projective translations are: the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ of the biquaternion case is replaced by the disjoint union $\mathbb{P}^3 \sqcup \mathbb{P}^3$; the Clifford algebra $\mathrm{Cl}(\mathbb{B},N)\cong M_4(\mathbb{C})$ of the biquaternion case is replaced by the Clifford algebra of the split complex form, whose real part is definite; and the Weyl spinor lines of the biquaternion case have no counterpart, because the two minimal left ideals contain quaternions rather than two-component spinors.

## The Relation to the Lorentzian Geometry

On the Lorentzian four-plane $\mathbb{M}_-$ the split-biquaternion norm restricts to the real Lorentzian form of signature $(3,1)$ and the Hermitian form restricts to the same form up to sign, so the two null cones agree on $\mathbb{M}_-$: the null cone in $\mathbb{M}_-$ is the cone $q'^2_0 = \sum_k q_k^2$. Projectivising inside $\mathbb{P}(\mathbb{M}_-) = \mathbb{P}^3$ gives a real quadric surface of signature $(3,1)$, whose real points form a two-sphere $S^2$; the two-sphere is the boundary at infinity of the hyperbolic three-space carried by the timelike hyperboloid of $\mathbb{M}_-$, as in *Split-Biquaternions and Hyperbolic Geometry*. The neutral planes $\mathbb{D}e_\mu \oplus \mathbb{D}e_\nu$ have signature $(2,2)$, and their projective null quadrics contain real lines, the two rulings of the neutral case; the two signatures $(3,1)$ and $(2,2)$ are the two real forms of the same complex quadric, as recorded in *Split-Biquaternion Rotations and the Lorentz Group*.

**Theorem.** The projective null quadric of the Lorentzian slice $\mathbb{M}_-$ is a smooth real quadric surface in $\mathbb{P}^3$ whose real points form $S^2$ and which contains no real line; the projective null quadric of a neutral plane is a smooth real quadric surface whose real points form a torus $S^1\times S^1$ and which contains two families of real lines.

**Proof.** In coordinates the Lorentzian form is $q'^2_0 - \sum_k q_k^2$, whose projectivised real zero set is the image of the unit sphere $S^2$ of the spacelike three-space; a non-degenerate quadratic form on $\mathbb{R}^4$ of signature $(3,1)$ has no isotropic line, so no real line lies on its quadric. For signature $(2,2)$ the form is $a_1^2 + a_2^2 - a_3^2 - a_4^2$, whose real isotropic lines separate into the two families $a_1 = \pm a_3$-type and, after the standard change of coordinates, form two copies of $S^1$; the real points form $S^1\times S^1$.

## Summary

The split biquaternion algebra carries the split complex norm $N = \sum_\mu Q_\mu^2$ with polarisation the $\mathbb{D}$-valued dot product $B(\tilde P,\tilde{Q}) = \sum_\mu P_\mu Q_\mu$, orthonormal on the unit basis; these, with the real part $R$ of signature $(8,0)$, the imaginary part $I$ of signature $(4,4)$ and the Hermitian scalar form $g$ of signature $(4,4)$, are established in *Split-Biquaternion Norm and Invertibility*. The split-biquaternion norm is anisotropic, so its null cone is the origin; the non-invertible elements are instead those whose split-biquaternion norm is a zero divisor of $\mathbb{D}$, and they form the union $Z = \mathbb{H}\tilde\Pi_+ \cup \mathbb{H}\tilde\Pi_-$ of the two minimal left ideals, each a four-dimensional subspace, meeting only at the origin. These are exactly the elements of rank one, parametrised by a single quaternion as $\tilde{Q} = u \tilde\Pi_\pm$, the degenerate counterpart of the biquaternion outer product $uv^{T}$. The projective null quadric of the Hermitian form is a smooth six-dimensional quadric of Kleinian signature $(4,4)$ in $\mathbb{P}^7$, containing two families of maximal isotropic three-spaces, the ideals projecting to one member of each. The biquaternion Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ does not degenerate into another Segre structure but vanishes, and the projectivised zero divisor locus is the disjoint union $\mathbb{P}^3\sqcup\mathbb{P}^3$. On the Lorentzian four-plane $\mathbb{M}_-$ the two null cones agree, and their projectivised real points form $S^2$ and contain no real line; on a neutral plane the quadric is a torus containing two families of real lines. The projective geometry of the split biquaternion system is thus affine and incidence-theoretic on the Lorentzian slices and disjoint-linear on the zero divisor locus, in contrast to the Segre and spinor geometry of the biquaternion case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Split complex norm |
| $R(\tilde{Q}), I(\tilde{Q})$ | Real part (Euclidean, $(8,0)$) and imaginary part ($(4,4)$) of $N$ |
| $g(\tilde{Q}) = \sum_\mu(q_\mu^2 - q'^2_\mu)$ | Hermitian scalar form, signature $(4,4)$ |
| $Z = \mathbb{H}\tilde\Pi_+\cup\mathbb{H}\tilde\Pi_-$ | Zero divisor locus, union of two ideals |
| $Q_\mu, q_\mu, q'_\mu$ | Split complex coefficient and its two real parts |
| $Q(g) \subset \mathbb{P}^7$ | Projective null quadric of $g$, dimension $6$ |
| $\mathbb{P}^1(\mathbb{H}) \cong S^4$ | The projective line over the quaternion division algebra, the analogue of the biquaternion spinor line |
| $\mathbb{P}(Z) = \mathbb{P}^3\sqcup\mathbb{P}^3$ | Projectivised zero divisor locus |
| $\tilde{Q} = u\tilde\Pi_\pm$ | Rank-one (zero divisor) parametrisation |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces, signatures $(1,3)$ and $(3,1)$ |
| $Q^2 = \mathbb{P}^1\times\mathbb{P}^1$ | The biquaternion Segre quadric, absent here |

## Further Reading

- Igor R. Shafarevich, *Basic Algebraic Geometry 1*, 3rd edition (Springer, 2013), for quadrics, their rulings and the Segre embedding.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the null cones of the classical forms, their links and their rank-one descriptions.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for quadratic and Hermitian forms over a ring with zero divisors and the associated Clifford algebras.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for quadrics of signature $(p,q)$, their compact duals and the associated symmetric spaces.
