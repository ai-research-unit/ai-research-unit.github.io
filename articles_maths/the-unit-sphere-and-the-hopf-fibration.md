# __The Unit Sphere and the Hopf Fibration__

## Introduction

This article treats the unit sphere $S^3\subset\mathbb{C}^2$ and the map
$$
h:S^3\longrightarrow\mathbb{CP}^1,\qquad h(z_1,z_2)=[z_1:z_2],
$$
the **Hopf map**. The map is a fibre bundle with fibre the circle $S^1$, its base is the two-sphere, its total space is the three-sphere, and its class generates $\pi_3(S^2)\cong\mathbb{Z}$. The article computes the bundle, the exact sequence of homotopy groups, the linking number of two fibres, and the identification $S^3\cong\mathrm{SU}(2)$.

The article is the third of the topological articles of the category. The topology of $\mathbb{C}^2$ is *The Topology of $\mathbb{C}^2$*; the compactifications, and the role of the Hopf map as the attaching map of the projective compactification, are *The Compactifications of $\mathbb{C}^2$*; the homotopy groups and the general Hopf fibrations are *Homotopy Groups and Fibrations*; the linking number is *Knot Theory*; and the quaternionic model of the sphere is *Quaternion Topology* and *Introduction to Topology on the Quaternions*. None of these is restated here.

**The Hopf map is the simplest nontrivial circle bundle whose total space is a sphere.** It is locally a product $S^2\times S^1$, globally not, and its nontriviality is measured by the first Chern class and by the Hopf invariant. The fibres are circles, any two of them are linked once, and the total space is the Lie group $\mathrm{SU}(2)$.

## The Unit Sphere

**The unit sphere $S^3$ is a compact, connected, simply connected three-dimensional manifold and a Lie group; it is the total space of the Hopf bundle.**

**Definition.** The **unit sphere** is
$$
S^3=\{z=(z_1,z_2)\in\mathbb{C}^2:\lVert z\rVert=1\}.
$$

**Proposition (the manifold and its invariants).** The sphere $S^3$ is a compact, connected, simply connected smooth manifold of dimension $3$, with
$$
H_0(S^3;\mathbb{Z})=H_3(S^3;\mathbb{Z})=\mathbb{Z},\qquad H_1=H_2=0,
$$
and
$$
\pi_1(S^3)=\pi_2(S^3)=0,\qquad \pi_3(S^3)=\mathbb{Z}.
$$

*Proof.* The sphere is closed and bounded in $\mathbb{C}^2\cong\mathbb{R}^4$, hence compact; it is connected for dimension at least $1$ and simply connected for dimension at least $2$ (*The Fundamental Group and Covering Spaces*); its homology is computed by the cell decomposition $S^3=e^0\cup e^3$ (*Simplicial and Singular Homology*); and the Hurewicz theorem gives $\pi_3(S^3)\cong H_3(S^3)=\mathbb{Z}$ because the sphere is simply connected (*Homotopy Groups and Fibrations*).

**Proposition (the unitary action).** The unitary group $\mathrm{U}(2)$ acts transitively on $S^3$ by $A\cdot z=Az$, and the stabilizer of $e_1=(1,0)$ is the diagonal circle
$$
\left\{\begin{pmatrix}1&0\\0&\lambda\end{pmatrix}:\lvert\lambda\rvert=1\right\}\cong\mathrm{U}(1).
$$
Hence $S^3\cong\mathrm{U}(2)/\mathrm{U}(1)$ as a homogeneous space. The special unitary group $\mathrm{SU}(2)$ acts transitively and freely, and $S^3\cong\mathrm{SU}(2)$ as a manifold.

*Proof.* Every unit vector is the first column of a unitary matrix, so the action is transitive. A unitary matrix fixing $e_1$ has first column $e_1$ and is diagonal with a unit entry in the second place. The special unitary group acts transitively because it contains the unitary matrices of determinant $1$ that send $e_1$ to any unit vector; the stabilizer is trivial because a special unitary matrix with first column $e_1$ is the identity.

**Remark (the sphere as a Lie group).** The identification $S^3\cong\mathrm{SU}(2)$ is proved in the last section; it makes the sphere a compact Lie group, hence parallelizable. **The group structure is not visible from the inclusion $S^3\subset\mathbb{C}^2$ alone**, but it is the structure that the Hopf map exploits.

The invariants are collected below.

