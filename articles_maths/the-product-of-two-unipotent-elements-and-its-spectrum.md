# __The Product of Two Unipotent Elements and Its Spectrum__

## Introduction

The unipotent elements of the biquaternion algebra are the elements $U=e_t+\vec\Upsilon$ with $\vec\Upsilon$ a pure nilpotent, $\vec\Upsilon^2=0$; the element is non-trivial when $\vec\Upsilon\neq0$. They are units of norm one, their spectrum is the double eigenvalue $1$, and the non-trivial ones have minimal polynomial $(X-1)^2$. The product of two non-trivial unipotents is again a unit of norm one, but it is not usually unipotent. This article computes its spectrum and shows that one complex number decides it.

Let $U_i=e_t+\vec\Upsilon_i$ and $T=U_1U_2$. Put $t=\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)$, the trace of the product of the two nilpotent parts. Then

$$
p_T(\lambda)=\lambda^2-(2+t)\lambda+1,
$$

with discriminant $\Delta=t(t+4)$, scalar part $Q_t=1+t/2$ and vector square $B^2(T)=-t(t+4)/4$. The product is defective exactly at $t=0$ and $t=-4$, with the scalar exception $T=e_t$ at $t=0$; otherwise it is regular. On the regular set, the spectrum is on the unit circle exactly when $t$ is real and $-4<t<0$, real and reciprocal when $t$ is real and $t>0$ or $t<-4$, and non-real and reciprocal when $t$ is not real. For real $t$, the sign of $t$ alone does not decide the type: the type is fixed by whether $t$ lies in $(-4,0)$ or outside it, equivalently by the sign of $t(t+4)$, and the sign of $t$ then separates the positive real branch from the negative one.

The two examples show two of the regular types. With $t=-1$ the product has eigenvalues $e^{\pm i\pi/3}$; with $t=1$ it has eigenvalues $(3\pm\sqrt5)/2$. The two values differ only in the pairing of the two nilpotent parts. The article also proves that every element of the norm-one group except $-e_t$ is a product of two non-trivial unipotent elements, and that every element of the unit group is a central scalar times an element of the norm-one slice.

The product law on the spectral-degenerate sector, which uses the pairing $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$, is *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*, §*The Group Law*; the spectral criterion, the characteristic polynomial and the cone are *The Spectrum*; the norm, the norm-one group and the matrix model are *The N-Regular Sector* and *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The relation $t=-2s$ is the bridge between the two computations, and nothing of the cited articles is reproved here.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The **quaternionic norm**, written $N$, is

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

and the matrix model is fixed by

$$
\mathsf{M}_2(e_t)=\mathrm I_2,\qquad
\mathsf{M}_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf{M}_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf{M}_2(\vec e_z)=-i\sigma_3.
$$

The trace is $\operatorname{Tr}$, with $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t=2\operatorname{Sc}\tilde Q$; for $\tilde Q\in\mathbb{B}$ we write $\operatorname{Tr}\tilde Q$ for $\operatorname{Tr}\mathsf{M}_2(\tilde Q)$. The determinant is $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$, and we write $\det\tilde Q$ for it. The **norm-one group** is

$$
\mathbb{B}^{\times}_1=\{\tilde Q:N(\tilde Q)=1\}\cong SL_2(\mathbb{C}).
$$

A **pure nilpotent** is a vector $\vec\Upsilon=\upsilon_x\vec e_x+\upsilon_y\vec e_y+\upsilon_z\vec e_z$ with $\vec\Upsilon^2=-B^2e_t=0$; it is **non-zero** when $\vec\Upsilon\neq0$. The dot product is $\vec\Upsilon_1\cdot\vec\Upsilon_2=\sum_k\upsilon_{1k}\upsilon_{2k}$, and $\operatorname{Sc}(\vec\Upsilon_1\vec\Upsilon_2)=-\vec\Upsilon_1\cdot\vec\Upsilon_2$. A **unipotent** element is $U=e_t+\vec\Upsilon$ with $\vec\Upsilon$ a pure nilpotent; it is **non-trivial** when $\vec\Upsilon\neq0$. An element is **regular** (spectrally regular) when $B^2\neq0$, that is when it is semisimple with two distinct eigenvalues, and **defective** when it is not semisimple, that is when $B^2=0$ and $\vec Q\neq0$. The **spectral-degenerate cone** is $\mathcal S=\{B^2=0\}$, and the **null cone** is $\mathcal N=\{N=0\}$. The algebra, the norm and the cone are *The Biquaternion Algebra*, *N-Regularity and N-Degeneracy in the Biquaternion Algebra* and *The Spectrum*.

