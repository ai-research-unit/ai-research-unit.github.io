# __Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$__

## Introduction

**One element of order $n$ with simple spectrum produces all $n$ idempotents of the frame.** This is the first step of the construction that the four matrix categories instantiate. No second element is needed, and no idempotent is chosen in advance: the root produces them by polynomial interpolation.

The article states the interpolation, proves that the projectors are polynomials in the root, reads the $\mathbb{Z}/n$ grading that the root defines, counts the root set, and records the case $n=2$, which is the biquaternion root of $+1$. The Peirce decomposition that the idempotents produce is *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*; the choice of vectors inside the resulting lines, and the gauge that acts on them, is *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*.

## The Root and Its Spectrum

**A root of unity of order $n$ is an element $H\in M_n(\mathbb{C})$ with $H^{n}=I$.** Let $\zeta=e^{2\pi i/n}$ and $\zeta_k=\zeta^{k-1}$, $k=1,\dots,n$, the $n$ distinct roots of $x^{n}-1$. The polynomial $x^{n}-1$ has the $n$ distinct roots $\zeta_k$ and no repeated factor, so it is square-free.

**The minimal polynomial of $H$ divides a square-free polynomial, hence $H$ is diagonalisable.** If $H^{n}=I$ then $H$ satisfies $x^{n}-1$, whose roots are simple; the minimal polynomial therefore has simple roots, and a matrix whose minimal polynomial has simple roots is diagonalisable. Its eigenvalues lie in $\{\zeta_1,\dots,\zeta_n\}$.

**Simple spectrum means $n$ distinct eigenvalues.** Since there are exactly $n$ roots and $n$ eigenvalues counted with multiplicity, simple spectrum is equivalent to $H$ having all $n$ roots of unity as eigenvalues, each once. Equivalently, the minimal polynomial of $H$ is exactly $x^{n}-1$.

**Standing hypothesis.** For the rest of the article $H^{n}=I$ and $H$ has simple spectrum. Write

$$
H=\sum_{k=1}^{n}\zeta_k P_k
$$

for the spectral decomposition, with $P_k$ the projection onto the eigenspace of $\zeta_k$.

## The Lagrange Projectors

**The projector of an eigenvalue is the Lagrange polynomial in $H$ that is $1$ at that eigenvalue and $0$ at the others.** Define

$$
P_k=\prod_{l\ne k}\frac{H-\zeta_l I}{\zeta_k-\zeta_l},\qquad k=1,\dots,n.
$$

Each factor is a polynomial in $H$, so $P_k$ is a polynomial in $H$; the product is the Lagrange interpolation polynomial of the indicator of $\zeta_k$ on the set $\{\zeta_1,\dots,\zeta_n\}$.

**Proposition.** The elements $P_k$ are idempotent, orthogonal and complete:

$$
P_k^{2}=P_k,\qquad P_kP_l=0\ (k\ne l),\qquad \sum_{k=1}^{n}P_k=I,
$$

and $HP_k=\zeta_kP_k$. Conversely, if a family with these properties is given, then $H=\sum_k\zeta_kP_k$ and the $P_k$ are recovered from $H$ by the formula above.

*Proof.* On the eigenspace of $\zeta_m$, every factor $(H-\zeta_lI)/(\zeta_k-\zeta_l)$ with $l\ne k$ acts as $(\zeta_m-\zeta_l)/(\zeta_k-\zeta_l)$; the product is $1$ when $m=k$ and $0$ otherwise, because one factor has numerator $0$ when $m=l\ne k$. Hence $P_k$ acts as the identity on the eigenspace of $\zeta_k$ and as $0$ on the others. The three properties and $HP_k=\zeta_kP_k$ follow. For the converse, $\sum_k\zeta_kP_k$ acts as $\zeta_m$ on the eigenspace of $P_m$, hence equals $H$, and the interpolation formula applied to that $H$ returns $P_k$. $\square$

**The projectors are canonical.** They are polynomials in $H$ with coefficients depending only on $n$, so they are fixed by $H$ alone. In particular they do not depend on any choice of basis, on any gauge, or on any second element.

**Idempotents, not nilpotents.** Each $P_k$ satisfies $P_k^{2}=P_k$ and $P_k\ne0$; the rank of $P_k$ is $1$ because the eigenvalue $\zeta_k$ is simple. The $P_k$ are the primitive idempotents of the frame. The nilpotents $E_{k,k+1}$ of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$* are different objects: they square to $0$, they are not polynomials in $H$, and they carry the gauge.

## The $\mathbb{Z}/n$ Grading

**Conjugation by $H$ grades the algebra by the $n$-th roots of unity.** For $X\in M_n(\mathbb{C})$ put

$$
\operatorname{Ad}_H(X)=HXH^{-1}.
$$

