# __Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$__

## Introduction

**Every matrix $A\in M_3(\mathbb{C})$ has a characteristic cubic $\chi_A(t)=t^{3}-\tau t^{2}+\sigma t-\delta$, and its three roots, counted with multiplicity, are the spectrum.** The spectral theorem for a single matrix is the Lagrange interpolation formula: when the spectrum is simple,

$$
P_k=\prod_{l\neq k}\frac{A-\lambda_l I}{\lambda_k-\lambda_l},
\qquad
A=\sum_{k=1}^{3}\lambda_k P_k,
\qquad
P_kP_l=\delta_{kl}P_k,
\qquad
\sum_k P_k=I .
$$

The $P_k$ are the **spectral projectors**; they are the idempotents of the spectral decomposition, and each has rank equal to the multiplicity of $\lambda_k$. When the spectrum is repeated, the Lagrange formula is replaced by the Riesz integral

$$
P_k=\frac{1}{2\pi i}\oint_{\gamma_k}(tI-A)^{-1}\,dt,
$$

with $\gamma_k$ a small circle around $\lambda_k$ separating it from the other eigenvalues. For $H$ with $H^{3}=I$ and simple spectrum, the spectral projectors are exactly the Lagrange idempotents $P_k=\prod_{l\neq k}(H-\zeta_l I)/(\zeta_k-\zeta_l)$ of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*; the root is the special case in which the eigenvalues are fixed at the cube roots of unity.

The article proves the Lagrange formula, identifies the projectors with the residues of the resolvent, treats the repeated and the Jordan cases, computes the root case explicitly, and relates the spectrum to the trace form, the spectral radius and the discriminant. The cubic and its discriminant are *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*; the Jordan classification is *The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$*.

## The Characteristic Cubic

**Definition.** For $A\in M_3(\mathbb{C})$ the **characteristic polynomial** is

$$
\chi_A(t)=\det(tI-A)=t^{3}-\tau t^{2}+\sigma t-\delta,
$$

where

