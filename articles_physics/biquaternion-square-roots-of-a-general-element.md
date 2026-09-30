# __Biquaternion Square Roots of a General Element__

## Introduction

This article solves the square-root problem in the biquaternion algebra $\mathbb{B}$: given $Q\in\mathbb{B}$, find every $\xi\in\mathbb{B}$ with
$$
\xi^2 = Q .
$$
It is the general case of the three central values $-1,0,+1$ treated in *Biquaternion Square Roots of Minus One, Zero and Plus One*. Physically, the square-root problem is the problem of **halving a transformation**: a biquaternion $\xi$ generates the one-parameter subgroup $\exp(\theta\xi)$, and a square root of $Q$ is an element whose **doubled** exponential is the transformation $\exp$ of $Q$ — the bosonic case of the spinor double cover, where a rotation through $\theta$ is the square of one through $\theta/2$. The problem also governs the boundary of the polar representation, since its answer depends on the same data as the norm and the null cone.

The method is the one of Acus and Dargys: the algebra is identified with the Euclidean Clifford algebra $Cl_{3,0}$, in which the square-root problem reduces to a complex quadratic. The identification and its dictionary are *Biquaternion Clifford Structure*; the square-root algorithm in $Cl_{3,0}$ is proved in the mathematics article *Clifford Algebras in Finite Dimensions* and is restated here in full so that the article stands alone. The three central values and the idempotents they produce are *Biquaternion Square Roots of Minus One, Zero and Plus One*; the zero-divisor set, of which the nonzero roots of $0$ are a part, is *Biquaternion Zero Divisors*, and is named here only where the classification touches it. The norm, the null cone and the group of units are *Biquaternion Norm and Invertibility*, and the polar decomposition is *The Polar Element Representation of Biquaternions*.

**Conventions.** The quaternion basis is $e_0=1,e_1,e_2,e_3$, the scalar imaginary is $i$, and a general element is $\tilde Q=\sum_{\mu=0}^3 Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The norm is $N(\tilde Q)=\sum_\mu Q_\mu^2$ and the polar form is $B(\tilde P,\tilde Q)=\sum_\mu P_\mu Q_\mu$. The material coordinate is $ict\,e_0+\mathbf{x}$ and the informational coordinate is $ct'\,e_0+i\mathbf{x}'$.

## The Identification with the Euclidean Clifford Algebra

**Theorem (the working identification).** The biquaternion algebra is the Euclidean Clifford algebra $Cl_{3,0}$ as a real algebra, $\mathbb{B}\cong Cl_{3,0}$.

This is proved in *Biquaternion Clifford Structure*, together with the dictionary that matches the four biquaternion components to the four Clifford grades under $\gamma_k\mapsto ie_k$ on the generators and $\omega=\gamma_1\gamma_2\gamma_3\mapsto i$ on the volume element. Writing $Q_\mu=q_\mu+iq'_\mu$ with real parts $q_\mu,q'_\mu$, the multivector $B=\Phi(\tilde Q)$ has the eight Clifford coefficients

$$
B = q_0 + \sum_{k=1}^{3} q'_k\gamma_k - q_3\gamma_1\gamma_2 - q_2\gamma_3\gamma_1 - q_1\gamma_2\gamma_3 + q'_0\,\omega,
$$

that is $b_0=q_0$, $b_{123}=q'_0$, $b_k=q'_k$, and $(b_{12},b_{13},b_{23})=(-q_3,-q_2,-q_1)$.

**Corollary.** $\xi^2=Q$ in $\mathbb{B}$ holds if and only if $\Phi(\xi)^2=\Phi(Q)$ in $Cl_{3,0}$; the root set of $Q$ is the $\Phi$-image of the root set of the multivector $\Phi(Q)$.

## The Algorithm

Let $B\in Cl_{3,0}$ be written

$$
B = b_0 + b_1\gamma_1+b_2\gamma_2+b_3\gamma_3 + b_{12}\gamma_1\gamma_2+b_{13}\gamma_1\gamma_3+b_{23}\gamma_2\gamma_3 + b_{123}\omega,
$$

and put

$$
c_1=b_{23},\quad c_2=-b_{13},\quad c_3=b_{12},\qquad
P=\sum_{k=1}^3 b_kc_k,\qquad R=\sum_{k=1}^3\bigl(b_k^2-c_k^2\bigr),
$$
$$
b_S = b_0^2-b_{123}^2-R,\qquad b_I = 2\bigl(P-b_0b_{123}\bigr),\qquad \Delta = b_S^2+b_I^2 .
$$

**Theorem (isolated roots).** Write $\beta=b_0-ib_{123}$ and $\gamma=R-2iP$. For each of the two complex numbers

