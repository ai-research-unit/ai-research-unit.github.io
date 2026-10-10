# __The Topology of the Zero-Divisor Cone__

## Introduction

The biquaternion algebra is not a division algebra, and its zero divisors are not scattered through it: they form a cone. This article is the topology of that cone. Nothing below is read from the four forms. The cone is the **singular set** of the algebra, singled out by the failure of invertibility alone, and the only metric input is the topological norm

$$
\|\tilde Q\|_E=\Bigl(\sum_{\mu=0}^{3}|Q_\mu|^{2}\Bigr)^{1/2}
$$

of the underlying real space $\mathbb{B}\cong\mathbb{R}^8$ (*Topology in the Space of Biquaternions*). That norm is one of the equivalent norms of that space; any equivalent norm gives the same topology, the same singular set and the same link, and it is the only metric input of the article.

That the singular set is also the null set $\{\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}$ of the algebraic norm is a computational convenience and nothing more. The equation describes the cone; it does not equip the space with its topology, which is fixed by the linear structure alone. The algebraic norm itself — its multiplicativity, its real forms and its polarisations — belongs to *Biquaternion Norm and Invertibility*, and the zero-divisor set in its own right to *Zero Divisors of the General Plain Algebra*. The space with its unique topology is *Topology in the Space of Biquaternions*; the ambient Euclidean structure, the topological unit sphere and the contractibility of the algebra are *The Euclidean Topology of the Biquaternion Algebra*; the complement of the cone, with its group structure and its own topology, is *The Biquaternion Unit Group as a Topological Group*; and the projective geometry of the complex lines the cone contains — the quadric surface, its two rulings and its polarity — is *The Null Quadric and Its Projective Geometry*.

**Scope.** The article owns the singular set as a closed algebraic cone, its smooth structure away from its apex, its contractibility, its link with the topological unit sphere, and the homotopy invariants of that link, together with the sphere of real roots of $-1$ that the pure real slice carries. The ambient Euclidean structure and the unit sphere are quoted from *The Euclidean Topology of the Biquaternion Algebra* rather than re-derived; the two facts about the cone that are read from that sphere are proved here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, and central imaginary unit $i$ with $i^{2}=-1$; the natural conjugation ${}^{\natural}$ negates $e_1,e_2,e_3$ and fixes $e_0$ and $i$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, and the topological norm is $\|\tilde Q\|_E=(\sum_\mu|Q_\mu|^{2})^{1/2}$.

## The Singular Set

**Definition (the singular set).** An element is **singular** if it is nonzero and not invertible. A **zero divisor** is a nonzero $\tilde Q$ for which there is a nonzero $\tilde R$ with $\tilde Q\tilde R=0$ or $\tilde R\tilde Q=0$. For the biquaternion algebra the two notions coincide (*Zero Divisors of the General Plain Algebra*): a nonzero element is singular exactly when it is a zero divisor. The **singular set** of the algebra is

$$
\mathcal{N}=\mathcal{Z}\cup\{0\},\qquad \mathcal{Z}=\{\tilde Q\in\mathbb{B}:\tilde Q\neq0\text{ and }\tilde Q\text{ is not invertible}\},
$$

and $\mathcal{Z}$ is the **zero-divisor cone**. The group of units is its complement, $\mathbb{B}^\times=\mathbb{B}\setminus\mathcal{N}$ (*The Biquaternion Unit Group as a Topological Group*).

The two descriptions agree with the null set of the algebraic norm.

**Proposition (the singular set is the null set; quoted).** $\mathcal{N}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}$, with $\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu=0}^{3}Q_\mu^{2}$; so $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ (*The Four Pairings of the Biquaternion Algebra*, §*The Algebraic Norm*; *Zero Divisors of the General Plain Algebra*). $\square$

**Proposition (elementary properties).** With the Euclidean topology of the ambient space:

1. $\mathcal{N}$ is **closed**, and $\mathcal{Z}$ is neither open nor closed.
2. $\mathcal{N}$ has **empty interior**; consequently $\mathbb{B}^\times$ is open and dense in $\mathbb{B}$.
3. $\mathcal{N}$ is a **real algebraic cone** with apex $0$: if $\tilde Q\in\mathcal{N}$ then $\lambda\tilde Q\in\mathcal{N}$ for every $\lambda\in\mathbb{C}$.
4. $\mathcal{N}$ has real **dimension $6$**.

