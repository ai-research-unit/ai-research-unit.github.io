# __Biquaternion Topology__


This article collects the topology of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as a space: its contractibility, the Euclidean unit sphere, the null cone, and the link of the null cone. It uses the algebra and fixed-point subspaces of *Biquaternion Algebra*, the norm form $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ and invertibility criterion of *Biquaternion Norm and Invertibility*, the zero divisor set of *Biquaternion Zero Divisors*, the null cone and its rulings of *Biquaternion Null Quadric and Projective Geometry*, and *Lie Groups*. No physics is invoked and no new result is claimed.

**Scope.** The topology of the **group of units** $\mathbb{B}^\times$ — the polar decomposition, the retractions onto its compact subgroups, the homotopy groups and the universal cover — belongs to the Lie theory of the algebra and is treated in *Biquaternion Lie Algebra and Lie Group Structure*. This article owns the ambient space and its distinguished subsets, and takes from that article only the homotopy type of $\mathbb{B}^\times$ when a comparison is needed.

**Conventions.** The units are $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, the central scalar imaginary is $i$, and $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$. The norm form is $N(\tilde{Q})=\sum_\mu Q_\mu^2$ and the Euclidean norm is $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$.

The algebra itself has no interesting topology: as a real vector space it is $\mathbb{R}^8$, hence contractible. The two distinguished subsets studied here are the **Euclidean unit sphere** $S^7_E$ and the **null cone** $\{N(\tilde{Q})=0\}$, together with the link of the latter.

## The underlying space and its contractibility

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

So $\mathbb{M}_\pm$ carry no topology beyond that of $\mathbb{R}^4$; their Minkowski content comes from the restricted quadratic form (*Biquaternion Null Quadric and Projective Geometry*, §*Real forms and split signature* and §*The light cone in the Minkowski slices*), not from the topology.

## The Euclidean unit sphere

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

The level set that *is* a subgroup of $\mathbb{B}^\times$ is $N(\tilde{Q})=1$, not $\|\tilde{Q}\|_E=1$: the **norm-one group** $\mathbb{B}^\times_1$ is developed with the rest of the group structure in *Biquaternion Lie Algebra and Lie Group Structure*, §*The Group of Units*.

## The null cone

The **null cone**, or singular set, is

$$
\mathcal{N}=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z},
$$

where $\mathcal{Z}$ is the zero-divisor set.

It is closed, with empty interior, so $\mathbb{B}^\times$ is dense; it is a real algebraic cone with apex $0$, since $N$ is homogeneous of degree $2$; and its real dimension is $6$, as the complex hypersurface $N=0$ in $\mathbb{B}\cong\mathbb{C}^4$. Away from the origin its two real gradients are independent, so $\mathcal{N}\setminus\{0\}$ is a smooth real $6$-manifold; at the origin it is not a manifold (§*The link of the null cone*).

**Contractibility.** The homotopy $K(s,\tilde{Q})=(1-s)\tilde{Q}$ maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling a null element by a complex number preserves nullity, and contracts $\mathcal{N}$ to the apex. The null cone is thus homotopy trivial, like the algebra, but is a singular subset of it.

## The link of the null cone

The **link** of the null cone is

$$
L=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=0,\ \|\tilde{Q}\|_E=1\}=\mathcal{N}\cap S^7_E.
$$

Every nonzero null element is uniquely $t\,u$ with $t=\|\tilde{Q}\|_E>0$ and $u\in L$, so $\mathcal{N}$ is the cone on $L$ and is contractible (§*The null cone*). Since $\dim_{\mathbb{R}}\mathcal{N}=6$, the link has real dimension $5$. Under $M=uv^{T}$ with $\|u\|=\|v\|=1$,

$$
L\cong(S^3\times S^3)/U(1),
$$

where $U(1)=S^1$ acts by $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$, the relation under which $uv^{T}$ is unchanged. Here $Q=\mathbb{P}(\mathcal{N})\cong\mathbb{P}^1\times\mathbb{P}^1$ is the projectivised null cone, the smooth Segre quadric of *Biquaternion Null Quadric and Projective Geometry*, §*Rank-one description and the Segre embedding* and §*The two rulings of null planes*. The Hopf maps combine to a bundle projection

$$
q:L\to Q\cong S^2\times S^2,\qquad[(u,v)]\mapsto([u],[v]),
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

