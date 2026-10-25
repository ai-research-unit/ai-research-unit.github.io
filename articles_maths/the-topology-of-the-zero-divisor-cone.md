# __The Topology of the Zero-Divisor Cone__

## Introduction

The biquaternion algebra is not a division algebra, and its zero divisors are not scattered through it: with the origin adjoined they form the **null cone** $\mathcal{N}=\{N=0\}$, a complex cone of real dimension six. This article reads the topology of that cone.

The cone is a closed subset of a contractible space, and it is itself a cone, so its own homotopy is trivial. The object that is not trivial is its **link** $L=\mathcal{N}\cap S^{7}_{E}$, the intersection with the Euclidean unit sphere. The link is a closed connected real $5$-manifold, and it is explicitly

$$
\boxed{\; L\cong S^{2}\times S^{3} \;}.
$$

That identification is the result of the article. It also proves that the apex is a genuine singular point: if $0$ were a manifold point of $\mathcal{N}$, its link would be a $5$-sphere, and $\pi_2(S^{2}\times S^{3})\cong\mathbb{Z}\neq0$.

Nothing below is read from the four forms as forms. The cone is selected by the failure of invertibility alone, and the only metric input is the Euclidean norm of the underlying real space (*Topology in the Space of Biquaternions*). The algebraic norm and its multiplicativity are *The Four Forms and the Four Algebraic Norms*; the zero-divisor criterion and the two strata are *Norm Regularity and Degeneracy in the Biquaternion Algebra*; the ambient Euclidean structure, the sphere and the contractibility of the algebra are *The Euclidean Topology of the Biquaternion Algebra*; and the complement, with its group structure, is *The Biquaternion Unit Group as a Topological Group*.

## The Null Cone and Its Link

**Definition (null cone, zero-divisor set).** With $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu}Q_\mu^{2}$,

$$
\mathcal{N}=\{\tilde Q\in\mathbb{B}:N(\tilde Q)=0\},\qquad
\mathcal Z=\mathcal{N}\setminus\{0\}.
$$

The set $\mathcal Z$ is the **zero-divisor set**; adding the apex gives the **null cone** $\mathcal{N}$.

**Proposition (quoted).** $\mathcal{N}$ is closed, of empty interior and of real dimension $6$; it is a complex cone; and $\mathbb{B}^{\times}=\mathbb{B}\setminus\mathcal{N}$ (*Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Group of Units*, §*The Zero Divisors*).

**Definition (link).** The **link** of the cone is

$$
L=\mathcal{N}\cap S^{7}_{E}.
$$

**Proposition (the cone is the cone on its link).** Every $\tilde Q\in\mathcal{N}\setminus\{0\}$ is uniquely $\tilde Q=t u$ with $t=\|\tilde Q\|_E>0$ and $u\in L$. Hence $\mathcal{N}$ is the cone on $L$, and it is contractible.

*Proof.* The norm is homogeneous, so $u=\tilde Q/\|\tilde Q\|_E$ lies in $L$ and $t=\|\tilde Q\|_E$; the pair is unique because the norm of $tu$ is $t$. The straight-line homotopy $H(s,\tilde Q)=(1-s)\tilde Q$ carries $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, fixes the apex and contracts the cone to it.

**Proposition (the punctured cone is smooth).** $0$ is the only singular point of $\mathcal{N}$; the punctured cone $\mathcal Z$ is a smooth complex $3$-manifold.

*Proof.* $N$ is a nondegenerate quadratic form in four variables, hence irreducible over $\mathbb{C}$, and its gradient $2(Q_t,Q_x,Q_y,Q_z)$ vanishes only at $0$. The singular locus of $\{N=0\}$ is therefore $\{0\}$, and the punctured cone is smooth of complex dimension $3$.

**Remark (the word singular).** The word *singular* is used in two senses. Geometrically, a singular point of $\mathcal{N}$ is a point where the hypersurface fails to be a manifold, and the apex is the only one. Algebraically, the cone is the set of non-units, and it is sometimes called the *singular cone* for that reason. The apex is both; every other point of the cone is a non-unit but a smooth point.

## The Link Is $S^{2}\times S^{3}$

