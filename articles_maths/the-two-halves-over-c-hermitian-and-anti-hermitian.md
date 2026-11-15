# __The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian__

## Introduction

**Over the complex field the conjugate transpose cuts the algebra into the Hermitian matrices and the anti-Hermitian ones, and the cut is even: two real subspaces of the same real dimension $n^{2}$, unlike the unequal halves of the transpose over $\mathbb{R}$.**

The article proves the direct sum, computes the dimensions, identifies the anti-Hermitian half with the Lie algebra $\mathfrak{u}(n)$ and with $i$ times the Hermitian half, and settles the orthogonality question: the two halves are orthogonal for the real part of the trace form and not for the form itself. It computes the signature of the trace bilinear form on each half, which is $(n^{2},0)$ and $(0,n^{2})$, and it reads the exponentials, which are the unitary group and the positive definite Hermitian matrices. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the real case and *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* for the classification of the conjugate transpose among the involutions. It defers the spectral theorems to *The Spectral Theorem: the Hermitian Case* and *The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum*, and the polar decomposition to *The Polar Decomposition from the Two Halves*.

## The Split

**Every complex matrix is Hermitian plus anti-Hermitian, uniquely.** With $A^{*}=\bar A^{\mathsf T}$,

$$
A=\underbrace{\tfrac12(A+A^{*})}_{H}+\underbrace{\tfrac12(A-A^{*})}_{K},\qquad H^{*}=H,\quad K^{*}=-K .
$$

The two summands are real, the decomposition is the eigenspace decomposition of the conjugate transpose, and the half is determined by its diagonal: the diagonal entries of $H$ are real and those of $K$ are purely imaginary. The decomposition is additive and real-linear, and it is not complex-linear, since $iA$ has halves $iH$ and $iK$ with the roles of Hermitian and anti-Hermitian exchanged.

**The two halves have real dimension $n^{2}$ each.** A Hermitian matrix is determined by $n$ real diagonal entries and $\binom{n}{2}$ complex entries above the diagonal, so

$$
\dim_{\mathbb{R}}\operatorname{Herm}_n=n+2\binom{n}{2}=n^{2},\qquad \dim_{\mathbb{R}}\operatorname{SkewHerm}_n=n^{2},
$$

and the two dimensions add to the real dimension $2n^{2}$ of the algebra. The equality of the dimensions is the structural difference from the real case, where the halves have dimensions $n(n+1)/2$ and $n(n-1)/2$.

**The halves are exchanged by multiplication by $i$.** For Hermitian $H$ the product $iH$ is anti-Hermitian, since $(iH)^{*}=-iH^{*}=-iH$. So

$$
\operatorname{SkewHerm}_n=i\,\operatorname{Herm}_n ,
$$

an isomorphism of real vector spaces. The two halves are therefore the same real space up to the complex structure, and no invariant of the pair can distinguish them except the ones that see $i$.

## The Hermitian Half

**The Hermitian half is a real Jordan algebra, and its spectrum is real.** For Hermitian $H$ the anticommutator $\tfrac12(HK+KH)$ of two Hermitian matrices is Hermitian, and the Jordan identity holds as in the real case, so $\operatorname{Herm}_n$ is a Jordan algebra over $\mathbb{R}$, of dimension $n^{2}$. Its elements have real eigenvalues: from $Hv=\lambda v$ and $H=H^{*}$,

$$
\lambda\|v\|^{2}=v^{*}Hv=\overline{v^{*}Hv}=\bar\lambda\|v\|^{2},
$$

so $\lambda=\bar\lambda$. The spectral theorem gives the sharper statement: $H=U\Lambda U^{*}$ with $U$ unitary and $\Lambda$ real diagonal.

**The positive definite elements form an open cone.** The set $\{H\succ0\}$ is open in $\operatorname{Herm}_n$, convex, and closed under the product only when the factors commute. The cone is the image of the Hermitian half under the exponential, and its boundary is the set of singular positive semidefinite matrices; the whole geometry is in *The Positive Cone and Its Boundary* and *The Cone of Positive Semidefinite Matrices*.

**The Hermitian half is the fixed set of the conjugate transpose, and its elements are the observables of the corpus.** The name *observable* is the physical reading of a Hermitian matrix: real spectrum, orthonormal eigenbasis, and a real expectation value $\operatorname{tr}(H\rho)$ against a positive semidefinite matrix of trace one. The mathematics used below needs only the first two.