$$
\tau=\operatorname{tr}A,\qquad
\sigma=\frac{1}{2}\big((\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\big),\qquad
\delta=\det A .
$$

**Proposition (Vieta).** If the eigenvalues are $\lambda_1,\lambda_2,\lambda_3$, counted with algebraic multiplicity, then

$$
\tau=\lambda_1+\lambda_2+\lambda_3,\qquad
\sigma=\lambda_1\lambda_2+\lambda_2\lambda_3+\lambda_3\lambda_1,\qquad
\delta=\lambda_1\lambda_2\lambda_3 .
$$

**Proof.** Expand $\det(tI-A)$ along the permutations of the symmetric group; the three terms give the three elementary symmetric functions of the eigenvalues, because the characteristic polynomial of an upper triangular matrix is $\prod(t-\lambda_i)$ and every matrix is triangularisable over $\mathbb{C}$. The coefficients are continuous in the entries, so the identity extends from the diagonalisable matrices to all matrices.

**The derivative and the discriminant.** The derivative is

$$
\chi_A'(t)=3t^{2}-2\tau t+\sigma,
$$

with critical points

$$
t_\pm=\frac{\tau\pm\sqrt{\tau^{2}-3\sigma}}{3}.
$$

The **discriminant** is

$$
\Delta=\prod_{i<j}(\lambda_i-\lambda_j)^{2}
=\tau^{2}\sigma^{2}-4\sigma^{3}-4\tau^{3}\delta-27\delta^{2}+18\tau\sigma\delta .
$$

The spectrum is simple exactly when $\Delta\neq0$. When $\Delta=0$ two eigenvalues coincide, and the cubic has a double root; when in addition $\tau^{2}=3\sigma$ the three roots coincide and $\chi_A(t)=(t-\tau/3)^{3}$.

**Proof of the discriminant formula.** The resultant of $\chi$ and $\chi'$ is $\prod_i\chi'(\lambda_i)=\prod_i\prod_{j\neq i}(\lambda_i-\lambda_j)=(-1)^{3}\prod_{i<j}(\lambda_i-\lambda_j)^{2}$; evaluating the resultant of the cubic and its derivative gives the displayed polynomial. The sign is $(-1)^{3}=-1$ for degree $3$, and the formula is the standard one for a cubic.

**Worked example.** For

$$
A=\begin{pmatrix}2&1&0\\0&2&1\\0&0&3\end{pmatrix}
$$

one has $\tau=7$, $\sigma=16$, $\delta=12$, and

$$
\chi_A(t)=t^{3}-7t^{2}+16t-12=(t-2)^{2}(t-3).
$$

The discriminant is

$$
\Delta=49\cdot256-4\cdot4096-4\cdot343\cdot12-27\cdot144+18\cdot7\cdot16\cdot12
=12544-16384-16464-3888+24192=0,
$$

as it must be for a repeated root. The derivative $3t^{2}-14t+16$ has roots $t=2$ and $t=8/3$; the double root $2$ is a critical point, and $8/3$ lies between the roots $2$ and $3$.

## The Minimal Polynomial

**Definition.** The **minimal polynomial** $m_A$ is the monic polynomial of least degree with $m_A(A)=0$. It divides every polynomial that annihilates $A$; in particular $m_A\mid\chi_A$ by Cayley–Hamilton.

**Theorem.** The roots of $m_A$ are exactly the eigenvalues of $A$, and the exponent of $(t-\lambda)$ in $m_A$ is the size of the largest Jordan block of $A$ at $\lambda$. Hence:

- for a simple spectrum, $m_A=\chi_A=(t-\lambda_1)(t-\lambda_2)(t-\lambda_3)$;
- for a double eigenvalue $\lambda$ with a $2$-block and a simple eigenvalue $\mu$, $m_A=(t-\lambda)^{2}(t-\mu)$; with two $1$-blocks at $\lambda$, $m_A=(t-\lambda)(t-\mu)$;
- for a triple eigenvalue $\lambda$, $m_A=(t-\lambda)^{3}$ for one $3$-block, $m_A=(t-\lambda)^{2}$ for the type $2+1$, and $m_A=(t-\lambda)$ for the scalar $aI$.

A matrix is diagonalisable exactly when $m_A$ has distinct linear factors.

**Proof.** In Jordan form $A=\bigoplus_i J_{d_i}(\lambda_i)$. A polynomial $p$ annihilates the block $J_d(\lambda)$ exactly when $p(\lambda)=p'(\lambda)=\cdots=p^{(d-1)}(\lambda)=0$, that is, when $(t-\lambda)^{d}\mid p$. The least common multiple over the blocks is $\prod_{\lambda}(t-\lambda)^{\max_i d_i}$, which is $m_A$. The diagonalisability criterion is the corresponding statement that all blocks have size one.

**The projectors as polynomials.** Since $m_A=\prod_{\lambda}(t-\lambda)^{m_\lambda}$ is a product of coprime powers, the Chinese remainder theorem gives idempotents $E_\lambda\in\mathbb{C}[A]$ with $E_\lambda\equiv1\pmod{(t-\lambda)^{m_\lambda}}$ and $E_\lambda\equiv0\pmod{(t-\mu)^{m_\mu}}$ for $\mu\neq\lambda$. These are the Riesz projectors. When the spectrum is simple they are the Lagrange interpolants; at a double root the Hermite interpolant is the corresponding idempotent. Every spectral projector is therefore a polynomial in $A$, unique modulo $m_A$.

## The Resolvent and the Riesz Projectors

**The resolvent.** For $t$ not in the spectrum, the **resolvent** is

$$
R(t)=(tI-A)^{-1}=\frac{\operatorname{adj}(tI-A)}{\chi_A(t)} .
$$

Its entries are rational functions with poles exactly at the eigenvalues.

**The Riesz projector.** For an eigenvalue $\lambda_k$ of algebraic multiplicity $m_k$, let $\gamma_k$ be a positively oriented circle around $\lambda_k$ enclosing no other eigenvalue. The **Riesz projector** is

$$
P_k=\frac{1}{2\pi i}\oint_{\gamma_k}(tI-A)^{-1}\,dt .
$$

**Theorem.** The $P_k$ are idempotent, orthogonal, sum to $I$, commute with $A$, and cut out the generalised eigenspaces:

$$
P_k^{2}=P_k,\qquad
P_kP_l=0\ (k\neq l),\qquad
\sum_k P_k=I,\qquad
AP_k=P_kA,
$$

$$
\operatorname{im}P_k=\ker(A-\lambda_k I)^{m_k},\qquad
\operatorname{tr}P_k=m_k .
$$

Moreover

$$
A=\sum_k\big(\lambda_k P_k+N_k\big),\qquad
N_k=P_k(A-\lambda_k I)P_k,
$$

with $N_k$ nilpotent of degree at most $m_k$, and the $N_k$ commute with one another.

**Proof.** The resolvent satisfies the resolvent identity $R(t)-R(s)=-(t-s)R(t)R(s)$, and Cauchy's theorem gives $P_k^{2}=P_k$ and $P_kP_l=0$ for $k\neq l$; the sum over all $k$ is the contour integral of $R(t)$ around a large circle, which is $I$ because $R(t)\sim t^{-1}I$ at infinity. The commutation $AP_k=P_kA$ follows from $AR(t)=R(t)A$. On the generalised eigenspace $E_k=\ker(A-\lambda_k I)^{m_k}$, the operator $A-\lambda_k I$ is nilpotent, so $R(t)$ has a pole of order at most $m_k$ and the residue is the projector onto $E_k$ along the sum of the other generalised eigenspaces. The trace of $P_k$ is the dimension of $E_k$, which is $m_k$.

**The residue formula.** If the eigenvalues are simple, the residue at $\lambda_k$ of $R(t)$ is the Lagrange projector

$$
P_k=\prod_{l\neq k}\frac{A-\lambda_l I}{\lambda_k-\lambda_l},
$$

because the partial fraction decomposition of $R(t)$ is

$$
(tI-A)^{-1}=\sum_k\frac{P_k}{t-\lambda_k},
$$

and the coefficient of $(t-\lambda_k)^{-1}$ is the residue.

**Proof of the Lagrange formula.** Multiply the partial fraction decomposition by $t-\lambda_k$ and set $t=\lambda_k$: the left side becomes the residue $P_k$, and the right side becomes $P_k$ plus the terms $(t-\lambda_k)P_l/(t-\lambda_l)$ for $l\neq k$, which vanish at $t=\lambda_k$. On the other hand, the residue is the value at $\lambda_k$ of

$$
(t-\lambda_k)(tI-A)^{-1}
=\left(\prod_{l\neq k}(t-\lambda_l)\right)\left(\prod_{l\neq k}(A-\lambda_l I)\right)^{-1},
$$

so $P_k=\prod_{l\neq k}(A-\lambda_l I)\big/\prod_{l\neq k}(\lambda_k-\lambda_l)$.

**The polynomial form.** The projectors are polynomials in $A$ of degree at most $2$:

$$
P_k=\frac{1}{\chi_A'(\lambda_k)}\prod_{l\neq k}(A-\lambda_l I)
=\frac{1}{\chi_A'(\lambda_k)}\big(A^{2}-(\tau-\lambda_k)A+\mu_k I\big),
$$

where $\mu_k=\prod_{l\neq k}(-\lambda_l)$ is the product of the other two roots with sign, equal to $\delta/\lambda_k$ when $\lambda_k\neq0$, and $\chi_A'(\lambda_k)=\prod_{l\neq k}(\lambda_k-\lambda_l)$.

**Worked example.** For $A=\operatorname{diag}(1,2,4)$,

$$
P_1=\frac{(A-2I)(A-4I)}{(1-2)(1-4)}=\frac{(A-2I)(A-4I)}{3},
$$

and similarly

$$
P_2=\frac{(A-I)(A-4I)}{(2-1)(2-4)}=\frac{(A-I)(A-4I)}{-2},
\qquad
P_3=\frac{(A-I)(A-2I)}{(4-1)(4-2)}=\frac{(A-I)(A-2I)}{6}.
$$

Each $P_k$ is the diagonal matrix with $1$ in the $k$-th place and $0$ elsewhere, and $\sum_k\lambda_kP_k=A$. The denominators are the derivatives at the roots. Here $\chi_A(t)=(t-1)(t-2)(t-4)=t^{3}-7t^{2}+14t-8$, so $\chi_A'(t)=3t^{2}-14t+14$, and

$$
\chi_A'(1)=3,\qquad \chi_A'(2)=-2,\qquad \chi_A'(4)=6,
$$

which are exactly $3$, $-2$ and $6$, the denominators displayed above.

## The Simple Spectrum

**Theorem (Lagrange spectral decomposition).** Let $A$ have three distinct eigenvalues $\lambda_1,\lambda_2,\lambda_3$. Set

$$
P_k=\prod_{l\neq k}\frac{A-\lambda_l I}{\lambda_k-\lambda_l}.
$$

Then

$$
P_k^{2}=P_k,\qquad P_kP_l=0\ (k\neq l),\qquad \sum_{k=1}^{3}P_k=I,
$$

$$
A=\sum_{k=1}^{3}\lambda_k P_k,\qquad
\operatorname{tr}P_k=1,\qquad
\operatorname{rank}P_k=1 .
$$

**Proof.** The polynomial $p_k(t)=\prod_{l\neq k}(t-\lambda_l)/(\lambda_k-\lambda_l)$ is the Lagrange basis polynomial: $p_k(\lambda_k)=1$ and $p_k(\lambda_l)=0$ for $l\neq k$. For a diagonalisable matrix with these eigenvalues, $p_k(A)$ acts as $1$ on the $\lambda_k$ eigenspace and as $0$ on the other two, so $P_k$ is the projector onto the $\lambda_k$ eigenline. For a general matrix with simple spectrum, the same identities hold because both sides are polynomials in $A$ that agree on the three eigenlines, which span $\mathbb{C}^{3}$. The rank is $1$ because the eigenspace is one-dimensional, and the trace of a rank-one projector is $1$.

**The interpolation identity.** For any polynomial $f$ of degree at most $2$,

$$
f(A)=\sum_{k=1}^{3}f(\lambda_k)P_k .
$$

In particular the choice $f(t)=t$ gives $A=\sum\lambda_kP_k$, and $f(t)=1$ gives $\sum P_k=I$. For $f(t)=t^{m}$ with $m\ge3$, the identity still holds because $A^{3}=\tau A^{2}-\sigma A+\delta I$ by Cayley–Hamilton.

**Cayley–Hamilton.** The characteristic polynomial annihilates the matrix:

$$
A^{3}-\tau A^{2}+\sigma A-\delta I=0 .
$$

**Proof.** The adjugate identity $\operatorname{adj}(tI-A)(tI-A)=\chi_A(t)I$ is an identity of polynomials in $t$ with matrix coefficients; comparing coefficients gives the relation. Equivalently, the identity holds for diagonalisable matrices by the eigenvalue computation and extends by continuity.

**The rank-one case.** For $A$ with simple spectrum, each $P_k$ is a rank-one idempotent, hence of the form $u_k\varphi_k$ with $\varphi_k(u_k)=1$. In the eigenbasis,

$$
P_k=e_ke_k^{\mathsf T},\qquad
u_k=e_k,\qquad
\varphi_k=e_k^{\mathsf T}.
$$

The spectral decomposition is the resolution of the identity into three rank-one projectors, and it is the matrix form of the Lagrange interpolation of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*.

**Worked example.** For $A=\operatorname{diag}(1,2,4)$ the three projectors are $E_{11}$, $E_{22}$, $E_{33}$, and $A=1\cdot E_{11}+2\cdot E_{22}+4\cdot E_{33}$. For

$$
A=\begin{pmatrix}1&1&0\\0&2&1\\0&0&4\end{pmatrix}
$$

the projectors are not diagonal, but the identity $A=\sum\lambda_kP_k$ still holds, with each $P_k$ a polynomial in $A$ of degree $2$.

## The Repeated Spectrum

**The semisimple case.** If $A$ is diagonalisable with a repeated eigenvalue, say $\lambda_1=\lambda_2=\lambda$ and $\lambda_3=\mu$, the eigenspace of $\lambda$ is two-dimensional and the spectral projector is the projector onto it:

$$
P_\lambda=\frac{A-\mu I}{\lambda-\mu},
\qquad
P_\mu=I-P_\lambda=\frac{A-\lambda I}{\mu-\lambda}.
$$

These are the Hermite interpolation polynomials: $P_\lambda$ is the polynomial of degree $1$ that is $1$ at $\lambda$ and $0$ at $\mu$, evaluated at $A$.

**Proof.** On the $\lambda$-eigenspace, $(A-\mu I)/(\lambda-\mu)=(\lambda-\mu)/(\lambda-\mu)=1$; on the $\mu$-eigenspace it is $0$. Since $A$ is diagonalisable, these two eigenspaces span $\mathbb{C}^{3}$, and the displayed operator is the projector onto the first along the second. The second formula follows from $P_\lambda+P_\mu=I$.

**The Jordan case.** If $A$ has a Jordan block of size $2$ at $\lambda$ and a simple eigenvalue $\mu$, the spectral projector onto the generalised $\lambda$-eigenspace is the **Hermite interpolant**

$$
P_\lambda=I-\left(\frac{A-\lambda I}{\lambda-\mu}\right)^{2},
\qquad
P_\mu=\left(\frac{A-\lambda I}{\lambda-\mu}\right)^{2}=I-P_\lambda .
$$

Then

$$
A=\lambda P_\lambda+\mu P_\mu+N,\qquad
N=(A-\lambda I)P_\lambda,
\qquad
N^{2}=0 .
$$

**Proof.** The polynomial $p(t)=1-\big((t-\lambda)/(\lambda-\mu)\big)^{2}$ satisfies $p(\lambda)=1$, $p'(\lambda)=0$ and $p(\mu)=0$. On the generalised $\lambda$-eigenspace, $A-\lambda I$ is nilpotent of degree $2$, so $p(A)=I$ there; on the $\mu$-eigenspace, $p(\mu)=0$. Hence $p(A)$ is the projector onto the first generalised eigenspace along the second. The difference $A-\lambda P_\lambda-\mu P_\mu$ is $(A-\lambda I)P_\lambda$, supported on the generalised $\lambda$-eigenspace, and its square is $(A-\lambda I)^{2}P_\lambda=0$.

**Worked example.** For

$$
A=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix}
$$

one has $A-2I=\begin{pmatrix}0&1&0\\0&0&0\\0&0&1\end{pmatrix}$ and

$$
\left(\frac{A-2I}{2-3}\right)^{2}=(2I-A)^{2}
=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix},
$$

so

$$
P_2=I-(2I-A)^{2}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix},
\qquad
P_3=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}.
$$