compact, connected and simply connected, with $\pi_2(S^2)\cong\mathbb{Z}$, and not a group, since only $S^0,S^1,S^3$ admit Lie group structures. It is a homogeneous space of the unit quaternions and the base of the Hopf fibration $S^3\to S^2$; the sphere of roots of $+1$ is its image under multiplication by $i$, homeomorphic to it.

Finally, on either pure reality slice the restricted norm form is definite, being $q_1^2+q_2^2+q_3^2$ on $P\cap\mathbb{H}_{\mathbb{B}}$ and $-(q'^2_1+q'^2_2+q'^2_3)$ on $P\cap i\mathbb{H}_{\mathbb{B}}$. Hence $N(\tilde{Q})=0$ forces $\tilde{Q}=0$: the only null element of either pure reality slice is the origin, so the light cone meets these three-dimensional spaces only at its apex, unlike the Minkowski slices $\mathbb{M}_\pm$, whose null set is the three-dimensional light cone (*Biquaternion Null Quadric and Projective Geometry*, §*The light cone in the Minkowski slices*).

## Summary

- $\mathbb{B}\cong\mathbb{R}^8$ with the Euclidean topology is contractible, hence path-connected and simply connected with $\pi_n(\mathbb{B})=0$ for all $n\geq1$; the six distinguished real subspaces are contractible as well, so they carry no topology beyond that of $\mathbb{R}^n$.
- The Euclidean unit sphere $S^7_E$ is a closed, compact, connected $7$-manifold but not a group: $\|\cdot\|_E$ is not multiplicative and $S^7_E\not\subseteq\mathbb{B}^\times$. The level set that is a group, $N=1$, is the norm-one group treated in *Biquaternion Lie Algebra and Lie Group Structure*.
- The null cone $\mathcal{N}=\{N(\tilde{Q})=0\}=\{0\}\cup\mathcal{Z}$ is a closed real algebraic cone of real dimension $6$, smooth away from the apex and non-manifold at the apex, and contractible: it is the cone on its link.
- The link $L=\mathcal{N}\cap S^7_E$ is a closed connected $5$-manifold, an $S^1$-bundle over $S^2\times S^2$, simply connected with $\pi_2(L)\cong\mathbb{Z}$. Since $\pi_2(S^5)=0$, the apex is genuinely singular.
- The pure subspace $P\cong\mathbb{C}^3$ is contractible. In its real slice $P\cap\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^3$ the unit sphere is the sphere of real roots of $-1$, $S^2$, which is compact, connected and simply connected with $\pi_2(S^2)\cong\mathbb{Z}$ and is not a group.
- The restricted norm form is definite on each pure real slice, so the light cone of the Minkowski slices meets those slices only at the apex.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} \cong \mathbb{R}^8$ | Biquaternion algebra as a real topological space; contractible |
| $\|\tilde{Q}\|_E = \big(\sum_{\mu=0}^{3} \|Q_\mu\|^2\big)^{1/2}$ | Euclidean norm; makes $\mathbb{B}$ a topological algebra |
| $S^7_E = \{\|\tilde{Q}\|_E = 1\}$ | Euclidean unit sphere; a $7$-manifold, not a group |
| $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ | Norm form |
| $\mathcal{N} = \{N(\tilde{Q}) = 0\}$ | Null cone; closed, real dimension $6$, contractible, singular at $0$ |
| $\mathcal{Z}$ | Zero-divisor set; $\mathcal{N} = \{0\} \cup \mathcal{Z}$ |
| $L = \mathcal{N} \cap S^7_E$ | Link of the null cone; $S^1$-bundle over $S^2 \times S^2$, $\pi_1 = 0$, $\pi_2 \cong \mathbb{Z}$ |
| $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$ | Projectivised null cone, the Segre quadric (*Biquaternion Null Quadric and Projective Geometry*) |
| $P = \{Q_0 = 0\} \cong \mathbb{C}^3$ | Pure biquaternions; contractible |
| $S^2 = \{\mu \in \mathbb{H}_{\mathbb{B}} : \mu^2 = -e_0\}$ | Sphere of real roots of $-1$ |
| $\mathbb{B}^\times$ | Group of units; its topology is in *Biquaternion Lie Algebra and Lie Group Structure* |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015).
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
