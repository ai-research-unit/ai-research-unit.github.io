# __The Exponential Polar Decomposition of $M_3(\mathbb{C})$__

## Introduction

**Every invertible $A\in M_3(\mathbb{C})$ factors as $A=e^{H}e^{iK}$ with $H,K$ Hermitian; this is the left polar decomposition $A=P'U'$ written in exponential form.** The Hermitian factor $H$ is unique, the $*$-unitary factor $e^{iK}$ is unique, and $K$ is unique modulo $2\pi$. The factorisation is different from the right polar decomposition $A=UP=e^{iK'}e^{H'}$: the two share the $*$-unitary factor, and their positive factors are conjugate by it. The two orderings coincide exactly when $A$ is normal, equivalently when $[H,K]=0$.

The decomposition is the global Cartan decomposition

$$
GL_3(\mathbb{C})=\exp(\operatorname{Herm}_3)\,U(3),
\qquad
\mathfrak{gl}_3=\operatorname{Herm}_3\oplus\mathfrak{u}(3),
$$

with real dimensions $18=9+9$. It exists exactly on the invertible matrices: a singular matrix has no such factorisation, because both factors are invertible, but every singular matrix is a limit of matrices that do. The article proves the decomposition, relates it to the polar decomposition, characterises the normal case, computes an explicit example with exact numbers, describes the degeneration at the singular set, and compares the complex case with the split cases of the biquaternion series.