Then $P_2^{2}=P_2$, $P_2P_3=0$, $P_2+P_3=I$, and

$$
2P_2+3P_3=\begin{pmatrix}2&0&0\\0&2&0\\0&0&3\end{pmatrix},
\qquad
N=A-2P_2-3P_3=E_{12},
\qquad
N^{2}=0 .
$$

The spectral decomposition is $A=2P_2+3P_3+N$, with a nilpotent part in the repeated eigenspace. The naive Lagrange formula $(A-3I)/(2-3)$ gives $3I-A=P_2-N$, which is not idempotent; the Hermite derivative condition is what removes the nilpotent part.

**The general multiplicity.** For an eigenvalue $\lambda$ of algebraic multiplicity $m$, the spectral projector is the Hermite interpolant of degree at most $2$ that equals $1$ at $\lambda$, has zero derivative there, and vanishes at the other eigenvalues. In size $3$ the only possibility beyond the simple case is $m=2$, and the formula above is the complete list. The triple eigenvalue $m=3$ occurs only for the scalar matrix, where the projector is $I$ and the nilpotent part is zero.

## The Root Case

**The root.** Let $H\in M_3(\mathbb{C})$ satisfy $H^{3}=I$ and have simple spectrum. Its eigenvalues are the three cube roots of unity

