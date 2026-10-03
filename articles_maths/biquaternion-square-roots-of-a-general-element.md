# __Biquaternion Square Roots of a General Element__

## Introduction

This article solves the square-root problem in the biquaternion algebra $\mathbb{B}$: given $Q \in \mathbb{B}$, find every $\xi \in \mathbb{B}$ with
$$
\xi^2 = Q .
$$
The problem is not the same as the three central cases $\xi^2 = -1,0,+1$ treated in *Biquaternion Square Roots of Minus One, Zero and Plus One*. For those three values the set of roots is a union of small families found directly from the vector–scalar decomposition; for a general $Q$ the answer is a finite set — generically four elements, falling to two — or a four-parameter continuum, or empty, and finding it needs the Clifford structure of the algebra rather than a case check. This article owns that classification and states the algorithm that produces it, in the form the algebra is usually written in.

The method is the one of Acus and Dargys: the biquaternion algebra is identified with the Clifford algebra $Cl_{3,0}$ of *The Clifford Structure of the Biquaternion Algebra*, in which the square-root problem reduces to a complex quadratic. The identification and its dictionary are *The Clifford Structure of the Biquaternion Algebra*; the square-root algorithm in $Cl_{3,0}$ is *Clifford Algebras in Finite Dimensions*, where it is proved. The three special data $Q=-1,0,+1$ and the relation to the idempotents are *Biquaternion Square Roots of Minus One, Zero and Plus One*; the zero-divisor cone, of which the nonzero roots of $0$ are a part, is *Biquaternion Zero Divisors*, and is named here only where the classification touches it and not developed. The polar and exponential decompositions that the answer must be consistent with are *Biquaternion Polar Element Representation*.

The treatment is mathematically honest: every claim is either proved or cited to the article that proves it, and the algorithm is verified against the worked examples. No physics is invoked.

Throughout, the quaternion basis is $e_0=1,e_1,e_2,e_3$, the scalar imaginary is $i$, and a general biquaternion is $\tilde Q = Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_\mu\in\mathbb{C}$. The norm is $N(\tilde Q)=\sum_\mu Q_\mu^2$.

## The Identification with the Clifford Algebra

**Theorem (the working identification).** The biquaternion algebra is the Clifford algebra $Cl_{3,0}$ as a real algebra, $\mathbb{B}\cong Cl_{3,0}$.

This is proved in *The Clifford Structure of the Biquaternion Algebra*, together with the dictionary that identifies the four biquaternion components with the four Clifford grades under the assignment $\gamma_k\mapsto ie_k$ on the generators, $\omega=\gamma_1\gamma_2\gamma_3\mapsto i$ on the volume element. The dictionary is, in full, a linear bijection

$$
\Phi:\mathbb{B}\to Cl_{3,0},
$$

$$
\Phi(e_0)=1,\quad \Phi(e_k)=-\gamma_j\gamma_l,\quad \Phi(ie_k)=\gamma_k,\quad \Phi(i)=\omega,
$$

with $(j,l)$ the two indices different from $k$ in even order ($\Phi(e_1)=-\gamma_2\gamma_3$, $\Phi(e_2)=-\gamma_3\gamma_1$, $\Phi(e_3)=-\gamma_1\gamma_2$). Writing $Q_\mu=q_\mu+iq'_\mu$ with real $q_\mu,q'_\mu$, the multivector of $\tilde Q$ has the eight Clifford coefficients

$$
b_0 = q_0,\quad b_{123}=q'_0,\qquad b_k = q'_k,\quad b_{jk}^{\,\Phi} = -q_l \quad (k\text{ read off as above}),
$$

that is

$$
B = \Phi(\tilde Q) = q_0 + \sum_{k=1}^{3} q'_k \gamma_k\;-\; q_3\gamma_1\gamma_2\;-\;q_2\gamma_3\gamma_1\;-\;q_1\gamma_2\gamma_3\;+\;q'_0\omega .
$$

**Corollary (transport of the problem).** $\xi^2=Q$ in $\mathbb{B}$ holds if and only if $\Phi(\xi)^2 = \Phi(Q)$ in $Cl_{3,0}$. The square-root problem in $\mathbb{B}$ is therefore the square-root problem in $Cl_{3,0}$, transported by $\Phi$; the root set of $Q$ is the $\Phi$-image of the root set of $\Phi(Q)$.