*Proof.* (2) $\mathcal{N}$ is the zero set of the nonzero polynomial $\langle\tilde Q,\tilde Q\rangle_{\natural}$ on $\mathbb{C}^4$, so it is a complex hypersurface and has empty interior; the units, its complement, are therefore dense. (1) $\mathbb{B}^\times$ is the preimage of $\mathbb{C}\setminus\{0\}$ under the continuous map $\tilde Q\mapsto\tilde Q\tilde Q^{\natural}$, hence open, so $\mathcal{N}$ is closed. The cone $\mathcal{Z}$ fails to be closed, because the apex lies in its closure but not in it; and it fails to be open, because it is a nonempty subset of $\mathcal{N}$, which has empty interior. (3) $\langle\lambda\tilde Q,\lambda\tilde Q\rangle_{\natural}=\lambda^{2}\langle\tilde Q,\tilde Q\rangle_{\natural}$ by bilinearity, so $\lambda$ carries the null set into itself. (4) The zero set of one polynomial equation in $\mathbb{C}^4$ has complex dimension $3$, hence real dimension $6$. $\square$

## The Cone Is Smooth Away from Its Apex

The apex is the only singular point of the cone, and away from it the cone is a manifold.

**Proposition (regularity).** The algebraic norm $\langle\tilde Q,\tilde Q\rangle_{\natural}$ is irreducible over $\mathbb{C}$, and its complex gradient

$$
\bigl(2Q_0,2Q_1,2Q_2,2Q_3\bigr)
$$

vanishes only at $\tilde Q=0$. Hence $0$ is the only singular point of $\mathcal{N}$, and the punctured cone

$$
\mathcal{Z}=\mathcal{N}\setminus\{0\}
$$

is a smooth complex $3$-manifold, of real dimension $6$. $\square$

The complex structure of the punctured cone is induced from the ambient $\mathbb{C}^4$ and is analytic; it is read in the analysis of the algebra, which is where the local theory of functions on that manifold is developed.

**Remark (the apex is genuinely singular).** That the apex is not a manifold point is not a defect of the equation: it is a topological fact about the cone, proved by the homotopy invariants of its link in §*The Link of the Cone*. The link of a manifold point is a sphere; the link computed below is not one.

## The Contractibility of the Cone

The cone is homotopy trivial, like the algebra that surrounds it.

**Proposition (contractibility).** $\mathcal{N}$ is contractible, being the cone on its link.

*Proof.* The straight-line homotopy

$$
K(s,\tilde Q)=(1-s)\tilde Q,\qquad (s,\tilde Q)\in[0,1]\times\mathcal{N},
$$

maps $[0,1]\times\mathcal{N}$ into $\mathcal{N}$, since scaling by a complex number preserves the equation $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$, and it contracts $\mathcal{N}$ to the apex. It is continuous, fixes the apex at every $s$, and carries every element to $0$ at $s=1$. $\square$

The same homotopy contracts the ambient space $\mathbb{B}$, which is why the cone is homotopy trivial "as well"; but the two statements are different. The ambient contractibility is a statement about $\mathbb{B}$, and it is *The Euclidean Topology of the Biquaternion Algebra*; the contractibility of $\mathcal{N}$ is a statement about a singular subset of $\mathbb{B}$, and it is proved here.

## The Link of the Cone

**Definition (the link).** The **link** of the cone is its intersection with the topological unit sphere $S^7_E=\{\tilde Q:\|\tilde Q\|_E=1\}$,

$$
L=\mathcal{N}\cap S^7_E=\mathcal{Z}\cap S^7_E.
$$

Every nonzero element of $\mathcal{N}$ is uniquely $t\,u$ with $t=\|\tilde Q\|_E>0$ and $u\in L$, so $\mathcal{N}$ is the cone on $L$ and the link determines the cone.