$$
\zeta_1=1,\qquad \zeta_2=\omega=e^{2\pi i/3},\qquad \zeta_3=\omega^{2}=e^{4\pi i/3},
$$

and its characteristic polynomial is $t^{3}-1$. The spectral projectors are

$$
P_k=\frac{H^{2}+\zeta_k H+\zeta_k^{2}I}{3\zeta_k^{2}}
=\frac{(H-\zeta_l I)(H-\zeta_m I)}{(\zeta_k-\zeta_l)(\zeta_k-\zeta_m)},
$$

where $\{k,l,m\}=\{1,2,3\}$.

**Proof.** The denominator is $\prod_{l\neq k}(\zeta_k-\zeta_l)=3\zeta_k^{2}$, computed from the identity $\prod_{l\neq k}(X-\zeta_l)=X^{2}+\zeta_kX+\zeta_k^{2}$ at $X=\zeta_k$, which gives $3\zeta_k^{2}$. The numerator is $(H-\zeta_l I)(H-\zeta_m I)=H^{2}-(\zeta_l+\zeta_m)H+\zeta_l\zeta_mI=H^{2}+\zeta_kH+\zeta_k^{2}I$, because $\zeta_l+\zeta_m=-\zeta_k$ and $\zeta_l\zeta_m=\zeta_k^{-1}=\zeta_k^{2}$. The Lagrange theorem then gives the projector.