**Lemma (spinor factorisation; quoted).** In the coordinates

$$
Z_0=Q_t-iQ_z,\qquad Z_1=-iQ_x-Q_y,\qquad Z_2=-iQ_x+Q_y,\qquad Z_3=Q_t+iQ_z,
$$

the norm is $N=Z_0Z_3-Z_1Z_2$ and $\lvert Z\rvert^{2}=2\|\tilde Q\|_E^{2}$. A nonzero null element is

$$
(Z_0,Z_1,Z_2,Z_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$

for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ in $\mathbb{C}^{2}$, and the pair $(u,v)$ is determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ with $\lambda\in\mathbb{C}^{\times}$ (*Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spinor Factorisation of a Null Element*).

**Theorem.** $L\cong S^{2}\times S^{3}$.

*Proof.* Normalise $\|u\|=\|v\|=1$. Then $\lvert Z\rvert^{2}=2(|\alpha|^{2}+|\beta|^{2})(|\gamma|^{2}+|\delta|^{2})=2$, so $\|\tilde Q\|_E=1$; define

$$
\varphi:S^{3}\times S^{3}\longrightarrow L,\qquad
\varphi(u,v)=\text{the element with }Z\text{-coordinates }\sqrt2\,(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta).
$$

The map lands in $L$, is surjective by the lemma and the normalisation, and $\varphi(u,v)=\varphi(u',v')$ exactly when $(u',v')=(\lambda u,\lambda^{-1}v)$ with $\lvert\lambda\rvert=1$. Hence $\varphi$ induces a homeomorphism

$$
L\cong (S^{3}\times S^{3})/S^{1},
$$

the circle acting freely by $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$.

Put $w=\bar v$. Since $\bar\lambda=\lambda^{-1}$ for $\lvert\lambda\rvert=1$, the action becomes the diagonal action $(u,w)\mapsto(\lambda u,\lambda w)$. For a compact group $G$ and a closed subgroup $H$, the map

$$
(G\times G)/H\longrightarrow G\times(G/H),\qquad [g_1,g_2]\longmapsto(g_2^{-1}g_1,[g_2]),
$$

is a homeomorphism: it is continuous and invariant, and its inverse sends $(p,[g_2])$ to the orbit of $(g_2p,g_2)$. With $G=S^{3}$ and $H=S^{1}$,

$$
L\cong S^{3}\times(S^{3}/S^{1})\cong S^{3}\times S^{2}.
$$

**Corollary (homotopy of the link).** $\pi_1(L)=0$, $\pi_2(L)\cong\mathbb{Z}$ and $\pi_3(L)\cong\mathbb{Z}\oplus\mathbb{Z}$; in particular $L$ is not homeomorphic to $S^{5}$.

**Corollary (the apex is genuinely singular).** The cone is not a topological manifold at its apex. If it were, its link would be a $5$-sphere; the link is $S^{2}\times S^{3}$, whose $\pi_2$ is $\mathbb{Z}$, and $\pi_2(S^{5})=0$.

**Remark (the two bundle readings).** The projection $[u,v]\mapsto([u],[v])$ makes $L$ a circle bundle over $\mathbb{P}^{1}\times\mathbb{P}^{1}\cong S^{2}\times S^{2}$, with the relative phase of $u$ and $v$ as fibre; the theorem exhibits the same manifold as $S^{2}\times S^{3}$. The first description is the projectivised cone, the second the product structure.

**Remark (the classical name).** The manifold $S^{2}\times S^{3}$ is the Stiefel manifold $V_{2}(\mathbb{R}^{4})$ of orthonormal $2$-frames in $\mathbb{R}^{4}$; since $S^{3}$ is parallelizable, it is the unit tangent bundle of $S^{3}$ (*Grassmannians and Stiefel Manifolds*).

## The Real Slices

**Definition (pure subspace and its real slices).** The **pure subspace** is

$$
P=\{\tilde Q\in\mathbb{B}:Q_t=0\}\cong\mathbb{C}^{3},
$$

with the two real $3$-planes

$$
P_+=P\cap\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad
P_-=P\cap i\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}.
$$