| Invariant | Value |
|---|---|
| real dimension | $3$ |
| compact | yes |
| connected | yes |
| simply connected | yes |
| $H_0,H_3$ | $\mathbb{Z}$ |
| $H_1,H_2$ | $0$ |
| $\pi_1,\pi_2$ | $0$ |
| $\pi_3$ | $\mathbb{Z}$ |

## The Hopf Map

**The Hopf map sends a unit vector of $\mathbb{C}^2$ to the complex line it spans; its fibres are circles, and the map is a smooth surjection onto the two-sphere.**

**Definition.** The **Hopf map** is
$$
h:S^3\longrightarrow\mathbb{CP}^1,\qquad h(z_1,z_2)=[z_1:z_2].
$$

The map is well defined because $(z_1,z_2)\neq(0,0)$ on $S^3$, and it is smooth because it is the restriction of the smooth quotient map $\mathbb{C}^2\setminus\{0\}\to\mathbb{CP}^1$. The base is homeomorphic to $S^2$ by *The Subspaces of $\mathbb{C}^2$*, and the identification is written
$$
\mathbb{CP}^1\longrightarrow S^2,\qquad [w_1:w_2]\longmapsto\frac{w_1}{w_2}\in\mathbb{C}\cup\{\infty\},
$$
with the value $\infty$ at $[1:0]$.

**Proposition (the fibres).** For a unit vector $w=(w_1,w_2)\in S^3$, the fibre over $[w_1:w_2]$ is
$$
h^{-1}([w_1:w_2])=\{\lambda w:\lambda\in\mathbb{C},\ \lvert\lambda\rvert=1\}\cong S^1.
$$
The fibres are the orbits of the action of $\mathrm{U}(1)$ on $S^3$ by scalar multiplication, and two fibres are either equal or disjoint.

*Proof.* If $h(z)=[w]$, then $z=\lambda w$ for some $\lambda\in\mathbb{C}^{\times}$; the condition $\lVert z\rVert=\lVert w\rVert=1$ gives $\lvert\lambda\rvert=1$. Conversely, every $\lambda w$ with $\lvert\lambda\rvert=1$ lies in $S^3$ and has the same class as $w$. The action is free: $\lambda w=w$ with $w\neq0$ forces $\lambda=1$.

**Corollary (the quotient).** The map $h$ is the quotient map of the free action of $\mathrm{U}(1)$ on $S^3$, and
$$
S^3/\mathrm{U}(1)\cong\mathbb{CP}^1\cong S^2.
$$

*Proof.* The fibres are exactly the orbits, and a continuous surjection with compact fibres from a compact Hausdorff space to a Hausdorff space is a quotient map.

**Proposition (the standard fibres).** The fibre over $[1:0]$ is
$$
C_1=\{(e^{i\theta},0):\theta\in\mathbb{R}\},
$$
the fibre over $[0:1]$ is
$$
C_2=\{(0,e^{i\theta}):\theta\in\mathbb{R}\},
$$
and these two circles lie in perpendicular complex coordinate planes of $\mathbb{C}^2$.

*Proof.* The fibre over $[1:0]$ consists of the unit multiples of $(1,0)$, and the fibre over $[0:1]$ of the unit multiples of $(0,1)$.

**Remark (the map is a submersion).** The differential of $h$ has rank $2$ at every point of $S^3$: the kernel is the tangent line of the fibre, and the quotient is the two-dimensional tangent space of $S^2$. **The map is therefore a submersion, and every fibre is a smoothly embedded circle.** The local product structure is made explicit in the next section.

## The Bundle

**The Hopf map is a locally trivial fibre bundle with fibre $S^1$ and structure group $\mathrm{U}(1)$; it is the unit sphere bundle of the tautological line bundle over $\mathbb{CP}^1$, and it is not trivial.**

**Theorem (local trivializations).** Over the two standard charts
$$
U_2=\{[w_1:w_2]:w_2\neq0\},\qquad U_1=\{[w_1:w_2]:w_1\neq0\},
$$
the map $h$ is trivial. On $U_2$, with $t=w_1/w_2$, the map
$$
\varphi_2:h^{-1}(U_2)\longrightarrow U_2\times S^1,\qquad \varphi_2(z)=\left([z_1:z_2],\frac{z_2}{\lvert z_2\rvert}\right),
$$
is a homeomorphism with inverse
$$
(t,\lambda)\longmapsto\frac{\lambda(t,1)}{\sqrt{1+\lvert t\rvert^2}}.
$$
On $U_1$, with $s=w_2/w_1$, the analogous map uses $z_1/\lvert z_1\rvert$. On the overlap, the transition function is
$$
g_{12}(t)=\frac{t}{\lvert t\rvert}\in\mathrm{U}(1).
$$