**The spectral identities.** Since $H^{3}=I$, the interpolation identity for the polynomial $t^{3}$ gives

$$
H^{3}=\sum_k\zeta_k^{3}P_k=\sum_k P_k=I,
$$

and the identities for $t$ and $t^{2}$ give

$$
H=\sum_k\zeta_kP_k,\qquad
H^{2}=\sum_k\zeta_k^{2}P_k .
$$

The grading is the $\mathbb{Z}/3$ decomposition

$$
M_3=\bigoplus_{r\in\mathbb{Z}/3}M_3^{(r)},\qquad
M_3^{(r)}=\{X:HXH^{-1}=\omega^{r}X\}
=\bigoplus_{i-j\equiv r}P_iM_3P_j,
$$

with the indices read modulo $3$. The dimension of each summand is $3$, because there are three pairs $(i,j)$ with $i-j\equiv r$, and each block $P_iM_3P_j$ is one-dimensional.

**Worked example: the cyclic permutation.** Take

$$
H=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
\qquad
H^{2}=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
$$

Then

$$
P_1=\frac{H^{2}+H+I}{3}
=\frac{1}{3}\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix},
$$

$$
P_2=\frac{H^{2}+\omega H+\omega^{2}I}{3\omega^{2}}
=\frac{1}{3}\begin{pmatrix}1&\omega^{2}&\omega\\ \omega&1&\omega^{2}\\ \omega^{2}&\omega&1\end{pmatrix},
$$