$$
z = \frac{\beta\pm\sqrt{b_S+ib_I}}{2}
$$

with $z\neq0$, let $\delta=\mathrm{Re}\,z$, $\tau=-\mathrm{Im}\,z$, $\sigma=|z|$, set

$$
s=\pm\sqrt{\frac{\sigma+\delta}{2}},\qquad S=\text{the choice of }\pm\sqrt{\frac{\sigma-\delta}{2}}\text{ with }2sS=\tau,
$$
$$
v_k=\frac{s\,b_k+S\,c_k}{2\sigma},\qquad V_k=\frac{s\,c_k-S\,b_k}{2\sigma}\qquad(k=1,2,3),
$$

and form $\Xi=s+\sum_k v_k\gamma_k+\bigl(S+\sum_k V_k\gamma_k\bigr)\omega$. Then $\Xi^2=B$, and the two signs of $s$ give the pair $\pm\Xi$. Each nonzero value of $z$ contributes a pair, so the isolated roots number two or four according as one or both values of $z$ are nonzero.

**Proof.** The reduction $\Xi=a+b\omega=s+v+(S+V)\omega$ by the central volume element, the graded equations, and the derivation of the complex quadratic $4z^2-4\beta z+\gamma=0$ with $\beta^2-\gamma=b_S+ib_I$ are proved in *Clifford Algebras in Finite Dimensions* §§28–30, where $R$ carries the name $Q$. The present article only transports the statement. $\square$

**Corollary (the biquaternion algorithm).** To compute the square roots of $Q\in\mathbb{B}$: transport $Q$ to $B=\Phi(Q)$, apply the theorem to $B$, and transport each root $\Xi$ back with $\Phi^{-1}$,

$$
\xi = (b_0+b_{123}i) + (-b_{23}+b_1i)e_1 + (-b_{13}+b_2i)e_2 + (-b_{12}+b_3i)e_3 .
$$

## The Continuum and the Classification

**Theorem (the continuum).** If and only if $B$ has vanishing vector and bivector parts — that is, $Q$ is a **complex scalar** $Q=q_0+q'_0i$ — the roots of $B$ include the four-parameter family $\Xi=\sum_k v_k\gamma_k+\bigl(\sum_k V_k\gamma_k\bigr)\omega$ whose real coefficients satisfy

$$
\sum_{k=1}^3 v_k^2-\sum_{k=1}^3 V_k^2=b_0,\qquad 2\sum_{k=1}^3 v_kV_k=b_{123},
$$

alongside the isolated roots supplied by the two values of $z$. The case $B=0$, the roots of $0$, is the extreme instance, whose nonzero members are the nilpotents $\sum_k v_k\gamma_k+\bigl(\sum_k V_k\gamma_k\bigr)\omega$ with $\sum_k v_k^2=\sum_k V_k^2$ and $\sum_k v_kV_k=0$.

The statement and proof are in *Clifford Algebras in Finite Dimensions* §31, transported by $\Phi$. In biquaternion terms a complex scalar is an element of the centre $\mathbb{C}_{\mathbb{B}}$, so the continuum is the centre's contribution to the root set.

Collecting the two theorems, every $Q$ falls into exactly one of the following cases:

| case | condition on the data of $B=\Phi(Q)$ | roots of $Q$ |
|---|---|---|
| none | $b_S=b_I=0$ and $b_0=b_{123}=0$, $Q$ not a complex scalar | $\varnothing$ |
| two | $b_S+ib_I=0$ and $\beta\neq0$, or one value of $z$ vanishes | a single pair $\pm\xi$ |
| four | $b_S+ib_I\neq0$ and both values of $z$ nonzero | two pairs |
| continuum | $b_1=\dots=b_{23}=0$ ($Q$ a complex scalar) | the four-parameter family, plus any isolated pairs |

The generic case is four roots. The scalar $\beta^2-\gamma=b_S+ib_I$ is the existence scalar: its vanishing separates four roots from two, and the further vanishing of $\beta$ is the frontier with the rootless case.

**Physical reading.** The four roots are generically two pairs of opposite **generators**, $\pm\xi$: the pair is the $\mathbb{Z}_2$ ambiguity of the square-root map, the same double cover that appears in the spinor representations. A complex scalar $Q$ is a central element, and its four-parameter family of roots is the freedom of writing a central transformation as a square of a non-central one; the family degenerates to the null elements when $Q=0$, which is the light cone.

## The Three Central Data

The classification specialises to the three central values of *Biquaternion Square Roots of Minus One, Zero and Plus One* and reproduces them, which is the check that the transport and the algorithm agree with the direct computation.

