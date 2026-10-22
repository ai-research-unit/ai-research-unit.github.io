# __Reduced Biquaternion Lie Group and Exponential Structure__

## Introduction

The reduced biquaternion algebra is a real associative algebra of dimension four, and as such it carries a Lie algebra structure under the commutator, an exponential map into its group of units, and the Lie-group structures attached to the two. This article records the Lie algebra, the exponential with its closed form and its kernel, the group of units, the norm-one group and the maximal compact subgroup, the elliptic and hyperbolic one-parameter subgroups, the polar and exponential parametrisation of an element, and the comparison with the biquaternion and split biquaternion cases. The treatment is purely mathematical; no physical interpretation is used.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The squared Euclidean norm is $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})$, and the algebra norm is $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$. The elementary functions and their closed forms are used from *Reduced Biquaternion Elementary Functions*.

## The Algebra as a Lie Algebra

**Definition.** The **commutator bracket** on $\mathbb{B}_{\mathrm{r}}$ is $[\breve Q_{1},\breve Q_{2}]=\breve Q_{1}\breve Q_{2}-\breve Q_{2}\breve Q_{1}$.

**Theorem (the bracket is zero).** The algebra is **commutative**, so
$$
[\breve Q_{1},\breve Q_{2}]=0\qquad\text{for all }\breve Q_{1},\breve Q_{2}\in\mathbb{B}_{\mathrm{r}}:
$$
the bracket is identically zero and $\mathbb{B}_{\mathrm{r}}$ is an **abelian** real Lie algebra of dimension four. Its centre is the whole algebra, its derived algebra is $\{0\}$, and it is the Lie algebra of its own group of units.

*Proof.* The multiplication is commutative, so $\breve Q_{1}\breve Q_{2}=\breve Q_{2}\breve Q_{1}$; an abelian Lie algebra has all brackets zero, its centre is the whole space and its derived algebra vanishes; and the Lie algebra of a Lie group is its tangent space at the identity with the commutator of the associative product, which here is the algebra itself.

**Corollary (the contrast with the halves).** The split biquaternion algebra is the reductive Lie algebra $\mathbb{R}^{2}\oplus\mathrm{SO}(4)$, with a six-dimensional derived algebra and a two-dimensional centre, and the biquaternion algebra is a real form of $\mathfrak{gl}_{2}(\mathbb{C})$, non-abelian; the reduced biquaternion algebra is the abelian extreme of the family, every point of the algebra being central.

*Proof.* The split biquaternion and biquaternion computations are those of *Split-Biquaternion Exponential and Lie Group Structure* and of the biquaternion counterpart; here the vanishing of the bracket reduces everything to the abelian case.

## The Exponential

**Definition.** For $\breve Q\in\mathbb{B}_{\mathrm{r}}$ the **exponential** is $\exp \breve Q=\sum_{n\ge0}\breve Q^{n}/n!$.

**Theorem (the closed form and the group law).** The exponential is the Lie-group exponential of the abelian Lie algebra, it is
$$
\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=e^{Q_{\blacktriangle}}\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr),
$$
and it satisfies $\exp(\breve Q_{1}+\breve Q_{2})=\exp \breve Q_{1}\exp \breve Q_{2}$ for **all** $\breve Q_{1},\breve Q_{2}$, with $\exp 0=1$. The differential of $\exp$ at the origin is the identity, so $\exp$ is a local diffeomorphism near $0$.

*Proof.* The closed form and the group law are those of *Reduced Biquaternion Elementary Functions*; the differential at the origin is the identity because the first-order term of the series is $\breve Q$, and the inverse function theorem applies.

**Theorem (the kernel and surjectivity).** The exponential is surjective onto the unit group and its kernel is the lattice
$$
\ker\exp=2\pi i\bigl(\mathbb{Z}\,\Pi_++\mathbb{Z}\,\Pi_-\bigr),
$$
isomorphic to $\mathbb{Z}^{2}$; consequently $\exp$ is a covering map $\mathbb{B}_{\mathrm{r}}\to\mathbb{B}_{\mathrm{r}}^{\times}$, and it is the universal covering, the algebra being simply connected.

