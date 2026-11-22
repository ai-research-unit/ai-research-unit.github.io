# __Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$__

## Introduction

**The question.** The word spinor names three objects: the plane, its first closure, and the sum of two copies of that closure. What are the three in the matrix display, what are their weights, and which sector of the two predicates does each of them meet?

**Why it is the same statement.** This is the in-depth matrix reading of [Spinors and Dirac Spinors in the Biquaternion Algebra](spinors-and-dirac-spinors-in-the-biquaternion-algebra.html). The three levels are
$$
\mathbb{C}P\subset M_2(\mathbb{C})P\subset M_2(\mathbb{C})=M_2P\oplus M_2P_{\perp},
$$
of real dimensions $2,4,8$, and the two predicates are $\det A$ and $\Delta=-4B^2$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The nesting of the three levels with a dimension table. The weight string: $+\tfrac12$ on the plane, and $\pm\tfrac12$ on the ideal, with the companion nilpotent $P_{\perp}E_2P$ as the $-\tfrac12$ vector. That a spinor is null: $\det=0$ and $B^2=-\lambda^2/4$. The sector of a spinor, which is $\Sigma_{01}$ or $\Sigma_{00}$. The Dirac spinor as a pair, with $\det X=2B(X_+,X_-)$ and the sector table. The right multiplication by a transverse axis, which exchanges the two ideals and preserves the determinant but not the discriminant. The axis as a parameter.