## The Algorithm

We recall the algorithm of *Clifford Algebras in Finite Dimensions* in the notation of that article, then transport it. Let $B\in Cl_{3,0}$ be written

$$
B = b_0 + b_1\gamma_1+b_2\gamma_2+b_3\gamma_3 + b_{12}\gamma_1\gamma_2+b_{13}\gamma_1\gamma_3+b_{23}\gamma_2\gamma_3 + b_{123}\omega,
$$

and set

$$
c_1 = b_{23},\quad c_2=-b_{13},\quad c_3=b_{12},
$$
$$
P = \sum_{k=1}^3 b_kc_k = b_1b_{23}-b_2b_{13}+b_3b_{12},
\qquad
R = \sum_{k=1}^3\bigl(b_k^2-c_k^2\bigr) = b_1^2+b_2^2+b_3^2-b_{12}^2-b_{13}^2-b_{23}^2,
$$
$$
b_S = b_0^2 - b_{123}^2 - R, \qquad b_I = 2\bigl(P - b_0b_{123}\bigr), \qquad \Delta = b_S^2+b_I^2 .
$$

**Theorem (isolated roots in $Cl_{3,0}$).** Write $\beta = b_0 - ib_{123}$ and $\gamma = R - 2iP$. The isolated square roots of $B$ are obtained as follows. For each of the two complex numbers

$$
z = \frac{\beta \pm \sqrt{b_S+ib_I}}{2}
$$

with $z\neq0$, put $\delta=\mathrm{Re}\,z$, $\tau=-\mathrm{Im}\,z$, $\sigma=|z|$, and let

$$
s = \pm\sqrt{\frac{\sigma+\delta}{2}},\qquad S=\text{the choice of }\pm\sqrt{\frac{\sigma-\delta}{2}}\text{ with }2sS=\tau,
$$
$$
v_k = \frac{s\,b_k + S\,c_k}{2\sigma}, \qquad V_k = \frac{s\,c_k - S\,b_k}{2\sigma}\qquad(k=1,2,3).
$$

Then

$$
\Xi = s + \sum_k v_k\gamma_k + \Bigl(S+\sum_k V_k\gamma_k\Bigr)\omega
$$

satisfies $\Xi^2 = B$, and the two signs of $s$ give the two elements $\pm\Xi$. Each nonzero value of $z$ contributes a pair, so the isolated roots are two or four in number according as one or both values of $z$ are nonzero.

**Proof.** The reduction $\Xi=a+b\omega=s+v+(S+V)\omega$, the graded equations, and the derivation of the complex quadratic $4z^2-4\beta z+\gamma=0$ with $\beta^2-\gamma=b_S+ib_I$ are proved in *Clifford Algebras in Finite Dimensions* §§28–30, where $\omega=e_1e_2e_3$ is central of square $-1$ and the symbols $P$ and $R$ of this article are the $P$ and $Q$ of that one. The present article only transports the statement. $\square$

**Corollary (the biquaternion algorithm).** To compute the square roots of $Q\in\mathbb{B}$, transport $Q$ to $B=\Phi(Q)$ by the dictionary of §*The Identification with the Clifford Algebra*, apply the theorem to $B$, and transport each root $\Xi$ back to $\xi=\Phi^{-1}(\Xi)$. Reading the inverse dictionary off the table,

$$
q_0 = b_0,\quad q'_0=b_{123},\qquad q'_k=b_k,\quad q_1=-b_{23},\quad q_2=-b_{13},\quad q_3=-b_{12},
$$

so that $\xi = (b_0 + b_{123}i) + (-b_{23}+b_1i)e_1 + (-b_{13}+b_2i)e_2 + (-b_{12}+b_3i)e_3$.

## The Continuum and the Classification

The algorithm of §*The Algorithm* assumes the scalar $\sigma=s^2+S^2$ of the root nonzero. Its complement is a four-parameter family.