## The Norm-One Slice and the Unipotent Elements

**The spectral criterion on the slice.** For a general element $\tilde Q=Q_te_t+\vec Q$ the characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2-2Q_tX+N(\tilde Q),
$$

with discriminant $-4B^2$ and eigenvalues $Q_t\pm iB$. On the norm-one slice $N=1$ the constant term is one, so

$$
p_{\tilde Q}(X)=X^2-2Q_tX+1,\qquad \Delta=4(Q_t^2-1)=-4B^2.
$$

The element is defective exactly when $B^2=0$ and $\vec Q\neq0$. On the slice this forces $Q_t^2=1$, hence $Q_t=\pm1$. The part $Q_t=1$ consists of the unipotents $e_t+\vec\Upsilon$, and the part $Q_t=-1$ consists of their negatives, $-e_t+\vec\Upsilon=-(e_t-\vec\Upsilon)$.

The table lists the $B^2=0$ part of the norm-one slice; in the last two rows $\vec\Upsilon$ is a non-zero pure nilpotent.

| element | $Q_t$ | $B^2$ | spectrum | minimal polynomial |
|---|---|---|---|---|
| $e_t$ | $1$ | $0$ | $\{1\}$ | $X-1$ |
| $e_t+\vec\Upsilon$ | $1$ | $0$ | $\{1\}$ | $(X-1)^2$ |
| $-e_t$ | $-1$ | $0$ | $\{-1\}$ | $X+1$ |
| $-e_t+\vec\Upsilon$ | $-1$ | $0$ | $\{-1\}$ | $(X+1)^2$ |

The two signs are exchanged by the central element $-e_t$, which multiplies the spectrum by $-1$ and leaves the defectivity unchanged; the classification of a single element is therefore the same on the two parts. The products computed below are products of two elements of the $Q_t=1$ part; the image theorem covers the rest of the group. The product of two non-trivial unipotents is again in the norm-one group, and the rest of the article computes its spectrum.

## The Product and Its Characteristic Polynomial

**Theorem (the product).** Let $\vec\Upsilon_1,\vec\Upsilon_2$ be non-zero pure nilpotents, $U_i=e_t+\vec\Upsilon_i$, $T=U_1U_2$, and $t=\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)$. Then

(i) $T=e_t+\vec\Upsilon_1+\vec\Upsilon_2+\vec\Upsilon_1\vec\Upsilon_2$;

(ii) $\operatorname{Tr}T=2+t$ and $\det T=1$;

(iii) the characteristic polynomial is

$$
p_T(\lambda)=\lambda^2-(2+t)\lambda+1,
$$

with discriminant $\Delta=t(t+4)$;

(iv) the scalar part and the vector square are

$$
Q_t=1+\frac t2,\qquad B^2(T)=-\frac{t(t+4)}4;
$$

(v) with $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$, one has $t=-2s$ and

$$
B^2(T)=s(2-s).
$$

*Proof.* The expansion is the product. Since $\vec\Upsilon_i$ is a pure vector, $\operatorname{Tr}\vec\Upsilon_i=2\operatorname{Sc}\vec\Upsilon_i=0$, and since $\vec\Upsilon_i^2=0$, $\det U_i=N(U_i)=1$. Hence

$$
\operatorname{Tr}T=\operatorname{Tr}(e_t)+\operatorname{Tr}(\vec\Upsilon_1)+\operatorname{Tr}(\vec\Upsilon_2)+\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)=2+t,
\qquad
\det T=\det U_1\det U_2=1.
$$

The characteristic polynomial of a $2\times2$ matrix is $\lambda^2-\operatorname{Tr}T\,\lambda+\det T$, which gives (iii), and its discriminant is $(2+t)^2-4=t(t+4)$. The scalar part is half the trace, $Q_t=1+t/2$. The product is a unit of norm one, because the norm is multiplicative and $N(U_i)=1$; hence $B^2(T)=N(T)-Q_t^2=1-Q_t^2=-t(t+4)/4$. Finally, $\operatorname{Sc}(\vec\Upsilon_1\vec\Upsilon_2)=-\vec\Upsilon_1\cdot\vec\Upsilon_2$ gives $t=2\operatorname{Sc}(\vec\Upsilon_1\vec\Upsilon_2)=-2s$, and substitution gives $B^2(T)=s(2-s)$.