The polar decomposition is *The Polar Decomposition of $M_3(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_3(\mathbb{C})$*; the spectral theory is *Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$*; the analysis is *Analysis on $M_3(\mathbb{C})$*.

## The Left Polar Decomposition

**Theorem (left polar decomposition).** Every invertible $A\in M_3(\mathbb{C})$ has a unique decomposition

$$
A=P'U',
$$

with $P'$ positive definite Hermitian and $U'$ $*$-unitary:

$$
P'=(AA^{*})^{1/2},\qquad
U'=P'^{-1}A .
$$

**Proof.** The matrix $AA^{*}$ is positive definite, so $P'=(AA^{*})^{1/2}$ is positive definite and invertible. Set $U'=P'^{-1}A$. Then

$$
U'^{*}U'=A^{*}P'^{-2}A=A^{*}(AA^{*})^{-1}A=I,
$$

so $U'$ is $*$-unitary. The decomposition is unique: $P'^{2}=AA^{*}$ forces $P'=(AA^{*})^{1/2}$, and then $U'=P'^{-1}A$.

**The right polar decomposition.** The same $A$ has the right polar decomposition

$$
A=UP,\qquad
P=(A^{*}A)^{1/2},\qquad
U=AP^{-1}.
$$

**The relation between the two.** The $*$-unitary factors agree, $U'=U$, and the positive factors are conjugate, $P'=UPU^{*}$.

**Proof.** From $A=UP$,

$$
AA^{*}=UPPU^{*}=UP^{2}U^{*},
$$

so $P'=(AA^{*})^{1/2}=UPU^{*}$, and

$$
U'=P'^{-1}A=(UPU^{*})^{-1}UP=UP^{-1}U^{*}UP=U .
$$

The left polar is the positive-$*$-unitary order $P'U'$; the right polar is the $*$-unitary-positive order $UP$.

## The Exponential Form

**The Hermitian logarithms.** Every positive definite $P'$ has a unique Hermitian logarithm $P'=e^{H}$ with $H=H^{*}=\log P'$. Every $*$-unitary $U'$ has a Hermitian logarithm $U'=e^{iK}$ with $K=K^{*}$, defined modulo the eigenvalues of $K$ shifted by $2\pi$; the principal logarithm chooses the eigenvalues in $(-\pi,\pi]$.

**Theorem (exponential polar decomposition).** Every invertible $A$ can be written as

$$
A=e^{H}e^{iK},
$$

with $H,K$ Hermitian. The factor $H$ is unique, the factor $e^{iK}$ is unique, and $K$ is unique modulo $2\pi$.

**Proof.** Apply the left polar decomposition $A=P'U'$ and set $P'=e^{H}$, $U'=e^{iK}$. The uniqueness of $P'$ gives the uniqueness of $H$; the uniqueness of $U'$ gives the uniqueness of $e^{iK}$; the logarithm $K$ is unique modulo the lattice of periods of the exponential.

**The right exponential form.** The right polar decomposition gives

$$
A=e^{iK'}e^{H'},
\qquad
H'=U^{*}HU,\quad K'=K,
$$

because $P=U^{*}P'U=U^{*}e^{H}U=e^{U^{*}HU}$. The two exponential forms share the $*$-unitary factor and differ by the conjugation of the Hermitian factor.

**The spectral form.** If $A$ is normal, there is a $*$-unitary $V$ and real diagonal matrices $\Lambda,\Theta$ with

$$
A=Ve^{\Lambda}e^{i\Theta}V^{*}=e^{V\Lambda V^{*}}e^{iV\Theta V^{*}} .
$$

The Hermitian factors commute, and the eigenvalues of $A$ are $e^{\lambda_k+i\theta_k}$.

**Proof.** A normal matrix is unitarily diagonalisable, $A=V\operatorname{diag}(\alpha_1,\alpha_2,\alpha_3)V^{*}$ with $\alpha_k\neq0$. Write $\alpha_k=e^{\lambda_k+i\theta_k}$ with $\lambda_k=\log|\alpha_k|$ and $\theta_k=\arg\alpha_k$. Then $H=V\operatorname{diag}(\lambda_k)V^{*}$ and $K=V\operatorname{diag}(\theta_k)V^{*}$ are Hermitian and give the factorisation.

## The Normal Case

**Theorem.** For invertible $A$ with exponential polar decomposition $A=e^{H}e^{iK}$, the following are equivalent:

1. $A$ is normal: $AA^{*}=A^{*}A$;
2. $H$ and $K$ commute: $[H,K]=0$;
3. the left and right exponential forms coincide: $H'=H$ and $K'=K$;
4. the left and right positive factors coincide: $P'=P$.

**Proof.** If $[H,K]=0$, then

$$
AA^{*}=e^{H}e^{iK}e^{-iK}e^{H}=e^{2H},
\qquad
A^{*}A=e^{-iK}e^{H}e^{H}e^{iK}=e^{2H},
$$

so $A$ is normal. Conversely, if $A$ is normal, the right polar factors $U$ and $P$ commute; then $P'=UPU^{*}=P$, so $H'=H$ and $K'=K$, and $H$ and $K$ commute because they are functions of the commuting normal matrix $A$ (the spectral theorem). The equivalence of 2, 3 and 4 is immediate from $H'=U^{*}HU$ and $K'=K$.

**The non-normal case.** For a non-normal $A$, the Hermitian factors do not commute, and the left and right exponential forms are genuinely different. The commutator $[H,K]$ is the obstruction to the two orderings coinciding.

**Example.** The matrix

$$
A=\begin{pmatrix}1&2&0\\0&1&0\\0&0&3\end{pmatrix}
$$

is not normal. Indeed

$$
A^{*}A=\begin{pmatrix}1&2&0\\2&5&0\\0&0&9\end{pmatrix},
\qquad
AA^{*}=\begin{pmatrix}5&2&0\\2&1&0\\0&0&9\end{pmatrix},
$$

and the two matrices differ in the $(1,1)$, $(1,2)$, $(2,1)$ and $(2,2)$ entries.

## The Cartan Decomposition

**The group decomposition.** The exponential polar decomposition is the left Cartan decomposition

$$
GL_3(\mathbb{C})=\exp(\operatorname{Herm}_3)\,U(3),
$$

and the right polar decomposition is the right Cartan decomposition

$$
GL_3(\mathbb{C})=U(3)\,\exp(\operatorname{Herm}_3).
$$

Both maps

$$
\operatorname{Herm}_3\times U(3)\longrightarrow GL_3,\qquad (H,U)\longmapsto e^{H}U,
$$

$$
U(3)\times\operatorname{Herm}_3\longrightarrow GL_3,\qquad (U,H)\longmapsto Ue^{H},
$$

are diffeomorphisms.

**The Lie algebra.** At the level of Lie algebras,

$$
\mathfrak{gl}_3=\operatorname{Herm}_3\oplus\mathfrak{u}(3),
$$

the Cartan decomposition with Cartan involution $\theta(X)=-X^{*}$. The real dimensions are $18=9+9$.

**The symmetric space.** The quotient

$$
GL_3/U(3)\cong P_+=\operatorname{Herm}_{>0}(3)
$$

is the symmetric space of positive definite Hermitian matrices, of real dimension $9$ and rank $3$. The exponential map $\operatorname{Herm}_3\to P_+$ is a diffeomorphism.

**Proof of the diffeomorphism.** The map is bijective by the polar decomposition and smooth, with smooth inverse $A\mapsto(\log P',P'^{-1}A)$ where $P'=(AA^{*})^{1/2}$; the inverse is smooth because $P'$ is positive definite and the matrix logarithm is smooth on the positive definite cone. The same argument applies to the other order.

## Worked Example

Take the matrix of the polar article,

$$
A=\begin{pmatrix}1&2&0\\0&1&0\\0&0&3\end{pmatrix}.
$$

Its right polar factors are

$$
P=\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ \tfrac{1}{\sqrt2}&\tfrac{3}{\sqrt2}&0\\ 0&0&3\end{pmatrix},
\qquad
U=\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ -\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ 0&0&1\end{pmatrix}.
$$

The matrix $U$ is the rotation by $-\pi/4$ in the first two coordinates, so

$$
U=e^{iK},\qquad
K=\begin{pmatrix}0&-\tfrac{i\pi}{4}&0\\ \tfrac{i\pi}{4}&0&0\\ 0&0&0\end{pmatrix},
$$

which is Hermitian. The positive factor has eigenvalues $1+\sqrt2$, $\sqrt2-1$, $3$; with $c=\log(1+\sqrt2)$,

$$
H=\log P
=\begin{pmatrix}-\tfrac{c}{\sqrt2}&\tfrac{c}{\sqrt2}&0\\ \tfrac{c}{\sqrt2}&\tfrac{c}{\sqrt2}&0\\ 0&0&\log3\end{pmatrix}.
$$

**Check.** The $2\times2$ block of $P$ is $\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&3\end{pmatrix}$, whose eigenvalues are $1+\sqrt2$ and $\sqrt2-1$, and the logarithm is $c$ times $\big(\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&3\end{pmatrix}-\sqrt2 I\big)$, which is the displayed block. The eigenvalues of $H$ are $\log(1+\sqrt2)$, $\log(\sqrt2-1)=-\log(1+\sqrt2)$, and $\log3$; the exponential recovers $P$.

The left polar factor is $P'=UPU^{*}$,

$$
P'=\frac{1}{\sqrt2}\begin{pmatrix}3&1&0\\1&1&0\\0&0&3\sqrt2\end{pmatrix},
\qquad
H'=\log P'=UHU^{*}
=\begin{pmatrix}\tfrac{c}{\sqrt2}&\tfrac{c}{\sqrt2}&0\\ \tfrac{c}{\sqrt2}&-\tfrac{c}{\sqrt2}&0\\ 0&0&\log3\end{pmatrix},
$$

and

$$
A=e^{H'}e^{iK}=e^{iK}e^{H}.
$$

**Verification.** The right form is $A=UP=e^{iK}e^{H}$; the left form is $A=P'U=e^{H'}e^{iK}$. The two Hermitian exponents are conjugate, $H'=UHU^{*}$, and they do not commute with $K$; the matrix $A$ is not normal.

## The Singular Case

**No exponential polar for singular matrices.** If $A$ is singular, it has no factorisation $A=e^{H}e^{iK}$ with $H,K$ Hermitian, because $e^{H}$ is positive definite and $e^{iK}$ is $*$-unitary, so their product is invertible. The exponential polar decomposition exists exactly on $GL_3(\mathbb{C})$.

**The polar decomposition survives.** The right polar decomposition $A=UP$ exists for every $A$, with $P$ positive semidefinite and $U$ a partial isometry; the left polar decomposition $A=P'U'$ exists with $P'=(AA^{*})^{1/2}$ positive semidefinite and $U'$ a partial isometry. The exponential form requires the invertibility of $P$ and $P'$.

**The limit.** For a family $A(\epsilon)$ of invertible matrices tending to a singular $A(0)$, the Hermitian factor $H(\epsilon)=\log P(\epsilon)$ tends to $-\infty$ in the direction of the kernel; the $*$-unitary factor may have a limit or not. The exponential polar decomposition degenerates at the singular set, while the polar decomposition with the partial isometry continues.

**Example.** The singular matrix

$$
A_0=\operatorname{diag}(1,0,0)
$$

is the limit of

$$
A_\epsilon=\operatorname{diag}(1,\epsilon,\epsilon)
=\exp\big(\operatorname{diag}(0,\log\epsilon,\log\epsilon)\big),
\qquad \epsilon>0 .
$$

The Hermitian factor is $H_\epsilon=\operatorname{diag}(0,\log\epsilon,\log\epsilon)$, which tends to $-\infty$ on the second and third coordinates, and the $*$-unitary factor is $I$. The limit $A_0$ is singular and is not itself an exponential.

**The singular values.** In the right exponential form $A=e^{iK'}e^{H'}$, the singular values of $A$ are $e^{h_k}$, where $h_k$ are the eigenvalues of $H'$. The exponential polar decomposition writes the singular values as exponentials of the Hermitian eigenvalues; the $*$-unitary factor carries the phases. At a zero singular value the logarithm diverges, which is the analytic form of the degeneration.

## The Root, the Frame and the Gauge

**The root.** A root $H$ with $H^{3}=I$ and simple spectrum is diagonalisable, with spectral projectors $P_k$ and eigenvalues $\zeta_k$. It is $*$-unitary exactly when it is normal, equivalently when the projectors $P_k$ are Hermitian. For the standard root $H_0=\operatorname{diag}(1,\omega,\omega^{2})$ and the cyclic permutation root, which are $*$-unitary, the right polar decomposition is $H=H\cdot I$ and the exponential polar decomposition is

$$
H=e^{iK},\qquad
K=\frac{2\pi}{3}\big(P_2+2P_3\big),
$$

where $P_k$ is the projector for $\zeta_k$, with $\zeta_1=1$. The Hermitian factor is $I$ and the Hermitian exponent is $0$. For a non-normal root the Hermitian factor is $P=(H^{*}H)^{1/2}\neq I$ and the phase factor is the $*$-unitary $(H^{*}H)^{-1/2}H$; the root is not $*$-unitary. The idempotents $P_k$ themselves are never $*$-unitary.

**The frame.** For a frame $S\in GL_3$ the exponential polar decomposition separates the phases from the stretching:

$$
S=e^{H}e^{iK},\qquad
H=\log(SS^{*})^{1/2},\quad e^{iK}=(SS^{*})^{-1/2}S .
$$

The gauge torus $T$ acts on the frame by $S\mapsto ST$, and the two Hermitian exponents do not transform separately: the decomposition of $ST$ mixes $H$ and $K$ unless $T$ is $*$-unitary.

**The gauge parameters.** In the additive coordinates $t=\operatorname{diag}(t_1,t_2,t_3)$, the nilpotents rescale as

$$
E_{12}\mapsto e^{t_1-t_2}E_{12},\qquad
E_{23}\mapsto e^{t_2-t_3}E_{23},\qquad
E_{13}\mapsto e^{t_1-t_3}E_{13}.
$$

The Hermitian exponent of the frame is the real part of $t$ in the appropriate trivialisation; the phase exponent is the imaginary part. The idempotents are invariant under the gauge, so they do not appear in $H$ or $K$ as gauge-dependent factors.

## Comparison with the Split Case

**The complex case.** Over $\mathbb{C}$ the exponential is surjective onto $GL_3(\mathbb{C})$, the positive cone $\operatorname{Herm}_{>0}(3)$ is definite and convex, and every invertible matrix has the exponential polar decomposition $A=e^{H}e^{iK}$ with $H$ unique and $K$ modulo $2\pi$.

**The split real cases.** In the real split algebras of the biquaternion series the exponential is not surjective onto the invertible group, and the polar decomposition carries an indefinite factor: the split-complex exponential misses the negative real axis, and the split-quaternion exponential misses matrices with a negative eigenvalue and a nontrivial Jordan block. The positive cone is replaced by an indefinite cone, and the polar factors can change sign.

**The reason.** The difference is the spectrum. Over $\mathbb{C}$ every nonzero complex number has a logarithm, so every invertible Jordan block has a logarithm; over $\mathbb{R}$ a negative eigenvalue has no real logarithm, and the indefinite norm allows null directions that the definite Hermitian cone does not have. The complex algebra has no null cone in the trace form, and the exponential polar decomposition is global on $GL_3$.

**The biquaternion case.** At $n=2$ the theorem is the same: every invertible $A\in M_2(\mathbb{C})$ is $e^{H}e^{iK}$ with $H,K$ Hermitian $2\times2$ matrices. The biquaternion algebra is the $n=2$ case of the same complex matrix theorem; the split real forms are different real sections of the same complex group.

## Summary

Every invertible $A\in M_3(\mathbb{C})$ has a unique left polar decomposition $A=P'U'$ with $P'=(AA^{*})^{1/2}$ positive definite and $U'=P'^{-1}A$ $*$-unitary. Writing $P'=e^{H}$ and $U'=e^{iK}$ gives the exponential polar decomposition

$$
A=e^{H}e^{iK},
$$

with $H$ Hermitian unique and $K$ Hermitian modulo $2\pi$. The right polar decomposition is $A=UP=e^{iK'}e^{H'}$, with $U'=U$, $P'=UPU^{*}$, $H'=U^{*}HU$, $K'=K$. The two orderings coincide exactly when $A$ is normal, equivalently when $[H,K]=0$; then $A$ is unitarily diagonalisable with eigenvalues $e^{\lambda_k+i\theta_k}$. The decomposition is the left Cartan decomposition $GL_3=\exp(\operatorname{Herm}_3)U(3)$, the other global form being $GL_3=U(3)\exp(\operatorname{Herm}_3)$; both are diffeomorphisms, with real dimensions $18=9+9$. The exponential polar decomposition exists exactly on $GL_3$; it degenerates at the singular set, where the Hermitian logarithm diverges. Over $\mathbb{C}$ the exponential is surjective and the positive cone is definite, in contrast with the split real cases.

$$
\boxed{\ A=e^{H}e^{iK}=P'U',\quad P'=(AA^{*})^{1/2},\quad U'=P'^{-1}A,\quad H=H^{*},\quad K=K^{*},\quad [H,K]=0\iff A\text{ normal}.\ }
$$

| Object | Formula |
|---|---|
| Left polar | $A=P'U'$, $P'=(AA^{*})^{1/2}$ |
| Right polar | $A=UP$, $P=(A^{*}A)^{1/2}$ |
| Relation | $U'=U$, $P'=UPU^{*}$ |
| Exponential polar | $A=e^{H}e^{iK}$ |
| Right exponential | $A=e^{iK'}e^{H'}$, $H'=U^{*}HU$ |
| Normal case | $[H,K]=0$ |
| Cartan decomposition | $GL_3=\exp(\operatorname{Herm}_3)U(3)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P'$ | left positive factor $(AA^{*})^{1/2}$ |
| $U'$ | left $*$-unitary factor $P'^{-1}A$ |
| $H$ | Hermitian logarithm of $P'$ |
| $K$ | Hermitian logarithm of $U'$, modulo $2\pi$ |
| $H'$ | $U^{*}HU$, the right Hermitian exponent |
| $\operatorname{Herm}_3$ | real space of Hermitian matrices |
| $P_+$ | positive definite cone $\operatorname{Herm}_{>0}(3)$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the Cartan decomposition and the exponential map.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition and the matrix logarithm.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the positive definite cone and the logarithm.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for the right polar decomposition and the singular case.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for the exponential and its image.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the Hermitian cone and the star.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the split comparison.