**Proposition (the link is a $5$-manifold).** $L$ is a closed connected real $5$-manifold, and it is an $S^1$-bundle over the space of complex lines contained in the cone.

*Proof.* In the linear coordinates

$$
Z_0=Q_0-iQ_3,\quad Z_1=-iQ_1-Q_2,\quad Z_2=-iQ_1+Q_2,\quad Z_3=Q_0+iQ_3
$$

the algebraic norm is $Z_0Z_3-Z_1Z_2$, and the two norms are related by the identity $|Z|^{2}=2\|\tilde Q\|_E^{2}$, since $|Z_0|^{2}+|Z_3|^{2}=2(|Q_0|^{2}+|Q_3|^{2})$ and $|Z_1|^{2}+|Z_2|^{2}=2(|Q_1|^{2}+|Q_2|^{2})$. A non-zero null element is exactly

$$
(Z_0,Z_1,Z_2,Z_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$

for a pair of non-zero vectors $u=(\alpha,\beta)$, $v=(\gamma,\delta)$ of $\mathbb{C}^2$, determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ (*The Null Quadric and Its Projective Geometry*). Normalise $\|u\|=\|v\|=1$; then

$$
|Z|^{2}=(|\alpha|^{2}+|\beta|^{2})(|\gamma|^{2}+|\delta|^{2})=1,
$$

so $\|\tilde Q\|_E=1/\sqrt2$. Define

$$
\varphi:S^3\times S^3\longrightarrow\mathbb{B},\qquad u,v\longmapsto\text{the element with }Z\text{-coordinates }\sqrt2\,(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta).
$$

For $\|u\|=\|v\|=1$ this element is null with $|Z|^{2}=2$, hence $\|\tilde Q\|_E=1$: so $\varphi$ lands in $L$. It is surjective, by the parametrisation together with the normalisation, and $\varphi(u,v)=\varphi(u',v')$ holds exactly when $(u',v')=(\lambda u,\lambda^{-1}v)$ with $|\lambda|=1$. The circle acts freely on $S^3\times S^3$ by $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$, so $\varphi$ induces a continuous bijection from the compact quotient $(S^3\times S^3)/S^1$ onto the Hausdorff space $L$, hence a homeomorphism. Therefore $L$ is a closed connected real $5$-manifold. Finally the map

$$
q:L\longrightarrow\mathbb{P}(\mathcal{N}),\qquad \varphi(u,v)\longmapsto([u],[v]),
$$

is well defined and is a fibre bundle whose fibre over $([u],[v])$ is the circle of pairs $(e^{i\theta}u_0,e^{-i\theta}v_0)$; the base is the projectivised cone $\mathbb{P}(\mathcal{N})$, a copy of $\mathbb{P}^1\times\mathbb{P}^1\cong S^2\times S^2$ whose geometry — the Segre quadric, its rulings and its polarity — is *The Null Quadric and Its Projective Geometry*. $\square$

**Proposition (homotopy invariants of the link).** The quotient map $S^3\times S^3\to L$ is a principal $S^1$-bundle, and its long exact homotopy sequence, with $\pi_1(S^3\times S^3)=\pi_2(S^3\times S^3)=0$, gives

$$
\pi_1(L)=0,\qquad \pi_2(L)\cong\pi_1(S^1)=\mathbb{Z}.
$$

Hence $L$ is simply connected but is **not** homeomorphic to $S^5$, whose $\pi_2$ vanishes. $\square$

**Corollary (the apex is a genuine singularity).** The cone is not a topological manifold at its apex. If it were, the link of the apex would be a sphere; the link computed above has $\pi_2\cong\mathbb{Z}$, and no sphere has that homotopy group in degree $2$. $\square$

## The Pure Slices and the Sphere of Real Roots of $-1$

A biquaternion is **pure** if its complex scalar part vanishes,

$$
P=\{\tilde Q\in\mathbb{B}:Q_0=0\}=\{Q_1e_1+Q_2e_2+Q_3e_3:Q_k\in\mathbb{C}\}\cong\mathbb{C}^3,
$$

a contractible real six-dimensional subspace of the algebra.

Complex conjugation splits $P$ into two real three-dimensional subspaces. The real condition $\bar{\tilde Q}=\tilde Q$ gives the **pure real quaternions**

$$
P\cap\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}\cong\mathbb{R}^3,
$$