**Remark (the product law on the sector).** For $\tilde Q_i=Q_{ti}(e_t+\vec\Upsilon_i)$, *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*, §*The Group Law*, proves

$$
B^2(\tilde Q_1\tilde Q_2)=Q_{t1}^2Q_{t2}^2\,s(2-s),\qquad s=\vec\Upsilon_1\cdot\vec\Upsilon_2.
$$

On the norm-one slice $Q_{t1}=Q_{t2}=1$, and $t=-2s$; the two formulas agree. The sector's criterion that the product stays on the spectral-degenerate cone exactly when $s=0$ or $s=2$ is the present criterion $t=0$ or $t=-4$.

## The Criterion

**Theorem (defective or regular).** With $T=U_1U_2$ and $t=\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)$:

(i) if $t\notin\{0,-4\}$, then $T$ is regular, with two distinct eigenvalues;

(ii) if $t=0$, then $T$ has the single eigenvalue $1$; it is $e_t$ exactly when $\vec\Upsilon_2=-\vec\Upsilon_1$, and otherwise it is a non-trivial unipotent, hence defective;

(iii) if $t=-4$, then $T$ has the single eigenvalue $-1$; it is $-e_t$ times a non-trivial unipotent, hence defective, and $T=-e_t$ is impossible.

*Proof.* (i) The discriminant $t(t+4)$ is non-zero, so the two roots of $p_T$ are distinct; a $2\times2$ matrix with distinct eigenvalues is diagonalisable, hence semisimple.

(ii) For $t=0$, $p_T(\lambda)=(\lambda-1)^2$. A semisimple element with this spectrum is $e_t$: a diagonalisable matrix with both eigenvalues $1$ is the identity. If $T=e_t$, then $U_2=U_1^{-1}=e_t-\vec\Upsilon_1$, so $\vec\Upsilon_2=-\vec\Upsilon_1$; conversely this choice gives $T=e_t$. If $T\neq e_t$, the minimal polynomial is $(X-1)^2$, so $T-e_t$ is a non-zero nilpotent and $T$ is a non-trivial unipotent.

(iii) For $t=-4$, $p_T(\lambda)=(\lambda+1)^2$. A semisimple element with this spectrum is $-e_t$. If $T=-e_t$, then $U_2=-U_1^{-1}=-e_t+\vec\Upsilon_1$, whose scalar part is $-1$, but $U_2=e_t+\vec\Upsilon_2$ has scalar part $1$; contradiction. Hence $T\neq-e_t$, the minimal polynomial is $(X+1)^2$, and $T=-e_t+M$ with $M^2=0$, $M\neq0$, that is $T=-(e_t-M)$ with $e_t-M$ unipotent.

The two roots therefore carry different exceptions.

| $t$ | $p_T(\lambda)$ | $T$ | type |
|---|---|---|---|
| $t\notin\{0,-4\}$ | two distinct roots | regular | semisimple |
| $t=0$, $\vec\Upsilon_2=-\vec\Upsilon_1$ | $(\lambda-1)^2$ | $e_t$ | scalar |
| $t=0$, $\vec\Upsilon_2\neq-\vec\Upsilon_1$ | $(\lambda-1)^2$ | non-trivial unipotent | defective |
| $t=-4$ | $(\lambda+1)^2$ | $-e_t$ times a non-trivial unipotent | defective |

## The Three Regular Types

**Theorem (the regular spectrum).** Let $t\notin\{0,-4\}$. The eigenvalues of $T$ are

$$
\lambda_\pm=1+\frac t2\pm\frac12\sqrt{t(t+4)},\qquad \lambda_+\lambda_-=1.
$$

(i) If $t$ is real and $-4<t<0$, the eigenvalues are non-real conjugates on the unit circle, $\lambda_-=\bar\lambda_+=\lambda_+^{-1}$; this is the **unit-circle type**.

(ii) If $t$ is real and $t>0$ or $t<-4$, the eigenvalues are real and reciprocal; they are both positive for $t>0$ and both negative for $t<-4$; this is the **real type**.