*Proof.* An element $\breve Q$ with coordinates $Q_{+},Q_{-}$ has $\exp \breve Q=1$ exactly when $e^{Q_{+}}=e^{Q_{-}}=1$, that is $Q_{+},Q_{-}\in2\pi i\mathbb{Z}$; a unit has $Q_{+},Q_{-}\neq0$ and choosing $S$ with coordinates $\log Q_{+},\log Q_{-}$ gives $\exp S=\breve Q$, so $\exp$ is onto the units. The kernel is discrete of rank two, so the map is a covering; the algebra is $\mathbb{R}^{4}$, simply connected, so it is the universal cover.

## The Group of Units

**Theorem (the structure of the unit group).** The group of units is
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
abelian, of real dimension four, connected but not simply connected, with fundamental group $\mathbb{Z}^{2}$. As a Lie group it is the product of the two complex multiplicative groups, and it is isomorphic to $\mathbb{R}^{2}\times T^{2}$ with $T^{2}=S^{1}\times S^{1}$ the two-torus.

*Proof.* The units are the elements with $Q_{+}\neq0$ and $Q_{-}\neq0$ by the unit criterion, and the multiplication is componentwise, so the group is the product of the two copies of $\mathbb{C}^{\times}$; each $\mathbb{C}^{\times}$ is diffeomorphic to $S^{1}\times\mathbb{R}$ and connected, with fundamental group $\mathbb{Z}$; the product inherits the connectedness and has fundamental group $\mathbb{Z}^{2}$.

**Corollary (the exponential is the universal cover).** Since the algebra is the universal cover of the unit group, the exponential is the covering homomorphism and the unit group is the quotient of the algebra by the lattice $2\pi i(\mathbb{Z}\Pi_++\mathbb{Z}\Pi_-)$.

*Proof.* The exponential is the local diffeomorphism of the preceding section and its kernel is the stated lattice, so it exhibits the algebra as a covering of the unit group, and the covering is universal by the simple connectedness of the algebra.

## The Norm-One Group

**Definition.** The **norm-one group** is $\{\breve Q\in\mathbb{B}_{\mathrm{r}}^{\times}:\langle \breve Q\rangle_{\mathrm{ts}}=1\}$, and the **maximal compact subgroup** is $T^{2}=\{\breve Q\in\mathbb{B}_{\mathrm{r}}^{\times}:\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}$.

**Theorem (the norm-one group).** The norm-one group is
$$
\{\breve Q:Q_{+}Q_{-}=1\}=\{(Q_{+},Q_{+}^{-1}):Q_{+}\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$
of real dimension two and **non-compact**; the maximal compact subgroup is
$$
T^{2}=\{\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}\cong S^{1}\times S^{1},
$$
compact of dimension two, and it is the group of units lying in the Euclidean unit sphere $S^{3}=\{K=1\}$.

*Proof.* The condition $Q_{+}Q_{-}=1$ determines $Q_{-}=Q_{+}^{-1}$ from $Q_{+}$, giving a copy of $\mathbb{C}^{\times}$, which is non-compact of real dimension two; the conditions $\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1$ give the product of the two unit circles, compact of dimension two, and they imply $K=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})=1$, so $T^{2}\subset S^{3}$.

**Corollary (the norm-one group is not compact, against the quaternion cases).** For the split biquaternion algebra the norm-one group is the compact $S^{3}\times S^{3}\cong\mathrm{Spin}(4)$; for the reduced biquaternion algebra the algebra norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ is **complex**-valued, so the condition $\langle \breve Q\rangle_{\mathrm{ts}}=1$ fixes only the product of the two coordinates and leaves their common modulus free, and the norm-one group is non-compact. The compact group of the reduced case is instead the maximal compact subgroup $T^{2}$, the Clifford torus inside $S^{3}$.

*Proof.* In the split biquaternion case the norm is valued in the split complex algebra and $N=e_t$ forces both quaternion halves to have unit quaternion norm, hence to lie in $S^{3}$; here the complex norm leaves the modulus of $Q_{+}$ free, and the maximum compact subgroup of $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ is the product of the two unit circles.

## The Elliptic and Hyperbolic Subgroups

**Definition.** A one-parameter subgroup $\exp(tX)$, $t\in\mathbb{R}$, is **elliptic** when it has compact closure and **hyperbolic** when it is unbounded.

**Theorem (the classification).** The subgroup $\exp(tX)$ has compact closure if and only if $\operatorname{Re}Q_{X+}=\operatorname{Re}Q_{X-}=0$, that is if and only if $X$ lies in the real span of the two definite directions $i$ and $ij$; it is then contained in $T^{2}$. It is hyperbolic if and only if $\operatorname{Re}Q_{X+}\neq0$ or $\operatorname{Re}Q_{X-}\neq0$, and the hyperbolic directions include the scalar line $\mathbb{R}$ and the split line $\mathbb{R}j$.