*Proof.* The inverse formula has norm $1$ and class $[t:1]$, and the two formulas are inverse by direct computation. The second component of $\varphi_2$ is unchanged when $z$ is multiplied by a unit scalar, so the trivialization is $\mathrm{U}(1)$-equivariant. The transition is computed by applying $\varphi_1$ to the point $\lambda(t,1)/\sqrt{1+\lvert t\rvert^2}$, whose first coordinate has modulus $\lvert t\rvert/\sqrt{1+\lvert t\rvert^2}$ and phase $\lambda t/\lvert t\rvert$.

**Corollary (the structure group).** The Hopf map is a principal $\mathrm{U}(1)$-bundle, with the action
$$
(z_1,z_2)\cdot\lambda=(\lambda z_1,\lambda z_2),\qquad \lvert\lambda\rvert=1.
$$

*Proof.* The local trivializations are equivariant for the action, and the action is free and transitive on each fibre.

**Proposition (the tautological bundle).** The Hopf bundle is the unit sphere bundle of the tautological line bundle
$$
\mathcal{O}(-1)=\{([w],v):w\in\mathbb{C}^2\setminus\{0\},\ v\in\mathbb{C} w\}\longrightarrow\mathbb{CP}^1,
$$
and the first Chern class of $\mathcal{O}(-1)$ is a generator of $H^2(\mathbb{CP}^1;\mathbb{Z})\cong\mathbb{Z}$.

*Proof.* The unit sphere bundle consists of the pairs $([w],v)$ with $\lVert v\rVert=1$ and $v\in\mathbb{C} w$. The map $v\mapsto([v],v)$ is a homeomorphism from $S^3$ onto that bundle, and its projection to $\mathbb{CP}^1$ is $h$. The transition function $g_{12}(t)=t/\lvert t\rvert$ has winding number $1$ around the origin, so the first Chern number is $\pm1$; the sign depends on the orientation convention, and the class is a generator.

**Proposition (non-triviality).** The Hopf bundle is not trivial. Equivalently, there is no homeomorphism $S^3\cong S^2\times S^1$.

*Proof.* If the bundle were trivial, its total space would be $S^2\times S^1$, whose fundamental group is $\mathbb{Z}$; but $\pi_1(S^3)=0$. The non-vanishing first Chern class gives the same conclusion.

**Remark (why the bundle is not detected by covering spaces).** The total space $S^3$ is simply connected, so the bundle cannot be detected by the monodromy of a covering. **The obstruction is the first Chern class**, a degree-two cohomology class, and it is the reason the Hopf bundle is the standard example of a non-trivial bundle over a simply connected base.

The bundle is summarised below.

| Property | Value |
|---|---|
| total space | $S^3$ |
| base | $\mathbb{CP}^1\cong S^2$ |
| fibre | $S^1$ |
| structure group | $\mathrm{U}(1)$ |
| first Chern class | a generator of $H^2(S^2;\mathbb{Z})$ |
| trivial | no |
| $\pi_1$ of the total space | $0$ |
| $\pi_3$ of the total space | $\mathbb{Z}$ |

## The Homotopy Exact Sequence

**The Hopf bundle yields the exact sequence that computes the low homotopy groups of $S^2$; in particular $\pi_3(S^2)\cong\mathbb{Z}$, generated by the Hopf map.**

**Theorem (the exact sequence).** The fibration
$$
S^1\longrightarrow S^3\stackrel{h}{\longrightarrow}S^2
$$
gives the exact sequence
$$
\cdots\longrightarrow\pi_n(S^1)\longrightarrow\pi_n(S^3)\longrightarrow\pi_n(S^2)\longrightarrow\pi_{n-1}(S^1)\longrightarrow\cdots
$$
and, in low degrees,
$$
0=\pi_3(S^1)\to\pi_3(S^3)=\mathbb{Z}\to\pi_3(S^2)\to\pi_2(S^1)=0,
$$
$$
0=\pi_2(S^3)\to\pi_2(S^2)\to\pi_1(S^1)=\mathbb{Z}\to\pi_1(S^3)=0,
$$
$$
0=\pi_1(S^3)\to\pi_1(S^2)\to\pi_0(S^1)=0.
$$
Hence
$$
\pi_1(S^2)=0,\qquad \pi_2(S^2)\cong\mathbb{Z},\qquad \pi_3(S^2)\cong\mathbb{Z}.
$$