**Theorem (the continuum).** If and only if the multivector $B$ has vanishing vector and bivector parts — that is, $b_1=b_2=b_3=b_{12}=b_{13}=b_{23}=0$, so that $B=b_0+b_{123}\omega$ and, in biquaternion terms, $Q$ is a **complex scalar** $Q=q_0+q'_0i$ — the roots of $B$ include the four-parameter family of elements $\Xi=\sum_k v_k\gamma_k+\bigl(\sum_k V_k\gamma_k\bigr)\omega$ whose real coefficients $v_k,V_k$ satisfy

$$
\sum_{k=1}^3 v_k^2-\sum_{k=1}^3 V_k^2 = b_0, \qquad 2\sum_{k=1}^3 v_kV_k = b_{123},
$$

alongside the isolated roots supplied by the two values of $z$. The case $B=0$ is the extreme instance: the roots of $0$ are the nonzero elements $\sum_k v_k\gamma_k+\bigl(\sum_k V_k\gamma_k\bigr)\omega$ with $\sum_k v_k^2=\sum_k V_k^2$ and $\sum_k v_kV_k=0$, the nilpotent set.

The statement and proof are in *Clifford Algebras in Finite Dimensions* §31; the transport to $\mathbb{B}$ uses the same dictionary. The family is the complex-scalar locus of the algebra, and in biquaternion terms a complex scalar is exactly an element of the centre $\mathbb{C}_{\mathbb{B}}$.

Collecting the two theorems, and reading the number of solutions off the quadratic, every $Q$ falls into exactly one of:

| case | condition on the data of $B=\Phi(Q)$ | roots of $Q$ |
|---|---|---|
| none | $b_S=b_I=0$ and $b_0=b_{123}=0$, $B$ not a complex scalar | $\varnothing$ |
| two | $b_S+ib_I=0$ and $\beta\neq0$, or one value of $z$ vanishes | a single pair $\pm\xi$ |
| four | $b_S+ib_I\neq0$ and both values of $z$ nonzero | two pairs |
| continuum | $b_1=\dots=b_{23}=0$ ($Q$ a complex scalar) | the four-parameter family, plus any isolated pairs |

The generic case is four roots. The existence scalar is $\beta^2-\gamma=b_S+ib_I$: its vanishing separates the four-root case from the two-root case, and the further vanishing of $\beta$ is the frontier with the rootless case.

## The Three Central Data

The classification specialises to the three central values of *Biquaternion Square Roots of Minus One, Zero and Plus One*, and reproduces them; the correspondence is a check that the transport and the algorithm agree with the direct computation.

**$Q=-1$ and $Q=+1$ are complex scalars**, so both fall in the continua row. For $Q=-1$ the pair $z$ is $(0,-1)$: the zero value gives no isolated root and opens the family, the value $-1$ gives the pair $\pm i\omega$ in the Clifford picture, that is $\pm i$ in $\mathbb{B}$. For $Q=+1$ the pair is $(1,0)$: the value $1$ gives $\pm1$, the zero value opens the family. The families are $\sum_k v_k^2-\sum_k V_k^2=\mp1$, $2\sum_k v_kV_k=0$.

**$Q=0$** has $b_0=b_{123}=0$ and $b_S=b_I=0$, the rootless row for a nonzero vector–bivector part, but $B=0$ is a complex scalar, so it lies in the continuum row: its roots are the nonzero null elements, the nilpotent cone of *Biquaternion Zero Divisors*.

The three sets are therefore the degenerate data of the general classification, and the general article is where the four-root and two-root cases live.

## Worked Examples

The examples are computed with the algorithm and verified by squaring; the verification is the multiplication check $\xi^2=Q$.

**A pure imaginary quaternion.** For $Q=-ie_3$ (that is $-Ik$ in the notation of Acus and Dargys) the transport gives the multivector $-e_3$, with $b_S=-1$, $b_I=0$ and $\beta=0$, so $b_S+ib_I\neq0$. The two values of $z$ are distinct and nonzero and the four roots are

$$
\xi = \pm\tfrac12\bigl(1 - i + e_3 - ie_3\bigr), \qquad \xi = \pm\tfrac12\bigl(1 + i - e_3 - ie_3\bigr),
$$

in agreement with the roots of $-Ik$ computed directly. Squaring recovers $-ie_3$ in each case.