For $Q=-1$ the pair $z$ is $(0,-1)$: the zero value opens the family, the value $-1$ gives the pair $\pm i$. For $Q=+1$ the pair is $(1,0)$: the value $1$ gives $\pm1$, the zero value opens the family. Both are complex scalars, so both lie in the continuum row. For $Q=0$ the data give $b_S=b_I=0$ and the scalar row, but $Q=0$ is a complex scalar, so it too lies in the continuum row, and its nonzero roots are the nilpotents. In physical terms the three root families are the elliptic, hyperbolic and parabolic generators, which is the trichotomy of the square of a generator recorded in the companion article.

## Worked Examples

The examples are computed with the algorithm and verified by squaring.

**An imaginary quaternion.** For $Q=-ie_3$ the transport gives the multivector $-e_3$, with $b_S=-1$, $b_I=0$ and $\beta=0$, so $b_S+ib_I\neq0$; there are four roots,

$$
\xi = \pm\tfrac12\bigl(1-i+e_3-ie_3\bigr),\qquad \xi=\pm\tfrac12\bigl(1+i-e_3-ie_3\bigr).
$$

**A central element.** For $Q=-1+i$ the two values of $z$ are $0$ and $-1-i$; there are two isolated roots,

$$
\xi = \pm\Bigl(\sqrt{\tfrac{\sqrt2-1}{2}}+i\sqrt{\tfrac{\sqrt2+1}{2}}\Bigr),
$$

and a four-parameter continuum, the central case of the reading above.

**A rootless element.** For $Q=e_1-ie_3$ the transport gives $b_3=b_{23}=-1$ with $b_S=b_I=0$ and $\beta=0$: the rootless row, and $Q$ has no square root.

**A general four-root case.** For $Q=-(2+i)e_3$ the transport gives $b_{12}=2$, $b_3=-1$ and four roots, for instance

$$
\xi = \pm\bigl(0.2429+0.2429\,e_3-1.0291\,i-1.0291\,ie_3\bigr).
$$

**A parabolic root.** For $Q=0$ the roots are the nilpotent cone; $\xi=e_1+ie_2$ is a member, with $\xi^2=0$.

## Summary

The square roots of $Q\in\mathbb{B}$ are computed by transporting $Q$ to $Cl_{3,0}$ through the identification of *Biquaternion Clifford Structure*, applying the closed-form algorithm of *Clifford Algebras in Finite Dimensions*, and transporting back.

The algorithm solves $4z^2-4\beta z+\gamma=0$ with $\beta=b_0-ib_{123}$, $\gamma=R-2iP$ and discriminant $16(b_S+ib_I)$; each nonzero value $z=(\beta\pm\sqrt{b_S+ib_I})/2$ yields a pair $\pm\xi$ through $s=\pm\sqrt{(\sigma+\delta)/2}$, $S$ signed by $2sS=\tau$, $\sigma=|z|$, and the vector formulas. The existence scalars are $b_S=b_0^2-b_{123}^2-R$ and $b_I=2(P-b_0b_{123})$.

The classification is: **no root** when $b_S=b_I=0$, $\beta=0$ and $Q$ is not central; **two roots** when one value of $z$ vanishes or when $b_S+ib_I=0$ with $\beta\neq0$; **four roots** generically; and the **four-parameter continuum** when and only when $Q$ is a complex scalar, alongside any isolated pairs. Physically the roots are the generators of the doubled one-parameter subgroups, in opposite pairs; the central data carry the continuum; and the rootless elements are the ones whose square would have to be produced by no generator at all.

The three central data $-1,0,+1$ are treated in *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the nilpotent cone of the roots of $0$ is *Biquaternion Zero Divisors*. This article owns the classification of $\xi^2=Q$ for a general $Q$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $Q$ | The element whose square roots are sought |
| $\xi$ | A square root of $Q$ |
| $\Phi$ | The identification $\mathbb{B}\to Cl_{3,0}$ |
| $B=\Phi(Q)$ | The multivector of $Q$ |
| $c_k$ | $c_1=b_{23}$, $c_2=-b_{13}$, $c_3=b_{12}$ |
| $P,R$ | $P=\sum b_kc_k$, $R=\sum(b_k^2-c_k^2)$ |
| $b_S,b_I$ | $b_S=b_0^2-b_{123}^2-R$, $b_I=2(P-b_0b_{123})$ |
| $\beta,\gamma$ | $\beta=b_0-ib_{123}$, $\gamma=R-2iP$; $\beta^2-\gamma=b_S+ib_I$ |
| $z$ | $\frac{\beta\pm\sqrt{b_S+ib_I}}{2}$ |
| $s,S,v,V$ | Paravector data of a root, $\xi=s+v+(S+V)i$ in Clifford form |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square-root algorithm and the worked examples of complexified quaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the central case.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the nilpotent cone.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford background.