(iii) If $t$ is not real, the eigenvalues are non-real and reciprocal, with $\lvert\lambda_\pm\rvert\neq1$; this is the **non-real type**.

*Proof.* The formula is the quadratic formula for $p_T$, and the product of the roots is the constant term, one.

(i) For real $t$ in $(-4,0)$, $\Delta=t(t+4)<0$, so the roots are non-real conjugates; a conjugate pair with product one has modulus one.

(ii) For real $t$ outside $[-4,0]$, $\Delta>0$, so the roots are real and distinct; their product is one, so they are reciprocal. For $t>0$, $Q_t=1+t/2>1$ and both roots $Q_t\pm\sqrt{Q_t^2-1}$ are positive; for $t<-4$, $Q_t<-1$ and both are negative.

(iii) If $t$ is not real, the roots cannot be real, since their sum $2+t=2Q_t$ would then be real. They are reciprocal because the product is one. If $\lvert\lambda\rvert=1$, then $1/\lambda=\bar\lambda$, so the two roots are $\lambda$ and $\bar\lambda$, and their sum $2Q_t$ is real, which forces $t$ real; contradiction. Hence $\lvert\lambda\rvert\neq1$.

| $t$ | $Q_t$ | spectrum | type |
|---|---|---|---|
| real, $-4<t<0$ | $-1<Q_t<1$ | $Q_t\pm iB$, $\lvert\lambda\rvert=1$ | unit circle |
| real, $t>0$ | $Q_t>1$ | real, reciprocal, positive | real |
| real, $t<-4$ | $Q_t<-1$ | real, reciprocal, negative | real |
| not real | not real | non-real, reciprocal, $\lvert\lambda\rvert\neq1$ | non-real |

**Remark (the special line $t=-2+ib$).** On this line, $Q_t=ib/2$ is purely imaginary and $B^2=1+b^2/4>0$ is real positive, but the eigenvalues are $i(b/2\pm\sqrt{1+b^2/4})$, purely imaginary and reciprocal. They are not on the unit circle unless $b=0$. Thus $B^2>0$ alone does not imply the unit-circle type; the reality of $Q_t$ is also needed. For the product, $Q_t$ is real exactly when $t$ is real.

## The Sign of the Pairing

The invariant $t$ is the trace of the product of the two nilpotent parts; the invariant $s=\vec\Upsilon_1\cdot\vec\Upsilon_2=-t/2$ is their pairing, the one used in the product law on the sector. In terms of $s$, the criterion reads as follows.

| $s$ | $t=-2s$ | spectrum | type |
|---|---|---|---|
| real, $s<0$ | $t>0$ | real, reciprocal, positive | real, positive |
| real, $0<s<2$ | $-4<t<0$ | unit circle | unit circle |
| real, $s>2$ | $t<-4$ | real, reciprocal, negative | real, negative |
| not real | not real | non-real, reciprocal | non-real |
| $s=0$ | $t=0$ | $\{1\}$ | trivial or non-trivial unipotent |
| $s=2$ | $t=-4$ | $\{-1\}$ | $-e_t$ times a non-trivial unipotent |

The sign of $s$ alone does not decide the type. It is positive on $(0,2)$ and on $(2,\infty)$, which give the unit-circle and the real types respectively; it is negative on $(-\infty,0)$, which gives the real type. The type is fixed by whether $s$ lies in $(0,2)$ or outside it, equivalently by the sign of $s(2-s)$ when $s$ is real; the sign of $s$ then separates the two real branches. Since $B^2(T)=s(2-s)$, the type is read off the sign of $B^2(T)$ on the real line away from the two roots.

In particular, the statement that a positive pairing gives a real spectrum and a negative pairing a unit-circle spectrum is false as stated: the positive interval $(0,2)$ gives the unit-circle type, and the positive interval $(2,\infty)$ gives the real type. The correct statement is that the unit-circle type is the interval $0<s<2$, the real type is $s<0$ or $s>2$, and the two endpoints are the scalar and defective roots.

## Two Examples

### A Unit-Circle Product

Take

$$
\vec\Upsilon_1=\frac i2\vec e_x-\frac12\vec e_y,\qquad
\vec\Upsilon_2=-\frac i2\vec e_x-\frac12\vec e_y.
$$

Both are pure nilpotents: each has $B^2=(i/2)^2+(-1/2)^2=0$, so $\vec\Upsilon_i^2=0$. Their pairing is