*Proof.* This is the long exact sequence of the fibration (*Homotopy Groups and Fibrations*), together with $\pi_k(S^1)=0$ for $k\ge2$, $\pi_1(S^1)=\mathbb{Z}$, $\pi_0(S^1)=0$, and $\pi_1(S^3)=\pi_2(S^3)=0$, $\pi_3(S^3)=\mathbb{Z}$.

**Corollary (the generator).** The map
$$
h_*:\pi_3(S^3)\longrightarrow\pi_3(S^2)
$$
is an isomorphism, and the class of the Hopf map generates $\pi_3(S^2)\cong\mathbb{Z}$.

*Proof.* The exact sequence gives $0\to\pi_3(S^3)\to\pi_3(S^2)\to0$, so $h_*$ is an isomorphism. The generator of $\pi_3(S^3)$ is the class of the identity, and its image is the class of $h$.

**Proposition (the Hopf invariant).** The Hopf invariant of $h$ is $1$. The map $h$ is essential, that is, not nullhomotopic, although it induces the zero map on reduced homology.

*Proof.* The Hopf invariant is the integer computed from a form whose pullback is exact; for the Hopf map it is $1$ (*Homotopy Groups and Fibrations*). The map is essential because its class in $\pi_3(S^2)$ is a generator. On homology, $h$ sends $H_2(S^3)=0$ to $H_2(S^2)=\mathbb{Z}$ and $H_3(S^3)=\mathbb{Z}$ to $H_3(S^2)=0$, so it is zero in every positive degree.

**Remark (homology against homotopy).** The Hopf map is the standard witness that homology does not determine homotopy: it is invisible to homology and non-trivial in homotopy. **The first non-trivial homotopy group above the dimension of the target is $\pi_3(S^2)$**, and the Hopf map is its generator.

The low homotopy groups are collected below.

| Group | Value |
|---|---|
| $\pi_1(S^1)$ | $\mathbb{Z}$ |
| $\pi_k(S^1)$, $k\ge2$ | $0$ |
| $\pi_1(S^3)$, $\pi_2(S^3)$ | $0$ |
| $\pi_3(S^3)$ | $\mathbb{Z}$ |
| $\pi_1(S^2)$ | $0$ |
| $\pi_2(S^2)$ | $\mathbb{Z}$ |
| $\pi_3(S^2)$ | $\mathbb{Z}$, generated by $h$ |

## The Linking of Two Fibres

**Any two distinct fibres of the Hopf fibration are linked circles, with linking number $1$.**

**Definition.** Let $K_1$ and $K_2$ be two disjoint oriented knots in $S^3$. The **linking number** $\operatorname{lk}(K_1,K_2)$ is the algebraic intersection number of $K_2$ with a Seifert surface of $K_1$; it is symmetric, $\operatorname{lk}(K_1,K_2)=\operatorname{lk}(K_2,K_1)$ (*Knot Theory*).

**Theorem (the standard pair).** The circles
$$
C_1=\{(e^{i\theta},0)\},\qquad C_2=\{(0,e^{i\theta})\}
$$
have linking number $1$.

*Proof.* The set
$$
\Sigma=\{(z_1,z_2)\in S^3:\operatorname{Im}z_2=0,\ \operatorname{Re}z_2\ge0\}
$$
is a closed disk: it is the graph of $z_2=\sqrt{1-\lvert z_1\rvert^2}$ over the closed unit disk in the $z_1$-plane. Its boundary is $C_1$. The circle $C_2$ meets $\Sigma$ exactly at the point $(0,1)$: a point of $C_2$ has $z_1=0$ and $z_2=e^{i\theta}$, and the conditions $\operatorname{Im}z_2=0$, $\operatorname{Re}z_2\ge0$ leave $\theta=0$. The intersection is transverse, since the tangent plane of $\Sigma$ at $(0,1)$ is $\{(v,0):v\in\mathbb{C}\}$ and the tangent line of $C_2$ is $\{(0,it):t\in\mathbb{R}\}$, which meet only at $0$. The intersection number is therefore $\pm1$, and with the orientations induced by increasing $\theta$ on both circles it is $+1$.