*Proof.* $\exp(tX)$ has coordinates $e^{tQ_{X+}},e^{tQ_{X-}}$, which are bounded for all real $t$ exactly when both $Q_{X+}$ and $Q_{X-}$ are purely imaginary; the coordinates $Q_{X+}=Q_{X\blacktriangle}+Q_{X\blacktriangledown}$ and $Q_{X-}=Q_{X\blacktriangle}-Q_{X\blacktriangledown}$ are simultaneously purely imaginary exactly when $Q_{X\blacktriangle}$ and $Q_{X\blacktriangledown}$ are, that is when $X\in\mathbb{R}i\oplus\mathbb{R}ij$; the two subspaces $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ are the real and the purely imaginary $Q_{\blacktriangle}$-and-$Q_{\blacktriangledown}$ parts, and the complement condition gives the hyperbolic case.

**Corollary (the model subgroups and the maximal torus).** The **elliptic circle** $\exp(i\theta)=\cos\theta+i\sin\theta$ is the compact subgroup in the plane $\mathbb{R}\{1,i\}$, and the **hyperbolic subgroup** $\exp(j\phi)=\cosh\phi+j\sinh\phi$ is the non-compact subgroup in the plane $\mathbb{R}\{1,j\}$. The full elliptic subgroup is generated by the whole two-plane $\mathbb{R}\{i,ij\}$ of definite directions: for $X=i\alpha+ij\beta$ the coordinates are $Q_{X+}=i(\alpha+\beta)$ and $Q_{X-}=i(\alpha-\beta)$, so $\exp(tX)$ sweeps the whole two-torus $T^{2}$ as $\alpha,\beta$ vary. The hyperbolic directions are those with a non-zero component in the complementary two-plane $\mathbb{R}\{1,j\}$, the component in $\mathbb{R}\{i,ij\}$ contributing only an elliptic factor, and the unit group is the product of the two-torus and the two real directions,
$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong T^{2}\times\mathbb{R}^{2},
$$
the maximal compact subgroup being the maximal torus $T^{2}$.

*Proof.* The two closed forms are those of the elementary functions; the coordinates of $X=i\alpha+ij\beta$ are computed from $Q_{X\blacktriangle}=i\alpha$ and $Q_{X\blacktriangledown}=i\beta$; the exponential of the two-plane gives the product of the two unit circles, on which the elliptic subgroups are dense; the group is commutative, so the elliptic and hyperbolic subgroups commute, and their product with the two positive scales is the whole unit group, whose maximal compact subgroup is the product of the two circles.

## Polar and Exponential Parametrisation

**Theorem (the polar form).** Every element has a polar form
$$
\breve Q=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-,\qquad \rho_{1}=\lvert Q_{+}\rvert,\ \rho_{2}=\lvert Q_{-}\rvert\ge0,\ \theta_{1},\theta_{2}\in(-\pi,\pi],
$$
unique under the phase-range convention, and it is a unit exactly when $\rho_{1}\rho_{2}>0$. Every **unit** has the exponential parametrisation $\breve Q=\exp S$ with $S=\log Q_{+}\,\Pi_++\log Q_{-}\,\Pi_-$.

*Proof.* The polar form is that of *Modulus–Unit Polar Decomposition of Reduced Biquaternions*, the scales being the moduli of the two coordinates and the phases their arguments; the exponential parametrisation of a unit is the surjectivity statement above.

**Corollary (the parametrisation of the unit group).** The unit group is parametrised by two positive scales and two phases, $\mathbb{B}_{\mathrm{r}}^{\times}\cong(\mathbb{R}_{>0})^{2}\times(S^{1})^{2}$, and the exponential realises the covering $\mathbb{R}^{4}=(\mathbb{R}\times\mathbb{R})\times(\mathbb{R}\times\mathbb{R})\to$ the unit group, the source being the two log-scales and the two lifted phases.

*Proof.* Each coordinate is $Q_{+}=\rho_{1}e^{i\theta_{1}}$ with $\rho_{1}>0$, and the product of the two complex multiplicative groups is the displayed product; the exponential replaces each $\rho_{1}>0$ by the real parameter $\log\rho_{1}$.