Since $H$ is invertible and $H^{-1}=\sum_k\zeta_k^{-1}P_k$, the operator $\operatorname{Ad}_H$ is diagonalisable with eigenvalues in $\{\zeta^{r}: r=0,\dots,n-1\}$. Define

$$
M^{(r)}=\{X:\operatorname{Ad}_H(X)=\zeta^{r}X\},\qquad r\in\mathbb{Z}/n\mathbb{Z}.
$$

**Proposition.** The algebra is the direct sum $M_n(\mathbb{C})=\bigoplus_{r\in\mathbb{Z}/n\mathbb{Z}}M^{(r)}$, and the product respects the grading,

$$
M^{(r)}M^{(s)}\subseteq M^{(r+s)}.
$$

*Proof.* The operator $\operatorname{Ad}_H$ is diagonalisable, so the eigenspaces span and intersect only at $0$. If $X\in M^{(r)}$ and $Y\in M^{(s)}$ then $\operatorname{Ad}_H(XY)=\operatorname{Ad}_H(X)\operatorname{Ad}_H(Y)=\zeta^{r+s}XY$. $\square$

**The graded pieces in Peirce form.** Since $H P_k=\zeta_kP_k$ and $P_kH=\zeta_kP_k$, an element $X\in P_kM_nP_l$ satisfies

$$
\operatorname{Ad}_H(X)=HXH^{-1}=\zeta_k\zeta_l^{-1}X=\zeta^{k-l}X.
$$

Hence

$$
M^{(r)}=\bigoplus_{k-l\equiv r\ (\mathrm{mod}\ n)}P_kM_nP_l.
$$

In particular $M^{(0)}$ is the centraliser of $H$, of dimension $n$: it consists of the matrices that preserve every eigenspace, and it is the algebra of polynomials in $H$. The grading is coarser than the Peirce decomposition; the latter has $n^{2}$ lines, the former $n$ pieces.

**The case $n=2$.** The grading is by $\pm1$: $M^{(0)}$ is the centraliser of $H$, of dimension $2$, and $M^{(1)}$ is the off-diagonal part, of dimension $2$. The four Peirce lines of the biquaternion frame are the two lines inside $M^{(0)}$ and the two inside $M^{(1)}$.

## The Root Set and Its Dimension

**The roots of order $n$ with simple spectrum form one orbit of $PGL_n(\mathbb{C})$.** Let

$$
\mathcal{R}_n=\{H\in M_n(\mathbb{C}): H^{n}=I,\ \text{the eigenvalues of $H$ are distinct}\}.
$$

$PGL_n(\mathbb{C})$ acts on $\mathcal{R}_n$ by conjugation, $H\mapsto SHS^{-1}$. Every $H\in\mathcal{R}_n$ is diagonalisable to $H_0=\operatorname{diag}(1,\zeta,\zeta^{2},\dots,\zeta^{n-1})$, so the action is transitive. The stabiliser of $H_0$ in $PGL_n(\mathbb{C})$ is the image of the diagonal torus: if $S$ commutes with $H_0$ and $H_0$ has distinct eigenvalues, then $S$ preserves each eigenspace, hence is diagonal. That image has dimension $n-1$. Therefore

$$
\mathcal{R}_n\cong PGL_n(\mathbb{C})/T,\qquad \dim_{\mathbb{C}}\mathcal{R}_n=n^{2}-1-(n-1)=n(n-1).
$$

The real dimension is $2n(n-1)$.

**The count in the two cases that matter.** For $n=2$,

$$
\dim_{\mathbb{R}}\mathcal{R}_2=2\cdot2\cdot1=4,
$$

which is the four real parameters of the biquaternion root $\tilde\Xi$ with $\tilde\Xi^{2}=e_t$. For $n=3$, $\dim_{\mathbb{R}}\mathcal{R}_3=12$; for $n=4$, $24$; for $n=5$, $40$; for $n=6$, $60$. These are the dimensions of the root in the five-article count of each category.

**The root is not a frame.** A frame modulo overall scale has complex dimension $n^{2}-1$, and $\mathcal{R}_n$ has dimension $n(n-1)$. The difference,

$$
(n^{2}-1)-n(n-1)=n-1,
$$

is the gauge of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*: one complex parameter per simple nilpotent. For $n=2$ the root contributes $4$ real dimensions and the gauge $2$, which is the six-dimensional basis of the biquaternion frame.

## The Root of $+1$ and the Biquaternion Case

**At $n=2$ the construction is the biquaternion frame.** The roots are $+1$ and $-1$, and

$$
P_{+}=\frac{I+H}{2},\qquad P_{-}=\frac{I-H}{2},\qquad H=P_{+}-P_{-}.
$$

These are exactly the idempotents $\tilde\Pi_\pm=(e_t\pm\tilde\Xi)/2$ of the biquaternion article, with $H=\tilde\Xi$ and $I=e_t$. The root of $+1$ is therefore not a separate principle: it is the order-two case of one root of order $n$.