**Theorem (any two fibres).** Any two distinct fibres of $h$ have linking number $1$.

*Proof.* The group $\mathrm{GL}_2(\mathbb{C})$ acts on $S^3$ by
$$
A\cdot z=\frac{Az}{\lVert Az\rVert},
$$
and the action is smooth and sends fibres to fibres, because $h(A\cdot z)=[Az]=A\cdot[z]$. The group $\mathrm{GL}_2(\mathbb{C})$ is connected, so the action preserves the orientation of $S^3$; it covers the action of $\mathrm{PGL}_2(\mathbb{C})$ on $\mathbb{CP}^1$, which is $3$-transitive, hence $2$-transitive. Therefore any two distinct fibres are carried to $C_1$ and $C_2$ by an orientation-preserving homeomorphism of $S^3$, and the linking number is invariant under such a homeomorphism. The standard pair has linking number $1$, so every pair does.

**Corollary (the Hopf invariant is the linking number).** The Hopf invariant of $h$ equals the linking number of two fibres, and both are $1$.

*Proof.* For a map $S^3\to S^2$, the Hopf invariant equals the linking number of the preimages of two regular values (*Homotopy Groups and Fibrations*); the Hopf invariant of $h$ is $1$ and the linking number is $1$ by the theorem.

**Remark (the geometry of the fibres).** The fibres are disjoint circles that are pairwise linked; the fibration is a **linking of circles**, and the linking number is the same for every pair. **The Hopf map is the standard example of a fibration whose fibres are linked**, and the linking is the geometric content of the generator of $\pi_3(S^2)$.

## The Identification with $\mathrm{SU}(2)$

**The sphere $S^3$ is the Lie group $\mathrm{SU}(2)$, the group of unit quaternions; in this model the Hopf map is the orbit map of the conjugation action, $q\mapsto qiq^{-1}$, and the fibre is the circle of unit complex numbers.**

**Theorem ($S^3\cong\mathrm{SU}(2)$).** The map
$$
\mathrm{SU}(2)\longrightarrow S^3,\qquad
\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}\longmapsto(\alpha,\beta),
$$
is a homeomorphism. With the quaternion multiplication on $S^3$, it is an isomorphism of Lie groups.

*Proof.* A matrix of the displayed form is unitary and has determinant $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$, so it lies in $\mathrm{SU}(2)$; conversely, the unitarity and the determinant condition force the form. The map is continuous, bijective, with continuous inverse $(\alpha,\beta)\mapsto\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}$. The multiplication of these matrices is the multiplication of the quaternions $\alpha+\beta j$, so the map is a group isomorphism.

**Proposition (the Hopf map in the quaternionic model).** Under the identification $S^3\cong\mathrm{SU}(2)$, the Hopf map is
$$
h(q)=q\,i\,q^{-1},\qquad q\in S^3,
$$
with values in the unit imaginary quaternions, which form a two-sphere. Its fibre over $i$ is the circle $\mathrm{U}(1)=\{a+bi:\lvert a\rvert^2+\lvert b\rvert^2=1\}$.

*Proof.* For a unit quaternion $q$, the quaternion $qiq^{-1}$ is imaginary, because it is conjugate to $i$, and it has norm $1$; hence it lies in the unit imaginary quaternions. The map is surjective because every unit imaginary quaternion is conjugate to $i$. The fibre over $i$ is the set of unit quaternions commuting with $i$, which is the unit complex numbers.

**Proposition (the homogeneous description).** The Hopf bundle is the quotient
$$
\mathrm{SU}(2)\longrightarrow\mathrm{SU}(2)/\mathrm{U}(1)\cong S^2
$$
by the left action of the diagonal circle
$$
\lambda\longmapsto\begin{pmatrix}\lambda&0\\0&\overline{\lambda}\end{pmatrix},\qquad \lvert\lambda\rvert=1.
$$
The left action of $\mathrm{SU}(2)$ by group multiplication is transitive and free, and the Hopf map is equivariant for it.

*Proof.* Under the identification of the theorem, left multiplication by $\operatorname{diag}(\lambda,\overline{\lambda})$ sends $(\alpha,\beta)$ to $(\lambda\alpha,\lambda\beta)$, which is the scalar multiplication defining the fibres; since the circle is abelian, the same orbits are the orbits of the right action used in the local trivializations. The quotient is $\mathbb{CP}^1\cong S^2$. The left action of $\mathrm{SU}(2)$ on itself is transitive and free.