**A complex scalar.** For $Q=-1+i$ (that is $-1+I$), a complex scalar with $b_0=-1$, $b_{123}=1$, the two values of $z$ are $0$ and $-1-i$, so one is zero and there are two isolated roots,

$$
\xi = \pm\Bigl(\sqrt{\tfrac{\sqrt2-1}{2}} + i\sqrt{\tfrac{\sqrt2+1}{2}}\Bigr),
$$

and a continuum. Squaring the displayed root gives $-1+i$.

**A rootless element.** For $Q=e_1-ie_3$ (that is $i-Ik$) the transport gives $b_3=b_{23}=-1$, with $b_S=b_I=0$ and $\beta=0$. The row is the rootless one, and $Q$ has no square root. This is the example of Acus and Dargys.

**Four roots of a non-scalar.** For $Q=-(2+i)e_3$ (that is $-(2+I)k$) the transport gives $b_{12}=2$, $b_3=-1$; the algorithm returns four roots, for instance

$$
\xi = \pm\bigl(0.2429 + 0.2429\,e_3 - 1.0291\,i - 1.0291\,ie_3\bigr),
$$

whose square is $-(2+i)e_3$.

**A nilpotent root of $0$.** For $Q=0$ the algorithm gives the continuum, whose nonzero members are the nilpotents; $\xi=e_1+ie_2$ is one of them, with $\xi^2=0$.

## Summary

The square roots of $Q\in\mathbb{B}$ are computed by transporting $Q$ to the Clifford algebra $Cl_{3,0}$ through the identification $\mathbb{B}\cong Cl_{3,0}$ of *The Clifford Structure of the Biquaternion Algebra*, with dictionary $\Phi$; applying there the closed-form algorithm of *Clifford Algebras in Finite Dimensions*; and transporting the roots back.

The algorithm solves a complex quadratic $4z^2-4\beta z+\gamma=0$ with $\beta=b_0-ib_{123}$, $\gamma=R-2iP$, whose discriminant is $16(b_S+ib_I)$; each nonzero root $z$ yields a pair $\pm\xi$ through $s=\pm\sqrt{(\sigma+\delta)/2}$, $S$ signed by $2sS=\tau$, $\sigma=|z|$, and the vector formulas. The existence scalars are $b_S=b_0^2-b_{123}^2-R$ and $b_I=2(P-b_0b_{123})$.

The classification is: **no root** when $b_S=b_I=0$, $\beta=0$ and $Q$ is not a complex scalar; **two roots** when one value of $z$ vanishes or when $b_S+ib_I=0$ with $\beta\neq0$; **four roots** generically; and the **four-parameter continuum** when and only when $Q$ is a complex scalar, alongside the isolated pairs.

The three central data $-1,0,+1$ are the degenerate entries of the classification and are treated in *Biquaternion Square Roots of Minus One, Zero and Plus One*; the nonzero roots of $0$ are the nilpotent cone of *Biquaternion Zero Divisors*, named here and not developed. This article owns the classification of $\xi^2=Q$ for a general $Q$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $Q$ | The element whose square roots are sought |
| $\xi$ | A square root of $Q$ |
| $\Phi$ | The identification $\mathbb{B}\to Cl_{3,0}$ |
| $B=\Phi(Q)$ | The multivector of $Q$, coefficients $b_0,b_k,b_{jk},b_{123}$ |
| $c_k$ | $c_1=b_{23}$, $c_2=-b_{13}$, $c_3=b_{12}$ |
| $P,R$ | $P=\sum b_kc_k$, $R=\sum(b_k^2-c_k^2)$ |
| $b_S,b_I$ | $b_S=b_0^2-b_{123}^2-R$, $b_I=2(P-b_0b_{123})$ |
| $\beta,\gamma$ | $\beta=b_0-ib_{123}$, $\gamma=R-2iP$; $\beta^2-\gamma=b_S+ib_I$ |
| $z$ | $\frac{\beta\pm\sqrt{b_S+ib_I}}{2}$ |
| $s,S,v,V$ | Paravector data of a root, $\xi=s+v+(S+V)i$ in Clifford form |

## Further Reading

- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square-root algorithm and the worked examples of complexified quaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the central case.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the nilpotent cone.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford background.