$$
s=\vec\Upsilon_1\cdot\vec\Upsilon_2=\frac i2\left(-\frac i2\right)+\left(-\frac12\right)\left(-\frac12\right)=\frac12,
$$

hence $t=-1$. The unipotents are

$$
U_1=e_t+\frac i2\vec e_x-\frac12\vec e_y,\qquad
U_2=e_t-\frac i2\vec e_x-\frac12\vec e_y,
$$

with matrix images

$$
\mathsf{M}_2(U_1)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(U_2)=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
$$

The product is

$$
T=U_1U_2=\frac12e_t-\vec e_y-\frac i2\vec e_z,\qquad
\mathsf{M}_2(T)=\begin{pmatrix}0&1\\-1&1\end{pmatrix}.
$$

Its invariants are $Q_t=1/2$, $B^2(T)=3/4$, $N(T)=1$, and its characteristic polynomial is

$$
p_T(\lambda)=\lambda^2-\lambda+1,
$$

with eigenvalues $\lambda_\pm=(1\pm i\sqrt3)/2=e^{\pm i\pi/3}$. The product is regular and of unit-circle type.

### A Real Product

Keep $\vec\Upsilon_1$ and replace the second nilpotent by

$$
\vec\Upsilon_3=\frac i2\vec e_x+\frac12\vec e_y=-\vec\Upsilon_2.
$$

It is a pure nilpotent, and

$$
s=\vec\Upsilon_1\cdot\vec\Upsilon_3=\frac i2\cdot\frac i2+\left(-\frac12\right)\frac12=-\frac12,
$$

hence $t=1$. The unipotent is

$$
U_3=e_t+\frac i2\vec e_x+\frac12\vec e_y,\qquad
\mathsf{M}_2(U_3)=\begin{pmatrix}1&0\\1&1\end{pmatrix},
$$

and the product is

$$
T_3=U_1U_3=\frac32e_t+i\vec e_x+\frac i2\vec e_z,\qquad
\mathsf{M}_2(T_3)=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
$$

Its invariants are $Q_t=3/2$, $B^2(T_3)=-5/4$, $N(T_3)=1$, and its characteristic polynomial is

$$
p_{T_3}(\lambda)=\lambda^2-3\lambda+1,
$$

with eigenvalues $(3\pm\sqrt5)/2$. The product is regular and of real type.

| data | unit-circle example | real example |
|---|---|---|
| second nilpotent | $\vec\Upsilon_2=-\frac i2\vec e_x-\frac12\vec e_y$ | $\vec\Upsilon_3=\frac i2\vec e_x+\frac12\vec e_y$ |
| $s$ | $1/2$ | $-1/2$ |
| $t$ | $-1$ | $1$ |
| product | $\frac12e_t-\vec e_y-\frac i2\vec e_z$ | $\frac32e_t+i\vec e_x+\frac i2\vec e_z$ |
| $p_T$ | $\lambda^2-\lambda+1$ | $\lambda^2-3\lambda+1$ |
| spectrum | $e^{\pm i\pi/3}$ | $(3\pm\sqrt5)/2$ |
| type | unit circle | real |

## The Two Roots

### The Identity at $t=0$

At $t=0$ the product is $e_t$ or a non-trivial unipotent. Both occur, and the difference is the inverse:

- with $U_2=U_1^{-1}=e_t-\vec\Upsilon_1$, the product is $T=e_t$;
- with $U_2=U_1$, the product is $T=e_t+2\vec\Upsilon_1$, a non-trivial unipotent.

Both have $s=0$, characteristic polynomial $(\lambda-1)^2$, norm one and scalar part one; they differ in the minimal polynomial, $X-1$ against $(X-1)^2$. The root $t=0$ is therefore not a defective locus without exception: it is the coalescence of the scalar $e_t$ and the unipotent Jordan block.

### The Second Root at $t=-4$

A witness is

$$
\vec\Upsilon_1=\frac i2\vec e_x-\frac12\vec e_y,\qquad
\vec\Upsilon_4=-\frac32i\vec e_x-\frac52\vec e_y+2i\vec e_z.
$$

The second is a pure nilpotent, because

$$
\left(-\frac32i\right)^2+\left(-\frac52\right)^2+(2i)^2=-\frac94+\frac{25}4-4=0,
$$