**Remark (the four Hopf fibrations).** The Hopf map is the complex member of a family of four fibrations, one for each normed division algebra.

| Scalars | Total space | Base | Fibre |
|---|---|---|---|
| $\mathbb{R}$ | $S^1$ | $S^1$ | $S^0$ |
| $\mathbb{C}$ | $S^3$ | $S^2$ | $S^1$ |
| $\mathbb{H}$ | $S^7$ | $S^4$ | $S^3$ |
| $\mathbb{O}$ | $S^{15}$ | $S^8$ | $S^7$ |

**The complex row is the subject of this article**; the quaternionic and octonionic rows are *Homotopy Groups and Fibrations*, and the quaternionic sphere is *Quaternion Topology*.

## Summary

The unit sphere $S^3\subset\mathbb{C}^2$ is a compact, connected, simply connected three-manifold, with $H_3=\mathbb{Z}$ and $\pi_3=\mathbb{Z}$. The Hopf map $h(z_1,z_2)=[z_1:z_2]$ sends $S^3$ onto $\mathbb{CP}^1\cong S^2$, and its fibre over a point is the circle of unit multiples of a representative, so the fibres are the orbits of the free $\mathrm{U}(1)$ action by scalar multiplication. The map is a principal $\mathrm{U}(1)$-bundle, locally trivial over the two standard charts, with transition function $t/\lvert t\rvert$ of winding number $1$; it is the unit sphere bundle of the tautological line bundle, its first Chern class is a generator, and the bundle is not trivial because $S^3$ is simply connected and $S^2\times S^1$ is not.

The exact sequence of the fibration gives $\pi_1(S^2)=0$, $\pi_2(S^2)=\mathbb{Z}$ and $\pi_3(S^2)=\mathbb{Z}$, the last generated by the Hopf map, whose Hopf invariant is $1$. The fibres are linked circles: the standard pair has linking number $1$, and the $\mathrm{GL}_2(\mathbb{C})$ action, which is orientation-preserving and $2$-transitive on the base, carries any pair of distinct fibres to the standard pair. The sphere is the Lie group $\mathrm{SU}(2)$ of unit quaternions, and in that model the Hopf map is $q\mapsto qiq^{-1}$, the quotient of $\mathrm{SU}(2)$ by the diagonal circle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^3=\{z\in\mathbb{C}^2:\lVert z\rVert=1\}$ | the unit sphere |
| $h(z_1,z_2)=[z_1:z_2]$ | the Hopf map $S^3\to\mathbb{CP}^1$ |
| $C_1=\{(\lambda,0):\lvert\lambda\rvert=1\}$ | the fibre over $[1:0]$ |
| $C_2=\{(0,\lambda):\lvert\lambda\rvert=1\}$ | the fibre over $[0:1]$ |
| $\mathrm{U}(1)$ | the structure group, acting by scalar multiplication |
| $\mathcal{O}(-1)$ | the tautological line bundle over $\mathbb{CP}^1$ |
| $\operatorname{lk}(K_1,K_2)$ | the linking number of two oriented knots |
| $\mathrm{SU}(2)$ | the special unitary group, isomorphic to $S^3$ |
| $q\mapsto qiq^{-1}$ | the Hopf map in the quaternionic model |

## Further Reading

- [The Topology of $\mathbb{C}^2$](the-topology-of-the-complex-two-space.html), the previous article, for the sphere as a topological space.
- [The Compactifications of $\mathbb{C}^2$](the-compactifications-of-the-complex-two-space.html), the previous article, for the Hopf map as the attaching map at infinity.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), for the projective line and the complex directions.
- [Homotopy Groups and Fibrations](homotopy-groups-and-fibrations.html), for the long exact sequence, the Hopf invariant and the four Hopf fibrations.
- [The Fundamental Group and Covering Spaces](the-fundamental-group-and-covering-spaces.html), for simple connectivity and covering spaces.
- [Knot Theory](knot-theory.html), for the linking number and Seifert surfaces.
- [Quaternion Topology](quaternion-topology.html), for the quaternionic sphere and its topology.
- [Introduction to Topology on the Quaternions](introduction-to-topology-on-the-quaternions.html), for the topology of the quaternion algebra.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for $\mathrm{U}(2)$, $\mathrm{SU}(2)$ and their homogeneous spaces.
