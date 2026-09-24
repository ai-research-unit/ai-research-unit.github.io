# __Biquaternion Topology__

## Introduction

This article collects the standard topology of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its group of units, using the algebra and fixed-point subspaces of *Biquaternion Algebra*, the norm form $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ and invertibility criterion of *Biquaternion Norm and Invertibility*, the zero divisor set of *Biquaternion Zero Divisors*, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ with $N=\det$ of *Biquaternion Algebraic Representations*, the projective picture, and *Lie Groups*. No physics is invoked and no new result is claimed.

**Conventions.** The units are $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, the central scalar imaginary is $i$, and $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The norm form is $N(\tilde{Q})=\sum_\mu Q_\mu^2$ and the Euclidean norm is $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$.

The algebra itself has no interesting topology: as a real vector space it is $\mathbb{R}^8$, hence contractible. The interesting topology lies in the **unit group** $\mathbb{B}^\times\cong GL(2,\mathbb{C})$ and the **null cone** $\{N(\tilde{Q})=0\}$.

# Part I: The Algebra as a Topological Space

## 1. The underlying space and its contractibility

The real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and

$$
\tilde{Q}\mapsto(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)
$$

is a linear isometry of $(\mathbb{B},\|\cdot\|_E)$ onto $\mathbb{R}^8$. Thus the topology of $\mathbb{B}$ is the Euclidean topology of $\mathbb{R}^8$. The product is bilinear, hence continuous, so $\mathbb{B}$ is a topological algebra over $\mathbb{R}$; inversion is continuous on the units, so $\mathbb{B}^\times$ is a topological group.

**Theorem.** $\mathbb{B}$ is contractible, hence path-connected and simply connected, with $\pi_n(\mathbb{B})=0$ for all $n\geq1$.

**Proof.** The straight-line homotopy

$$
H(t,\tilde{Q})=(1-t)\tilde{Q},\qquad t\in[0,1],
$$

is continuous with $H(0,\tilde{Q})=\tilde{Q}$ and $H(1,\tilde{Q})=0$, so the identity is homotopic to the constant map at $0$. $\square$

Thus every map into $\mathbb{B}$ is null-homotopic, and by the same homotopy the fixed-point subspaces are contractible:

$$
\mathbb{C}_{\mathbb{B}}\cong\mathbb{R}^2,\qquad \mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4,\qquad \mathbb{M}_+\cong\mathbb{R}^4,\qquad \mathbb{M}_-\cong\mathbb{R}^4.
$$

So $\mathbb{M}_\pm$ carry no topology beyond that of $\mathbb{R}^4$; their Minkowski content comes from the restricted quadratic form (§7), not from the topology.

# Part II: The Unit Sphere and the Unit Group

## 2. The Euclidean unit sphere

$$
S^7_E=\{\tilde{Q}\in\mathbb{B}:\|\tilde{Q}\|_E=1\}\cong S^7
$$

is a closed, compact, connected $7$-manifold, but it is the wrong object here. Multiplication does not preserve $\|\cdot\|_E$: for $\tilde{Q}=e_1+ie_2$,

$$
\tilde{Q}^2=0,\qquad \|\tilde{Q}\|_E=\sqrt2,\qquad \|\tilde{Q}^2\|_E=0\neq\|\tilde{Q}\|_E^2=2.
$$

Normalizing, $\tilde{Q}_0=(e_1+ie_2)/\sqrt{2}$ has $\|\tilde{Q}_0\|_E=1$ but $N(\tilde{Q}_0)=0$, so $\tilde{Q}_0$ is a zero divisor, and

$$
S^7_E\not\subseteq\mathbb{B}^\times.
$$

For the normed division algebras the norm is multiplicative and the unit sphere is a Lie group, $S^0,S^1,S^3$, while $S^7$ is a Moufang loop for the octonions; since $\mathbb{B}$ is not a division algebra, none of this applies.

## 3. The norm-one group and the group of units

Because $N$ is multiplicative and $N(e_0)=1$, the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=1\}
$$

is a closed subgroup of real dimension $6$, and under $\rho:\mathbb{B}\to M_2(\mathbb{C})$, where $N=\det$,

$$
\{\tilde{Q}:N(\tilde{Q})=1\}\cong SL(2,\mathbb{C})
$$