$$
P_3=\frac{H^{2}+\omega^{2}H+\omega I}{3\omega}
=\frac{1}{3}\begin{pmatrix}1&\omega&\omega^{2}\\ \omega^{2}&1&\omega\\ \omega&\omega^{2}&1\end{pmatrix}.
$$

Each is idempotent, $P_kP_l=\delta_{kl}P_k$, $\sum_kP_k=I$, and

$$
P_1+\omega P_2+\omega^{2}P_3
=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}=H .
$$

The check of the $(1,2)$ entry is $1+\omega\cdot\omega^{2}+\omega^{2}\cdot\omega=1+1+1=3$, divided by $3$ gives $1$; the check of the $(1,3)$ entry is $1+\omega^{2}\cdot\omega^{2}+\omega\cdot\omega=1+\omega+\omega^{2}=0$. The three projectors are the Lagrange idempotents of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*, and their columns are the eigenvectors of $H$.

**The diagonal root.** For $H=\operatorname{diag}(1,\omega,\omega^{2})$ the projectors are $P_1=E_{11}$, $P_2=E_{22}$, $P_3=E_{33}$, and the identities above reduce to the diagonal entries. Every root is conjugate to this one, so every root has the same spectral decomposition up to the change of frame.

## The Spectrum and the Trace Form