**What the article does not do.** It does not treat the Fierz–Kofink identities, which are [The Fierz–Kofink Identities and the Classification of Spinors in $M_2(\mathbb{C})$](the-fierz-kofink-identities-and-the-classification-of-spinors-in-m2c.html); it does not treat the carrier family in full, which is [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$; the spin generators are $S_k=\tfrac12 iE_k=\tfrac12\sigma_k$, Hermitian, and the axis generator is $S\cdot n=\tfrac12n\cdot\sigma$. The projection is $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ and $P_{\perp}=\mathrm I_2-P$. $N=\det$, $B^2=\det-\tfrac14\tau^2$, $\Delta=-4B^2$.

**Boundaries.** The predicates and the sectors are defined in [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html). The carriers are [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](the-carriers-the-representation-the-spin-and-the-closure-in-m2c.html). The sectors on the ideal are [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $P$ a rank-one projection, $\lambda$ a complex number, $\nu$ the companion nilpotent, $X_\pm$ the two parts of a Dirac spinor, $M$ the multiplier of an exchange.

## The Three Levels

**The projection.** $P^2=P$, $P=P^{\dagger}$, $\operatorname{tr}P=1$, $PP_{\perp}=0$, $P+P_{\perp}=\mathrm I_2$, all verified exactly.

**The three levels.**

| level | space | $\dim_\mathbb{R}$ | $\dim_\mathbb{C}$ | generators |
|---|---|---|---|---|
| spinor | $\mathbb{C}P$ | $2$ | $1$ | $P$ |
| spinor space | $M_2P$ | $4$ | $2$ | $P$, $E_2P$ |
| Dirac spinor | $M_2P\oplus M_2P_{\perp}=M_2$ | $8$ | $4$ | both ideals |

**The nesting.** $\mathbb{C}P\subset M_2P\subset M_2$, and the real dimension doubles at each step: $2,4,8$.

**Why the plane is the carrier and the ideal the closure.** The plane is invariant under the rotations about $n$ alone; the ideal is invariant under every left multiplication. The closure makes the object a module, the plane makes it irreducible.

## The Weight

**The axis identity.** $S\cdot n=\tfrac12n\cdot\sigma$ satisfies
$$
(S\cdot n)P=+\tfrac12P,\qquad (S\cdot n)P_{\perp}=-\tfrac12P_{\perp},
$$
verified exactly. This is the matrix form of $\vec u\tilde\Pi_\pm=\mp i\tilde\Pi_\pm$, because $S\cdot n$ times $i$ is $\tfrac i2n\cdot\sigma$ and $n\cdot\sigma P=P$.

**The companion nilpotent.** In the corner $P_{\perp}M_2P$,
$$
\nu=P_{\perp}E_2P=\begin{pmatrix}0&0\\-i&0\end{pmatrix}\quad(n=e_3),
$$
with $\nu^2=0$ and $(S\cdot n)\nu=-\tfrac12\nu$, verified exactly. It is the $-\tfrac12$ vector of the ideal.

**The weight string.** The ideal carries $+\tfrac12$ on the line $\mathbb{C}P$ and $-\tfrac12$ on the line $\mathbb{C}\nu$; the string is $(+\tfrac12,-\tfrac12)$, of length two, and $2s+1=2=\dim_\mathbb{C}M_2P$.

**The half angle.** The rotor acts on the plane as $e^{-i\theta/2}$; at $\theta=2\pi$ the multiplier is $-\mathrm I_2$ and the spinor returns with the opposite sign, while a vector returns unchanged.

## The Sector of a Spinor

**The null theorem.** For every $\lambda$,
$$
\det(\lambda P)=0,\qquad B^2(\lambda P)=-\frac{\lambda^2}{4},
$$
verified. The eigenvalues are $0$ and $\lambda$, the trace is $\lambda$, and the discriminant is $\lambda^2$.

**The reading.** A non-zero spinor is singular, so it is a zero divisor and lies in neither $\Sigma_{11}$ nor $\Sigma_{10}$.

**The intersection with $\Sigma_{01}$.** $\{\lambda P:\lambda\neq0\}$, since $\det=0$ and $\Delta=\lambda^2\neq0$.

**The intersection with $\Sigma_{00}$.** $\{0\}$ alone.

| sector | condition on $\lambda$ | intersection |
|---|---|---|
| $\Sigma_{11}$ | impossible | $\varnothing$ |
| $\Sigma_{10}$ | impossible | $\varnothing$ |
| $\Sigma_{01}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}P$ |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ |

**The eigenvector.** For $\lambda\neq0$ the eigenvalue $\lambda$ has eigenvector $P$ itself, since $P$ is a projection acting on its own image as the identity.

## The Dirac Spinor Is a Pair

**The decomposition.** Every matrix splits uniquely as
$$
X=X_++X_-,\qquad X_+=XP,\quad X_-=XP_{\perp},
$$
of complex dimensions $2+2=4$.

**The norm is the pairing.** Since $\det X_\pm=0$,
$$
\det X=2B(X_+,X_-),\qquad B(X,Y)=\tfrac12\left(\det(X+Y)-\det X-\det Y\right),
$$
verified on random pairs.

**The weight string of the pair.** Each ideal carries $+\tfrac12$ and $-\tfrac12$ once, so on the Dirac spinor each weight occurs twice.

## The Sector of a Dirac Spinor

**The two indices are independent.** The first is $\det X=2B(X_+,X_-)$ and the second is $\Delta(X)$; neither determines the other.

| sector | condition | witness | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $\det\neq0$, $\Delta\neq0$ | $\mathrm I_2+2E_1$: $\det=5$, $\Delta=-16$ | $8$ |
| $\Sigma_{10}$ | $\det\neq0$, $\Delta=0$ | $\mathrm I_2$: $\det=1$, $\Delta=0$ | $6$ |
| $\Sigma_{01}$ | $\det=0$, $\Delta\neq0$ | $P$: $\det=0$, $\Delta=1$ | $6$ |
| $\Sigma_{00}$ | $\det=0$, $\Delta=0$ | $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ | $4$ |

**The witnesses.** $\det(\mathrm I_2+2E_1)=1+4=5$ and $B^2=5-1=4$, so $\Delta=-16$; verified. The matrix $P$ has $\det=0$, $\tau=1$, $B^2=-\tfrac14$, $\Delta=1$.

**The doubly degenerate locus is the nilpotent cone.** $\det X=0$ and $\tau(X)=0$ together are $X^2-\tau X+\det\mathrm I_2=0$, that is $X^2=0$. So
$$
\Sigma_{00}=\{X:X^2=0\},
$$
of complex dimension two and real dimension four: the single nilpotent orbit of $\mathrm{GL}_2(\mathbb{C})$, the conjugates of $\begin{pmatrix}0&1\\0&0\end{pmatrix}$.

**The invertibility criterion.** $X$ is invertible exactly when its two parts pair, $B(X_+,X_-)\neq0$, and then both parts are non-zero.

## The Two Parts Are Exchanged on the Right

**No left multiplication crosses.** $A(M_2P)\subseteq M_2P$ and $A(M_2P_{\perp})\subseteq M_2P_{\perp}$: each summand is a left ideal.

**A transverse multiplier exchanges them.** Let $M=E_2=-i\sigma_2$ for an axis $n$ transverse to $e_2$. Then $M^2=-\mathrm I_2$, $\det M=1$, and
$$
(M_2P)M=M_2(PM),\qquad (PM)P=0,
$$
verified: $PM$ lies in the other ideal. So $X\mapsto XM$ carries $S_+$ to $S_-$ bijectively and squares to $-\mathrm{id}$.

**The exchange preserves the determinant and not the discriminant.** $\det(XM)=\det X\det M=\det X$, so the null cone is preserved; but $\Delta$ is not preserved. With $X=\mathrm I_2$ (sector $\Sigma_{10}$), the image $M$ has $\tau=0$, $\det=1$, $\Delta=-4$: the sector $\Sigma_{11}$. So the first index is exchange-invariant and the second is not.

**The exchanges form a complex line.** A left-linear map $S_+\to S_-$ that is a right multiplication by $M$ requires $PMP=0$, and two multipliers give the same map exactly when their difference is killed by $P$ on the left. The maps are therefore the maps $X\mapsto XE$ with $E$ in the corner $PM_2P_{\perp}$, a complex line. Every such $E$ has rank one and square zero: it is a multiple of $\nu$.

**The pair is one spinor space taken twice.** As a left module $M_2\cong S\oplus S$ with $S$ the simple module $M_2P$; the Dirac spinor is not a four-dimensional irreducible module.

## The Axis Is a Parameter

**The conjugation moves the axis.** For unitary $U$ with $UnU^{\dagger}=n'$, the map $X\mapsto UXU^{\dagger}$ carries $P(n)$ to $P(n')$, the plane to the plane, each ideal to the corresponding ideal, and preserves both predicates. So the family is one family and the axis is a parameter.