as real Lie groups. It is noncompact and, by §10, deformation retracts onto $SU(2)\cong S^3$; hence it is simply connected with the homotopy type of $S^3$ and $\pi_3\cong\mathbb{Z}$.

Thus there are two "unit spheres": $S^7_E$ is a sphere but not a group, while $\{N=1\}$ is a group but neither Euclidean nor compact. The condition that makes a level set a group is $N=1$, not $\|\cdot\|_E=1$.

By the invertibility criterion, $\mathbb{B}^\times=\{\tilde{Q}:N(\tilde{Q})\neq0\}=\mathbb{B}\setminus\{N=0\}$, which is open, as the preimage of $\mathbb{C}\setminus\{0\}$ under $N$, and dense, its complement having real dimension $6$; and

$$
\mathbb{B}^\times\cong GL(2,\mathbb{C}),
$$

the units being the invertible matrices. It is a noncompact real $8$-manifold (complex dimension $4$), with centre $\mathbb{C}^\times\simeq S^1$ and Lie algebra $\mathfrak{gl}_2(\mathbb{C})=\mathbb{B}$.

# Part III: The Null Cone, Its Link, and the Light Cone

## 4. The null cone

The **null cone**, or singular set, is

$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z},
$$

where $\mathcal{Z}$ is the zero-divisor set; under $\rho$ it is the determinantal variety

$$
\rho(\mathcal{N})=\{A\in M_2(\mathbb{C}):\det A=0\}=\{A:\operatorname{rank}A\leq1\}.
$$

It is closed, with empty interior, so $\mathbb{B}^\times$ is dense; it is a real algebraic cone with apex $0$, since $N$ is homogeneous of degree $2$; and its real dimension is $6$, as the complex hypersurface $N=0$ in $\mathbb{B}\cong\mathbb{C}^4$. Away from the origin its two real gradients are independent, so $\mathcal{N}\setminus\{0\}$ is a smooth real $6$-manifold; at the origin it is not a manifold (§6).

**Contractibility.** The homotopy $K(s,\tilde{Q})=(1-s)\tilde{Q}$ maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling a null element by a complex number preserves nullity, and contracts $\mathcal{N}$ to the apex. The null cone is thus homotopy trivial, like the algebra, but is a singular subset of it.

## 5. The Segre map and the two rulings

Let $S=\mathbb{C}^2$ be the two-component spinor space, with $u=(u_1,u_2)^T$, and $S^*$ its dual, so that $M_2(\mathbb{C})=S\otimes S^*$. For $u,v\in\mathbb{C}^2$ put

$$
M(u,v)=uv^{T}=\begin{pmatrix}u_1v_1&u_1v_2\\u_2v_1&u_2v_2\end{pmatrix}.
$$

Then $\det M(u,v)=0$, and every matrix of rank at most one arises this way, with rank one precisely when $u\neq0\neq v$. Hence the **Segre-type map**

$$
\sigma:\mathbb{C}^2\times\mathbb{C}^2\to M_2(\mathbb{C}),\qquad \sigma(u,v)=uv^{T},
$$

has image $\rho(\mathcal{N})$, with fibre $\sigma^{-1}(uv^{T})=\{(\lambda u,\lambda^{-1}v):\lambda\in\mathbb{C}^\times\}\cong\mathbb{C}^\times$ over each rank-one matrix and $\sigma^{-1}(0)=(\{0\}\times\mathbb{C}^2)\cup(\mathbb{C}^2\times\{0\})$. Projectivizing, $\sigma$ descends to the **Segre embedding**

$$
\bar{\sigma}:P(S)\times P(S)\to P(M_2(\mathbb{C}))=P^3,\qquad([u],[v])\mapsto[uv^{T}],
$$

with image the smooth quadric surface $Q=\{[M]\in P^3:\det M=0\}$. Since $\bar{\sigma}$ embeds $P^1\times P^1$ and $P^1(\mathbb{C})\cong S^2$,

$$
Q\cong P^1\times P^1\cong S^2\times S^2.
$$

Thus $Q$ is compact, connected and simply connected, of real dimension $4$, with $b_2(Q)=2$ and $\chi(Q)=4$, for the projective details. The two factors of $P^1\times P^1$ are the **two rulings**: the lines $\{[u]\}\times P(S)$ and the lines $P(S)\times\{[v]\}$. Each point of $Q$ lies on exactly one line of each ruling, lines of the same ruling are disjoint, and lines of different rulings meet in one point.