**The trace form.** On $M_3$ the form

$$
\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)=\sum_{i,j}\overline{X_{ij}}Y_{ij}
$$

is a positive definite Hermitian inner product. The adjoint of $L_A$ is $L_{A^{*}}$, and the adjoint of $R_A$ is $R_{A^{*}}$.

**The spectral radius.** The **spectral radius** is

$$
r(A)=\max_k|\lambda_k| .
$$

It is a norm on the spectrum but not on the algebra: $r(A)=0$ for every nilpotent, and $r$ is not subadditive on $M_3$. The Gelfand formula is

$$
r(A)=\lim_{n\to\infty}\|A^{n}\|^{1/n},
$$

for every algebra norm, and for a normal matrix,

$$
\|A\|_2=r(A).
$$

For a non-normal matrix the operator norm can be strictly larger: the nilpotent $N=E_{12}$ has $r(N)=0$ and $\|N\|_2=1$.

**The Frobenius norm.** With respect to the trace form,

$$
\|A\|_F^{2}=\operatorname{tr}(A^{*}A)=\sum_{i,j}|a_{ij}|^{2},
$$

and the real part of the Hermitian form, $\operatorname{Re}\operatorname{tr}(A^{*}B)$, is the real inner product whose norm is the Frobenius norm. The singular set $\det A=0$ is a complex hypersurface of real codimension $2$, and the Hermitian trace form $\operatorname{tr}(A^{*}B)$ is positive definite on all of $M_3$, including the singular set: there is no null direction and no null cone.

**The numerical range.** The **numerical range** is

$$
W(A)=\{\langle v,Av\rangle:\|v\|=1\}\subset\mathbb{C}.
$$

It is a convex compact set containing the spectrum, by the Toeplitz–Hausdorff theorem. For a normal matrix it is the convex hull of the eigenvalues. For $A=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ in $M_2$ it is the disk of radius $1$; in $M_3$ the nilpotent $E_{12}$ has numerical range the disk of radius $1/2$. These are the elementary cases of the general theory of numerical ranges; the relevant account for this algebra is in *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*.

## Perturbation and the Discriminant

**Theorem (analytic perturbation).** On the open set where the discriminant $\Delta$ does not vanish, the eigenvalues $\lambda_k(A)$ and the projectors $P_k(A)$ are real-analytic (indeed holomorphic) functions of the entries of $A$. The derivative of an eigenvalue is

$$
d\lambda_k=\operatorname{tr}(P_k\,dA),
$$

and the derivative of the projector is

$$
dP_k=-P_k\,dA\,P_k+\sum_{l\neq k}\frac{P_l\,dA\,P_k}{\lambda_k-\lambda_l}
+\sum_{l\neq k}\frac{P_k\,dA\,P_l}{\lambda_l-\lambda_k}.
$$

**Proof.** The resolvent is holomorphic in $A$ and $t$ away from the spectrum, and the projector is the contour integral of the resolvent, hence holomorphic. The eigenvalue derivative follows from $\chi_A(\lambda_k(A))=0$ and $\partial_t\chi_A(\lambda_k)=\chi_A'(\lambda_k)=\prod_{l\neq k}(\lambda_k-\lambda_l)$, together with $\partial_A\det(tI-A)=-\operatorname{tr}(\operatorname{adj}(tI-A)\,dA)$ evaluated at $t=\lambda_k$, which gives $-\chi_A'(\lambda_k)\operatorname{tr}(P_k\,dA)$. The projector derivative is the derivative of the Riesz integral, using the resolvent identity and the residue calculus.

**The discriminant locus.** The set $\Delta=0$ is the union of the loci where two eigenvalues coincide. It is a hypersurface in $M_3$, of complex dimension $8$ (real dimension $16$), and it is the singular set of the eigenvalue map. On its complement the eigenvalues are three holomorphic functions, and the projectors are three holomorphic rank-one idempotents. The strata are *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*.