## Comparison with the Biquaternion and Split-Biquaternion Cases

The biquaternion algebra is simple, its Lie algebra is a real form of $\mathfrak{gl}_{2}(\mathbb{C})$, non-abelian, and its unit group is essentially $\mathrm{GL}_{2}(\mathbb{C})$. The split biquaternion algebra is the reductive Lie algebra $\mathbb{R}^{2}\oplus\mathrm{SO}(4)$, with unit group $\mathbb{R}_{>0}^{2}\times S^{3}\times S^{3}$, connected and simply connected, of dimension eight, and norm-one group the compact $S^{3}\times S^{3}\cong\mathrm{Spin}(4)$. The reduced biquaternion algebra is the abelian case: the Lie algebra has zero bracket and dimension four, the unit group is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}\cong\mathbb{R}^{2}\times T^{2}$, abelian and **not** simply connected, and the exponential is the universal covering map with kernel $\mathbb{Z}^{2}$. The norm-one group, compact in the split biquaternion case, is non-compact here because the norm is complex-valued; the compact group that replaces it is the Clifford torus $T^{2}$. The elliptic and hyperbolic one-parameter subgroups are the pair generated by the definite directions $\mathbb{R}\{i,ij\}$ and the indefinite directions $\mathbb{R}\{1,j\}$, exactly as the two complex structures of the algebra suggest.

## Summary

The reduced biquaternion algebra is an abelian real Lie algebra of dimension four under the commutator, its bracket being identically zero because the multiplication is commutative; its centre is the whole algebra and its derived algebra vanishes. The exponential is $\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-=e^{Q_{\blacktriangle}}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$, satisfies the group law for all arguments, and is a covering map onto the unit group with kernel the lattice $2\pi i(\mathbb{Z}\Pi_++\mathbb{Z}\Pi_-)$; it is the universal covering, the algebra being simply connected. The unit group is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, abelian, connected, of dimension four and fundamental group $\mathbb{Z}^{2}$, isomorphic to $\mathbb{R}^{2}\times T^{2}$. The norm-one group $\{\langle \breve Q\rangle_{\mathrm{ts}}=1\}\cong\mathbb{C}^{\times}$ is non-compact of dimension two, because the algebra norm is complex-valued, and the maximal compact subgroup is the Clifford torus $T^{2}=\{\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}$ of the Euclidean unit sphere $S^{3}$. The elliptic one-parameter subgroups are generated by the definite directions $\mathbb{R}\{i,ij\}$ and the hyperbolic ones by the indefinite directions $\mathbb{R}\{1,j\}$, with the model subgroups $\exp(i\theta)$ and $\exp(j\phi)$. Every element has the polar form $\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-$ and every unit the exponential parametrisation. Against the non-abelian biquaternion case and the reductive split biquaternion case, the reduced case is the abelian extreme, its unit group toroidal and its compact group the two-torus rather than the product of the two three-spheres.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[\breve Q_{1},\breve Q_{2}]=\breve Q_{1}\breve Q_{2}-\breve Q_{2}\breve Q_{1}=0$ | Commutator bracket, identically zero |
| $\mathbb{B}_{\mathrm{r}}$ | Abelian Lie algebra of dimension four |
| $\exp \breve Q=e^{Q_{+}}\Pi_++e^{Q_{-}}\Pi_-$ | Exponential |
| $\ker\exp=2\pi i(\mathbb{Z}\Pi_++\mathbb{Z}\Pi_-)$ | Kernel of the exponential |
| $\mathbb{B}_{\mathrm{r}}^{\times}=\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | Group of units |
| $\{\breve Q:\langle \breve Q\rangle_{\mathrm{ts}}=1\}\cong\mathbb{C}^{\times}$ | Norm-one group |
| $T^{2}=\{\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}$ | Maximal compact subgroup |
| $\exp(i\theta)=\cos\theta+i\sin\theta$ | Elliptic subgroup |
| $\exp(j\phi)=\cosh\phi+j\sinh\phi$ | Hyperbolic subgroup |
| $\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-$ | Polar form |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the Lie-group exponential, the covering structure and the one-parameter subgroups.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Benjamin, 1965), for the abelian case and the correspondence between the algebra and the group.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential, the polar form and the units of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent description of the units and the exponential of the commutative algebra.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the structure of abelian Lie groups and their compact subgroups.
