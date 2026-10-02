# __The Antipodal Map and the Adjoint__

## Introduction

The **antipodal map** $\alpha(x) = -x$ of the sphere is the free involution of *Borsuk's Theorem and the Antipodal Involution*, and it is also an operator on the cohomology of the sphere. The article computes the operator: on the top cohomology $H^{n}(S^{n})$ it is multiplication by the degree, $\deg\alpha = (-1)^{n+1}$, so that the antipodal map preserves the orientation of the sphere in odd dimensions and reverses it in even dimensions. The article then computes its **adjoint** with respect to the cup-product pairing, the archetypal pairing of the operator group. The adjoint turns out to be a scalar multiple of the operator itself, $\operatorname{Ad}(\alpha^{*}) = (-1)^{n+1}\alpha^{*}$, so that the antipodal operator is self-adjoint in odd dimensions and skew-adjoint in even dimensions; the computation is the model of the Hermitian pairings of *Hermitian Pairings on a Topological Space*, and the fixed part of the operator is computed at the same time, the invariant cohomology being the whole ring in the odd case and the degree-zero part alone in the even case.

The article continues *The Involution on the Cohomology Operators*, whose general involution it specialises to the antipodal map, and *Borsuk's Theorem and the Antipodal Involution*, whose degree it recomputes and whose rigidity it reinterprets. It prepares *Hermitian Pairings on a Topological Space*. It uses the cohomology ring and the cup product of *Cup and Cap Products*, the degree of a map of spheres from the homology of this Part, and the antipodal involution of the sphere. Nothing analytic and nothing geometric is used: the sphere is the set of unit vectors, the antipodal map is the restriction of the linear map $-I$, and the only geometry is the determinant of that linear map, read as the sign of the degree; no metric is chosen on the cohomology and no length or angle on the sphere.

## The Antipodal Map as an Operator

### The Involution of the Sphere

**Definition.** The **antipodal map** of the sphere $S^{n} = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ is $\alpha(x) = -x$. It is the restriction of the linear operator $-I$ of $\mathbb{R}^{n+1}$ to the sphere.

**Theorem.** The antipodal map is a homeomorphism of the sphere of order two, $\alpha^{2} = \mathrm{id}$, with no fixed point; it commutes with the group of rotations of the sphere, and the orbit space $S^{n}/\alpha$ is real projective space $\mathbb{RP}^{n}$. The map is the free involution whose orbit map is the universal two-fold covering $S^{n} \to \mathbb{RP}^{n}$.

**Proof.** The restriction of a linear homeomorphism to the sphere is a homeomorphism, $(-I)^{2} = I$ restricts to $\alpha^{2} = \mathrm{id}$, and $-x = x$ forces $x = 0$, which is not on the sphere; the orbit space is the projective space by the definition of the latter, and the covering statement is that of *The Orbit Space of a Free Involution*.

### The Induced Operator on Cohomology

**Definition.** The **antipodal operator** is the induced map

$$
\alpha^{*} : H^{*}(S^{n};R) \longrightarrow H^{*}(S^{n};R),
$$

the involution of the cohomology ring induced by the antipodal map, with coefficients in a commutative ring $R$.

**Theorem.** The cohomology of the sphere is $H^{0}(S^{n};R) = R$, $H^{n}(S^{n};R) = R$, and the intermediate groups are zero, so the antipodal operator is determined by its action on the two generators: it is the identity on $H^{0}(S^{n};R)$, because $S^{n}$ is connected, and it is the multiplication by an element $c \in R$ on $H^{n}(S^{n};R)$, which is the degree of the antipodal map,

$$
\alpha^{*}(u_{n}) = \deg(\alpha)\, u_{n}, \qquad \alpha^{*}(u_{0}) = u_{0},
$$

where $u_{n}$ is a chosen generator of $H^{n}(S^{n};R)$ and $u_{0}$ the unit.

**Proof.** The cohomology of the sphere is the standard computation of the homology and cohomology of a sphere in *Simplicial and Singular Homology* and *Cohomology and the Universal Coefficient Theorem*; the degree of a self-map of the sphere is by definition the integer by which it acts on the top cohomology, and it acts as the identity on $H^{0}$ because a map of a connected space to itself induces the identity on the degree-zero cohomology.