**Worked example.** For $A=\operatorname{diag}(1,2,4)$ and $B=\operatorname{diag}(0,1,0)$, the derivative of the second eigenvalue in the direction $B$ is $\operatorname{tr}(P_2B)=\operatorname{tr}(E_{22}B)=1$, which is the derivative of $2+\epsilon$ at $\epsilon=0$. For the root $H$ and a direction $B$, the derivative of the eigenvalue $\zeta_k$ is $\operatorname{tr}(P_kB)$, the $k$-th diagonal entry of $B$ in the eigenbasis of $H$.

## Summary

Every $A\in M_3(\mathbb{C})$ has the characteristic cubic $\chi_A(t)=t^{3}-\tau t^{2}+\sigma t-\delta$, with $\tau=\operatorname{tr}A$, $\sigma=\frac12(\tau^{2}-\operatorname{tr}A^{2})$ and $\delta=\det A$; its roots are the spectrum. When the spectrum is simple, the spectral projectors are the Lagrange polynomials $P_k=\prod_{l\neq k}(A-\lambda_l I)/(\lambda_k-\lambda_l)$; they are orthogonal idempotents summing to $I$, of rank one and trace one, and $A=\sum\lambda_kP_k$. When the spectrum is repeated, the projectors are the Riesz contour integrals; for a double eigenvalue the Hermite interpolant $P_\lambda=I-((A-\lambda I)/(\lambda-\mu))^{2}$ replaces the Lagrange formula, and $A=\lambda P_\lambda+\mu P_\mu+N$ with $N$ nilpotent. For $H^{3}=I$ with simple spectrum, $P_k=(H^{2}+\zeta_kH+\zeta_k^{2}I)/(3\zeta_k^{2})$, and $H=\sum\zeta_kP_k$ is the $\mathbb{Z}/3$ grading. The trace form $\operatorname{tr}(X^{*}Y)$ is positive definite, the spectral radius is the Gelfand limit, and the eigenvalues and projectors are holomorphic on the complement of the discriminant, with $d\lambda_k=\operatorname{tr}(P_k\,dA)$.

$$
\boxed{\ A=\sum_{k=1}^{3}\lambda_kP_k,\quad P_kP_l=\delta_{kl}P_k,\quad \sum_kP_k=I,\quad \operatorname{tr}P_k=1;\qquad P_k=\frac{1}{2\pi i}\oint_{\gamma_k}(tI-A)^{-1}dt.\ }
$$

| Case | Projector formula | Decomposition |
|---|---|---|
| simple spectrum | $\prod_{l\neq k}(A-\lambda_l I)/(\lambda_k-\lambda_l)$ | $A=\sum\lambda_kP_k$ |
| double $\lambda$, simple $\mu$ | $I-((A-\lambda I)/(\lambda-\mu))^{2}$ | $A=\lambda P_\lambda+\mu P_\mu+N$ |
| root $H^{3}=I$ | $(H^{2}+\zeta_kH+\zeta_k^{2}I)/(3\zeta_k^{2})$ | $H=\sum\zeta_kP_k$ |
| scalar $\lambda I$ | $I$ | $A=\lambda I$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A(t)$ | the characteristic cubic $t^{3}-\tau t^{2}+\sigma t-\delta$ |
| $m_A(t)$ | the minimal polynomial, the monic generator of $\{p:p(A)=0\}$ |
| $\tau,\sigma,\delta$ | trace, second elementary symmetric function, determinant |
| $\Delta$ | the discriminant $\prod_{i<j}(\lambda_i-\lambda_j)^{2}$ |
| $P_k$ | the spectral projector of $\lambda_k$ |
| $R(t)=(tI-A)^{-1}$ | the resolvent |
| $r(A)$ | the spectral radius |
| $\|A\|_F$ | the Frobenius norm $\operatorname{tr}(A^{*}A)^{1/2}$ |
| $\zeta_k$ | the cube roots of unity $1,\omega,\omega^{2}$ |

## Further Reading

- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the Riesz integral, the spectral projectors and analytic perturbation.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the characteristic polynomial, the discriminant and the spectral radius.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the residue calculus of the resolvent.
- [The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the cubic and its discriminant.
- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root-first construction.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m3c.html), for the Jordan classification.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the trace form and the numerical range.
