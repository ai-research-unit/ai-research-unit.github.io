# __Biquaternion Topology__

## Introduction

This article collects the topology of the **null cone** of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its projective geometry: the null cone and its link, the Segre embedding and the two rulings of null planes, the projective null quadric $Q^2$ with its tangency and its polarity, and the Klein–Plücker geometry of the lines of $\mathbb{P}^3$. The Euclidean structure of the ambient space, its contractibility and the Euclidean unit sphere read the *Hermitian* form and belong to *The Euclidean Topology of the Biquaternion Algebra*; they are quoted from there wherever the geometry of the null cone needs them.

The norm $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ decides invertibility and vanishes exactly on the zero divisors together with the origin (*Biquaternion Norm and Invertibility*, *Biquaternion Zero Divisors*); both treatments are algebraic, and the projective sections below treat the same form geometrically, as the equation of a quadric. The article uses the algebra and fixed-point subspaces of *Biquaternion Algebra*, the zero divisor set of *Biquaternion Zero Divisors*, and *Lie Groups*. The polarisation of the norm, its real forms and its associated Clifford algebra are in *Biquaternion Norm and Invertibility*; the Lorentzian and conformal reading of the real slices is in *Biquaternion Lorentzian and Conformal Geometry*. No physics is invoked and no new result is claimed.

**Scope.** The topology of the **group of units** $\mathbb{B}^\times$ — the polar decomposition, the retractions onto its compact subgroups, the homotopy groups and the universal cover — is read on the Hermitian form and is treated in *The Unitary Group of the Biquaternion Algebra*, the algebraic group itself being *The Biquaternion Unit Group as a Topological Group*. This article owns the null cone, its link and their projective geometry, quoting the ambient Euclidean structure from *The Euclidean Topology of the Biquaternion Algebra* and the homotopy type of $\mathbb{B}^\times$ from those articles when a comparison is needed.

**Conventions.** The units are $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, the central scalar imaginary is $i$, and $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\sum_\mu Q_\mu^2$ and the Euclidean norm is $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$.

As a real vector space the algebra is $\mathbb{R}^8$, hence contractible, and the Euclidean structure that exhibits this, the Euclidean unit sphere and the contractibility of the six distinguished subspaces are *The Euclidean Topology of the Biquaternion Algebra*; only the contractibility of the ambient space is quoted here. The distinguished subset studied in this article is the **null cone** $\{N(\tilde{Q})=0\}$ together with its link.

## The Ambient Space

The algebra is $\mathbb{R}^8$ with the Euclidean topology of *The Euclidean Topology of the Biquaternion Algebra*, and it is contractible: the straight-line homotopy $H(s,\tilde{Q})=(1-s)\tilde{Q}$ contracts it to the origin, so $\pi_n(\mathbb{B})=0$ for every $n\geq1$ and every map into $\mathbb{B}$ is null-homotopic. The homotopy preserves every linear subspace, hence also the six distinguished subspaces and the null cone, so the null cone is homotopy trivial as well, like the algebra around it; but it is a singular subset of it, and its smooth structure away from the apex is what the rest of the article uses. Nothing in the projective sections rests on the metric; the Euclidean input is used only through the metric topology it induces.

## The null cone

The **null cone**, or singular set, is

$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z},
$$

where $\mathcal{Z}$ is the zero-divisor set.

It is closed, with empty interior, so $\mathbb{B}^\times$ is dense; it is a real algebraic cone with apex $0$, since $N$ is homogeneous of degree $2$; and its real dimension is $6$, as the complex hypersurface $N=0$ in $\mathbb{B}\cong\mathbb{C}^4$. The polynomial $N$ is irreducible and its complex gradient $2(Q_0,Q_1,Q_2,Q_3)$ vanishes only at the origin, so $0$ is the only singular point and the punctured cone $\mathcal{N}\setminus\{0\}=\mathcal{Z}$ is a smooth complex $3$-manifold, exactly the zero-divisor set. Away from the origin it is a real $6$-manifold, and at the origin it is not a manifold; the smooth structure, which is analytic, is in *Biquaternion Analysis*, and the local picture at the apex in §*The link of the null cone*.

**Contractibility.** The homotopy $K(s,\tilde{Q})=(1-s)\tilde{Q}$ maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling a null element by a complex number preserves nullity, and contracts $\mathcal{N}$ to the apex. The null cone is thus homotopy trivial, like the algebra, but is a singular subset of it.

## The Segre embedding