## The Degree

### The Degree of the Antipodal Map

**Theorem.** For $n \geq 1$ the degree of the antipodal map of $S^{n}$ is

$$
\deg(\alpha) = (-1)^{n+1} .
$$

**Proof.** The degree is multiplicative, $\deg(f \circ g) = \deg(f)\deg(g)$, for self-maps of the sphere, and the degree of a reflection is $-1$. The linear operator $-I$ of $\mathbb{R}^{n+1}$ is the composite of the $n+1$ reflections $\rho_{i}$ that change the sign of the $i$-th coordinate, and each $\rho_{i}$ restricts to a reflection of the sphere, a homeomorphism that fixes the equator of the $i$-th coordinate and exchanges the two hemispheres, of degree $-1$. Hence the antipodal map, the restriction of $-I = \rho_{1}\circ\cdots\circ\rho_{n+1}$, has degree $(-1)^{n+1}$.

**Corollary.** The antipodal map preserves the orientation of the sphere in the odd dimensions and reverses it in the even dimensions; on the top cohomology it is multiplication by $(-1)^{n+1}$, and the induced map on the fundamental class is

$$
\alpha_{*}[S^{n}] = (-1)^{n+1}[S^{n}] .
$$

**Proof.** The orientation of the sphere is a choice of generator of the top homology, and the degree is the multiplier by which a self-map acts on that generator; the sign is the theorem.

### Two Computations of the Sign

**Remark.** The sign has two independent computations, and the article records both. The first is the product of the reflections above, which uses the multiplicativity of the degree and the degree of a single reflection; the second is the determinant of the linear operator, $\det(-I) = (-1)^{n+1}$, which the degree of the restriction of a linear isomorphism to the sphere reproduces, because the orientation of the sphere is carried by the volume form that the linear operator scales by the determinant. The two agree, and the agreement is the reason the sign can be read off the linear algebra of $\mathbb{R}^{n+1}$ without a separate computation on the sphere.

**Example.** For $n = 1$ the antipodal map is the rotation by $\pi$, of degree $1 = (-1)^{2}$, and it is homotopic to the identity on the circle; it is then invisible on the cohomology, in accordance with the general statement that the involution is orientation-preserving in the odd dimensions. For $n = 2$ the antipodal map is the orientation-reversing involution of the two-sphere, of degree $-1 = (-1)^{3}$. The case $n = 0$ is exceptional: $S^{0}$ is disconnected, the antipodal map interchanges the two points, and it acts on $H^{0}(S^{0};R) = R \oplus R$ by the exchange of the two summands, not by the multiplication by a scalar, so the degree is defined for $n \geq 1$.

## The Pairing and the Adjoint

### The Cup-Product Pairing

**Definition.** The **cup-product pairing** on the cohomology of the sphere, with coefficients in a commutative ring $R$, is

$$
b : H^{*}(S^{n};R) \times H^{*}(S^{n};R) \longrightarrow R, \qquad b(u,v) = \langle u \cup v, [S^{n}]\rangle,
$$

the evaluation of the cup product on the fundamental class; it is nondegenerate in the sense of Poincaré duality, and it vanishes unless the degrees of $u$ and $v$ sum to $n$. On the middle group $H^{n}(S^{n};R)$ it is the symmetric form $b(u,v) = u_{n}$-coefficient of $u \cup v$, and it is $\varepsilon$-symmetric with the graded sign $\varepsilon = (-1)^{n}$: symmetric in the even dimensions and alternating in the odd dimensions.

**Proof.** The cup product is graded-commutative, $u \cup v = (-1)^{|u||v|}v \cup u$, so the pairing is symmetric when both degrees are even and alternating when both are odd; the only nonzero case for the sphere has $|u| = |v| = n$ in the middle, giving the stated sign. The nondegeneracy is Poincaré duality of the sphere, *Poincaré Duality*.

### The Adjoint of the Antipodal Operator

**Theorem.** The antipodal operator scales the cup-product pairing by its degree:

$$
b(\alpha^{*}u, \alpha^{*}v) = (-1)^{n+1}\, b(u,v) \qquad (u, v \in H^{*}(S^{n};R)).
$$

Consequently the adjoint of the antipodal operator with respect to the pairing is the same operator multiplied by that scalar,

$$
\operatorname{Ad}(\alpha^{*}) = (-1)^{n+1}\,\alpha^{*},
$$

so that the antipodal operator is **self-adjoint** in the odd dimensions and **skew-adjoint** in the even dimensions; in both cases it satisfies $\operatorname{Ad}(\alpha^{*}) = \pm\alpha^{*}$ and it is an involution up to the sign of the degree. The pairing is invariant under the antipodal operator exactly in the odd dimensions and anti-invariant in the even dimensions.

**Proof.** The antipodal operator is a ring homomorphism, so $\alpha^{*}(u\cup v) = \alpha^{*}u \cup \alpha^{*}v$; naturality of the evaluation gives

$$
b(\alpha^{*}u,\alpha^{*}v) = \langle \alpha^{*}(u\cup v),[S^{n}]\rangle = \langle u\cup v, \alpha_{*}[S^{n}]\rangle = (-1)^{n+1}b(u,v),
$$

using $\alpha_{*}[S^{n}] = (-1)^{n+1}[S^{n}]$ of the corollary. For the adjoint, the defining relation of the adjoint operator and the fact that $\alpha^{*}$ is an involution give

$$
b(\alpha^{*}u, v) = (-1)^{n+1}b(u,\alpha^{*}v),
$$

because $v = \alpha^{*}\alpha^{*}v$ and the isometry-up-to-sign relation applies to the pair $(u,\alpha^{*}v)$; hence $\operatorname{Ad}(\alpha^{*}) = (-1)^{n+1}\alpha^{*}$. The self-adjoint and the skew-adjoint statements are the two cases of the sign, and the invariance and anti-invariance are the two cases of the displayed scaling.

**Corollary.** The pairing defined by the antipodal operator through the adjoint is the scaled pairing $b_{\alpha}(u,v) = b(\alpha^{*}u,v) = (-1)^{n+1}b(u,\alpha^{*}v)$; it is symmetric in the even dimensions and skew-symmetric in the odd dimensions, and it is nondegenerate exactly when the cup-product pairing is, since $\alpha^{*}$ is an invertible operator.

**Proof.** The displayed identity is the definition of $b_{\alpha}$ read through the adjoint. For the symmetry, the defining relation of the adjoint and the graded symmetry of $b$ give $b_{\alpha}(u,v) = (-1)^{n+1}b(u,\alpha^{*}v) = (-1)^{n+1}\cdot(-1)^{n}b(\alpha^{*}v,u) = (-1)^{n}b_{\alpha}(v,u)$, since $\alpha^{*}$ is an involution and $b(\alpha^{*}v,u) = b_{\alpha}(v,u)$; hence the symmetry sign of $b_{\alpha}$ is $(-1)^{n}$, as stated. Nondegeneracy is preserved by the invertible operator $\alpha^{*}$.

## The Fixed Part of the Antipodal Operator

**Theorem.** The fixed part of the antipodal operator on the cohomology of the sphere is

$$
H^{*}(S^{n};R)^{\alpha^{*}} = \begin{cases} H^{0}(S^{n};R) \oplus H^{n}(S^{n};R), & n \text{ odd}, \\ H^{0}(S^{n};R), & n \text{ even}, \end{cases}
$$

and the anti-invariant part is the complementary summand when two is invertible: the whole of $H^{n}$ in the even case and zero in the odd case. In the even dimensions the invariant cohomology is only the degree-zero part, and in the odd dimensions it is the whole ring.

**Proof.** The cohomology of the sphere is concentrated in degrees $0$ and $n$, the operator is the identity in degree zero, and in degree $n$ it is the multiplication by $(-1)^{n+1}$; the fixed elements of the multiplication by a scalar $c$ on the rank-one module $R$ are the elements annihilated by $c-1$, which is the whole module when $c = 1$ and is zero when $c - 1$ is not a zero-divisor, in particular for $c = -1$. The two cases are therefore as stated, and the anti-invariant part is the other eigenspace.