## The Anti-Hermitian Half

**The anti-Hermitian half is the Lie algebra $\mathfrak{u}(n)$.** For anti-Hermitian $K,L$,

$$
[K,L]^{*}=(KL-LK)^{*}=L^{*}K^{*}-K^{*}L^{*}=LK-KL=-[K,L],
$$

so the commutator stays in the half, and the Jacobi identity holds automatically. The dimension is $n^{2}$, and the traceless part is the Lie algebra $\mathfrak{su}(n)$, of dimension $n^{2}-1$, which is the Lie algebra of $SU(n)$.

**A anti-Hermitian matrix has a purely imaginary spectrum.** If $Kv=\lambda v$ then $\lambda\|v\|^{2}=v^{*}Kv$ and taking conjugates gives $\bar\lambda\|v\|^{2}=v^{*}K^{*}v=-v^{*}Kv=-\lambda\|v\|^{2}$, so $\lambda=-\bar\lambda$. The eigenvalues are therefore purely imaginary, and the matrix is unitarily diagonalisable with imaginary diagonal: $K=Ui\Theta U^{*}$ with $\Theta$ real diagonal.

**The half contains no nonzero real multiple of the identity, and that is what makes it a Lie algebra and not a Jordan algebra.** The identity is Hermitian and not anti-Hermitian, so the half has no unit. The anticommutator of two anti-Hermitian matrices is Hermitian, so the half is not closed under the Jordan product; the commutator is the product it carries.

## The Two Forms

**The two halves are orthogonal for the real part of the trace form and not for the form itself.** With $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ and $H$ Hermitian, $K$ anti-Hermitian,

$$
\overline{\operatorname{tr}(H^{*}K)}=\operatorname{tr}(K^{*}H)=-\operatorname{tr}(KH)=-\operatorname{tr}(HK),
$$

so $\operatorname{tr}(HK)$ is purely imaginary. Its real part vanishes identically, which is all that orthogonality of two real subspaces needs for the Euclidean form, and its imaginary part generally does not, so the Hermitian form itself does not vanish on the pair. The computation at $n=2,3,4$ gives a real part of zero to machine precision and an imaginary part of order one.

**The trace bilinear form has signature $(n^{2},n^{2})$, with opposite signs on the halves.** For Hermitian $H$ and anti-Hermitian $K$,

$$
\operatorname{tr}(H^{2})=\operatorname{tr}(H^{*}H)>0,\qquad \operatorname{tr}(K^{2})=-\operatorname{tr}(K^{*}K)<0 ,
$$

so the bilinear form $B(A,B)=\operatorname{tr}(AB)$ is positive definite on the Hermitian half of dimension $n^{2}$ and negative definite on the anti-Hermitian half of the same dimension. The total signature is $(n^{2},n^{2})$, a split form, against the Euclidean form $\operatorname{tr}(A^{*}B)$ which is positive definite on the whole algebra.

**The two forms must not be confused.** The form $\operatorname{tr}(A^{*}B)$ is the Hilbert–Schmidt form, positive definite and used for the metric; the form $\operatorname{tr}(AB)$ is the trace bilinear form, indefinite and used for the adjoints and for the Killing form. On the Hermitian half the first restricts to the second, and on the anti-Hermitian half the two differ by a sign. The article *The Hilbert–Schmidt Form* keeps the two apart.

## The Exponential of Each Half

**The exponential of a anti-Hermitian matrix is unitary.** If $K^{*}=-K$ then

$$
(e^{K})^{*}e^{K}=e^{K^{*}}e^{K}=e^{-K}e^{K}=\mathrm{I},\qquad |\det e^{K}|=e^{\operatorname{Re}\operatorname{tr}K}=1 ,
$$

so $e^{K}\in\mathrm{U}(n)$, and $e^{K}\in\mathrm{SU}(n)$ when $\operatorname{tr}K=0$. Both checks were verified at $n=2,3,4$ by summing the series. The map is surjective onto $\mathrm{U}(n)$, since a unitary matrix is unitarily diagonalisable with eigenvalues on the circle.