**The two axes of a pair.** $P(-n)=P_{\perp}(n)$: the unordered pair is indexed by $n$ up to sign.

## Worked Example: the Axis $e_3$

**The objects.**
$$
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad P_{\perp}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad S=\left\{\begin{pmatrix}a&0\\c&0\end{pmatrix}\right\},\quad \nu=\begin{pmatrix}0&0\\-i&0\end{pmatrix}.
$$

**A spinor.** $X=3P$: $\det=0$, $\tau=3$, eigenvalues $3,0$, $B^2=-\tfrac94$.

**A Dirac spinor.** $X=3P+2P_{\perp}=\operatorname{diag}(3,2)$: $\det=6$, $\Delta=1$, sector $\Sigma_{11}$.

**An exchange.** Right multiplication by $M=-i\sigma_2$: the image has determinant $6$ still and trace $0$, so $B^2=6$ and $\Delta=-24$, verified.

## Where $n=2$ Differs

**The number of levels.** At $n=2$ the chain has three levels, of real dimensions $2,4,8$, and it stops. At order $n$ the chain is a line $\subset$ ideal of dimension $n\subset$ algebra of dimension $n^2$, and the bispinor level is a splitting into $n$ ideals and not two.

**The weight string.** At $n=2$ the string of the ideal is $(+\tfrac12,-\tfrac12)$. At order $n$ it is $(\tfrac{n-1}{2},\dots,-\tfrac{n-1}{2})$, and the spin is $\tfrac{n-1}{2}$.

**The nilpotent cone.** At $n=2$ the doubly degenerate locus is a single nilpotent orbit. At order $n$ it is a union of orbits indexed by the partitions of $n$.

## Summary

The three levels are $\mathbb{C}P\subset M_2P\subset M_2$, of real dimensions $2,4,8$. The generator $S\cdot n=\tfrac12n\cdot\sigma$ acts on the plane as $+\tfrac12$ and on the companion nilpotent $\nu=P_{\perp}E_2P$ as $-\tfrac12$, so the string of the ideal is $(+\tfrac12,-\tfrac12)$.

A spinor is null: $\det(\lambda P)=0$ and $B^2=-\lambda^2/4$, so the punctured plane lies in $\Sigma_{01}$ and the origin in $\Sigma_{00}$. A Dirac spinor is a pair $X=X_++X_-$ with $\det X=2B(X_+,X_-)$, and its four sectors are the open dense $\Sigma_{11}$, the invertible-degenerate $\Sigma_{10}$, the null cone $\Sigma_{01}$ and the nilpotent cone $\Sigma_{00}=\{X^2=0\}$, of real dimensions $8,6,6,4$.

Right multiplication by a transverse axis exchanges the two ideals, preserves the determinant and changes the discriminant; the exchanges are the maps $X\mapsto XE$ with $E$ in the corner $PM_2P_{\perp}$, a complex line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ | rank-one projection, the spinor |
| $P_{\perp}=\mathrm I_2-P$ | complementary projection |
| $\nu=P_{\perp}E_2P$ | companion nilpotent, weight $-\tfrac12$ |
| $X_\pm=XP,\,XP_{\perp}$ | the two parts of a Dirac spinor |
| $B(X,Y)$ | polar form of the determinant |
| $M=E_2$ | transverse multiplier of the exchange |

## Further Reading

- [Spinors and Dirac Spinors in the Biquaternion Algebra](spinors-and-dirac-spinors-in-the-biquaternion-algebra.html), for the source's three levels and its Dirac pairing.
- [The Fierz–Kofink Identities and the Classification of Spinors in $M_2(\mathbb{C})$](the-fierz-kofink-identities-and-the-classification-of-spinors-in-m2c.html), for the classification of spinors by the invariants.
- [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html), for the family of planes and ideals.
- [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-spectral-regularity-in-m2c.html), for the eigenvalues of an ideal element.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector table read in full.