and its pairing with $\vec\Upsilon_1$ is

$$
s=\frac i2\left(-\frac32i\right)+\left(-\frac12\right)\left(-\frac52\right)=\frac34+\frac54=2,
$$

hence $t=-4$. The product is

$$
T_4=U_1U_4=-e_t-2i\vec e_x-2\vec e_y=-\bigl(e_t+2i\vec e_x+2\vec e_y\bigr),
$$

and the bracket is unipotent, since the square of its vector part is zero. So $T_4$ is $-e_t$ times a non-trivial unipotent. The scalar $-e_t$ itself is not a product: if $U_1U_2=-e_t$, then $U_2=-U_1^{-1}=-e_t+\vec\Upsilon_1$, whose scalar part is $-1$, not $1$.

## The Image of the Product Map

**Theorem (the image).** Every element of the norm-one group except $-e_t$ is a product of two non-trivial unipotent elements. The element $-e_t$ is not.

*Proof.* Work in $M_2(\mathbb{C})$, with $I=\mathrm I_2$. If $g=-I$, suppose $g=U_1U_2$ with $U_i=I+K_i$, $K_i^2=0$. Then $U_2=-U_1^{-1}=-I+K_1$, whose trace is $-2$, while $U_2$ has trace $2$; contradiction. If $g=I$, take any non-zero nilpotent $K$ and write $I=(I+K)(I-K)$. If $g$ is unipotent and $g\neq I$, put $K=g-I$; then $K^2=0$, $K\neq0$, and $g=(I+K/2)^2$. Otherwise $g$ is neither scalar nor unipotent, so $\operatorname{Tr}g\neq2$ and $g$ is not scalar. The linear form $\varphi(K)=\operatorname{Tr}(Kg)$ is non-zero on $\mathfrak{sl}_2$, because the trace pairing is non-degenerate and $g$ is not scalar. Since the nilpotent cone spans $\mathfrak{sl}_2$ (the remark below), $\varphi$ is non-zero at some nilpotent $K_0$; the cone is closed under scaling, so $K=\lambda K_0$ with $\lambda=(\operatorname{Tr}g-2)/\varphi(K_0)$ is a non-zero nilpotent with $\varphi(K)=\operatorname{Tr}g-2$. Put $U_1=I+K$ and $X=U_1^{-1}g=(I-K)g$. Then $\operatorname{Tr}X=\operatorname{Tr}g-\operatorname{Tr}(Kg)=2$ and $\det X=1$. If $X=I$, then $g=I+K$ is unipotent, contrary to the case; so $X\neq I$, and a non-scalar element of trace $2$ and determinant $1$ is unipotent. Hence $g=U_1X$ is a product of two unipotent elements. In each construction the two factors are non-trivial: the nilpotent $K$ is chosen non-zero, and in the last case $X\neq I$.

**Remark (the spanning of $\mathfrak{sl}_2$).** The matrices

$$
A_+=\begin{pmatrix}-1&1\\-1&1\end{pmatrix},\qquad
A_-=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}
$$

are nilpotent, and $A_- - A_+ = 2\operatorname{diag}(1,-1)$. Together with $E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $E_{21}=\begin{pmatrix}0&0\\1&0\end{pmatrix}$, which are also nilpotent, they span $\mathfrak{sl}_2$. Hence the nilpotent cone spans $\mathfrak{sl}_2$.

**Corollary.** The product map from pairs of non-trivial unipotent elements to the norm-one group is surjective onto $\mathbb{B}^{\times}_1\setminus\{-e_t\}$. In particular, every regular element and every defective element of the norm-one group occurs; the only element missed is the scalar $-e_t$.

## Scaling and the General Unit Group

The restriction to the norm-one slice loses nothing for defective elements. Every defective element of the unit group is of the form

$$
\tilde P=c\,U,\qquad c\in\mathbb{C}^{\times},\quad U=e_t+\vec\Upsilon,\quad \vec\Upsilon^2=0,\quad\vec\Upsilon\neq0,
$$

by *The N-Regular, Spectrally Degenerate Sector*, §*Definition and Characterisation*. For two such elements $\tilde P_i=c_iU_i$,

$$
\tilde P_1\tilde P_2=c_1c_2\,T,
$$

with $T=U_1U_2$ the product on the norm-one slice. The characteristic polynomial is