**The exponential of $i$ times a Hermitian matrix is unitary, and the exponential of a Hermitian matrix is positive definite.** For Hermitian $H$,

$$
e^{iH}\in\mathrm{U}(n),\qquad e^{H}\ \text{Hermitian and positive definite},
$$

the second because the eigenvalues of $e^{H}$ are $e^{\lambda_k}>0$ with $\lambda_k$ real. Conversely every positive definite Hermitian matrix is $e^{H}$ for a unique Hermitian $H=\log P$, so $\exp$ is a bijection from the Hermitian half onto the positive cone.

**The two exponentials generate the group and the cone.** The polar decomposition of an invertible element is $A=UP$ with $U$ unitary and $P$ positive definite, and the two factors are the exponentials of the two halves of the polar data. The decomposition is proved in *The Polar Decomposition from the Two Halves*; the version for the group $GL_n(\mathbb{C})$ is the Cartan decomposition of *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$*.

## The Case $n=2$

**At $n=2$ the split is $8=4+4$ in real dimensions.** The Hermitian half is spanned over $\mathbb{R}$ by $\mathrm{I},\sigma_1,\sigma_2,\sigma_3$, and the anti-Hermitian half is $i$ times it, spanned by $i\mathrm{I},i\sigma_1,i\sigma_2,i\sigma_3$. This is the cleanest instance of the equal split, and it is the reason the biquaternion algebra is read through the Hermitian and anti-Hermitian halves rather than through the symmetric and antisymmetric ones.

**The two halves are the two sectors of the biquaternion reading.** A Hermitian element of $M_2(\mathbb{C})$ corresponds to a biquaternion whose four coordinates satisfy a reality condition, and a anti-Hermitian element to one with $i$ times that condition. The Peirce idempotents $\tilde\Pi_\pm$ are Hermitian, so they lie in the first half; the companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ are neither Hermitian nor anti-Hermitian, since they satisfy $\vec\Upsilon_{-+}=\vec\Upsilon_{+-}^{*}$ and their squares vanish. The mixed corners of the Peirce decomposition therefore leave both halves, which is the algebraic reason the Peirce frame is not a Hermitian frame.

## Summary

The conjugate transpose splits $M_n(\mathbb{C})$ into the Hermitian half and the anti-Hermitian half, two real subspaces of dimension $n^{2}$ each, exchanged by multiplication by $i$. The Hermitian half is a real Jordan algebra with real spectrum and unitary diagonalisation; the anti-Hermitian half is $\mathfrak{u}(n)$, of dimension $n^{2}$ with traceless part $\mathfrak{su}(n)$ of dimension $n^{2}-1$, and its elements have purely imaginary spectrum. The halves are orthogonal for the real part of the trace form and not for the form, and the trace bilinear form has signature $(n^{2},0)$ on the first and $(0,n^{2})$ on the second, totalling the split signature $(n^{2},n^{2})$. The exponential of the anti-Hermitian half is the unitary group and the exponential of the Hermitian half is the positive cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_n$ | the Hermitian half, of real dimension $n^{2}$ |
| $\operatorname{SkewHerm}_n=i\operatorname{Herm}_n$ | the anti-Hermitian half, of real dimension $n^{2}$ |
| $A^{*}=\bar A^{\mathsf T}$ | the conjugate transpose |
| $\mathfrak{u}(n)$ | the anti-Hermitian half as a Lie algebra, of dimension $n^{2}$ |
| $\mathfrak{su}(n)$ | its traceless part, of dimension $n^{2}-1$ |
| $\operatorname{tr}(A^{*}B)$ | the Hilbert–Schmidt form, positive definite |
| $\operatorname{tr}(AB)$ | the trace bilinear form, of signature $(n^{2},n^{2})$ |
| $\mathrm{I},\sigma_1,\sigma_2,\sigma_3$ | the Pauli list, a real basis of $\operatorname{Herm}_2$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for Hermitian and anti-Hermitian matrices, their spectra and the trace forms.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $\mathfrak{u}(n)$, $\mathfrak{su}(n)$ and the exponential map.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the cone of positive definite Hermitian matrices and its logarithm.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the real case that this one completes.
- [The Involutions over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-over-r-and-over-c.html), for the conjugate transpose as an involution of the second kind.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the trace form and the algebra $\mathfrak{u}(n)$.