**Corollary.** For odd $n$ the antipodal operator is the identity on the cohomology, the involution is cohomologically invisible, and the induced involution on the cohomology ring of the projective space is the identity; for even $n$ the invariant cohomology is the degree-zero part and the top class is anti-invariant. The contrast with the quotient $\mathbb{RP}^{n}$, whose mod-two cohomology is larger, shows that the invariant cohomology of the free action forgets the quotient in the odd case and retains only the bottom in the even case; the forgetfulness is the cohomological shadow of the orientation reversal.

**Proof.** The first clauses are the theorem; the comparison with the projective space uses the mod-two cohomology $H^{*}(\mathbb{RP}^{n};\mathbb{Z}/2) = \mathbb{Z}/2[\omega]/(\omega^{n+1})$ of *Borsuk's Theorem and the Antipodal Involution*, which is not the fixed part in either case, so that the fixed part of the involution on the sphere is a coarser invariant than the quotient.

## Summary

The antipodal map is a free involution of the sphere, the orbit map is the universal two-fold covering of the projective space, and the induced operator on the cohomology is the identity in degree zero and the multiplication by the degree in the top degree. The degree is $(-1)^{n+1}$: it is computed as the product of the degrees of the $n+1$ reflections whose composite is $-I$, and equally as the determinant of the linear operator, and the two agree. With respect to the cup-product pairing of Poincaré duality the antipodal operator scales the pairing by its degree, and its adjoint is therefore the same operator multiplied by the degree; the antipodal operator is self-adjoint in odd dimensions and skew-adjoint in even dimensions, and the pairing it defines through the adjoint is symmetric in the odd dimensions and skew-symmetric in the even dimensions. Its fixed part on the cohomology of the sphere is the whole ring in the odd dimensions and the degree-zero part in the even dimensions, with the complementary top class anti-invariant when two is invertible; the fixed part is coarser than the cohomology of the quotient, and the article that follows develops the pairings of which this computation is the model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(x) = -x$ | The antipodal map of $S^{n}$; the restriction of $-I$ |
| $S^{n}/\alpha = \mathbb{RP}^{n}$ | The orbit space; the universal two-fold covering quotient |
| $\alpha^{*}$ | The antipodal operator on $H^{*}(S^{n};R)$ |
| $\deg(\alpha) = (-1)^{n+1}$ | The degree of the antipodal map |
| $\alpha_{*}[S^{n}] = (-1)^{n+1}[S^{n}]$ | The action on the fundamental class |
| $b(u,v) = \langle u\cup v,[S^{n}]\rangle$ | The cup-product (intersection) pairing |
| $\varepsilon = (-1)^{n}$ | The symmetry sign of the middle pairing |
| $b(\alpha^{*}u,\alpha^{*}v) = (-1)^{n+1}b(u,v)$ | The scaling of the pairing by the degree |
| $\operatorname{Ad}(\alpha^{*}) = (-1)^{n+1}\alpha^{*}$ | The adjoint of the antipodal operator |
| self-adjoint / skew-adjoint | Odd dimensions / even dimensions |
| $b_{\alpha}(u,v) = b(\alpha^{*}u,v)$ | The pairing defined by the antipodal operator |
| $H^{*}(S^{n})^{\alpha^{*}}$ | Invariant cohomology: whole ring if $n$ odd, degree zero if $n$ even |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the degree of a self-map of a sphere, the cohomology of the sphere and the cup-product pairing.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the degree, the multiplicativity of the degree and the action on the fundamental class.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the antipodal map, its degree and the orientation of the sphere.
- Jean Dieudonné, *A History of Algebraic and Differential Topology 1900–1960* (Birkhäuser, 1989), for the origins of the degree and the antipodal map.
- William S. Massey, *A Basic Course in Algebraic Topology* (Springer, 1991), for Poincaré duality, the intersection pairing and the adjoint of a map with respect to it.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators III", *Annals of Mathematics* 87 (1968), 546–604, for the equivariant refinement of the signature and the pairing, which the later articles name.