$$
p(\lambda)=\lambda^2-c_1c_2(2+t)\lambda+(c_1c_2)^2,
$$

the discriminant is $(c_1c_2)^2t(t+4)$, and the norm is $(c_1c_2)^2$. The discriminant vanishes exactly when $t(t+4)=0$, so the product is scalar or defective exactly at the two roots; the scalar exception at $t=0$ is scaled to $c_1c_2e_t$. The spectrum is scaled by the central factor $c_1c_2$: the modulus is multiplied by $\lvert c_1c_2\rvert$ and the argument is shifted by $\arg(c_1c_2)$. The unit-circle type is preserved only when $\lvert c_1c_2\rvert=1$, and the real/non-real dichotomy is preserved by a real scale but not in general by a non-real one. The three types are properties of the norm-one slice, and that is why the classification is stated there.

## Summary

The product of two non-trivial unipotent elements is a norm-one element whose spectrum is governed by the single number $t=\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)$. The characteristic polynomial is $\lambda^2-(2+t)\lambda+1$, the discriminant is $t(t+4)$, the scalar part is $1+t/2$, and the vector square is $-t(t+4)/4=s(2-s)$ with $s=\vec\Upsilon_1\cdot\vec\Upsilon_2=-t/2$.

The product is defective exactly at the two roots $t=0$ and $t=-4$, with the scalar exception $T=e_t$ at $t=0$; at $t=-4$ the product is always $-e_t$ times a non-trivial unipotent, and $-e_t$ itself never occurs. Off the roots the product is regular. The regular spectrum is on the unit circle exactly for real $t$ in $(-4,0)$, real and reciprocal for real $t$ in $(0,\infty)\cup(-\infty,-4)$, and non-real and reciprocal for non-real $t$.

The type is not fixed by the sign of $t$, nor by the sign of $s$. It is fixed by whether $t$ lies in $(-4,0)$ or outside it, equivalently by the sign of $t(t+4)$ for real $t$, equivalently by whether $s$ lies in $(0,2)$ or outside it. The sign of $t$ then separates the positive real branch from the negative one. The two examples $t=-1$ and $t=1$ illustrate two of the regular types.

Every element of the norm-one group except $-e_t$ is a product of two non-trivial unipotents. The general defective case reduces to the norm-one slice by the central scaling $\tilde P_i=c_iU_i$, which scales the spectrum and leaves the defectivity unchanged.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\mathbb{B}^{\times}_1=\{N=1\}$ | the norm-one group, $SL_2(\mathbb{C})$ |
| $\vec\Upsilon_i$ | a non-zero pure nilpotent, $\vec\Upsilon_i^2=0$ |
| $U_i=e_t+\vec\Upsilon_i$ | a non-trivial unipotent element |
| $T=U_1U_2$ | the product |
| $t=\operatorname{Tr}(\vec\Upsilon_1\vec\Upsilon_2)$ | the trace of the product of the nilpotent parts |
| $s=\vec\Upsilon_1\cdot\vec\Upsilon_2=-t/2$ | the pairing of the nilpotents |
| $p_T(\lambda)=\lambda^2-(2+t)\lambda+1$ | the characteristic polynomial of $T$ |
| $\Delta=t(t+4)=-4B^2(T)$ | the discriminant |
| $Q_t=1+t/2$ | the scalar part of $T$ |
| $B^2(T)=-t(t+4)/4=s(2-s)$ | the vector square of $T$ |
| $\operatorname{Tr}$ | the matrix trace, $\operatorname{Tr}\tilde Q=2Q_t$ |

## Further Reading

- [The N-Regular Sector](the-n-regular-sector.html), for the norm-one group, the matrix identification $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$ and the polar retraction.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the quaternionic norm, its zero locus and the two norm cases.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the unipotent elements, the scalar line and the Jordan part.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the group law on the sector, the product formula $B^2=Q_{t1}^2Q_{t2}^2s(2-s)$ and the two roots $s=0$ and $s=2$.
- [The Spectrum](the-spectrum.html), for the characteristic polynomial, the discriminant, the cone and the similarity classification.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the place of the defective elements in them.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the matrix model, the basis images and the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$.
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t$ and $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the pure nilpotents and the nilpotent stratum.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the defective elements, their Jordan form and their centraliser.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, the conjugation and the remarkable subspaces.