**Grassmannian description.** Since $P(S)=\operatorname{Gr}(1,S)$ is the Grassmannian of lines in $S\cong\mathbb{C}^2$,

$$
Q\cong\operatorname{Gr}(1,S)\times\operatorname{Gr}(1,S):
$$

a point of $Q$ is a pair of spinor lines, equivalently a decomposable tensor $u\otimes v\in S\otimes S^*$.

## 6. The link of the null cone

The **link** of the null cone is

$$
L=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0,\ \|\tilde{Q}\|_E=1\}=\mathcal{N}\cap S^7_E.
$$

Every nonzero null element is uniquely $t\,u$ with $t=\|\tilde{Q}\|_E>0$ and $u\in L$, so $\mathcal{N}$ is the cone on $L$ and is contractible (§4). Since $\dim_{\mathbb{R}}\mathcal{N}=6$, the link has real dimension $5$. Under $M=uv^{T}$ with $\|u\|=\|v\|=1$,

$$
L\cong(S^3\times S^3)/U(1),
$$

where $U(1)=S^1$ acts by $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$, the relation under which $uv^{T}$ is unchanged. The Hopf maps combine to a bundle projection

$$
q:L\to Q\cong S^2\times S^2,\qquad[(u,v)]\mapsto([u],[v]),
$$

whose fibre over $([u],[v])$ is the circle of pairs $(e^{i\theta}u_0,e^{-i\theta}v_0)$. Hence $L$ is a closed connected $5$-manifold that is an $S^1$-bundle over $S^2\times S^2$.

The map $S^3\times S^3\to L$ is a principal $S^1$-bundle, and its long exact homotopy sequence, with $\pi_1(S^3\times S^3)=\pi_2(S^3\times S^3)=0$, gives

$$
\pi_1(L)=0,\qquad \pi_2(L)\cong\pi_1(S^1)=\mathbb{Z}.
$$

So $L$ is simply connected but not homeomorphic to $S^5$, whose $\pi_2$ vanishes: the null cone is genuinely non-manifold at its apex.

## 7. The light cone in the Minkowski subspaces

The restriction of $N$ to the anti-Hermitian subspace is real and indefinite. Writing $\tilde{Q}=iq'_0e_0+q_1e_1+q_2e_2+q_3e_3\in\mathbb{M}_-$ with real coordinates,

$$
N(\tilde{Q})=-(q'_0)^2+q_1^2+q_2^2+q_3^2,
$$

a form of signature $(3,1)$; on $\mathbb{M}_+$ the signature is $(1,3)$. Either subspace is thereby identified with Minkowski space $\mathbb{R}^{1,3}$, and its null set,

$$
N(\tilde{Q})=0\iff(q'_0)^2=q_1^2+q_2^2+q_3^2,
$$

is the **light cone**, a double cone with apex at the origin. With this identification, the **null biquaternions of the Minkowski subspace** are exactly the elements of the light cone.

Intersecting with the unit sphere of $\mathbb{M}_-\cong\mathbb{R}^4$ gives $q'_0=\pm1/\sqrt2$ and $q_1^2+q_2^2+q_3^2=1/2$, so the link of the light cone is the disjoint union

$$
S^2\sqcup S^2,
$$

one sphere per nappe. Each nappe is the cone on its sphere, and the complement of the light cone in $\mathbb{M}_-$ has exactly three connected components, the future timelike, past timelike and spacelike regions, as in *Biquaternion Norm and Invertibility*.

Two warnings are in order: the light cone is a real cone of real dimension $3$ in $\mathbb{M}_-\cong\mathbb{R}^4$, not the full null cone $\mathcal{N}$ of §4, which has real dimension $6$; and $\mathcal{N}$ is the complex cone over the Segre quadric, whose intersection with $\mathbb{M}_-$ recovers the light cone, so the Minkowski null biquaternions form a three-dimensional real cone while the null elements of the full algebra form a six-dimensional one.

## 8. Pure biquaternions and reality conditions

A biquaternion is **pure** if its complex scalar part vanishes,

$$
P=\{\tilde{Q}\in\mathbb{B}:Q_0=0\}=\{Q_1e_1+Q_2e_2+Q_3e_3:Q_k\in\mathbb{C}\}\cong\mathbb{C}^3,
$$

a contractible real six-dimensional subspace; its topology is trivial, and the interesting sets are the real forms cut out by a reality condition.

Complex conjugation splits $P$ into two real three-dimensional subspaces. The real condition $\tilde{Q}^*=\tilde{Q}$ gives the **pure real quaternions**

$$
P\cap\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}\cong\mathbb{R}^3,
$$

whose unit sphere consists of the unit imaginary quaternions $\mu$ with $\mu^2=-e_0$, the family of **real roots of $-1$** classified in *Biquaternion Roots of Minus One*. The imaginary condition $\tilde{Q}^*=-\tilde{Q}$ gives

$$
P\cap i\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}\cong\mathbb{R}^3,
$$