Choose on $\mathbb{B}$ the linear coordinates
$$
X_0=Q_0-iQ_3,\qquad X_1=-iQ_1-Q_2,\qquad X_2=-iQ_1+Q_2,\qquad X_3=Q_0+iQ_3,
$$
an invertible $\mathbb{C}$-linear change of the coordinates $Q_0,\dots,Q_3$. In them the norm is a split form,
$$
N(\tilde{Q})=\sum_{\mu=0}^{3}Q_\mu^2=X_0X_3-X_1X_2,
$$
since $X_0X_3=(Q_0-iQ_3)(Q_0+iQ_3)=Q_0^2+Q_3^2$ and $X_1X_2=(-iQ_1-Q_2)(-iQ_1+Q_2)=-Q_1^2-Q_2^2$. The null cone is therefore the affine hypersurface $X_0X_3=X_1X_2$, and each of its nonzero points is a pair of one-dimensional subspaces of $\mathbb{C}^2$. Indeed, for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ the point
$$
(X_0,X_1,X_2,X_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$
lies on the null cone, since $\alpha\gamma\cdot\beta\delta=\alpha\delta\cdot\beta\gamma$, and conversely every null point is of this form: if $X_0\neq0$ the pair $u=(1,X_2/X_0)$, $v=(X_0,X_1)$ reproduces it, and the other cases are the same argument applied to a coordinate that is nonzero. The pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. Projectivising gives the **Segre embedding**
$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta],
$$
whose image is exactly the projective null quadric
$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}.
$$
The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed.

## The two rulings of null planes

In the coordinates above the polar form of $N$ is
$$
B(X,Y)=\tfrac12\bigl(X_0Y_3+X_3Y_0-X_1Y_2-X_2Y_1\bigr),
$$
the polarisation of $X_0X_3-X_1X_2$, with $B(X,X)=N(X)$. For each $[u]=[\alpha:\beta]\in\mathbb{P}^1$ the two-dimensional subspace
$$
W_{[u]}=\operatorname{span}\{(\alpha,0,\beta,0),\,(0,\alpha,0,\beta)\}=\{(\alpha\sigma,\alpha\tau,\beta\sigma,\beta\tau):\sigma,\tau\in\mathbb{C}\}
$$
is totally isotropic: for $X$ built from $\sigma,\tau$ and $Y$ from $\sigma',\tau'$ the form above gives $B(X,Y)=\tfrac12\alpha\beta(\sigma\tau'+\tau\sigma'-\tau\sigma'-\sigma\tau')=0$. Since $\dim W_{[u]}=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, $W_{[u]}$ is a **null plane**, and the same holds for
$$
W^{[v]}=\operatorname{span}\{(\gamma,\delta,0,0),\,(0,0,\gamma,\delta)\},\qquad [v]=[\gamma:\delta].
$$
Their projectivisations $\ell_{[u]}=\mathbb{P}(W_{[u]})$ and $m_{[v]}=\mathbb{P}(W^{[v]})$ are the **two rulings**: each family is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point, the point $[(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)]$ that the pair $([u],[v])$ determines.


## The projective null quadric $Q^2$

The projectivised null cone
$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:N(\tilde{Q})=0\}
$$
is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of $B$ gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*: empty for the definite form on $\mathbb{H}_{\mathbb{B}}$; the sphere $S^2$ for the Lorentzian form on $\mathbb{M}_+$ (or $\mathbb{M}_-$); the torus $S^1\times S^1$ for the split form of signature $(2,2)$. Only in the split case does the real quadric contain real lines.

## Lines in $\mathbb{P}^3$, the Klein quadric, and the Plücker embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $x,y$ of $U$, the **Plücker coordinates** are the six minors
$$
p_{ij}=x_iy_j-x_jy_i,\qquad 0\le i < j\le3,
$$
the coordinates of the decomposable bivector $x\wedge y\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plücker embedding**
$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$
whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plücker relation
$$
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0 .
$$
Over $\mathbb{R}$ the Plücker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plücker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plücker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## Tangency and polarity

The form $B$ defines a **polarity**, the correlation
$$
[\tilde{P}]\longmapsto[\tilde{P}]^{\perp}=\{[\tilde{Q}]:B(\tilde{P},\tilde{Q})=0\},
$$
well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde{P}]\in Q^2\iff B(\tilde{P},\tilde{P})=0$. For $[\tilde{P}]\in Q^2$, since the differential of $N$ at $\tilde{P}$ is $2B(\tilde{P},\cdot\,)$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde{P}]$,
$$
Q^2\cap[\tilde{P}]^{\perp}=\ell_{[u]}\cup m_{[v]},
$$
one line from each family. For two distinct null points $[\tilde{P}],[\tilde{Q}]$, the biquaternion norm on the line $\tilde{P}+t\tilde{Q}$ is $2t\,B(\tilde{P},\tilde{Q})$, so
$$
[\tilde{P}][\tilde{Q}]\subset Q^2\iff B(\tilde{P},\tilde{Q})=0,
$$
in which case the two points lie on a common ruling line. A line through $[\tilde{P}]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde{P}]$.