and the imaginary condition $\bar{\tilde Q}=-\tilde Q$ gives

$$
P\cap i\mathbb{H}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}\cong\mathbb{R}^3.
$$

Both slices are closed, and both are subspaces of real dimension three inside the eight-dimensional algebra.

**Proposition (the cone meets a pure slice only at the apex).** $\mathcal{N}\cap(P\cap\mathbb{H}_{\mathbb{B}})=\{0\}$ and $\mathcal{N}\cap(P\cap i\mathbb{H}_{\mathbb{B}})=\{0\}$.

*Proof.* Write an element of the first slice as $\tilde Q=q_1e_1+q_2e_2+q_3e_3$ with $q_k\in\mathbb{R}$. Its algebraic norm is

$$
\langle\tilde Q,\tilde Q\rangle_{\natural}=q_1^{2}+q_2^{2}+q_3^{2},
$$

a sum of three squares, which vanishes only at $\tilde Q=0$; so $\mathcal{N}$ meets the first slice only at the apex. Write an element of the second slice as $\tilde Q=i(q'_1e_1+q'_2e_2+q'_3e_3)$, again with $q'_k\in\mathbb{R}$. Its algebraic norm is

$$
\langle\tilde Q,\tilde Q\rangle_{\natural}=-\bigl((q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}\bigr),
$$

the negative of a sum of three squares, which likewise vanishes only at $\tilde Q=0$. $\square$

**Remark (what the argument does and does not use).** The two slices are **not** subalgebras, and no multiplication property is invoked above. Neither is closed under multiplication: $e_1^{2}=-e_0$ leaves the first slice, and $(ie_1)(ie_2)=-e_3$ leaves the second. What makes each slice meet the cone only at the apex is that the algebraic norm restricted to it is **definite** — positive on the first slice, negative on the second.

**Proposition (the sphere of real roots of $-1$).** The unit sphere of the slice $P\cap\mathbb{H}_{\mathbb{B}}$ is

$$
S^2=\{\mu\in\mathbb{H}_{\mathbb{B}}:\mu^{2}=-e_0\},
$$

the sphere of **real roots of $-1$**; it is compact, connected and simply connected, with $\pi_2(S^2)\cong\mathbb{Z}$, and it is **not** a group. It is a homogeneous space of the unit quaternions and the base of the Hopf fibration $S^3\to S^2$; the sphere of roots of $+1$ in the slice $i\mathbb{H}_{\mathbb{B}}$ is its image under multiplication by the central unit $i$ and is homeomorphic to it.

*Proof.* A real root of $-1$ in the slice is an element $\mu=q_1e_1+q_2e_2+q_3e_3$ with $q_k\in\mathbb{R}$ and $\mu^{2}=-e_0$. Since

$$
\mu^{2}=-\bigl(q_1^{2}+q_2^{2}+q_3^{2}\bigr)e_0,
$$

the condition is $q_1^{2}+q_2^{2}+q_3^{2}=1$: the real roots of $-1$ are exactly the unit vectors of the three-dimensional slice, so the set is the ordinary $2$-sphere. Its cell structure gives compactness, connectedness and simple connectedness, and $\pi_2(S^2)\cong\mathbb{Z}$ is standard; conjugation by the unit quaternions acts transitively on it, so it is the homogeneous space $Sp(1)/U(1)$ and the base of the Hopf fibration $S^{3}\to S^{2}$. It is not a group, since the only spheres that carry a continuous group structure are $S^0$, $S^1$ and $S^3$. For the roots of $+1$: if $\mu$ is a root of $-1$ in the slice then $(i\mu)^{2}=i^{2}\mu^{2}=e_0$, and conversely every root of $+1$ in $i\mathbb{H}_{\mathbb{B}}$ is of this form, so the two spheres correspond under multiplication by $i$ and are homeomorphic. The classifications of the roots of $-1$, $0$ and $+1$ are *Biquaternion Square Roots of Minus One, Zero and Plus One*. $\square$

The three-dimensional spaces above are the pure real slices. The Minkowski slices $\mathbb{M}_\pm$ behave differently: their null set is the three-dimensional light cone, treated in the Lorentzian reading of the real slices (*Biquaternion Lorentzian and Conformal Geometry*, §*The Lorentzian Slice and Its Light Cone*). The point of the contrast is that the cone of the algebra meets the pure slices only at its apex while it cuts the Minkowski slices in a genuine three-dimensional cone.

## Summary

- The **singular set** $\mathcal{N}=\mathcal{Z}\cup\{0\}$ of the algebra is the set of non-units together with the origin; it coincides with the null set of the algebraic norm, quoted from *The Four Pairings of the Biquaternion Algebra*. It is closed, of empty interior, a real algebraic cone with apex $0$ and real dimension $6$; the group of units is its open and dense complement.
- The cone is **smooth away from its apex**: the algebraic norm is irreducible with gradient vanishing only at the origin, so $0$ is the only singular point and the punctured cone $\mathcal{Z}$ is a smooth complex $3$-manifold.
- The cone is **contractible**, contracted to the apex by $\tilde Q\mapsto(1-s)\tilde Q$; the ambient contractibility of $\mathbb{B}$ is a separate statement, owned by *The Euclidean Topology of the Biquaternion Algebra*.
- The **link** $L=\mathcal{N}\cap S^7_E$ is a closed connected real $5$-manifold, an $S^1$-bundle over the projectivised cone $S^2\times S^2$; it is simply connected with $\pi_2(L)\cong\mathbb{Z}$, and it is not $S^5$, so the apex is genuinely singular.
- The **pure subspace** $P\cong\mathbb{C}^3$ is contractible. Its two real slices $P\cap\mathbb{H}_{\mathbb{B}}$ and $P\cap i\mathbb{H}_{\mathbb{B}}$ are three-dimensional subspaces, and are **not** subalgebras; the algebraic norm is definite on each — positive on the first and negative on the second — so the cone meets each of them only at the apex. The unit sphere of the first is the sphere of real roots of $-1$, $S^2$, compact, connected and simply connected with $\pi_2(S^2)\cong\mathbb{Z}$, and not a group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} \cong \mathbb{R}^8$ | Biquaternion algebra as a real topological space; contractible |
| $\|\tilde Q\|_E = \big(\sum_{\mu=0}^{3} \lvert Q_\mu\rvert^2\big)^{1/2}$ | Topological norm of the underlying real space; makes $\mathbb{B}$ a topological algebra |
| $S^7_E = \{\|\tilde Q\|_E = 1\}$ | Euclidean unit sphere; a $7$-manifold, not a group |
| $\langle\tilde Q,\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^2$ | Algebraic norm; its null set is the singular set (quoted) |
| $\mathcal{Z}$ | Zero-divisor cone; nonzero non-invertible elements |
| $\mathcal{N} = \mathcal{Z} \cup \{0\}$ | Singular set; closed, real dimension $6$, contractible, singular at $0$ |
| $L = \mathcal{N} \cap S^7_E$ | Link of the cone; closed connected $5$-manifold, $S^1$-bundle over $S^2 \times S^2$ |
| $\pi_1(L) = 0$, $\pi_2(L) \cong \mathbb{Z}$ | Homotopy of the link; distinguishes it from $S^5$ |
| $\mathbb{P}(\mathcal{N}) \cong S^2 \times S^2$ | Projectivised cone; its geometry is *The Null Quadric and Its Projective Geometry* |
| $P = \{Q_0 = 0\} \cong \mathbb{C}^3$ | Pure biquaternions; contractible |
| $P \cap \mathbb{H}_{\mathbb{B}}$, $P \cap i\mathbb{H}_{\mathbb{B}}$ | The two pure real slices, each $\cong \mathbb{R}^3$ |
| $S^2 = \{\mu \in \mathbb{H}_{\mathbb{B}} : \mu^2 = -e_0\}$ | Sphere of real roots of $-1$ |
| $\mathbb{B}^\times$ | Group of units; complement of $\mathcal{N}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, Graduate Texts in Mathematics 98, 1985).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015).
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