Each is a copy of $\mathbb{R}^3$; for the first the unit sphere is

$$
S^2=\{\mu\in\mathbb{H}_{\mathbb{B}}:\mu^2=-e_0\},
$$

compact, connected and simply connected, with $\pi_2(S^2)\cong\mathbb{Z}$, and not a group, since only $S^0,S^1,S^3$ admit Lie group structures. It is a homogeneous space of the unit quaternions,

$$
S^2\cong SU(2)/U(1)\cong SO(3)/SO(2),
$$

the base of the Hopf fibration and the quotient of $S^3$ by the maximal torus of $SU(2)$; the sphere of roots of $+1$ is its image under multiplication by $i$, homeomorphic to it.

Finally, on either pure reality slice the restricted norm form is definite, being $q_1^2+q_2^2+q_3^2$ on $P\cap\mathbb{H}_{\mathbb{B}}$ and $-(q'^2_1+q'^2_2+q'^2_3)$ on $P\cap i\mathbb{H}_{\mathbb{B}}$. Hence $N(\tilde{Q})=0$ forces $\tilde{Q}=0$: the only null element of either pure reality slice is the origin, so the light cone meets these three-dimensional spaces only at its apex, unlike the Minkowski subspaces $\mathbb{M}_\pm$, which contain a full three-dimensional light cone.

# Part IV: Retractions and Homotopy Groups

## 9. The retraction of $GL(2,\mathbb{C})$ onto $U(2)$

Every $A\in GL(2,\mathbb{C})$ has a unique polar decomposition $A=UP$, where $U\in U(2)$ and $P=(A^*A)^{1/2}$ is Hermitian positive definite. For $t\in[0,1]$ put $P_t=(1-t)P+tI$ and

$$
H(t,A)=UP_t.
$$

The eigenvalues of $P_t$ are $(1-t)\lambda+t$ with $\lambda>0$, hence positive, so $P_t$ is positive definite and $H(t,A)\in GL(2,\mathbb{C})$; the map $H$ is continuous because the positive-definite square root depends continuously on $A$. Moreover

$$
H(0,A)=UP=A,\qquad H(1,A)=U\in U(2),\qquad H(t,U)=U\ \text{ for } U\in U(2).
$$

So $U(2)$ is a strong deformation retract of $GL(2,\mathbb{C})$, and the two are homotopy equivalent, whence $\pi_n(GL(2,\mathbb{C}))\cong\pi_n(U(2))$ for all $n$. Every $A$ is joined to a unitary matrix, and $U(2)$ is connected (§11), so $GL(2,\mathbb{C})$ and hence $\mathbb{B}^\times$ are connected, in agreement with *Biquaternion Norm and Invertibility*. (The statement that there are two components distinguished by the determinant concerns $GL(2,\mathbb{R})$, not $GL(2,\mathbb{C})$, where the determinant moves continuously to $1$.) Under $\rho$, the retraction takes $\mathbb{B}^\times$ onto its maximal compact subgroup, the **unitary biquaternions**

$$
\{\tilde{Q}\in\mathbb{B}:\tilde{Q}^\dagger\tilde{Q}=e_0\}\cong U(2).
$$

## 10. The retraction of $SL(2,\mathbb{C})$ onto $SU(2)$

Let $A\in SL(2,\mathbb{C})$ have polar decomposition $A=UP$. Then $1=\det A=\det U\det P$ with $\det U\in U(1)$ and $\det P\in(0,\infty)$, so $\det U=1$ and $\det P=1$, that is $U\in SU(2)$. For $t\in[0,1]$ define

$$
P_t=\frac{(1-t)P+tI}{\det\big((1-t)P+tI\big)^{1/2}}.
$$

The denominator is a positive real number, so $P_t$ is Hermitian positive definite of determinant $1$. The map $H(t,A)=UP_t$ is continuous, lies in $SL(2,\mathbb{C})$ since $\det(UP_t)=1$, and satisfies $H(0,A)=A$, $H(1,A)=U\in SU(2)$, and $H(t,U)=U$ for unitary $U$. Hence $SU(2)$ is a strong deformation retract of $SL(2,\mathbb{C})$.

Thus $SL(2,\mathbb{C})\simeq SU(2)\cong S^3$: it is connected and simply connected with $\pi_3\cong\mathbb{Z}$ and the homotopy type of $S^3$, but is not homeomorphic to $S^3$, being a noncompact real $6$-manifold. The norm-one group of §3 is therefore simply connected of homotopy type $S^3$.

## 11. The structure of $U(2)$ and $SU(2)$

The unit quaternions form $S^3$, and $SU(2)\cong S^3=\{q\in\mathbb{H}:|q|=1\}$ as Lie groups and spaces; $SU(2)$ is compact, connected and simply connected, the double cover of $SO(3)$.

Every $U\in U(2)$ is a scalar multiple of a special unitary matrix: if $\det U=e^{i\theta}$ and $z^2=\det U$, then $A=z^{-1}U$ has $\det A=1$ and $U=zA$. Hence

$$
U(2)=U(1)\cdot SU(2),\qquad U(1)\cap SU(2)=\{\pm I\},
$$

and the multiplication map $U(1)\times SU(2)\to U(2)$ is a surjective homomorphism with kernel $\{(I,I),(-I,-I)\}\cong\mathbb{Z}/2$, so by the first isomorphism theorem for Lie groups

$$
U(2)\cong(U(1)\times SU(2))/\{\pm I\}\cong(S^1\times S^3)/\{\pm1\},
$$

with $\{\pm1\}$ acting diagonally by $(z,q)\mapsto(-z,-q)$. Moreover $\det:U(2)\to U(1)$ is a principal $SU(2)$-bundle, each fibre being a coset of $SU(2)$, and it admits the section $s(z)=\begin{pmatrix}z&0\\0&1\end{pmatrix}$; a principal bundle with a section is trivial, so

$$
U(2)\cong U(1)\times SU(2)\cong S^1\times S^3.
$$

This is a homeomorphism, not an isomorphism of Lie groups: the map above is two-to-one, while the centre of $U(2)$ is connected but that of $U(1)\times SU(2)$ is not.

The diagonal matrices form a maximal torus $T^2\cong S^1\times S^1\subset U(2)$. It is **not** true that $U(2)$ deformation retracts onto $T^2$: that would give $\pi_1(U(2))\cong\pi_1(T^2)$, but these are $\mathbb{Z}$ and $\mathbb{Z}^2$. Every element of $U(2)$ does lie in some maximal torus, and the quotient is the complete flag variety

$$
U(2)/T^2\cong P^1\cong S^2,
$$

so $U(2)$ is a fibre bundle over $S^2$ with fibre $T^2$; and $U(2)$ is not homotopy equivalent to $T^2$, being homeomorphic to $S^1\times S^3$.

## 12. Homotopy groups and generators

The retractions give $SU(2)\cong S^3$, $U(2)\cong S^1\times S^3$, $SL(2,\mathbb{C})\simeq S^3$, $GL(2,\mathbb{C})\simeq U(2)\simeq S^1\times S^3$, and $\mathbb{B}^\times\cong GL(2,\mathbb{C})$. Hence

$$
\pi_1(SU(2))=\pi_2(SU(2))=0,\qquad\pi_3(SU(2))\cong\mathbb{Z},
$$

$$
\pi_1(U(2))\cong\mathbb{Z},\qquad\pi_2(U(2))=0,\qquad\pi_3(U(2))\cong\mathbb{Z},
$$

and likewise $\pi_1(SL(2,\mathbb{C}))=0$, $\pi_1(GL(2,\mathbb{C}))\cong\mathbb{Z}$, with $\pi_2=0$ and $\pi_3\cong\mathbb{Z}$ for both.

**Generators.** The group $\pi_3(SU(2))\cong\mathbb{Z}$ is generated by the class $[\operatorname{id}_{S^3}]$ of the identity map under $SU(2)\cong S^3$, and $\pi_3(U(2))\cong\mathbb{Z}$ by $\iota_*[\operatorname{id}_{S^3}]$ for the inclusion $\iota:SU(2)\hookrightarrow U(2)$, which induces an isomorphism on $\pi_3$. The group $\pi_1(U(2))\cong\mathbb{Z}$ is generated by the loop

$$
\gamma(t)=\begin{pmatrix}e^{2\pi it}&0\\0&1\end{pmatrix},\qquad t\in[0,1],
$$

and $\det_*:\pi_1(U(2))\to\pi_1(U(1))\cong\mathbb{Z}$ is an isomorphism, so a generator is a loop whose determinant winds once. The universal covers are

$$
\widetilde{U(2)}\cong\widetilde{GL(2,\mathbb{C})}\cong\mathbb{R}\times S^3,
$$

while $SU(2)$ and $SL(2,\mathbb{C})$ are their own universal covers. By Hurewicz, $H_1(U(2))\cong H_1(GL(2,\mathbb{C}))\cong\mathbb{Z}$ and $H_1(SU(2))=H_1(SL(2,\mathbb{C}))=0$; and $\pi_n(U(2))\cong\pi_n(S^3)$ for $n\geq2$.

## Summary

- The algebra $\mathbb{B}\cong\mathbb{R}^8$ is contractible with all homotopy groups zero: it is homotopy trivial.
- The Euclidean unit sphere $S^7_E$ is not a group and meets the zero divisors, since $\|\cdot\|_E$ is not multiplicative; the group is the norm-form level set $\{N=1\}\cong SL(2,\mathbb{C})\simeq S^3$.
- The units $\mathbb{B}^\times\cong GL(2,\mathbb{C})$ are open, dense and connected and retract onto $U(2)$; $SU(2)\cong S^3$, $U(2)\cong S^1\times S^3$, $SL(2,\mathbb{C})\simeq S^3$, $GL(2,\mathbb{C})\simeq S^1\times S^3$, with $\pi_1=0,\mathbb{Z},0,\mathbb{Z}$ (the $\mathbb{Z}$ entries from the determinant) and $\pi_2=0$, $\pi_3\cong\mathbb{Z}$ in all four cases.
- The null cone $\{N=0\}$ is closed, of real dimension $6$, contractible and non-manifold at $0$; its projectivization is the quadric $P^1\times P^1\cong S^2\times S^2$ with two rulings, and its link is an $S^1$-bundle over $S^2\times S^2$ with $\pi_1=0$, $\pi_2\cong\mathbb{Z}$. The light cone of the Minkowski subspaces is its real slice, with link $S^2\sqcup S^2$; the pure reality slices are copies of $\mathbb{R}^3$ with unit sphere $S^2\cong SU(2)/U(1)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} \cong \mathbb{R}^8$ | Biquaternion algebra with its Euclidean topology; contractible |
| $S^7_E$ | Euclidean unit sphere in $\mathbb{B}$; not a group, and it meets the zero divisors |
| $\{N = 1\}$ | Norm-form level set; a group, $\cong SL(2,\mathbb{C}) \simeq S^3$ |
| $\mathbb{B}^\times \cong GL(2,\mathbb{C})$ | Group of units; open, dense, connected, retracting onto $U(2)$ |
| $U(2) \cong S^1 \times S^3$, $SU(2) \cong S^3$ | Maximal compact subgroup and its determinant-one part |
| $\{N = 0\}$ | Null cone; closed, real dimension $6$, contractible, non-manifold at $0$ |
| Link of the null cone | $S^1$-bundle over $S^2 \times S^2$, with $\pi_1 = 0$ and $\pi_2 \cong \mathbb{Z}$ |
| $P^1 \times P^1 \cong S^2 \times S^2$ | Projectivised null cone (Segre variety), with its two rulings |
| Light cone in $\mathbb{M}_\pm$ | Real slice of the null cone, with link $S^2 \sqcup S^2$ |
| $\pi_k$ | Homotopy groups of the spaces above |



## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015).
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