**The older "second root" is the gauge, not a second primitive.** The biquaternion frame was sometimes presented as a root of $+1$ together with a second root anticommuting with it. That presentation is correct as a description of a normalised frame but wrong as a description of the primitive data. The second element does not produce new idempotents: the two idempotents are already produced by the first root. What the second element supplies is a vector in each mixed Peirce line, that is, a normalisation of the nilpotents, and that data is the gauge parameter $\lambda$ of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*. The construction is root-first: one root, then the gauge. There is no primitive root pair.

**What changes for $n>2$.** For $n\ge3$ there is no second root at all. One root of order $n$ produces $n$ idempotents and $n$ Peirce lines directly. The analogue of the missing normalisation is the $(n-1)$-parameter gauge, not a pair of roots.

## An Explicit Example: the Cyclic Shift

**The cyclic shift has the $n$-th roots of unity as eigenvalues, and its Lagrange projectors are the Fourier projectors.** Let $C$ act on $\mathbb{C}^{n}$ with basis $e_1,\dots,e_n$ by

$$
Ce_j=e_{j-1},\qquad j\in\mathbb{Z}/n\mathbb{Z}\quad(e_0=e_n).
$$

Then $C^{n}=I$. The vector

$$
v_k=\sum_{j=1}^{n}\zeta^{(k-1)(j-1)}e_j
$$

satisfies

$$
Cv_k=\sum_{j=1}^{n}\zeta^{(k-1)(j-1)}e_{j-1}=\sum_{j=1}^{n}\zeta^{(k-1)j}e_j=\zeta^{k-1}v_k,
$$

with the indices read modulo $n$, so $v_k$ is an eigenvector of eigenvalue $\zeta_k=\zeta^{k-1}$, and the $n$ vectors $v_k$ are independent (they form the discrete Fourier basis). The spectrum is simple, and

$$
P_k=\frac{1}{n}v_kv_k^{*}=\frac{1}{n}\sum_{j=1}^{n}\zeta^{-(k-1)(j-1)}C^{j-1}.
$$

The second expression is the Lagrange formula evaluated on $C$: the characters of $\mathbb{Z}/n\mathbb{Z}$ are orthogonal, and $\frac1n\sum_{j=1}^{n}\zeta^{(j-1)(l-k)}=\delta_{kl}$.

For $n=2$ this is $C=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $P_\pm=\tfrac12(I\pm C)$, the biquaternion case again. For $n=3$ the three projectors are the rank-one matrices $\tfrac13 v_kv_k^{*}$ with $v_k=(1,\zeta^{k-1},\zeta^{2(k-1)})^{\mathsf T}$, and $C=P_1+\zeta P_2+\zeta^{2}P_3$.

**The example shows that the root need not be diagonal.** The shift is not diagonal, its projectors are not the coordinate matrices $E_{kk}$, and the frame they define is the Fourier frame. The construction depends on the root, not on a choice of basis.

## Summary

A root $H$ of order $n$ with simple spectrum is diagonalisable with the $n$ roots of unity as eigenvalues, and the Lagrange polynomials in $H$ produce $n$ primitive orthogonal idempotents $P_k$, complete and summing to $I$, with $H=\sum_k\zeta_kP_k$. The root grades the algebra by $\mathbb{Z}/n$, with $M^{(r)}=\bigoplus_{k-l\equiv r}P_kM_nP_l$ and $M^{(r)}M^{(s)}\subseteq M^{(r+s)}$. The root set is $PGL_n(\mathbb{C})/T$ of complex dimension $n(n-1)$; the remaining $n-1$ complex dimensions of a frame are the gauge. At $n=2$ the root is the biquaternion root of $+1$, and the older "second root" is the gauge, not a second primitive.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\zeta=e^{2\pi i/n}$ | the primitive $n$-th root of unity |
| $\zeta_k=\zeta^{k-1}$ | the $n$ roots of $x^{n}-1$ |
| $H$ | a root, $H^{n}=I$ with simple spectrum |
| $P_k$ | the Lagrange projector of $\zeta_k$, a polynomial in $H$ |
| $M^{(r)}$ | the graded piece on which $\operatorname{Ad}_H$ acts by $\zeta^{r}$ |
| $\mathcal{R}_n$ | the set of roots of order $n$ with simple spectrum |
| $T$ | the diagonal torus, the stabiliser of $\operatorname{diag}(1,\zeta,\dots,\zeta^{n-1})$ |
| $C$ | the cyclic shift, the example with Fourier projectors |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral decomposition and the Lagrange interpolation formula for matrices.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, orthogonal families and Peirce decompositions.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the ambient algebra and its groups.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the lines that the idempotents produce.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the vectors and the gauge that complete the root to a frame.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion case at $n=2$.
- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), the case $n=3$.
- [Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), the case $n=4$.
- [Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), the case $n=5$.
- [Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m6c.html), the case $n=6$.