**Proposition (the cone meets a definite plane only at the apex).** $\mathcal{N}\cap P_+=\{0\}$ and $\mathcal{N}\cap P_-=\{0\}$.

*Proof.* On $P_+$ the norm is $q_x^{2}+q_y^{2}+q_z^{2}$, a sum of three squares; on $P_-$ it is $-\bigl((q'_x)^{2}+(q'_y)^{2}+(q'_z)^{2}\bigr)$, the negative of one. Each vanishes only at the origin.

**Remark (what the argument uses).** The planes $P_\pm$ are not subalgebras, and no multiplication is used: $\vec e_x^{2}=-e_t$ leaves $P_+$, and $(i\vec e_x)(i\vec e_y)=-\vec e_z$ leaves $P_-$. What the argument uses is that the norm is **definite** on each plane, positive on $P_+$ and negative on $P_-$; the cone is a complex phenomenon, and a real form that makes the norm definite removes it.

The two planes sit inside the **Lorentzian slices**

$$
\mathbb{M}_+=\{Q_t\in\mathbb{R},\ Q_x,Q_y,Q_z\in i\mathbb{R}\},\qquad
\mathbb{M}_-=\{Q_t\in i\mathbb{R},\ Q_x,Q_y,Q_z\in\mathbb{R}\},
$$

the Hermitian and anti-Hermitian subspaces of signatures $(1,3)$ and $(3,1)$ (*Remarkable Subspaces and the Four General Products, Forms and Norms*, §*The Four Algebraic Norms*). Thus $P_-\subset\mathbb{M}_+$ and $P_+\subset\mathbb{M}_-$: each Lorentzian slice contains a definite plane, and the cone meets that plane only at the apex; the rest of the slice carries a genuine null cone.

**Proposition (the Lorentzian link).** On $\mathbb{M}_+$ and $\mathbb{M}_-$ the cone cuts the three-dimensional null cone of the slice, whose link in $S^{7}_{E}$ is $S^{2}\sqcup S^{2}$, one sphere per nappe.

*Proof.* On $\mathbb{M}_+$ write $\tilde Q=a e_t+i\vec p$ with $a\in\mathbb{R}$ and $\vec p\in\mathbb{R}^{3}$. Then $N=a^{2}-\lvert\vec p\rvert^{2}$, so the null cone is $a=\pm\lvert\vec p\rvert$; intersecting it with the unit sphere $a^{2}+\lvert\vec p\rvert^{2}=1$ gives $a=\pm1/\sqrt2$ and $\lvert\vec p\rvert=1/\sqrt2$, that is two copies of $S^{2}$. The slice $\mathbb{M}_-$ is the image of $\mathbb{M}_+$ under multiplication by $i$, and the argument is the same.

**Proposition (the sphere of real roots of $-1$).** The unit sphere of $P_+$ is

$$
S^{2}=\{\mu\in P_+:\mu^{2}=-e_t\},
$$

the sphere of **real roots of $-1$**; it is compact, connected and simply connected, with $\pi_2(S^{2})\cong\mathbb{Z}$, and it is **not** a group. It is the homogeneous space $Sp(1)/\mathrm{U}(1)$ and the base of the Hopf fibration $S^{3}\to S^{2}$ (*Quaternion Geometry*, §*The Hopf Fibration*). Multiplication by $i$ carries it to the unit sphere of $P_-$, the sphere of roots of $+1$ in that slice (*Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Roots of Minus One*).

*Proof.* A real root of $-1$ in $P_+$ is $\mu=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with $\mu^{2}=-(q_x^{2}+q_y^{2}+q_z^{2})e_t$, so the condition is $q_x^{2}+q_y^{2}+q_z^{2}=1$: the unit sphere of $P_+$, which is the ordinary $2$-sphere. The identification with $Sp(1)/\mathrm{U}(1)$ and the Hopf fibration are those of *Quaternion Geometry*. If $\mu\in P_+$ is a root of $-1$, then $(i\mu)^{2}=i^{2}\mu^{2}=e_t$, and conversely every root of $+1$ in $P_-$ is $i\mu$ for such a $\mu$.

## Summary

- The **null cone** $\mathcal{N}=\{N=0\}$ is closed, of empty interior, of real dimension $6$, and its complement is the group of units $\mathbb{B}^{\times}$; the **zero-divisor set** is $\mathcal Z=\mathcal{N}\setminus\{0\}$.
- The apex is the only singular point of $\mathcal{N}$; the punctured cone $\mathcal Z$ is a smooth complex $3$-manifold.
- $\mathcal{N}$ is the cone on its **link** $L=\mathcal{N}\cap S^{7}_{E}$, hence contractible; the interesting topology is that of $L$.
- The link is $L\cong S^{2}\times S^{3}\cong V_{2}(\mathbb{R}^{4})$, a closed connected $5$-manifold with $\pi_1=0$, $\pi_2\cong\mathbb{Z}$ and $\pi_3\cong\mathbb{Z}\oplus\mathbb{Z}$; it is not $S^{5}$, so the apex is genuinely singular.
- The cone meets the definite planes $P_+$ and $P_-$ of the pure subspace only at the apex, while on the Lorentzian slices $\mathbb{M}_\pm$ it cuts a three-dimensional null cone with link $S^{2}\sqcup S^{2}$. The unit sphere of $P_+$ is the sphere of real roots of $-1$, $S^{2}$, the base of the Hopf fibration.

## Summary of Notation

One rule governs the letters: $\mathcal{N}$ is the null cone, and no other cone uses it. The positive cone of the reduced algebra is $\mathcal C_{+}$, the Krein cone is $\mathcal K$, and the second quadratic cone of the spectral analysis, the zero set of $B^{2}$, is $\mathcal S$.

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\cong\mathbb{R}^{8}$ | Biquaternion algebra as a real space; contractible |
| $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$ | Euclidean norm; defines the topology and the unit sphere |
| $S^{7}_{E}=\{\lVert\tilde Q\rVert_E=1\}$ | Euclidean unit sphere |
| $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | Algebraic norm; its null set is $\mathcal{N}$ |
| $\mathcal{N}=\{N=0\}$ | Null cone; closed, real dimension $6$, contractible |
| $\mathcal Z=\mathcal{N}\setminus\{0\}$ | Zero-divisor set; smooth complex $3$-manifold |
| $L=\mathcal{N}\cap S^{7}_{E}$ | Link of the cone; $L\cong S^{2}\times S^{3}\cong V_{2}(\mathbb{R}^{4})$ |
| $\pi_1(L)=0$, $\pi_2(L)\cong\mathbb{Z}$, $\pi_3(L)\cong\mathbb{Z}\oplus\mathbb{Z}$ | Homotopy of the link |
| $\mathbb{P}(\mathcal{N})\cong S^{2}\times S^{2}$ | Projectivised cone |
| $P=\{Q_t=0\}\cong\mathbb{C}^{3}$ | Pure subspace |
| $P_+$, $P_-$ | The definite $3$-planes in $P$; unit spheres $S^{2}$ each |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Lorentzian slices, signatures $(1,3)$ and $(3,1)$; links $S^{2}\sqcup S^{2}$ |
| $\mathbb{B}^{\times}$ | Group of units; complement of $\mathcal{N}$ |

## Further Reading

- [Topology in the Space of Biquaternions](topology-in-the-space-of-biquaternions.html), for the topology and the norm used here
- [The Euclidean Topology of the Biquaternion Algebra](the-euclidean-topology-of-the-biquaternion-algebra.html), for the ambient Euclidean structure and the contractibility of the algebra
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the algebraic norm and its multiplicativity
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion, the strata and the spinor factorisation
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the complement of the cone and its group structure
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the signatures of the Lorentzian slices
- [Quaternion Geometry](quaternion-geometry.html), for the Hopf fibration and the homogeneous sphere $S^{2}$
- [Grassmannians and Stiefel Manifolds](grassmannians-and-stiefel-manifolds.html), for $V_{2}(\mathbb{R}^{4})$ and the unit tangent bundle of $S^{3}$
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the roots of $-1$ and $+1$
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
- Glen E. Bredon, *Topology and Geometry* (Graduate Texts in Mathematics 139, Springer, 1993), for the link of a cone.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401--416.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381--395.