## Automorphisms of the complex quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of $N$:
$$
\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\},
$$
acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. Its identity component $PSO_4(\mathbb{C})$ preserves each ruling; the outer component swaps them.


## The link of the null cone

The **link** of the null cone is

$$
L=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0,\ \|\tilde{Q}\|_E=1\}=\mathcal{N}\cap S^7_E.
$$

Every nonzero null element is uniquely $t\,u$ with $t=\|\tilde{Q}\|_E>0$ and $u\in L$, so $\mathcal{N}$ is the cone on $L$ and is contractible (§*The null cone*). Since $\dim_{\mathbb{R}}\mathcal{N}=6$, the link has real dimension $5$. Under $M=uv^{T}$ with $\|u\|=\|v\|=1$,

$$
L\cong(S^3\times S^3)/U(1),
$$

where $U(1)=S^1$ acts by $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$, the relation under which $uv^{T}$ is unchanged. Here $Q^2=\mathbb{P}(\mathcal{N})\cong\mathbb{P}^1\times\mathbb{P}^1$ is the projectivised null cone, the Segre quadric of §*The Segre embedding* and §*The two rulings of null planes*. The Hopf maps combine to a bundle projection

$$
q:L\to Q^2\cong S^2\times S^2,\qquad[(u,v)]\mapsto([u],[v]),
$$

whose fibre over $([u],[v])$ is the circle of pairs $(e^{i\theta}u_0,e^{-i\theta}v_0)$. Hence $L$ is a closed connected $5$-manifold that is an $S^1$-bundle over $S^2\times S^2$.

The map $S^3\times S^3\to L$ is a principal $S^1$-bundle, and its long exact homotopy sequence, with $\pi_1(S^3\times S^3)=\pi_2(S^3\times S^3)=0$, gives

$$
\pi_1(L)=0,\qquad \pi_2(L)\cong\pi_1(S^1)=\mathbb{Z}.
$$

So $L$ is simply connected but not homeomorphic to $S^5$, whose $\pi_2$ vanishes: the null cone is genuinely non-manifold at its apex.

## Pure biquaternions and reality conditions

A biquaternion is **pure** if its complex scalar part vanishes,

$$
P=\{\tilde{Q}\in\mathbb{B}:Q_0=0\}=\{Q_1e_1+Q_2e_2+Q_3e_3:Q_k\in\mathbb{C}\}\cong\mathbb{C}^3,
$$

a contractible real six-dimensional subspace; its topology is trivial, and the interesting sets are the real forms cut out by a reality condition.

Complex conjugation splits $P$ into two real three-dimensional subspaces. The real condition $\bar{\tilde{Q}}=\tilde{Q}$ gives the **pure real quaternions**

$$
P\cap\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}\cong\mathbb{R}^3,
$$

whose unit sphere consists of the unit imaginary quaternions $\mu$ with $\mu^2=-e_0$, the family of **real roots of $-1$** classified in *Biquaternion Square Roots of Minus One, Zero and Plus One*. The imaginary condition $\bar{\tilde{Q}}=-\tilde{Q}$ gives

$$
P\cap i\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}\cong\mathbb{R}^3,
$$

Each is a copy of $\mathbb{R}^3$; for the first the unit sphere is

$$
S^2=\{\mu\in\mathbb{H}_{\mathbb{B}}:\mu^2=-e_0\},
$$

compact, connected and simply connected, with $\pi_2(S^2)\cong\mathbb{Z}$, and not a group, since only $S^0,S^1,S^3$ are groups. It is a homogeneous space of the unit quaternions and the base of the Hopf fibration $S^3\to S^2$; the sphere of roots of $+1$ is its image under multiplication by $i$, homeomorphic to it.

Finally, on either pure reality slice the restricted norm is definite, being $q_1^2+q_2^2+q_3^2$ on $P\cap\mathbb{H}_{\mathbb{B}}$ and $-((q'_1)^2+(q'_2)^2+(q'_3)^2)$ on $P\cap i\mathbb{H}_{\mathbb{B}}$. Hence $N(\tilde{Q})=0$ forces $\tilde{Q}=0$: the only null element of either pure reality slice is the origin, so the light cone meets these three-dimensional spaces only at its apex, unlike the Minkowski slices $\mathbb{M}_\pm$, whose null set is the three-dimensional light cone (*Biquaternion Lorentzian and Conformal Geometry*, §*The Lorentzian Slice and Its Light Cone*).

## Summary

- $\mathbb{B}\cong\mathbb{R}^8$ with the Euclidean topology is contractible, hence path-connected and simply connected with $\pi_n(\mathbb{B})=0$ for all $n\geq1$; the Euclidean structure itself, the six distinguished real subspaces and the Euclidean sphere are *The Euclidean Topology of the Biquaternion Algebra*, §*The Contractibility of the Algebra* and §*The Euclidean Unit Sphere*.
- The Euclidean unit sphere $S^7_E$ is a closed, compact, connected $7$-manifold but not a group: $\|\cdot\|_E$ is not multiplicative and $S^7_E\not\subseteq\mathbb{B}^\times$. Its Hermitian topology is *The Euclidean Topology of the Biquaternion Algebra*; the level set that is a group, $N=1$, is the norm-one group treated in *The Biquaternion Unit Group as a Topological Group*.
- The null cone $\mathcal{N}=\{N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z}$ is a closed real algebraic cone of real dimension $6$, irreducible, with the origin as its only singular point; it is a manifold away from the apex and non-manifold at the apex, and contractible, being the cone on its link; punctured, it is exactly the zero-divisor set.
- The link $L=\mathcal{N}\cap S^7_E$ is a closed connected $5$-manifold, an $S^1$-bundle over $S^2\times S^2$, simply connected with $\pi_2(L)\cong\mathbb{Z}$. Since $\pi_2(S^5)=0$, the apex is genuinely singular.
- The projectivised null cone is the smooth quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, the Segre quadric; the null cone is the affine cone over it, and its two rulings are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$.
- In the coordinates of §*The Segre embedding* the norm is $X_0X_3-X_1X_2$ and the polar form is $B$; the quadric is the locus of self-polar points, and the polarity gives the tangency, with $Q^2\cap[\tilde{P}]^\perp=\ell_{[u]}\cup m_{[v]}$ at a point of the quadric.
- The quadric sits in the Plücker–Klein geometry of the lines of $\mathbb{P}^3$; its rulings are two conics on the Klein quadric. $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, while $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$, not the automorphism group of the complex quadric.
- The pure subspace $P\cong\mathbb{C}^3$ is contractible. In its real slice $P\cap\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^3$ the unit sphere is the sphere of real roots of $-1$, $S^2$, which is compact, connected and simply connected with $\pi_2(S^2)\cong\mathbb{Z}$ and is not a group.
- The restricted norm is definite on each pure real slice, so the light cone of the Minkowski slices meets those slices only at the apex.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} \cong \mathbb{R}^8$ | Biquaternion algebra as a real topological space; contractible |
| $\|\tilde{Q}\|_E = \big(\sum_{\mu=0}^{3} \|Q_\mu\|^2\big)^{1/2}$ | Euclidean norm; makes $\mathbb{B}$ a topological algebra |
| $S^7_E = \{\|\tilde{Q}\|_E = 1\}$ | Euclidean unit sphere; a $7$-manifold, not a group |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\mathcal{N} = \{N(\tilde{Q}) = 0\}$ | Null cone; closed, real dimension $6$, contractible, singular at $0$ |
| $\mathcal{Z}$ | Zero-divisor set; $\mathcal{N} = \{0\} \cup \mathcal{Z}$ |
| $L = \mathcal{N} \cap S^7_E$ | Link of the null cone; $S^1$-bundle over $S^2 \times S^2$, $\pi_1 = 0$, $\pi_2 \cong \mathbb{Z}$ |
| $Q^2 = \mathbb{P}(\mathcal{N}) \cong \mathbb{P}^1 \times \mathbb{P}^1$ | Projectivised null cone, the Segre quadric |
| $B(\tilde{P},\tilde{Q}) = \sum_\mu P_\mu Q_\mu$ | Polar form of $N$, the complex bilinear dot product; $B(e_\mu,e_\nu) = \delta_{\mu\nu}$ |
| $X_0,\dots,X_3$ | Linear coordinates on $\mathbb{B}$ in which $N = X_0X_3 - X_1X_2$; see §*The Segre embedding* |
| $s : \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ | Segre embedding, $([u],[v]) \mapsto [\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$; its image is $Q^2$ |
| $[u] = [\alpha:\beta]$, $[v] = [\gamma:\delta]$ | The two factors of a null point, determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$; the lines through $[\tilde{P}] \in Q^2$ |
| $p_{ij} = x_i y_j - x_j y_i$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |
| $P = \{Q_0 = 0\} \cong \mathbb{C}^3$ | Pure biquaternions; contractible |
| $S^2 = \{\mu \in \mathbb{H}_{\mathbb{B}} : \mu^2 = -e_0\}$ | Sphere of real roots of $-1$ |
| $\mathbb{B}^\times$ | Group of units; its topology is in *The Biquaternion Unit Group as a Topological Group* |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015).
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
